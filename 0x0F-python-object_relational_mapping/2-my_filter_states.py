#!/usr/bin/python3
"""A module which defines a script that takes in an argument
   and displays all values in the states table of
   hbtn_0e_0_usa where name matches the argument."""
if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) != 5:
        print("Use:script.py <username> <password> <database_name> <arg1>")
        sys.exit(1)
    username, password, database_name, arg1 = sys.argv[1:]
    dan = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            database=database_name
            )
    m = dan.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    try:
        m.execute(query, (arg1,))
        res = m.fetchall()
        for row in res:
            print(row)
    except MySQLdb.Error as e:
        print("Error: Unable to fetch data -", e)
    m.close()
    dan.close()
