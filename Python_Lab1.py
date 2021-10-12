#Exercise 1: Miles Converter
def kms_to_miles_converter():
    while True:
        try:
            distance = abs(float(input('What is the distance in miles?')))
            miles = distance * 0.6214
            return ("%.2f miles equals %.2f kilometres" % (distance, miles)) # expected result
        except ValueError:
            print('Use numeric symbols!') # returns to the input

kms_to_miles_converter()
#Exercise 2: Property Tax
def property_tax():
    while True:
        try:
            actual_value = float(input('What is the book value of your asset? (USD):'))
            if actual_value >= 0:
                assessment_value = actual_value * 0.6
                property_tax = assessment_value / 100 * 72 /100
                return ("The assessment value is %.2f, the tax is %.2f USD" % (assessment_value, property_tax)) # expected result
            else:
                print('Please enter a positive number:')
        except ValueError:
            print('Use numeric symbols!') # returns to the input

property_tax()

#Exercise 3: Maximum of Two Values
    # accepts 2 int arguments
    # displays the greater of two
    # prompts user to enter 2 int values
def maximum_of_two(value1 = None, value2 = None): # two arguments by default
    while True:
        try:
            if (not isinstance(value1, int) and not isinstance(value2, int)): # check if user did not provide any arguments
                arg_missing1 = input('Please enter the first integer number:')
                arg_missing2 = input('Please enter the second integer number:')
                return max(int(arg_missing1), int(arg_missing2))
            elif (not isinstance(value1, int)): # check if 1st value is missing
                arg_missing1 = input('The second integer number is %i, please enter the first integer number:' % (value2))
                return max(int(arg_missing1), int(value2))
            elif (not isinstance(value2, int)):# check if 2nd value is missing
                arg_missing2 = input('The first integer number is %i, please enter the second number:' % (value1))
                return max(int(value1), int(arg_missing2))

            else:
                return max(value1, value2)
        except ValueError:
            print("Values should be integers.")

#maximum_of_two(3)
#maximum_of_two(1.2, 2.2)
#maximum_of_two(1.2, 2)


#Exercise 4: Test Average and Grade
    # enter five test scores
    # display a letter grade for each score and the average test score
    # "calc_average"- This function should accept five test scores as arguments and return the average of the scores.
    # "determine_grade"- This function should accept a test score as an argument and return a letter grade for the score.
import pandas as pd
import numpy as np

scores_variants = list(range(101))
letters_variants =list("F" * 60 + "D" * 10 + "C" * 10+ "B" * 10 + "A" * 11)
scores_to_letters_df = pd.DataFrame(list(zip(scores_variants, letters_variants)), columns = ['Score', 'Letter_Grade']) # DataFrame to define grade letters

    # defining the function "calc_average()"
def calc_average(mark1 = None, mark2= None, mark3= None, mark4= None, mark5= None): # the function returns the average of integers
        marks = [mark1, mark2, mark3, mark4, mark5]
        global test_scores
        test_scores = list() # test scores will be furhter transfered to the "determine_grade(test_scores)"
        for mark in marks: # loop over the list of numeric marks
            if (isinstance(mark, int) and 0<= mark <= 100): #check if all arguments provided are integers
                test_scores.append(mark)
            else:
                while not isinstance(mark, int) or not 0<= mark <= 100: # repeat untill user enters proper value instead
                    try:
                        mark = int(input('Please enter the mark (%i/5):' % (len(test_scores)+1))) # input the mark
                        if 0<= mark <= 100: 
                            test_scores.append(mark) # append if integer from 0 to 100, then next missed value
                        elif mark <0:
                            print('Your mark cannot be negative! Try again:') # in case user enters a negative integer
                        else:
                            print('Mark should be an integer in a range (0:100)')
                    except ValueError:
                        print('Mark should be an integer in a range (0:100)') # in case user enters not integer
        #print(test_scores)
        return(np.mean(test_scores)) # returns nean score
        

#calc_average(10, 20, 30, 60, 80) # how it should normally work (UNCOMMENT TO TRY)
#calc_average(10, "Zhoka", 30.6, -60, "Boka") # how it works some arguments are invalid (UNCOMMENT TO TRY)
#calc_average(10, 20, 30, 60) # how it works if one argument is missing (UNCOMMENT TO TRY)
#calc_average(10, 20, 30, 60, 70, 90) # providing 6 arguments generates an error (UNCOMMENT TO TRY)

    # defining the function "determine_grade()"
def determine_grade(score): # This function accepts test score and returns a corresponding letter
        Letter = scores_to_letters_df.loc[scores_to_letters_df["Score"] == score, 'Letter_Grade'].iloc[0]
        print("For the score %i your mark is %s" % (score, Letter))

# determine_grade(50) # this function works separately on each mark provided
    ## let's test the program!

calc_average(10, 60, 69, 81, 95) # test 

for score in test_scores: # loop over test scores
    determine_grade(score)