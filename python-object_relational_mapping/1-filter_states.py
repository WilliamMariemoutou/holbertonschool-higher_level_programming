#!/usr/bin/python3

"""
lists all states with a name starting with N form the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and database name
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
    
    cur = db.cursor()

    # Select states beginning with 'N' (case-sensitive)
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    #fetch and display rows
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    #close cursor and connection
    cur.close()
    db.close()
