#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
taking 3 arguments: mysql username, mysql password and database name
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor object
    cursor = db.cursor()

    # Execute query to select all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
