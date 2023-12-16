#!/usr/bin/python3
"""Module to list all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        database=argv[3], charset="utf8")

    with connection.cursor() as cur:
        cur.execute("SELECT * FROM states")
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    connection.close()
