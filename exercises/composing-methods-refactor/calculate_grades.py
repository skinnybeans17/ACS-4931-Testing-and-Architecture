# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

    # Calculate the mean and standard deviation of the grades
def calculate_mean(grade_list):
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        total += grade
    return 1 * total / len(grade_list)

def calculate_sd(grade_list, mean):
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    return math.sqrt(sum_of_sqrs / len(grade_list))

def print_grade():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))

    mean = calculate_mean(grade_list)
    sd = calculate_sd(grade_list, mean)

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_grade()
