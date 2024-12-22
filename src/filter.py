import json
from datetime import datetime
import dateUtils
import logging
from collections import defaultdict

class FilterUtils:
    @staticmethod
    def filter_for_dupes(arr, prop, id):
        obj = {}

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
            if isinstance(entry, dict) and prop in entry:
                def filter_entry():
                    logging.ConsoleMessages.append_reason(obj[object_property][entry[prop]][0], reason)
                    logging.ConsoleMessages.duplicate_entry(prop, existing, current, entry[prop])
                    obj[dupe_string][entry[prop]].append(obj[object_property][entry[prop]].pop())
                    obj[object_property][entry[prop]].append(entry)

                if entry[prop] not in obj[object_property]:
                    obj[object_property][entry[prop]] = [entry]
                else:
                    existing = obj[object_property][entry[prop]][0]['entryDate']
                    current = entry['entryDate']
                    if dateUtils.Choose.is_same(existing, current) or dateUtils.Choose.is_before(existing, current):
                        if obj[dupe_string][entry[prop]]:
                            filter_entry()
                        else:
                            obj[dupe_string][entry[prop]] = []
                            filter_entry()
                    else:
                        logging.ConsoleMessages.append_reason(entry, reason)
                        logging.ConsoleMessages.duplicate_entry(prop, existing, current, entry[prop])
                        obj[dupe_string][entry[prop]].append(entry)
                        continue
            else:
                print(f"Skipping invalid entry: {entry}")

        return obj