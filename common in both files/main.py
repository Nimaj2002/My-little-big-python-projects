with open("file1.txt", "r") as file_1:
    all_data = file_1.readlines()
    numbers_in_file_1 = [int(number.strip("\n")) for number in all_data]

with open("file2.txt", "r") as file_2:
    all_data = file_2.readlines()
    numbers_in_file_2 = [int(number.strip("\n")) for number in all_data]

main_list = [number for number in numbers_in_file_1 if number in numbers_in_file_2]
print(main_list)
