from status import Status

def security_clearance(application):
    return (Status.PASS, "Applicant has security clearance.") if application.security_clearance else (Status.FAIL, "Applicant has no security_clearance.")
