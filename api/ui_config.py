"""Class to store customized UI parameters."""


class UIConfig():
    """Stores customized UI parameters."""

    def __init__(self, description='Description',
                 button_text='Submit',
                 placeholder='Default placeholder'):
        self.description = description
        self.button_text = button_text
        self.placeholder = placeholder

    def get_description(self):
        """Returns the input of the example."""
        return self.description

    def get_button_text(self):
        """Returns the intended output of the example."""
        return self.button_text

    def get_placeholder(self):
        """Returns the intended output of the example."""
        return self.placeholder

    def json(self):
        """Used to send the parameter values to the API."""
        return {"description": self.description,
                "button_text": self.button_text,
                "placeholder": self.placeholder}
