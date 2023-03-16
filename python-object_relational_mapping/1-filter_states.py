#!/usr/bin/python3
"""lists all states with a name starting with N from the database"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%';")

    result = cursor.fetchall()

    for row in result:
        print(row)
