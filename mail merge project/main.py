
starting_letter = open("./Input/Letters/starting_letter.txt")
invited_names = open("./Input/Names/invited_names.txt")

first_line = starting_letter.readline()
all_lines = starting_letter.readlines()
# print(all_lines)
name_list = invited_names.readlines()
new_name_list = []
for name in name_list:
    new_name = name.strip("\n")
    new_name_list.append(new_name)

for name in new_name_list:
    new_line = first_line.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter to {name}.txt", "a") as file:
        file.write(new_line)
        for m in all_lines:
            file.write(m)


starting_letter.close()
invited_names.close()


