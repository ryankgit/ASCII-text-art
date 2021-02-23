import json

def buildASCII(input_str):
    input_arr = [char for char in input_str]

    line = ''

    with open('ascii_text.json') as json_file:
        data = json.load(json_file)
        for i in range(6):
            for char in input_arr:
                line += data[char][i]

            line += ('\n')

    return line

def main():
    input_str = input("Enter text: ")
    print(buildASCII(input_str.lower()))

if __name__ == '__main__':
    main()
