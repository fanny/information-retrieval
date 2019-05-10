import csv

def write_in_csv(indexes):
    with open('../data/inverted_index.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(indexes.keys()))

        writer.writeheader()
        writer.writerow(indexes)