name = input()
surname = input()
year = input()
print(name + '_' + surname + '_' + year)
name, surname = surname, name
year = str(int(year) + 60)
print(name + '_' + surname + '_' + year)