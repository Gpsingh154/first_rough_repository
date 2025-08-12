import csv

def read_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    read_csv("sample.csv")
