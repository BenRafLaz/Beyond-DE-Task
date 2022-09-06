import csv
import sqlite3
import glob
import os


# Loops over each file in the directory
def load_directory(dirname, db):
    for filename in glob.glob(os.path.join(dirname, '*.csv')):
        load_file(filename, db)


def load_file(filename, db):
    with open(filename) as file:
        with db:
            data = csv.DictReader(file)
            cols = data.fieldnames
            table = os.path.splitext(os.path.basename(filename))[0]

            sql = 'drop table if exists "{}"'.format(table)
            db.execute(sql)

            sql = 'create table "{table}" ( {cols} )'.format(
                table=table,
                cols=','.join('"{}"'.format(col) for col in cols))
            db.execute(sql)

            sql = 'insert into "{table}" values ( {vals} )'.format(
                table=table,
                vals=','.join('?' for col in cols))
            db.executemany(sql, (list(map(row.get, cols)) for row in data))


if __name__ == '__main__':
    conn = sqlite3.connect('invalid.db')   # New db name
    load_directory('./invalid_dates', conn)  # Choose where the data is coming from
