import importlib
import os
import sys

from dicts.dictionary_main import *


lang_lib = None


def load_language():
    global lang_lib
    glaz_dir = os.path.dirname(os.path.abspath(__file__))
    LANG = open(f"{glaz_dir}/language", encoding="utf-8").read().strip()
    lang_module_name = f"dicts.dictionary_{LANG}"
    try:
        lang_lib = importlib.import_module(lang_module_name)
    except ModuleNotFoundError:
        print("Dictionary for the selected language not found!")
        sys.exit(-1)


def collect(command, data=None, skip_top=0, skip_down=0, skip_between_lines=0, is_launcher=False):

    # Load text and language
    load_language()

    # Add skips
    skip_top_text = ''
    skip_down_text = ''
    if skip_top:
        skip_top_text = "\n" * skip_top
    if skip_down:
        skip_down_text = "\n" * skip_down

    # Top skip
    print(skip_top_text,end='')

    # Check and get tag of command
    tag = command
    if tag not in COMMANDS_HANDLER and tag not in LAUNCHER_COMMANDS_HANDLER:
        if is_launcher:
            for cmd in LAUNCHER_COMMANDS:
                if command in LAUNCHER_COMMANDS[cmd]:
                    tag = cmd
        else:
            for cmd in COMMANDS:
                if command in COMMANDS[cmd]:
                    tag = cmd


    # Unknow command
    if tag not in ALL_TAGS:
        handler = COMMANDS_HANDLER['unknow_command']
        print(handler(lang_lib))

    # Know
    else:

        # Launcher commands
        if is_launcher:
            handler = LAUNCHER_COMMANDS_HANDLER[tag]
            print(handler(lang_lib, data=data))

        # Main terminal commands
        else:
            handler = COMMANDS_HANDLER[tag]
            print(handler(lang_lib, data=data))

    # Down skip
    print(skip_down_text,end='')
