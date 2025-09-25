class BaseModule:
    name = "Name"
    description = "Description"
    usage = "Usage"
    variables = {"variable": {"description": "description of variable", "is_required": True}} # REQUIRED !!!

    def run(self, VAR_VALUE_DICT):

        # Variables that are specified in the variables dictionary, and their values ​​are passed
        # to the module through the VAR_VALUE_DICT dictionary variable, in the form {var: value};
        # All values ​​passed to the module via the VAR_VALUE_DICT dictionary are of type string;

        # Переменные, которые указаны в словаре variables, и их значения передаются в модуль
        # через переменную-словарь VAR_VALUE_DICT в виде {переменная: значение};
        # Все значения передающиеся в модуль в перменной VAR_VALUE_DICT являются типом string;

        raise NotImplementedError("Модуль должен реализовать метод run()")
