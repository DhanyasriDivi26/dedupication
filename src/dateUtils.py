import json
from datetime import datetime
from collections import defaultdict
from dateutil import parser
import main


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
