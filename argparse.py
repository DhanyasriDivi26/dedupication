#.py
import json
from datetime import datetime
from collections import defaultdict
from dateutil import parser
import argparse
from filter import FilterUtils

	
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