
num = 3

def is_even(number):
    if isinstance(number, int) == True:
        if number == num:
            print("True")
            return True
        else:
            print("False")
            return False
    else:
        print ("This is NOT an integer")
        exit()

is_even(5)
