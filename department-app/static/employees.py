import pickle

with open('blnrs.pckl', 'rb') as file:
    employees_dict = pickle.load(file)
employees = []
for empl in employees_dict:
    employees.append(empl['commonName'])

# print(employees)