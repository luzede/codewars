# link: https://www.codewars.com/kata/520446778469526ec0000001

# description: Complete the function/method (depending on the language) to return true/True when 
#              its argument is an array that has the same nesting structures and same corresponding 
#              length of nested arrays as the first array.


def same_structure_as(original,other):
    if isinstance(original, list) and isinstance(other,list) and len(original) == len(other):
        for i in range(len(original)):
            if not same_structure_as(original[i], other[i]):
                return False
        return True
    elif not isinstance(original, list) and not isinstance(other, list):
        return True
    else:
        return False
