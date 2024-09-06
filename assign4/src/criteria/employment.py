from status import Status

def employment(application):
    return (Status.PASS, "Applicant has had previous employment.") if application.past_employment else (Status.FAIL, "Applicant has no previous employment.")
