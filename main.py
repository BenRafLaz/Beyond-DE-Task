import csv
import collections

src_path = ""
main_file = "./tripdata.csv."  # Your csv file here
choose_filter_date = "2020-01"

# Opens the file and sorts the relevant/invalid dates.
with open(main_file, "rt") as fp:
    root = csv.reader(fp, delimiter=",")
    result = collections.defaultdict(list)
    invalid = collections.defaultdict(list)
    next(root)
    for row in root:
        date = row[3].split(" ")
        if date[0].startswith(choose_filter_date + "-"):  # Choose_filter_date for when we want february f.e.
            result[date[0]].append(row)
        else:
            invalid[date[0]].append(row)

# Grabs the column names, to later inject into new files
with open('./tripdata.csv') as file:
    csv_reader = csv.reader(file, delimiter=",")
    col_names = []
    for row in csv_reader:
        col_names.append(row)
        break


# Creates files using the results and your chosen path
def write_files(res, pth):
    for i, j in res.items():  # res= result or invalid
        file_path = "./" + pth + "/%s%s.csv" % (src_path, i)  # Changes pth to where you will store CSV files
        with open(file_path, 'wt') as new_file:
            writer = csv.writer(new_file, delimiter=",")
            writer.writerows(col_names)
            writer.writerows(j)


write_files(invalid, "invalid_dates")
write_files(result, "january")
