#!/usr/bin/python3
import MySQLdb
dan = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="Eden",
        passwd="ogunyemi65",
        database="hbtn_0e_0_usa"
        )
mydan = dan.cursor()
mydan.execute("SELECT * FROM states ORDER BY id ASC")
res = mydan.fetchall()
for i in res:
    print(i)
