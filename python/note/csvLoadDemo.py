import csv

filename = 'csv\\test.csv'
with open(filename) as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)
    
    #print(header_row)
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    highs = []
    for row in reader:
        highs.append(row[0])
    print(highs)

    