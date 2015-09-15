__author__ = 'Gustav'


import csv


def read(file):
    records = []
    with open(file, 'rt') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if len(row) == 15:
                records.append({
                    "age": row[0],
                    "workclass": row[1],
                    "fnlwgt": row[2],
                    "education": row[3],
                    "education-num": row[4],
                    "martial-status": row[5],
                    "occupation": row[6],
                    "relationship": row[7],
                    "race": row[8],
                    "sex": row[9],
                    "capital-gain": row[10],
                    "capital-loss": row[11],
                    "hours-per-week": row[12],
                    "native-country": row[13],
                    "salary": row[14]
                })
            if len(row) == 14:
                records.append({
                    "age": row[0],
                    "workclass": row[1],
                    "fnlwgt": row[2],
                    "education": row[3],
                    "education-num": row[4],
                    "martial-status": row[5],
                    "occupation": row[6],
                    "relationship": row[7],
                    "race": row[8],
                    "sex": row[9],
                    "capital-gain": row[10],
                    "capital-loss": row[11],
                    "hours-per-week": row[12],
                    "native-country": row[13],
                    "salary": "?"
                })
    return records



data = read("../data/adult.test");
print(data)
