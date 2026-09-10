from Lesson_15.definition import CSV_FOLDER
from Lesson_15.definition import CSV_FILE_FOR_TESTING
import csv
import random

new_file = list(CSV_FOLDER.iterdir())
csv_colection = []
for i in new_file:
    if i.suffix == ".csv":
        csv_colection.append(i)
random_file = random.sample(csv_colection, 2)
rows = []
unic_rows = []
for i in random_file:
    with open(i, mode="r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
for i in rows:
    if i not in unic_rows:
        unic_rows.append(i)
with open(CSV_FILE_FOR_TESTING, mode="w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(unic_rows)




