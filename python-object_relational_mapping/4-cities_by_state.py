#!/usr/bin/python3

"""
Lists all the citites from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Prepare and execute the SQL query to get city information
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cur.execute(query)

    # Fetch all results
    results = cur.fetchall()

    # Print the results in the specified format
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
