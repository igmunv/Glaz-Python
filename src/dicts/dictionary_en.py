from dicts.dictionary_main import *

# Description commands
DESC_COMMANDS = {
    "help": "Print available commands",
    "exit": "Exit from Glaz",
    "modules": "Print available modules",
}

DESC_LAUNCHER_COMMANDS = {
    "help": "Print available commands",
    "exit": "Back to Glaz",
    "run": "Run module",
}

# Texts for print
TEXTS = {

    "module_load_p1": "Module",
    "module_load_p2": "loaded",

    "unknow_command": f"Unknow command. Enter '{COMMANDS['help'][0]}' to view commands",
    "exit": "Exit...",

    "main_help_output_begin": "All commands:",

    "modules_output_begin": "All loaded modules:",
    "modules_output_end": "Enter the number to run module",

    "modules_not_found": f"A module with this number is not loaded! Type '{COMMANDS['modules'][0]}' to view the modules",

    "module_run_exit": "Back to Glaz...",
    "module_run_var_not_found": "Variable is not found!",
    "module_run_value_not_found": f"Enter value of variable! Enter '{LAUNCHER_COMMANDS['help'][0]} to view commands and usage!'",
    "module_run_module_return_error": "Module error",
    "module_run_module_finish_work": "Module finished work!",
    "module_run_var_is_mand_p1": "Variable",
    "module_run_var_is_mand_p2": "is required!",

    "module_run_mand_vars_begin": "Required variables:",
    "module_run_optn_vars_begin": "Optional variables:",
    "module_run_vars_end": f"Enter 'VARIABLE VALUE' to assign a value to a variable. Example: 'host http://192.168.0.1/'",
    "": "",

}
