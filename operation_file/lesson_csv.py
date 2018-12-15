import csv


with open('test.csv', 'w') as csv_file:
    # header を設定
    fieldnames = ['Name', 'Like']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'Python', 'Like': 'Very like'})
    writer.writerow({'Name': 'javaSctipt', 'Like': 'Soso'})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['Name'], row['Like'])