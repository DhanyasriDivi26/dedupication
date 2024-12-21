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
    
    return deduplicated_data, removed_entries