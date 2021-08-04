# This program gets five test scores from the student
# then displays their average test score and grade

def main():
    # NEED TO ASK IN MAIN    
    print("Enter your exam scores")
    test1 = float(input("Enter score 1: "))
    test2 = float(input("Enter score 2: "))
    test3 = float(input("Enter score 3: "))
    test4 = float(input("Enter score 4: "))
    test5 = float(input("Enter score 5: "))

    # Calculate the Avereage
    average = calc_average(test1,test2,test3,test4,test5)

    # Calculate the grade
    grade1= determine_grade(test1)
    grade2= determine_grade(test2)
    grade3= determine_grade(test3)
    grade4= determine_grade(test4)
    grade5= determine_grade(test5)
    
    # Display results
    print("--------------------")
    print("You earned these grades on your exams") 
    print("Score\t Grade")
    print("--------------------")
    print(test1,"\t",grade1)
    print(test2,"\t",grade2)
    print(test3,"\t",grade3)
    print(test4,"\t",grade4)
    print(test5,"\t",grade5)
    print("********************")
    print("Your average exam score is",format(average, '.1f'), "points")
    
# Get the average
def calc_average(test1,test2,test3,test4,test5):
    average = (test1+test2+test3+test4+test5)/5
    return average

# Determine final grade based on average    
def determine_grade(test):
    if test >=90:
        score='A'
    elif test >=80:
        score='B'
    elif test >=70:
        score='C'
    elif test >=60:
        score='D'
    else:
        score='F'
    return score
        
main()
