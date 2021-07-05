from random import randint

def gen_n_digits(number):
    """
        generate number of digits
    """
    range_start = 10**(number-1)
    range_end = (10**number)-1
    return randint(range_start, range_end)