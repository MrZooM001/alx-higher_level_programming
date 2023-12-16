#!/usr/bin/python3
"""Module to takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""


import MySQLdb

if __name__ == "__main__":
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        database=argv[3], charset="utf8")

    with connection.cursor() as cur:
        cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY states.id".format(argv[4]))
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    connection.close()
