import json
from datetime import datetime
from collections import defaultdict


class ConsoleMessages:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'  

    @staticmethod
    def append_reason(obj, explanation_string):
        obj["reasonForRemoval"] = explanation_string
        return obj

    @staticmethod
    def summary_removed(property_name):
        description = (
            f"{ConsoleMessages.CYAN}\n---------------DUPLICATE ENTRIES REMOVED!---------------\n"
            f"{ConsoleMessages.GREEN}The database contained duplicates for the following "
            f"{ConsoleMessages.RED}{property_name} "
            f"{ConsoleMessages.GREEN}values.\nThose displayed were removed.\n"
            f"{ConsoleMessages.RESET}"
        )
        print(description)

    @staticmethod
    def greeting():
        design = f"{ConsoleMessages.MAGENTA}+++++=====+++++=====+++++"
        message = (
            f"\n1. See individual entryDate detail of duplicates vs output, and list of duplicate entries.\n"
            f"2. Find your deduplicated file, as well as a copy of your source file and a file containing the entries that were removed (just in case you need them)."
        )
        print(f"\n{design}{ConsoleMessages.YELLOW}JSON DEDUPLICATION MACHINE{design}{message}{ConsoleMessages.RESET}")

    @staticmethod
    def files():
        design = f"{ConsoleMessages.MAGENTA}+++++=====+++++"
        print(f"\n{design}{ConsoleMessages.YELLOW}FILE OUTPUT{design}{ConsoleMessages.RESET}")

    @staticmethod
    def duplicate_entry(prop, value_existing, value_current, dupe_value):
        string = (
            f"{ConsoleMessages.CYAN}----------Duplicate {ConsoleMessages.RED}{prop}{ConsoleMessages.CYAN} value found: {dupe_value}----------{ConsoleMessages.RESET}"
        )
        existing = f"{ConsoleMessages.GREEN}entryDate of more recent _id: {value_existing}{ConsoleMessages.RESET}"
        current = f"{ConsoleMessages.RED}entryDate of _id to be removed: {value_current}{ConsoleMessages.RESET}"
        print(f"\n{string}\n{existing}\n{current}")

    @staticmethod
    def error_log(action):
        string = (
            f"{ConsoleMessages.GREEN}An error occurred while {ConsoleMessages.RED}{action}{ConsoleMessages.GREEN}. "
            f"Please check your resources and try again.{ConsoleMessages.RESET}"
        )
        print(string)
