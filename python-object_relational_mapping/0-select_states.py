#!/usr/bin/python3
"""
This script lists all states from the database 'hbtn_0e_0_usa'.
It takes 3 arguments: MySQL username, MySQL password, and database name.
It connects to a MySQL server running on localhost at port 3306 and prints all states
sorted by their 'id' in ascending order.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get arguments from the command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute query to fetch all states, ordered by id in ascending order
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all rows from the result
    states = cursor.fetchall()

    # Print each state in the result set
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
