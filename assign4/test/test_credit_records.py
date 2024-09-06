import unittest
import sys
sys.path.append('src')
from application import Application
from criteria.credit_records import credit_records
from status import Status

class TestCreditRecords(unittest.TestCase):

    def test_credit_records_passes_applicant(self):
        credited_application = Application();
        credited_application.credit_record = True

        self.assertEqual((Status.PASS, "Application has credit records."), credit_records(credited_application))


    def test_credit_records_fails_applicant(self):
        no_credited_application = Application();
        no_credited_application.credit_record = False

        self.assertEqual((Status.FAIL, "Application has no credit records."), credit_records(no_credited_application))
