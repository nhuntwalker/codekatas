# Given an integer, write a function to determine if it is a power of three.
# follow up: can you do it without using any loop/recursion?

def power_of_three(x):
    # if is power of three, return True
    # if is not, return False

    # What are some checks on this?
    # - It must be divisible by 3
    # - If you test divisions by powers of three, then each result should be
    #   an integer until you reach the same power as the number, which should
    #   return one, then decimals...not a good check
    # - USE A LOG BASE 3!
    from math import log
    if log(x, 3) == int(log(x, 3)):
        return True

    else:
        return False

print power_of_three(6)
print power_of_three(9)
print power_of_three(81)
print power_of_three(123)
print power_of_three(59049)

# What about without importing anything?
def power_of_three2(x):
    if x == 1:
        return True

    elif (x < 3) and (x != 1):
        return False

    elif x == 3:
        return True

    elif (x/3) == (x/3.):
        return power_of_three2(x/3)

    else:
        return False

print power_of_three2(6)
print power_of_three2(9)
print power_of_three2(81)
print power_of_three2(123)
print power_of_three2(59049)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        test_vers = sys.argv[1]

    else:
        test_vers = 0
