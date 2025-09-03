class BaseModule:
    name = "Name"
    description = "Description"
    usage = "Usage"
    variables = {"variable": {"description": "description of variable", "is_mandatory": True}} # MANDATORY !!!

    def run(self, VAR_VALUE_DICT):
        # переменные, которые указаны в словаре variables, и их значения
        # передаются в модуль через переменную словарь VAR_VALUE_DICT
        # все значения которые передаются в модуль через словарь VAR_VALUE_DICT являются типом string
        raise NotImplementedError("Модуль должен реализовать метод run()")
