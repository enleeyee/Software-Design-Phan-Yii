import unittest
import sys
sys.path.append('src')
from application import Application
from criteria.criminal_records import criminal_records
from status import Status

class TestCriminalRecords(unittest.TestCase):

    def test_criminal_records_passes_applicant(self):
        no_criminal_record_application = Application();
        no_criminal_record_application.criminal_record = False

        self.assertEqual((Status.PASS, "Application has had no criminal records."), criminal_records(no_criminal_record_application))


    def test_criminal_records_fails_applicant(self):
        criminal_record_application = Application();
        criminal_record_application.criminal_record = True

        self.assertEqual((Status.FAIL, "Application has criminal records."), criminal_records(criminal_record_application))
