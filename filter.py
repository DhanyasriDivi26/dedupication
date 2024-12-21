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