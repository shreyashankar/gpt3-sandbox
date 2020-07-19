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
