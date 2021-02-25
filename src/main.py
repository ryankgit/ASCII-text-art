import json
import random

VERT_ARR = ['|','/','\\','}','{']
RAND_VERT_ARR = ['|','/','\\','}','{','!','#','$','&','(',')','?','@','[',']',':',';','<','>']

HOZ_ARR = ['_']
RAND_HOZ_ARR = [',','-','.','=','_','~']


def buildASCII(input_str):
    input_arr = [char for char in input_str]
    line = ''

    with open('src/ascii_text.json') as json_file:
        data = json.load(json_file)
        for i in range(6):
            for char in input_arr:
                # line += randOutln(data[char][i])
                line += data[char][i]
            line += ('\n')

    print(line)


def randOutln(str_sec):
    sec_arr = [char for char in str_sec]
    
    for index, char in enumerate(sec_arr):
        if not char.isspace():
            if char == '_':
                sec_arr[index] = random.choice(RAND_HOZ_ARR)
            else:
                sec_arr[index] = random.choice(RAND_VERT_ARR)

    return ''.join(sec_arr)


def randFill(str_sec):
    pass


def randBkgd(str_sec):
    pass


def main():
    input_str = input('Enter text: ')
    # add rand options here, or begin implementation of gui or webpage
    buildASCII(input_str.lower())


if __name__ == '__main__':
    main()


# TODO: implement randFill, randOutline, randBackground functions