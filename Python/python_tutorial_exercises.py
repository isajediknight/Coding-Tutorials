# Created By Luke on 06/14/2017
# Simple exercises for KCIT's to work through to learn Python

# To print a * without a new line:
# print('*',end='')

# To run your code use the following command:
# from python_tutorial_exercises import exercise_1
# exercise_1()

def exercise_0():
    """
    Use a For Loop to print 5 lines with a star on each line

    Expected Result:
    *
    *
    *
    *
    *
    """
    for x in range(0,5):
        print('*')

def exercise_1():
    """
    Use a For Loop to print 1 line with 5 *'s on it

    Expected Result:
    ******
    """
    for x in range(0,5):
        print('*',end='')

def exercise_2():
    """
    Use a For Loop to print 5 lines with 5 stars on each line

    Expected Result:
    *****
    *****
    *****
    *****
    *****
    """
    for x in range(0,5):
        print('*')

def exercise_3():
    """
    Use a For Loop to print 5 lines
    The first list has 1 *
    The second line has 2 *'s

    Expected Result:
    *
    **
    ***
    ****
    *****
    """
    for x in range(0,5):
        print('*')

def exercise_4():
    """
    Use a For Loop to print 5 lines
    The first line has 5 *'s
    The second line has 4 *'s

    Expected Result:
    *****
    ****
    ***
    **
    *
    """
    for x in range(0,5):
        print('*')

def exercise_5(number_of_lines):
    """
    Use a For Loop to print a user number of specified lines with a star

    Expected Result
    exercise_5(2)

    *
    *

    exercise_5(3)

    *
    *
    *
    """
    for x in range(0,5):
        print('*')

def exercise_6(triangle_height):
    """
    Use a For Loop to print a triangle that has a user specified hieght

    Expected Result

    exercise_6(3)

    *
    **
    ***

    exercise_6(1)

    *

    exercise_6(6)

    *
    **
    ***
    ****
    *****
    ******
    """
    for x in range(0,5):
        print('*')

def exercise_7(triangle_height):
    """
    Use a For Loop to print a triangle that has a user specified hieght

    Expected Result

    exercise_7(3)

    ***
    **
    *

    exercise_7(1)

    *

    exercise_7(6)

    ******
    *****
    ****
    ***
    **
    *
    """
    for x in range(0,5):
        print('*')

def exercise_8():
    """
    Use a For Loop to print only the even rowed number of *'s
    Start with 6 *'s

    Expected Result:
    ******
    ****
    **
    """
    for x in range(0,5):
        print('*')

def exercise_9():
    """
    Use a For Loop to print only the lines with a number divisible by 3
    Up to 9 *'s

    Epected Result:
    ***
    ******
    *********
    """
    for x in range(0,5):
        print('*')

# Warning - if the loop never finishes use CTRL-C to kill the process
# It is possible to make an infinite loop using a While Loop

def exercise_10():
    """
    Use a While Loop to print 5 lines with a star on each line

    Expected Result:
    *
    *
    *
    *
    *
    """
    counter = 0
    while(counter < 5):
        print('*')
        counter += 1

def exercise_11():
    """
    Use a While Loop to print 1 line with 5 *'s on it

    Expected Result:
    ******
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_12():
    """
    Use a While Loop to print 5 lines with 5 stars on each line

    Expected Result:
    *****
    *****
    *****
    *****
    *****
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_13():
    """
    Use a While Loop to print 5 lines
    The first list has 1 *
    The second line has 2 *'s

    Expected Result:
    *
    **
    ***
    ****
    *****
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_14():
    """
    Use a While Loop to print 5 lines
    The first line has 5 *'s
    The second line has 4 *'s

    Expected Result:
    *****
    ****
    ***
    **
    *
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_15(number_of_lines):
    """
    Use a While Loop to print a user number of specified lines with a star

    Expected Result
    exercise_15(2)

    *
    *

    exercise_15(3)

    *
    *
    *
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_16(triangle_height):
    """
    Use a While Loop to print a triangle that has a user specified hieght

    Expected Result

    exercise_16(3)

    *
    **
    ***

    exercise_16(1)

    *

    exercise_16(6)

    *
    **
    ***
    ****
    *****
    ******
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_17(triangle_height):
    """
    Use a While Loop to print a triangle that has a user specified hieght

    Expected Result

    exercise_17(3)

    ***
    **
    *

    exercise_17(1)

    *

    exercise_17(6)

    ******
    *****
    ****
    ***
    **
    *
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_18():
    """
    Use a While Loop to print only the even rowed number of *'s
    Start with 6 *'s

    Expected Result:
    ******
    ****
    **
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_19():
    """
    Use a While Loop to print only the lines with a number divisible by 3
    Up to 9 *'s

    Epected Result:
    ***
    ******
    *********
    """
    counter = 0
    while(counter < 5):
        print('*',end='')
        counter += 1

def exercise_20(times_to_call):
    """
    Use Recursion to to print 5 lines with a star on each line
    
    Expected Result:
    exercise_20(5)
    *
    *
    *
    *
    *
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_20(times_to_call-1)

def exercise_21(times_to_call):
    """
    Use Recursion to print 1 line with 5 *'s on it

    Expected Result:
    ******
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_21(times_to_call-1)

def exercise_22(times_to_call):
    """
    Use Recursion to print 5 lines with 5 stars on each line

    Expected Result:
    *****
    *****
    *****
    *****
    *****
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_22(times_to_call-1)

def exercise_23(times_to_call):
    """
    Use Recursion to print 5 lines
    The first list has 1 *
    The second line has 2 *'s

    Expected Result:
    *
    **
    ***
    ****
    *****
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_23(times_to_call-1)

def exercise_24(times_to_call):
    """
    Use Recursion to print 5 lines
    The first line has 5 *'s
    The second line has 4 *'s

    Expected Result:
    *****
    ****
    ***
    **
    *
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_24(times_to_call-1)

def exercise_25(times_to_call):
    """
    Use Recursion to print a user number of specified lines with a star

    Expected Result
    exercise_25(2)

    *
    *

    exercise_25(3)

    *
    *
    *
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_25(times_to_call-1)

def exercise_26(times_to_call,triangle_height):
    """
    Use Recursion to print a triangle that has a user specified hieght

    Expected Result

    exercise_26(3)

    *
    **
    ***

    exercise_26(1)

    *

    exercise_26(6)

    *
    **
    ***
    ****
    *****
    ******
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_26(times_to_call-1)

def exercise_27(times_to_call,triangle_height):
    """
    Use Recursion to print a triangle that has a user specified hieght

    Expected Result

    exercise_27(3)

    ***
    **
    *

    exercise_27(1)

    *

    exercise_27(6)

    ******
    *****
    ****
    ***
    **
    *
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_27(times_to_call-1)

def exercise_28(times_to_call):
    """
    Use Recursion to print only the even rowed number of *'s
    Start with 6 *'s

    Expected Result:
    ******
    ****
    **
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_28(times_to_call-1)

def exercise_29(times_to_call):
    """
    Use Recursion to print only the lines with a number divisible by 3
    Up to 9 *'s

    Epected Result:
    ***
    ******
    *********
    """
    if(times_to_call == 0):
        pass
    else:
        print('*')
        exercise_29(times_to_call-1)
