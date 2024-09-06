import unittest
import sys
sys.path.append('src')
from processor.criteria_loader import fetch_criterion
from criteria.employment import employment
from criteria.criminal_records import criminal_records

class testCriteriaLoader(unittest.TestCase):
    def test_fetch_employment_criteria(self):
        employment_criterion = fetch_criterion("employment")
        
        self.assertEqual(employment_criterion, employment)

    def test_fetch_criminal_records_criteria(self):
        criminal_records_criterion = fetch_criterion("criminal_records")
       
        self.assertEqual(criminal_records_criterion, criminal_records)
        