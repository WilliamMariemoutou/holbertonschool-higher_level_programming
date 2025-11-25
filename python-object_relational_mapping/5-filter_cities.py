#!/usr/bin/python3
import MySQLdb
import sys

"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.

Results are displayed in ascending order by city ID.
"""

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Query to get cities for the given state, ordered by city ID
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query safely with state_name as parameter
    cur.execute(query, (state_name,))

    # Fetch all the results
    results = cur.fetchall()

    # Print the cities as a comma-separated list
    if results:
        print(", ".join(city[0] for city in results))

    # Close the cursor and the database connection
    cur.close()
    db.close()
