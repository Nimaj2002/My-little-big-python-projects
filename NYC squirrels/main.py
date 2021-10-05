import pandas

all_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
all_colors_list = all_data.Primary_Fur_Color

# Gray = 0
# Cinnamon = 0
# Black = 0
# for color in all_colors_list:
#     if color == "Gray":
#         Gray += 1
#     elif color == "Cinnamon":
#         Cinnamon += 1
#     elif color ==  "Black":
#         Black += 1

Gray = len(all_data[all_data.Primary_Fur_Color == "Gray"])
Cinnamon = len(all_data[all_data.Primary_Fur_Color == "Cinnamon"])
Black = len(all_data[all_data.Primary_Fur_Color == "Black"])

print(f"Gray : {Gray}")
print(f"Cinnamon : {Cinnamon}")
print(f"Black : {Black}")

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray, Cinnamon, Black]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel Count.csv")