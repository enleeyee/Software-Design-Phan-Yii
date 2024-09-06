from status import Status
from functools import reduce

def process_applicant(application, *criteria): 
    if not criteria:
        return (Status.PASS, "Nothing to check")

    return reduce(merge_responses, map(lambda criterion: criterion(application), criteria))


def merge_responses(response1, response2):
    (status1, message1), (status2, message2) = response1, response2

    return Status.PASS if status1 == status2 == Status.PASS else Status.FAIL, f"{message1} {message2}"
