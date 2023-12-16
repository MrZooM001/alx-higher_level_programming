#!/usr/bin/python3
"""Module to list all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        database=argv[3], charset="utf8")

    with connection.cursor() as cur:
        sql_query = """SELECT * FROM states WHERE name 
        LIKE BINARY 'N%' ORDER BY states.id"""
        cur.execute(sql_query)
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    connection.close()
