def fizzBuzz(start, stop, numList=[]):
    """
    Returns a list of integer values from start to stop except where:
    integer is a multiple of 3 it is replaced by the word FIZZ
    integer is a multiple of 5 it is replaced by the word BUZZ
    integer is a multiple of 3 and 5 it is replaced by the word FIZZBUZZ
    
    start: integer > 0
    stop: integer > 0 and > start
    returns: list
    """
    answer = 0
    if start > stop:
        return numList
    
    if start%3 == 0:
        answer = answer + 1
    if start%5 == 0:
        answer = answer + 2
    
    if answer == 0:
        numList.append(start)
    elif answer == 1:
        numList.append('FIZZ')
    elif answer == 2:
        numList.append('BUZZ')
    elif answer == 3:
        numList.append('FIZZBUZZ')
    
    return fizzBuzz(start + 1, stop)