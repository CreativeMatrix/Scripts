import csv
import pandas


with open('weather_data.csv', 'r') as spreadsheet:
    csv_data = list(csv.reader(spreadsheet, delimiter=','))
    print(csv_data) #Prints the entire spreedsheet in a 2D list

    temperatures = []
    for data in csv_data:
        if data[1] != "temp":
            temperatures.append(int(data[1]))
    print(temperatures) # Prints the temp column in a list


data = pandas.read_csv('weather_data.csv')
print(data) #Prints the Entire spreedsheet and formats it using Pandas

print(data['temp']) #Calls the temp column using Pandas
print(data['temp'].mean())

print(data.temp.max()) #This also calls the column
print(data.temp.min()) 

print(data[data.day == 'Monday']) #Calls the Monday row
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"] #Gets the Row associated with Monday by using the column name
monday_temp = int(monday.temp) #Converts that one temp value into an interger
monday_temp_fahrenheit = monday_temp * 9/5 + 32 #The Formula that converts Celsius to Fahrenheit
print(monday_temp_fahrenheit)

#Creating a Dataframe from Scratch using Python data.
data_dict = {
    "students": ['Amy', "James", "Angela"],
    "scores": [76, 56, 65]
}
dataframe_dict = pandas.DataFrame(data_dict)
print(dataframe_dict)
dataframe_dict.to_csv("students.csv") #Converts to CSV