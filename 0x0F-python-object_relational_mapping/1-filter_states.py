#!/usr/bin/python3
"""  lists all states with a name starting with N (upper N) from the
database """
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY
                   id ASC""")

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
