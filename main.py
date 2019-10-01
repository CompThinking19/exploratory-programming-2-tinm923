#numPositive accept one parameter, expecting type list
def numPositive(arg):
    #if arg is not a list print TypeError
    if type(arg) != list:
        raise TypeError("Argument is not a list!")
    #count the number of positives
    count = 0
    #traverse the list and add to count if element is positive
    for element in arg:
        if (element > 0):
            count += 1
    #return the count of positive numbers in list
    return count

#Case 1 - call function with a list
numPositive([-1,-2,-3,1,2,3,4,5,6])
#Case 2 - call function with a string
numPositive("Hello World!")
