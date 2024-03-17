#!/usr/bin/python3
"""A module which defines a script for listing states"""
if __name__ == "__main__":
    import MySQLdb
    dan = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="Eden",
            passwd="ogunyemi65",
            database="hbtn_0e_0_usa"
            )
    mydan = dan.cursor()
    try:
        mydan.execute("SELECT * FROM states ORDER BY id ASC")
        res = mydan.fetchall()
        for row in res:
            print(row)
    except MySQLdb.Error as e:
        print("Error: Unable to fetch data -", e)
    mydan.close()
    dan.close()
