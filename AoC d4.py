# %%

f = open("inputs/input4.txt", "r")

# remove two spaces to ease split
lines = f.read().replace('  ', ' ').split('\n')

matches = []

for line in lines:
    numbers = line.split(': ')[1].split(' | ')
    winning_numbers = numbers[0].split(' ')
    elf_numbers = numbers[1].split(' ')

    power = len(set(winning_numbers).intersection(set(elf_numbers)))

    if(power > 0):
        matches.append(2**(power-1))

print(sum(matches))


# %%
f = open("inputs/input4.txt", "r")

# remove two spaces to ease split
lines = f.read().replace('  ', ' ').split('\n')

card_copies = {}

for card_index, line in enumerate(lines):
    card_index+=1
    numbers = line.split(': ')[1].split(' | ')
    winning_numbers = numbers[0].split(' ')
    elf_numbers = numbers[1].split(' ')

    next_copies = len(set(winning_numbers).intersection(set(elf_numbers)))
    
    number_current_cards = card_copies[card_index]+1 if card_index in card_copies.keys() else 1

    for i in range(1, next_copies+1):
        copy_index = i + card_index

        if (copy_index in card_copies.keys()):
            card_copies[copy_index] += number_current_cards
        else:
            card_copies[copy_index] = number_current_cards


print(sum(card_copies.values()) + len(lines))
# %%
