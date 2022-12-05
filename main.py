# Validation module
from validation import employee

if __name__ == '__main__':
    print(employee.validateName("Vineeth Kumar"))
    print(employee.validateMobileNumber("1234567890"))
    print(employee.validateEmailAddress("kommavineethkumar@gmail.com"))
    print(employee.validateAddress("7-136, Sri Nagar Colony"))
