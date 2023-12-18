#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:  #SETUP_EXCEPT
            if i > a:
                raise Exception("Too far")
            else:
                result = (a ** b) / i
        except:
            result = a + b
            break
    return result

