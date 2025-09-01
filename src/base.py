class BaseModule:
    name = "Name"
    description = "Description"

    def run(self, target):
        raise NotImplementedError("Модуль должен реализовать метод run()")
