from status import Status

def credit_records(application):
    return (Status.PASS, "Application has credit records.") if application.credit_record else (Status.FAIL, "Application has no credit records.")
