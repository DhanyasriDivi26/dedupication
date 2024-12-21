#.py
import json
from datetime import datetime
from collections import defaultdict
from dateutil import parser
import argparse

# Choose class for date comparisons
class Choose:
    @staticmethod
    def is_before(date1, date2):
        date1_parsed = parser.parse(date1) if isinstance(date1, str) else date1
        date2_parsed = parser.parse(date2) if isinstance(date2, str) else date2
        return date1_parsed < date2_parsed

    @staticmethod
    def is_same(date1, date2):
        date1_parsed = parser.parse(date1) if isinstance(date1, str) else date1
        date2_parsed = parser.parse(date2) if isinstance(date2, str) else date2
        return date1_parsed == date2_parsed


# Placeholder LogUtils class for logging
# class LogUtils:
#     @staticmethod
#     def append_reason(entry, reason):
#         print(f"Reason for removal: {reason} - {entry}")

#     @staticmethod
#     def duplicate_entry(prop, existing, current, dupe_value):
#         print(f"Duplicate {prop} value found: {dupe_value}")
#         print(f"Existing entryDate: {existing}")
#         print(f"Current entryDate: {current}")
class ConsoleMessages:
    # ANSI escape codes for colors
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'  # Resets to default color

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



# Example Usage
# if __name__ == "__main__":
#     LogUtils.greeting()
#     obj = {"_id": "abcd1234", "entryDate": "2024-12-19"}
#     updated_obj = LogUtils.append_reason(obj, "Duplicate entry detected and removed.")
#     print(updated_obj)
#     LogUtils.duplicate_entry("_id", "2024-12-18", "2024-12-19", "abcd1234")
#     LogUtils.summary_removed(obj, "_id")
#     LogUtils.error_log("processing the file")



# FilterUtils class to handle duplicate filtering
class FilterUtils:
    @staticmethod
    def filter_for_dupes(arr, prop, id):
        """
        Filters duplicates based on the provided property and identifier.

        Args:
            arr (list): List of dictionary entries to filter.
            prop (str): The property to check for duplicates (e.g., '_id' or 'email').
            id (bool): Flag indicating whether to use ID or email as a key.

        Returns:
            dict: Object containing filtered data and duplicates.
        """
        obj = {}

        # Initialize the output dictionary structure correctly
        if id:
            obj = {
                'output_data_id': defaultdict(list),
                'duplicate_id_data': defaultdict(list)
            }
            reason = "MORE RECENT ENTRY WITH SAME ID IN DATABASE"
            dupe_string = 'duplicate_id_data'
            object_property = 'output_data_id'
        else:
            obj = {
                'output_data_email': defaultdict(list),
                'duplicate_data': defaultdict(list)
            }
            reason = "MORE RECENT ENTRY WITH SAME EMAIL IN DATABASE"
            dupe_string = 'duplicate_data'
            object_property = 'output_data_email'

        for entry in arr:
            # Check if the entry is a dictionary and contains the 'prop' key
            if isinstance(entry, dict) and prop in entry:
                def filter_entry():
                    ConsoleMessages.append_reason(obj[object_property][entry[prop]][0], reason)
                    ConsoleMessages.duplicate_entry(prop, existing, current, entry[prop])
                    obj[dupe_string][entry[prop]].append(obj[object_property][entry[prop]].pop())
                    obj[object_property][entry[prop]].append(entry)

                # Ensure that obj[object_property] is initialized correctly
                if entry[prop] not in obj[object_property]:
                    obj[object_property][entry[prop]] = [entry]
                else:
                    existing = obj[object_property][entry[prop]][0]['entryDate']
                    current = entry['entryDate']
                    if Choose.is_same(existing, current) or Choose.is_before(existing, current):
                        if obj[dupe_string][entry[prop]]:
                            filter_entry()
                        else:
                            obj[dupe_string][entry[prop]] = []
                            filter_entry()
                    else:
                        LogUtils.append_reason(entry, reason)
                        LogUtils.duplicate_entry(prop, existing, current, entry[prop])
                        obj[dupe_string][entry[prop]].append(entry)
                        continue
            else:
                # Log a message for entries that are not dictionaries or lack the prop key
                print(f"Skipping invalid entry: {entry}")

        return obj

# from collections import defaultdict

# class FilterUtils:
#     @staticmethod
#     def filter_for_dupes(arr, prop, unique):
#         """
#         Filters duplicates in the array based on a specific property.

#         Args:
#             arr (list): List of dictionary entries.
#             prop (str): The property to check for duplicates (e.g., '_id', 'email').
#             unique (bool): Indicates if only unique values are allowed.

#         Returns:
#             dict: Object containing filtered data and duplicates.
#         """
#         result = {'filtered_data': [], 'duplicates': []}
#         seen = set()

#         for item in arr:
#             key = item.get(prop)
#             if key in seen:
#                 result['duplicates'].append(item)
#             else:
#                 seen.add(key)
#                 result['filtered_data'].append(item)

#         return result

class FormatUtils:
    @staticmethod
    def format_array(arr):
        """
        Formats the array as needed for further processing.

        Args:
            arr (list): List of dictionary entries to format.

        Returns:
            list: Formatted array.
        """
        # Example: Remove unwanted fields or clean the data.
        formatted = [{key: value for key, value in item.items()} for item in arr]
        return formatted


# Flatten deduplicated data function
def flatten_dict_values(data):
    return [entry for sublist in data.values() for entry in sublist]

# Main deduplication logic
def deduplicate(entries):
    filter_utils = FilterUtils()
    # Filter duplicates by '_id'
    filtered_by_id = filter_utils.filter_for_dupes(entries, '_id', True)
    # Filter duplicates by 'email' from the '_id' filtered data
    filtered_by_email = filter_utils.filter_for_dupes(flatten_dict_values(filtered_by_id['output_data_id']), 'email', False)

    # Flatten the final deduplicated data and removed entries
    deduplicated_data = flatten_dict_values(filtered_by_email['output_data_email'])
    removed_entries = flatten_dict_values(filtered_by_email['duplicate_data'])
    print(deduplicated_data)
    return deduplicated_data, removed_entries

	
import argparse
# Load and process the data
def main():
    parser = argparse.ArgumentParser(description="JSON Deduplication Tool")
    parser.add_argument("input_file", help="The input JSON file containing the data")
    #parser.add_argument("output_file", help="The output JSON file to save the deduplicated data")
    #parser.add_argument("--removed_file", help="Optional file to save removed entries", default=None)

    args = parser.parse_args()

    try:
        with open(args.input_file, "r") as file:
            leads_data = json.load(file)

        if "leads" not in leads_data or not isinstance(leads_data["leads"], list):
            raise ValueError("Input JSON file must contain a 'leads' key with a list of entries.")

        entries = leads_data["leads"]
        deduplicated_data, removed_entries = deduplicate(entries)
        print("Deduplicated Data:")
        print(json.dumps(deduplicated_data, indent=4))

        print("\nRemoved Entries:")
        print(json.dumps(removed_entries, indent=4))

        # Save the deduplicated data
    #     with open(args.output_file, "w") as outfile:
    #         json.dump({"leads": deduplicated_data}, outfile, indent=2)

    #     if args.removed_file:
    #         with open(args.removed_file, "w") as removed_file:
    #             json.dump({"removed": removed_entries}, removed_file, indent=2)

    #     print(f"Deduplication complete. Output saved to {args.output_file}.")
    #     if args.removed_file:
    #         print(f"Removed entries saved to {args.removed_file}.")

    # except FileNotFoundError:
    #     print(f"Error: '{args.input_file}' file not found.")
    # except ValueError as e:
    #     print(f"Error in input data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()