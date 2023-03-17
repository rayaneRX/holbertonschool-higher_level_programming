#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306,)

    cursor = db.cursor()

    cursor.execute(
            "SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = {}".format(sys.argv[4]))
    result = cursor.fetchall()

    for row in result:
        print(row)