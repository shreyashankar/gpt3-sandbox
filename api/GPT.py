import openai

class Example():
    def __init__(self, inp, out):
        self.input = inp
        self.output = out
    
    def format(self):
        return f"input: {self.input}\noutput: {self.output}\n"

class GPT:

    def __init__(self, engine='davinci',
                       temperature=0.5,
                       max_tokens=100):
        self.examples = []
        self.engine=engine
        self.temperature=temperature
        self.max_tokens=max_tokens

    def set_openai_key(self, key):
        openai.api_key=key

    def add_example(self, ex):
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples.append(ex.format())
    
    def get_prime_text(self):
        return '\n'.join(self.examples) + '\n'

    def get_engine(self):
        return self.engine

    def get_temperature(self):
        return self.temperature

    def get_max_tokens(self):
        return self.max_tokens

    def craft_query(self, prompt):
        return self.get_prime_text() + "input: " + prompt + "\n"

    def submit_request(self, prompt):
        response = openai.Completion.create(engine=self.get_engine(),
                                        prompt=self.craft_query(prompt),
                                        max_tokens=self.get_max_tokens(),
                                        temperature=self.get_temperature(),
                                        top_p=1,
                                        n=1,
                                        stream=False,
                                        stop="\ninput:")
        return response 

    def get_top_reply(self, prompt):
        response = self.submit_request(prompt)
        return response['choices'][0]['text'][7:]
