print("Enter your pyramid height")
height = input()

def build_pyramid_with_given_height(height):
    star = '*'
    space = ' '
    times = height
    for i in range(height):
        print(space*times + star)
        star = star + '**'
        times = times-1

build_pyramid_with_given_height(height)