print("Enter your pyramid height")
height = input()

def build_pyramid_with_given_height_and_direction(height, direction):
    if height.isdigit() == True:
        height = (int(height))
        if height > 0:
            if direction == "up":
                star = '*'
                space = ' '
                times = height
                for i in range(height):
                    print(space*times + star)
                    star = star + '**'
                    times = times-1
            elif direction == "down":
                star = '*'
                space = ''
                times = height
                for i in reversed(range(height)):
                    print(space+star*(i+1)+ star*(i))
                    space = space+' '
            else:
                print("Invalid input")
        else:
            print("Invalid input")
    else:
        print("Invalid input")

build_pyramid_with_given_height_and_direction(height, "down")