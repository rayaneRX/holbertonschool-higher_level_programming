#!/usr/bin/python3
""" script that lists all cities from the database"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306,)

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name , states.name\
                   FROM cities JOIN states ON states.id = cities.state_id\
                   ORDER BY cities.id;")

    result = cursor.fetchall()

    for row in result:
        print(row)
