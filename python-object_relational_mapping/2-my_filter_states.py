#!/usr/bin/python3

"""
Lists all values in the database where the states table mathces the argument    
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
    cur = db.cursor()

    # Prepare the SQL query to fetch states with a matching name
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                "ORDER BY states.id ASC".format(state_name))


    # Fetch all results
    results = cur.fetchall()

    # Print the results in the specified format
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
