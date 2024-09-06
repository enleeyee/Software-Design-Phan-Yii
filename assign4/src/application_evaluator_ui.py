from application import Application
from processor.criteria_loader import fetch_criterion
from processor.evaluation import process_applicant

def get_criteria_selection(available_criteria):
    while True:
        print("\nAvailable Criteria:")
        for i, criterion in enumerate(available_criteria, 1):
            print(f"{i}. {criterion}")
        
        selected = input("Select criteria by numbers (comma separated, e.g., 1,2): ")
        try:
            indices = map(int, selected.split(','))
            return [fetch_criterion(available_criteria[index - 1]) for index in indices]
        except (IndexError, ValueError):
            print("Invalid input. Please enter valid numbers separated by commas.")


def get_application_details():
    application = Application()
    application.past_employment = input("Has the applicant past employment? (yes/no): ").strip().lower() == 'yes'
    application.criminal_record = input("Does the applicant have a criminal record? (yes/no): ").strip().lower() == 'yes'
    application.credit_record = input("Does the applicant have a credit record? (yes/no): ").strip().lower() == 'yes'
    application.security_clearance = input("Does the applicant have security clearance? (yes/no): ").strip().lower() == 'yes'
    
    return application


print("Welcome to the Application Evaluation System!")
available_criteria = ['employment', 'criminal_records', 'credit_records', 'security_clearance']

criteria_functions = get_criteria_selection(available_criteria)

while True:
    application = get_application_details()
        
    result, message = process_applicant(application, *criteria_functions)
    print(f"\nEvaluation Result: {result.name}")
    print(f"Details: {message}")
        
    if input("\nWould you like to evaluate another application? (yes/no): ").lower() != 'yes':
        print("Thank you for using the Application Evaluation System. Goodbye!")
        break
