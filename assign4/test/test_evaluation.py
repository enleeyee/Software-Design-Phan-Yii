import unittest
import sys
sys.path.append('src')
from application import Application
from processor.evaluation import process_applicant
from status import Status

class TestApplicantEvaluation(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)


    def test_evaluate_applicant(self):
        self.assertEqual((Status.PASS, "Nothing to check"), process_applicant(Application()))


    def test_evaluate_employment_pass(self):
        employment_check = lambda application: (Status.PASS, "Applicant has had previous employment.")

        self.assertEqual((Status.PASS, "Applicant has had previous employment."), process_applicant(Application(), employment_check))


    def test_evaluate_employment_fail(self):
        employment_check = lambda application: (Status.FAIL, "Applicant has no previous employment.")

        self.assertEqual((Status.FAIL, "Applicant has no previous employment."), process_applicant(Application(), employment_check))


    def test_evaluate_employment_pass_criminal_record_pass(self):
        employment_check = lambda application: (Status.PASS, "Application has had previous employment.")
        criminal_record_check = lambda application: (Status.PASS, "Application has had no criminal records.")
       
        self.assertEqual((Status.PASS, "Application has had previous employment. Application has had no criminal records."), process_applicant(Application(), employment_check, criminal_record_check))
        

    def test_evaluate_employment_fail_criminal_record_pass(self):
        employment_check = lambda application: (Status.FAIL, "Application has no previous employment.")
        criminal_record_check = lambda application: (Status.PASS, "Application has had no criminal records.")
       
        self.assertEqual((Status.FAIL, "Application has no previous employment. Application has had no criminal records."), process_applicant(Application(), employment_check, criminal_record_check))
        
        
    def test_evaluate_employment_fail_criminal_record_fail(self):
        employment_check = lambda application: (Status.PASS, "Application has had previous employment.")
        criminal_record_check = lambda application: (Status.FAIL, "Application has criminal records.")
       
        self.assertEqual((Status.FAIL, "Application has had previous employment. Application has criminal records."), process_applicant(Application(), employment_check, criminal_record_check))
        