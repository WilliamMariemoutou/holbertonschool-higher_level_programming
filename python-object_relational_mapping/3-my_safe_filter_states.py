#!/bin/usr/python3

"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Prepare the SQL query using a placeholder for the state name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state_name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all results
    results = cursor.fetchall()

    # Print the results in the specified format
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
