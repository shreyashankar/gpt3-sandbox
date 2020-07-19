class UIConfig():

    def __init__(self, description='Description',
                       buttonText='Submit',
                       placeholder='Default placeholder'):
        self.description = description
        self.buttonText = buttonText
        self.placeholder = placeholder

    def json(self):
        return {"description": self.description,
                "buttonText": self.buttonText,
                "placeholder": self.placeholder}
