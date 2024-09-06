import unittest
import sys
sys.path.append('src')
from application import Application
from criteria.employment import employment
from status import Status

class TestEmployment(unittest.TestCase):
    def test_employment_passes_applicant(self):
        employed_application = Application();
        employed_application.past_employment = True

        self.assertEqual((Status.PASS, "Applicant has had previous employment."), employment(employed_application))


    def test_employment_fails_applicant(self):
        unemployed_application = Application();
        unemployed_application.past_employment = False

        self.assertEqual((Status.FAIL, "Applicant has no previous employment."), employment(unemployed_application))
