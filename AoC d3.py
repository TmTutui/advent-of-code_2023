# %%
f = open("inputs/input3.txt", "r")

lines = f.read().split('\n')
numbers = []
symbols = {}  # [line_index]: [symbol_index1, symbol_index2, symbol_index3]

def symbol_present(curr_line, start_index, end_index, init_line=-1, end_line=1):
    start_index = start_index-1 if start_index-1 >= 0 else 0
    end_index = end_index+1
    
    for y in range(init_line, end_line+1):
        for char in lines[curr_line+y][start_index:end_index]:
            if(not char.isnumeric() and char != '.'):
                return True
        
    return False

number = ''
line_index = 0
for char_index, char in enumerate(lines[line_index]):
    if(char.isnumeric()):
        number+=char
        continue
    
    if(number != '' and symbol_present(line_index, char_index-len(number), char_index, init_line=0)):
        numbers.append(int(number))

    number = ''

    # if(char != '.'):
    #     symbols[line_index].append(char_index)


if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
    numbers.append(int(number))

number = ''


for line_index, line in list(enumerate(lines))[1:-1]:
    symbols[line_index] = []

    for char_index, char in enumerate(line):
        if(char.isnumeric()):
            number+=char
            continue
        
        if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
            numbers.append(int(number))

        number = ''

        # if(char != '.'):
        #     symbols[line_index].append(char_index)


    if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
        numbers.append(int(number))
    
    number = ''


line_index = len(lines) - 1
for char_index, char in enumerate(lines[line_index]):
    if(char.isnumeric()):
        number+=char
        continue
    
    if(number != '' and symbol_present(line_index, char_index-len(number), char_index, end_line=0)):
        numbers.append(int(number))
    
    number = ''

    # if(char != '.'):
    #     symbols[line_index].append(char_index)

if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
    numbers.append(int(number))

    

# %% Substitute number for H to find error
    f = open("inputs/input3.txt", "r")

    lines = f.read().split('\n')
    numbers = []
    symbols = {}

    super_string = ''

    number = ''
    line_index = 0
    for char_index, char in enumerate(lines[line_index]):
        if(char.isnumeric()):
            number+=char
            continue
        
        if(number != '' and symbol_present(line_index, char_index-len(number), char_index, init_line=0)):
            super_string+='H'*len(number)
            numbers.append(int(number))
            number = ''

        super_string+=number+char
        number = ''


    if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
        super_string+='H'*len(number)
        numbers.append(int(number))
        number = ''

    super_string+=number+'\n'
    number = ''


    for line_index, line in list(enumerate(lines))[1:-1]:
        symbols[line_index] = []

        for char_index, char in enumerate(line):
            if(char.isnumeric()):
                number+=char
                continue
            
            if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
                super_string+='H'*len(number)
                numbers.append(int(number))
                number = ''

            super_string+=number+char
            number = ''



        if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
            super_string+='H'*len(number)
            numbers.append(int(number))
            number = ''
        
        super_string+=number+'\n'
        number = ''


    line_index = len(lines) - 1
    for char_index, char in enumerate(lines[line_index]):
        if(char.isnumeric()):
            number+=char
            continue
        
        if(number != '' and symbol_present(line_index, char_index-len(number), char_index, end_line=0)):
            super_string+='H'*len(number)
            numbers.append(int(number))
            number = ''
        
        super_string+=number+char
        number = ''

    if(number != '' and symbol_present(line_index, char_index-len(number), char_index)):
        super_string+='H'*len(number)
        numbers.append(int(number))
        number = ''

    super_string+=number
    number = ''
    

# %%

def get_star_position(curr_line, start_index, end_index, init_line=-1, end_line=1):
    start_index = start_index-1 if start_index-1 >= 0 else 0
    end_index = end_index+1
    
    for y in range(init_line, end_line+1):
        for char_index, char in enumerate(lines[curr_line+y][start_index:end_index]):
            if(not char.isnumeric() and char == '*'):
                char_index+=start_index
                return (char_index, curr_line+y)  # coordinates of star
        
    return False  # star not present

def add_num_to_star_dict(star_position, star_nums):
    if(not star_position):
        return

    if (star_position in star_nums.keys()):
        star_nums[star_position].append(int(number))
    else:
        star_nums[star_position]= [int(number)]

f = open("inputs/input3.txt", "r")

lines = f.read().split('\n')

star_nums = {}

number = ''
line_index = 0
for char_index, char in enumerate(lines[line_index]):
    if(char.isnumeric()):
        number+=char
        continue
    
    if(number != ''):
        star_position = get_star_position(line_index, char_index-len(number), char_index, init_line=0)
        add_num_to_star_dict(star_position, star_nums)

    number = ''


if(number != ''):
    star_position = get_star_position(line_index, char_index-len(number), char_index, init_line=0)
    add_num_to_star_dict(star_position, star_nums)

number = ''


for line_index, line in list(enumerate(lines))[1:-1]:
    symbols[line_index] = []

    for char_index, char in enumerate(line):
        if(char.isnumeric()):
            number+=char
            continue
        
        if(number != ''):
            star_position = get_star_position(line_index, char_index-len(number), char_index)
            add_num_to_star_dict(star_position, star_nums)

        number = ''

    if(number != ''):
        star_position = get_star_position(line_index, char_index-len(number), char_index)
        add_num_to_star_dict(star_position, star_nums)
    
    number = ''


line_index = len(lines) - 1
for char_index, char in enumerate(lines[line_index]):
    if(char.isnumeric()):
        number+=char
        continue
    
    if(number != ''):
        star_position = get_star_position(line_index, char_index-len(number), char_index, end_line=0)
        add_num_to_star_dict(star_position, star_nums)
    
    number = ''

if(number != ''):
    star_position = get_star_position(line_index, char_index-len(number), char_index, end_line=0)
    add_num_to_star_dict(star_position, star_nums)
# %%

num_pairs = filter(lambda num_list: len(num_list) == 2, star_nums.values())
multiplied_pairs = map(lambda num_pair: num_pair[0]*num_pair[1], num_pairs)
print(sum(multiplied_pairs))

# %%
