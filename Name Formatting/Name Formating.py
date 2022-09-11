from os import remove
from posixpath import split
import pandas


cms_file = pandas.read_excel(r'C:\Users\username\Downloads\exceldocument')
cms_file['Name'] = cms_file['Name'].str.replace(r"[\"\',]", '')
cms_names = cms_file['Name'].tolist()

def formatted_names():
    new_list = []
    flat_list = []
    for names in cms_names:
        split_names = names.split()
        for elements in split_names:
            if len(split_names) == 4:
                split_names.pop(1)
                if len(split_names) == 3:
                    split_names.pop(2)
            elif len(split_names) == 3:
                split_names.pop(1)
        for index in range(len(split_names) // 2):
            split_names[index], split_names[-1 - index] = split_names[-1 -index], split_names[index]
        new_list.append(split_names)
    for element in new_list:
            flat_list.append(element[0] + ', ' + element[1])
    final_list = str(flat_list).upper()
    return final_list

print(formatted_names())    


    
  





