import unittest
import datetime as dt
from UserPrompt import get_symbol, get_chart_type, get_time_series, get_start_date, get_end_date

class Testing1(unittest.TestCase):

    # symbol: capitalized, 1-7 alpha characters
    def test_symbol_capitalized(self):
        result = get_symbol()
        self.assertEqual(result.isalpha(), True)
        self.assertGreaterEqual(len(result), 1, True)
        self.assertLessEqual(len(result), 7)
        self.assertTrue(result.isupper(), True)
        self.assertEqual(result.isalpha(), True)

    # chart type: 1 numeric character, 1 or 2
    def test_chart_type_valid(self):
        choice = get_chart_type()
        self.assertGreaterEqual(choice, 1, True)
        self.assertLessEqual(choice, 2, True)
        self.assertEqual(type(choice), int, True)
        
    # time series: 1 numeric character, 1 - 4
    def test_time_series_valid(self):
        choice = get_time_series()
        self.assertGreaterEqual(choice, 1, True)
        self.assertLessEqual(choice, 4, True)
        self.assertEqual(type(choice), int, True)

    # start date: date type YYYY-MM-DD.  Our function is built to retune as a string
    def test_start_date_valid(self):
        start_date = get_start_date()
        self.assertEqual(type(start_date), str, True)
        self.assertEqual(len(start_date), 10, True)
        self.assertEqual(start_date[4], "-", True)
        self.assertEqual(start_date[7], "-", True)

    # end date: date type YYYY-MM-DD.  Our function is built to retune as a string
    def test_end_date_valid(self):
        start_date = get_start_date()
        end_date = get_end_date(start_date)
        self.assertEqual(type(end_date), str, True)
        self.assertEqual(len(end_date), 10, True)
        self.assertEqual(end_date[4], "-", True)
        self.assertEqual(end_date[7], "-", True)
        self.assertGreaterEqual(end_date, start_date, True)
    

if __name__ == '__main__':
    unittest.main()
    