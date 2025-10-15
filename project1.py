import csv
def load_csv(penguins):
    data = []
    with open(penguins, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if '' in row:
                del row['']
            data.append(row)
    return data

if __name__ == "__main__":
    data = load_csv("penguins.csv")
    print("Number of rows:", len(data))
    print("Sample row:", data[0])

