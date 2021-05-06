builddir=build
testresults=$(builddir)/test-results.xml
env=.env
envfile=environment.yml
requirementsFile=requirements.txt
source=$(shell find . -path ./$(env) -prune -o -name '*.py')
sourcedirs=$(shell find . -path ./$(env) -prune -o -name '*.py' | xargs -I{} dirname {} | sort --unique | grep -v -e '^\.$$' | sed 's/$$/\//')
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
install_requirements=$(builddir)/installed-requirements
buildenv=$(builddir)/env-updated
CONDA_DIR=$(shell which conda | sed -E 's/(condabin|bin)\/conda//')


.PHONY: test
test: $(testresults)

.PHONY: env
env: $(install_requirements)

$(testresults): $(install_requirements) |$(builddir) $(source) $(sourcedirs) .
	mkdir -p $(builddir)
	source $(CONDA_DIR)etc/profile.d/conda.sh; \
	conda activate $(ROOT_DIR)/$(env); \
	python -m pytest --junitxml=$(testresults) --ignore=$(env);

$(install_requirements): $(requirementsFile) $(buildenv)
	mkdir -p $(builddir)
	source $(CONDA_DIR)etc/profile.d/conda.sh; \
   	conda activate $(ROOT_DIR)/$(env); \
    pip install -r $(requirementsFile) --ignore-installed;
	touch $(install_requirements)

$(requirementsFile):
	touch $(requirementsFile)

$(buildenv): $(envfile)
	mkdir -p $(builddir)
	source $(CONDA_DIR)etc/profile.d/conda.sh; \
	if [ -d $(env) ]; then \
		conda env update -f $(envfile) -p $(env); \
	else \
		conda env create -f $(envfile) -p $(env); \
	fi; \
	touch $(buildenv)

$(envfile):
	touch $(envfile)

.PHONY: clean
clean:
	rm -rf $(builddir)

.PHONY: clean-all
clean-all: clean
	source $(CONDA_DIR)etc/profile.d/conda.sh; \
	conda deactivate; \
    conda env remove -p $(ROOT_DIR)/$(env);
