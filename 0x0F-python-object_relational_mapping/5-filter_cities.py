#!/usr/bin/python3
""" All cities by state """
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    # Execute the query
    cursor.execute(query, (sys.argv[4],))

    # Fetch all the rows
    rows = cursor.fetchall()

    # Create a list of city names
    cities = [row[0] for row in rows]

    # Print the cities, joined by a comma and a space
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
