#!/usr/bin/python3
"""Module that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    connection = MySQLdb.connect(host="localhost",
                                 user=argv[1], passwd=argv[2],
                                 database=argv[3], port=3306)

    with connection.cursor() as cur:
        sql_query = """SELECT cities.name FROM cities
            LEFT JOIN states AS state
            ON state.id = cities.state_id
            WHERE state.name = %s """
        cur.execute(sql_query, (argv[4],))
        query_rows = cur.fetchall()
        rows_list = []
        for row in query_rows:
            for i in row:
                rows_list.append(i)

        print(*rows_list, sep=', ')

    connection.close()
