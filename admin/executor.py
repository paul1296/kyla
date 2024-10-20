import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('*.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Take a SQL query as input
def query_executor(sql_query: str):

    try:
        # Execute the query
        cursor.execute(sql_query)
        
        # If it's a SELECT statement, fetch results
        if sql_query.strip().upper().startswith("SELECT"):
            results = cursor.fetchall()
            return results
        else:
            # Commit changes if it's an INSERT, UPDATE, or DELETE statement
            connection.commit()
            return "Query executed successfully."
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    # Close the connection
    cursor.close()
    connection.close()
