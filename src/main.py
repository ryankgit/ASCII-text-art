import json
import random
import string

VERT_ARR = ["|", "/", "\\", "}", "{"]
RAND_VERT_ARR = [
    "|",
    "/",
    "\\",
    "}",
    "{",
    "!",
    "#",
    "$",
    "&",
    "(",
    ")",
    "?",
    "@",
    "[",
    "]",
    ":",
    ";",
    "<",
    ">",
]
RAND_HOZ_ARR = [",", "-", ".", "=", "_", "~"]
# Check for appropriate characters


def validate_input_str(input_str):
    for i in input_str:
        if i not in string.ascii_lowercase:
            return False
    return True


# Check the input
def validate_input(input_str):
    if input_str:
        try:
            assert validate_input_str(input_str)
        except AssertionError:
            raise ValueError(
                "Input has incorrect characters "
                f"{string.digits} or {string.punctuation} (actual) : {input_str}"
            )


# Builds ascii text art based on input string - reads ascii_text.json.
def buildASCII(input_str):
    validate_input(input_str)
    input_arr = [char for char in input_str]
    line = ""

    with open("src/ascii_text.json") as json_file:
        data = json.load(json_file)

        # each char in ascii_text.json is an array of 6 strings
        for i in range(6):
            for element in input_arr:
                str_sec = data[element][i]
                # line += randOutln(str_sec)
                # line += randBkgd(str_sec, ['.'])
                line += str_sec

                # prints for debugging
                # print(str_sec)
                # pos_arr = getSecElmts(str_sec)
                # print(pos_arr)
                # print('\n')

            line += "\n"

    # print in console for proof of concept
    print(line)


# Replaces standard outline characters w/ random
# characters from RAND_HOZ_ARR and RAND_VERT_ARR.
def randOutln(str_sec):
    sec_arr = [char for char in str_sec]

    for index, element in enumerate(sec_arr):
        if not element.isspace():
            if element == "_":
                sec_arr[index] = random.choice(RAND_HOZ_ARR)
            else:
                sec_arr[index] = random.choice(RAND_VERT_ARR)

    return "".join(sec_arr)


# Replaces standard background characters (spaces)
# with random pattern of passed in character(s).
# TODO: do not fill in elements, only fill bkgrd.
def randBkgd(str_sec, bkgd_arr):
    sec_arr = [char for char in str_sec]

    # determine need to randomly select from bkgd_arr
    multi_select = True
    if len(bkgd_arr) == 1:
        multi_select = False

    for index, element in enumerate(sec_arr):
        if element.isspace():
            if multi_select:
                sec_arr[index] = random.choice(bkgd_arr)
            else:
                sec_arr[index] = bkgd_arr[0]

    return "".join(sec_arr)


# TODO: Replaces standard fill characters (spaces)
# with random pattern of passed in character(s).
def randFill(str_sec):
    pass


# Returns arr that denotes where the borders/spaces in
# str_sec are. Return arr will be used as input in fillPos()
def getSecElmts(str_sec):
    pos_arr = []

    for index, element in enumerate(str_sec):
        if element.isspace():
            pos_arr.append(0)
        else:
            pos_arr.append(1)

    return pos_arr


# TODO: Determines if index should be filled with element.
# Will be used in randFill and randBkgrd.
# Takes getSecElmts() return arr as input
def fillPos(pos_arr, index):
    pass


def main():
    input_str = input("Enter text: ")
    # TODO: add rand options here, or begin implementation of gui or webpage.
    buildASCII(input_str.lower())


if __name__ == "__main__":
    main()
