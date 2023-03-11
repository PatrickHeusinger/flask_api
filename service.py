from models import TodoModel


class Service:
    def __init__(self):
        self.model = TodoModel()

    def create(self, params):
        return self.model.create(params["Title"], params["Description"])
