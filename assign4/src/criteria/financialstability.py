from status import Status

def financialstability(application):
    return (Status.PASS, "Applicant is good financially.") if application.past_employment or application.credit_record else (Status.FAIL, "Applicant not good financially.")
