print("Enter your pyramid height")
height = input()



def build_pyramid_with_given_height(height):
    if height.isdigit() == True:
        height = (int(height))
        star = '*'
        space = ' '
        times = height
        for i in range(height):
            print(space*times + star)
            star = star + '**'
            times = times-1
    else:
        print("Invalid input")

build_pyramid_with_given_height(height)