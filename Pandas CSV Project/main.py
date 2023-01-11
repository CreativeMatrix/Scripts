import pandas

data = pandas.read_csv('./Squirrel_Data.csv')
color_gray = sum(data['Primary Fur Color'] == 'Gray')
color_cinnamon = sum(data['Primary Fur Color'] == 'Cinnamon')
color_black = sum(data['Primary Fur Color'] == 'Black')


data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [color_gray, color_cinnamon, color_black]
}

squirrel_colors = pandas.DataFrame(data_dict)
squirrel_colors.to_csv("Squirrel_Colors.csv")
