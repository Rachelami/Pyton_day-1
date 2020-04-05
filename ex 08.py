
# I'm stuck

args = "x*x-x/x+x"
def solve_math(args,**kwargs):
    array = []
    a=[1,2,3,4,5]
    aa=0
    for i in args:
        if i == "*" or i == "-" or i == "/" or i == "+":
            array.append(i)
        elif i == "x":
            i = a[aa]
            aa= aa+1
            array.append(i)

    # str = ""
    # str.join(array)
    print(array)
solve_math("x*x-x/x+x", first=1, second=2)