#!/usr/bin/python3
"""Module to takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument,
and safe from MySQL injections"""


import MySQLdb

if __name__ == "__main__":
    from sys import argv

    connection = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        database=argv[3], charset="utf8")

    with connection.cursor() as cur:
        sql_query = "SELECT * FROM states WHERE name = %s ORDER BY states.id"
        cur.execute(sql_query, (argv[4],))
        query_rows = cur.fetchall()

        for row in query_rows:
            print(row)

    connection.close()
