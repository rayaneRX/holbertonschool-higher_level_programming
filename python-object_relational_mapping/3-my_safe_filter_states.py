#!/usr/bin/python3
"""isplays all values in the states"""

import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s", ((sys.argv[4], )))

    result = cursor.fetchall()

    for row in result:
        print(row)
