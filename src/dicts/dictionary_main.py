import dicts.str_handlers as H

COMMANDS = {
    "help": ["help", "h"],
    "exit": ["exit", "off"],
    "modules": ["modules", "ls"],
}

LAUNCHER_COMMANDS = {
    "help": ["help", "h"],
    "exit": ["exit", "back"],
    "run": ["run", "start"],
}

COMMANDS_HANDLER = {
    "help": H.help_,
    "exit": H.exit_,
    "modules": H.modules,
    "unknow_command": H.unknow_command,
    "unknow_module": H.unknow_module,
    "module_load": H.module_load,
}

LAUNCHER_COMMANDS_HANDLER = {
    "help": H.help_launcher,
    "exit": H.exit_launcher,
    "val_of_var_n_found": H.value_of_variable_not_found,
    "mod_error": H.module_error,
    "var_is_n_found": H.variable_is_not_found,
    "var_is_mand": H.variable_is_mandatory,
    "mod_finish": H.module_finish,
}

DESIGNATIONS = {
    "error": "[!]",
    "info": "[*]",
    "add": "[+]",
    "success": "[v]",
    "border": "|",
    "input": " > ",
}


ALL_TAGS = list(COMMANDS_HANDLER.keys())+ list(LAUNCHER_COMMANDS_HANDLER.keys())
