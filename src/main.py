#.py
import json
import sys
import format
from datetime import datetime
from collections import defaultdict


# Load and process the data
def main():

    if len(sys.argv) != 2:
        print("Usage: python script.py leads.json")
        sys.exit(1)

    fname = sys.argv[1]

    try:
        with open(fname, "r") as file:
            leads_data = json.load(file)

        entries = leads_data["leads"]
        deduplicated_data, removed_entries = format.deduplicate(entries)
        print("Deduplicated Data:")
        print(json.dumps(deduplicated_data, indent=4))

        print("\nRemoved Entries:")
        print(json.dumps(removed_entries, indent=4))


        # Save the deduplicated data in putput file.
        with open("output.txt", "w") as outfile:
            json.dump({"leads": deduplicated_data}, outfile, indent=2)

        with open("removed_entries.txt", "w") as removed_file:
            json.dump({"removed": removed_entries}, removed_file, indent=2)

        print(f"Deduplication complete. Output saved to output.txt")
        print(f"Removed entries saved to removed_entries.txt.")

    except FileNotFoundError:
        print(f"Error: 'leads.json' file not found.")
    except ValueError as e:
        print(f"Error in input data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()