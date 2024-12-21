class FormatUtils:
    @staticmethod
    def format_array(arr):
        formatted = [{key: value for key, value in item.items()} for item in arr]
        return formatted

def flatten_dict_values(data):
    return [entry for sublist in data.values() for entry in sublist]

def deduplicate(entries):
    filter_utils = FilterUtils()
    filtered_by_id = filter_utils.filter_for_dupes(entries, '_id', True)
    filtered_by_email = filter_utils.filter_for_dupes(flatten_dict_values(filtered_by_id['output_data_id']), 'email', False)
    deduplicated_data = flatten_dict_values(filtered_by_email['output_data_email'])
    removed_entries = flatten_dict_values(filtered_by_email['duplicate_data'])
    
    return deduplicated_data, removed_entries