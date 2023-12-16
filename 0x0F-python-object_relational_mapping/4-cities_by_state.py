#!/usr/bin/python3
"""Module that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb

if __name__ == "__main__":
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        database=argv[3], charset="utf8")

    with connection.cursor() as cur:
        sql_query = """SELECT cities.id, cities.name, state.name FROM cities
            LEFT JOIN states AS state
            ON state.id = cities.state_id
            ORDER BY cities.id"""
        cur.execute(sql_query)
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    connection.close()
