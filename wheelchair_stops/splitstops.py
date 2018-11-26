import sys
import csv

if len(sys.argv) < 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    exit(1)

filename = sys.argv[1]
print(filename)

yesl = []
nol = []
with open(filename,"r",encoding="utf-8") as f:
    # wheelchair je 6. nebo -1. sloupec
    reader = csv.reader(f)
    for row in reader:
        if row[-1] == "0":
            continue
        if row[-1] == "1":
            yesl.append(row)
        elif row[-1] == "2":
            nol.append(row)

print("Existuje {} bezbarierovych a {} barierovych zastavek".format(len(yesl),len(nol)))

# filename == "stops.txt"
suffix = filename[-4:] # .txt
prefix = filename[:-4] # stops
yes_filename = prefix + "_yes" + suffix
no_filename = prefix + "_no" + suffix
print(yes_filename,no_filename)

with open(yes_filename,"w",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(yesl)

with open(no_filename,"w",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(nol)


