import csv

with open('mails.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #Primera linea
            line_count += 1
        else:
            print(f'Empresa: {row[0]}')
            #Separo el string del campo Founder
            founder_split = row[2].split(",")[0]
            print(f'Fundador: {founder_split}')
            print(f'Contacto: {row[3]}')
            line_count += 1
            print("")
    print(f'\nContactos: {line_count}')