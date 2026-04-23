class BaseModel:
    def score(self):
        """Method to calculate the score for the model."""
        raise NotImplementedError("This method should be overridden in subclasses.")

    def check_conditions(self):
        """Method to check conditions relevant to the model."""
        raise NotImplementedError("This method should be overridden in subclasses.")