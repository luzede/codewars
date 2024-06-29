# link: https://www.codewars.com/kata/526989a41034285187000de4

# description: Implement a function that receives two IPv4 addresses,
#              and returns the number of addresses between them (including
#              the first one, excluding the last one).

def ips_between(start, end):
    start = [int(v) for v in start.split(".")]
    end = [int(v) for v in end.split(".")]
    diff = [end[i] - start[i] for i in range(4)]
    number_of_ips = 0
    for i in range(4):
        number_of_ips += diff[i]*pow(256, 3 - i)
    return number_of_ips
