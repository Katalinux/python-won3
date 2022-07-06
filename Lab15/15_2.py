with open('student.csv', 'r') as students:
    std = []
    for line in students:
        raw = []
        for x in line.split(','):
            raw.append(x.strip())
        std.append(raw)
    std.remove(std[0])

with open('15_2.sql', 'w') as queries:
    for cnt, item in enumerate(std):
        queries.write(f'insert into student(surname, first_name, class_nr, class_letter, birth_date, average_grade)'
                      f' values (\'{std[cnt][0]}\', \'{std[cnt][1]}\', \'{std[cnt][2]}\', \'{std[cnt][3]}\','
                      f' \'{std[cnt][4]}\', \'{std[cnt][5]}\');\n')
