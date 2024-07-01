# link: https://www.codewars.com/kata/52597aa56021e91c93000cb0

# description: Write an algorithm that takes an array and moves all of the zeros to the end,
#              preserving the order of the other elements.



def move_zeros(lst):
    new_lst = []
    zero_count = 0
    for v in lst:
        if v == 0:
            zero_count += 1
        else:
            new_lst.append(v)
    for _ in range(zero_count):
        new_lst.append(0)
    return new_lst
