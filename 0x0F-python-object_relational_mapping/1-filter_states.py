#!/usr/bin/python3
"""A module which defines a script for listing states that begins with N"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(sys.argv) != 4:
        print("Use: python script.py <username> <password> <database_name>")
        sys.exit(1)
    username, password, database_name = sys.argv[1:]
    dan = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            database=database_name
            )
    m = dan.cursor()
    try:
        m.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        res = m.fetchall()
        for row in res:
            print(row)
    except MySQLdb.Error as e:
        print("Error: Unable to fetch data -", e)
    m.close()
    dan.close()
