class Example():
    def __init__(self, inp, out):
        self.input = inp
        self.output = out
    
    def format(self):
        return f"input: {self.input}\noutput: {self.output}\n"

class GPT:

    def __init__(self):
        self.examples = []

    def add_example(self, ex):
        assert isinstance(ex, Example), "Please create an Example object."
        self.examples.append(ex.format())
    
    def get_prime_text(self):
        return '\n'.join(self.examples) + '\n'

