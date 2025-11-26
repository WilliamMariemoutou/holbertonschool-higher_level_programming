#!/usr/bin/python3

"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
Results are displayed in ascending order by city ID.
"""

import MySQLdb
import sys


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
    query = (
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Prints the city names
    cities = [row[0] for row in rows]

    print(", ".join(cities))

    cur.close()
    db.close()