
# Use the BaseModule class to create your own modules;
# Inherit your module class from BaseModule;
# Add a name, variables that you need from the user (in the Variables dictionary),
# implement the run() function, return -1 if an error occurs;
# Add the directory with.py file of your module to the modules directory;

# Используйте класс BaseModule для создания своих модулей;
# Насследуйте класс своего модуля от BaseModule;
# Добавьте имя, переменные которые нужны от пользователя (в словарь Variables),
# реализуйте функцию run(), верните -1 если случилась ошибка;
# Добавьте директорию с .py файлом вашего модуля в директорию modules;

class BaseModule:


    # Preferably a unique name (to see all modules: run Glaz and type 'module');

    # Желательно уникальное имя (чтобы посмотреть все модули: запустите Glaz и введите команду 'module');
    name = "Name"

    #

    #
    description = "Description"


    # Variables that the user must enter;
    # Required implementation;

    # Переменные, которые должен ввести пользователь;
    # Обязательно к реализации;
    variables = {"variable": {"description": "description of variable", "is_required": True}}


    def run(self, VAR_VALUE_DICT):


        # Variables that are specified in the variables dictionary, and their values ​​are passed
        # to the module through the VAR_VALUE_DICT dictionary variable, in the form {var: value};
        # All values ​​passed to the module via the VAR_VALUE_DICT dictionary are of type string;

        # Переменные, которые указаны в словаре variables, и их значения передаются в модуль
        # через переменную-словарь VAR_VALUE_DICT в виде {переменная: значение};
        # Все значения передающиеся в модуль в перменной VAR_VALUE_DICT являются типом string;


        # Return -1 if an error occurs;

        # Верните -1 если случилась ошибка;
        raise NotImplementedError("The module must implement the run() function!")
