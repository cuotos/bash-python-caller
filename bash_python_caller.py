#!/usr/bin/env python

import sys
import os
import inspect
import functions as fs

# this method is called if another doesnt exist with the name the user called
def default():
    print("no method found {}".format(os.path.basename(__file__)))
    sys.exit(1)


def get_pydoc(f):
    if not f.__doc__:
            return "warning: function contains no documentation"
    else:
        return f.__doc__


def main(a, f):
    # if the only argument is a question mark, print the python doc for that fuction
    if (len(a) == 2) and (a[1] == "?"):
        return [get_pydoc(f)]

    expectedArgs = inspect.getargspec(f).args
    # get the number of arguments that the function is expecting
    numberOfOptionalArgs = len(inspect.getargspec(f).defaults) if inspect.getargspec(f).defaults > 0 else 0 # number of args expected
    minNumberOfArgumentsReq = len(inspect.getargspec(f).args) - numberOfOptionalArgs # number of args expected, minus optional / default ones
    maxNumberOfArgumentsReq = len(inspect.getargspec(f).args) # total / max number of arguments a function can take

    # make sure the user has passed enough arguments to satisfy the function being called.
    # remove one from the number to account for element 0 being the name of the program iteself
    numberOfProvidedArgs = len(a) - 1 

    if (numberOfProvidedArgs < minNumberOfArgumentsReq) or (numberOfProvidedArgs > maxNumberOfArgumentsReq) :
        raise Exception('''
            invalid arguments, expected between {} and {}, but got {}
            expected "{}"'''.format(minNumberOfArgumentsReq, maxNumberOfArgumentsReq, numberOfProvidedArgs, '", "'.join(expectedArgs)))
    else:
        # rename for the sake of sanity
        n = numberOfProvidedArgs

        if n == 0:
            f_output = f()
        elif n == 1:
            f_output = f(a[1])
        elif n == 2:
            f_output = f(a[1], a[2])
        elif n == 3:
            f_output = f(a[1], a[2], a[3])
        elif n == 4:
            f_output = f(a[1], a[2], a[3], a[4])
        elif n == 5:
            f_output = f(a[1], a[2], a[3], a[4], a[5])
        elif n == 6:
            f_output = f(a[1], a[2], a[3], a[4], a[5], a[6])
        elif n == 7:
            f_output = f(a[1], a[2], a[3], a[4], a[5], a[6], a[7])
        elif n == 8:
            f_output = f(a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8])
        elif n == 9:
            f_output = f(a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9])
        elif n == 10:
            f_output = f(a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9], a[10])
        else:
            raise Exception("too many arguments. maximum of 10 supported")

    if not isinstance(f_output, list):
        raise Exception("ERROR: functions should always return a list")

    return f_output


if __name__ == "__main__":    
    # get function name that matches the executable that was called "the symlink pointing to this script".
    f = getattr(fs, os.path.basename(__file__))

    try:
        output = main(sys.argv, f)
        print(" ".join(output))
    except Exception as e:
        print(e)
        sys.exit(1)
