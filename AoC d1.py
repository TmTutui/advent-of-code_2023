# %%
import regex as re

# %% V1
f = open("input.txt", "r")

def v1(f):
    calibration_values = []

    for line in f:
        line_numbers = re.findall(r"[0-9]+", line)
        line_numbers = ''.join(line_numbers)
        calibration_value = line_numbers[0] + line_numbers[-1]
        
        calibration_values.append(int(calibration_value))

    return sum(calibration_values)

print(v1(f))

# %% V2
string_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def v2_wrong(f):
    """
    the problem is that words may overlap: 
    i.e. nineight, and eight will be replaced first, where nine should be first
    """
    text = f.read()

    for key in string_number:
        text = text.replace(key, string_number[key])

    text = text.split('\n')

    return v1(text[:-1])

# %%
def v2_wrong2(f):
    # is not ordering correctly the numbers in number_string
    calibration_values = []

    ## Sliding window
    for line in f:
        line_numbers = []

        substr = ''
        for char in line:
            if(char.isnumeric()):
                line_numbers.append(char)
                substr = ''
                continue
            
            substr += char

            number_string = [string_number[number] for number in string_number if number in substr]

            if(len(number_string) > 0):
                line_numbers.append(number_string[0])
                
                # Not sure if when number overlap both are valid
                substr = ''
        
        
        calibration_value = line_numbers[0] + line_numbers[-1]
        
        # calibration_values.append(''.join(line_numbers))#int(calibration_value))
        calibration_values.append(int(calibration_value))

    return sum(calibration_values)
    # print(sum(calibration_values))
    # return calibration_values


def v2(f):
    calibration_values = []
    regex = '|'.join(string_number.keys()) + "|[0-9]"

    for line in f:
        line_numbers = re.findall(regex, line, overlapped=True)
        line_numbers = ''.join([
            number 
            if number.isnumeric() 
            else string_number[number]
            for number in line_numbers
        ])
        
        calibration_value = line_numbers[0] + line_numbers[-1]
        
        # calibration_values.append(line_numbers)#int(calibration_value))
        calibration_values.append(int(calibration_value))


    return sum(calibration_values)
    # return calibration_values


f = open("input.txt", "r")
print(v2(f))
# list1 = v2(f)
# f = open("input.txt", "r")
# list2 = v2_wrong2(f)
#compare results
#[(index, pair) for index, pair in enumerate(zip(list1, list2)) if pair[0] != pair[1]]
# %%



# %%
