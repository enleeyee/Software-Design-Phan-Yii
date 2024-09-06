from status import Status

def criminal_records(application):
    return (Status.PASS, "Application has had no criminal records.") if not application.criminal_record else (Status.FAIL, "Application has criminal records.")
