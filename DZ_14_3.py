import csv

def write_holiday_cities(first_letter: str):
    been_to_these_cities = []
    want_to_visit = []
    never_was = []
    try:
        with open('travel-notes.csv', 'r', newline='') as holiday:
            reader = csv.reader(holiday, delimiter=',')
            for row in reader:
                if row[0][0] == first_letter:
                    been_to_these_cities.append(row[1])
                    want_to_visit.append(row[2])

        been_to_these_cities = list(set(';'.join(been_to_these_cities).split(';')))
        want_to_visit = list(set(';'.join(want_to_visit).split(';')))
        been_to_these_cities.sort()
        want_to_visit.sort()

        for sity in want_to_visit:
            if sity not in been_to_these_cities:
                never_was.append(sity)

        # print(f'Посетили: {', '.join(been_to_these_cities)}')
        # print(f'Хотят посетить: {', '.join(want_to_visit)}')
        # print(f'Никогда не были: {', '.join(never_was)}')
        # print(f'Следующим городом будет: {''.join(never_was[0])}')

        a = ['Посетители: ' + ', '.join(been_to_these_cities)]
        b = ['Хотят посетить: ' + ', '.join(want_to_visit)]
        c = ['Никогда не были: ' + ', '.join(never_was)]
        d = ['Следующим городом будет: ' + ''.join(never_was[0])]

        with open('holiday.csv', 'w', newline='') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerow(a)
            writer.writerow(b)
            writer.writerow(c)
            writer.writerow(d)
    except:
        print('Студента с таким именем нет')


write_holiday_cities((input('Введите первую букву имени студента: ')).upper())