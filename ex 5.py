def build_pyramid():
    star = '*'
    space = ' '
    times = 5
    for i in range(5):
        print(space*times + star)
        star = star + '**'
        times = times-1

build_pyramid()