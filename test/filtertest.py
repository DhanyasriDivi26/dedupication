
import unittest
from filter import Filter

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.test_data = [
            {
                '_id': '98719237198371',
                'email': "yes@no.maybe",
                'address': 'here',
                'name':'be',
                'entryDate':datetime(2024, 1, 1)
            },
            {
                '_id': '287598478947',
                'email': "how@now.cow",
                'address': 'there',
                'name':'ben',
                'entryDate':datetime(2023, 1, 1)

            },
            {
            	'_id': '98719237198371',
                'email': "yes@no.maybe",
                'address': 'here',
                'name':'berry',
                'entryDate':datetime(2024, 2, 1)
            }
        ]

    def test_returns_object(self):
        """Test that filterForDupes returns a dictionary object"""
        returned = Filter.filter_for_dupes(self.test_data, '_id', True)
        self.assertIsInstance(returned, dict)

    def test_returned_object_not_empty(self):
        """Test that returned dictionary has at least one key"""
        returned = Filter.filter_for_dupes(self.test_data, '_id', True)
        self.assertGreater(len(returned.keys()), 0)

    def test_duplicate_data(self):
    	filter_dups = Filter.filter_for_dupes(setUp, '_id',True)


    	assert 'output_data_id' in result
        assert 'duplicate_id_data' in result
        
      
        assert len(result['output_data_id']['98719237198371']) == 1
        assert result['output_data_id']['98719237198371'][0]['name'] == 'berry'
        assert len(result['duplicate_id_data']['98719237198371']) == 1
        assert result['duplicate_id_data']['98719237198371'][0]['name'] == 'be'

