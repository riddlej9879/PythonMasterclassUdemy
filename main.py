from section_03 import *


def print_hi(name):
    num = 1
    # print(f'Hi, {name}')
    hello_world()
    for x in range(47):
        num = num + (num-1)
        # print("num")
    print(num)


if __name__ == '__main__':
    print_hi('PyCharm')
