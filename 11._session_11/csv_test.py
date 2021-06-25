import csv

# csv.writer()
with open('testfiles/employee_file.csv', 'w') as f:
    employee_writer = csv.writer(f, delimiter=",")

    employee_writer.writerow([ 'Andreas Laursen', '25', 'IT'])
    employee_writer.writerow([ 'Findus Møller', '2', 'Cat'])




# csv.DictWriter()
with open ('testfiles/employee_file_dict.csv', 'w') as f:
    field_names = ['name', 'age', 'field']
    writer = csv.DictWriter(f, fieldnames=field_names)

    writer.writeheader()
    writer.writerow({ 'name': 'Ida Christina', 'age': 18, 'field': 'Paleontologist'})
    writer.writerow({ 'name': 'Karina Møller', 'age': 44, 'field': 'SOSU Assistent'})


# csv.reader()
with open('testfiles/employee_file.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=",")
    for row in csv_reader:
        if row != []:
            print(row)


#csv.DictReader()
with open('testfiles/employee_file_dict.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        if row != []:
            print(f'Unformatted: {row}')
            print(f'Formatted: {row["name"]} {row["age"]} {row["field"]}')


