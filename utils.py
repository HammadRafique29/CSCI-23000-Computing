import csv

def read_csv(file_name):
    Data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for data in reader:
            Data.append(data)
    return Data

def write_csv(file_name, data):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)
    return True
    
