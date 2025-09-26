
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

    description = "Description"


    # Determines whether a build is required:
    # - True  → the project contains C modules and needs to compile dependencies (source files are taken from build_sources)
    # - False → pure Python code, no build required
    # Works only with C language and GCC compiler!!!

    # Определяет необходимость сборки:
    # - True → проект содержит модули на C, требуется компиляция зависимостей (файлы для сборки берутся из build_sources)
    # - False → только Python-код, сборка не нужна
    # Работает только с языком C и компилятором GCC!!!

    build = False


    # Dictionary of main source files to be compiled.
    # Only top-level files should be listed here (their dependencies are included automatically).
    # Each entry is stored as {SOURCE_FILE: OUTPUT_EXECUTABLE_FILE}.
    # The path is set relative to the module directory

    # Словарь основных файлов, которые нужно компилировать.
    # Здесь указываются только верхнеуровневые файлы (их зависимости подключаются автоматически).
    # Каждая запись имеет вид {SOURCE_FILE: OUTPUT_EXECUTABLE_FILE}.
    # Путь задаётся относительно директории модуля

    build_sources = {"example.c": "example.a"}


    # Variables that the user must enter;
    # Required implementation;

    # Переменные, которые должен ввести пользователь;
    # Обязательно к реализации;

    variables = {"variable": {"description": "description of variable", "is_required": True}}


    # Validates that subclasses of BaseModule define required attributes:
    # name, description, variables, and build_sources (if build=True).

    # Проверяет, что у наследников BaseModule заданы обязательные атрибуты:
    # name, description, variables и build_sources (если build=True).

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not getattr(cls, "name", None) or cls.name == "Name":
            raise TypeError(f"Class {cls.__name__} must define a unique 'name' attribute")
        if not getattr(cls, "description", None) or cls.description == "Description":
            raise TypeError(f"Class {cls.__name__} must define a unique 'description' attribute")
        if cls.build and (not getattr(cls, "build_sources", None) or cls.build_sources == {"example.c": "example.a"}):
            raise TypeError(f"Class {cls.__name__} must define a unique 'build_sources' attribute")
        if not getattr(cls, "variables", None) or cls.variables == {}:
            raise TypeError(f"Class {cls.__name__} must define a unique 'variables' attribute")


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
