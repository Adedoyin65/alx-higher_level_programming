#!/usr/bin/python3
"""A script that defines a function called search_states"""
import MySQLdb
import sys


def search_states(username, password, database_name, state_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
            )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # SQL query with user input using format method
    sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    state_name_param = '%' + state_name + '%'

    try:
        # Execute the SQL command with parameterized query
        cursor.execute(sql_query, (state_name_param,))

        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()

        # Print the results
        for row in results:
            print(row)

    except Exception as e:
        print("Error: Unable to fetch data -", e)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Use: script.py <username> <password> <database_name> <state>")
        sys.exit(1)

    # Get MySQL credentials and state name from command-line arguments
    username, password, database_name, state_name = sys.argv[1:]

    # Call the function to search for states
    search_states(username, password, database_name, state_name)
