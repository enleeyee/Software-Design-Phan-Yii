import unittest
import sys
sys.path.append('src')
from application import Application
from criteria.security_clearance import security_clearance
from status import Status

class TestSecurity_Clearance(unittest.TestCase):
    def test_security_clearance_passes_applicant(self):
        cleared_application = Application();
        cleared_application.security_clearance = True

        self.assertEqual((Status.PASS, "Applicant has security clearance."), security_clearance(cleared_application))


    def test_security_clearance_fails_applicant(self):
        uncleared_application = Application();
        uncleared_application.security_clearance = False

        self.assertEqual((Status.FAIL, "Applicant has no security_clearance."), security_clearance(uncleared_application))
