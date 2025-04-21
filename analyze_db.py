import sqlite3
import re

def init_db():
    try:
        with sqlite3.connect("ecommerce.db") as conn:
            with open("init_db.sql", "r") as f:
                conn.executescript(f.read())
            conn.commit()
            print("Database initialized successfully.")
    except (sqlite3.Error, FileNotFoundError) as e:
        print("Error initializing database: {}".format(e))

def run_query(query_file):
    try:
        with sqlite3.connect("ecommerce.db") as conn:
            cursor = conn.cursor()
            with open(query_file, "r") as f:
                queries = [q.strip() for q in f.read().split(";") if q.strip()]
            
            for query in queries:
                # Skip empty or comment-only queries
                if not query or query.startswith("--"):
                    continue
                try:
                    cursor.execute(query)
                    # Check if the query returns results (SELECT) or modifies data (INSERT, UPDATE, etc.)
                    if cursor.description:  # Query returns a result set
                        columns = [desc[0] for desc in cursor.description]
                        print("\nQuery: {}".format(query.strip()))
                        print("Columns: {}".format(columns))
                        results = cursor.fetchall()
                        if results:
                            for row in results:
                                print(row)
                        else:
                            print("No results returned.")
                    else:
                        conn.commit()
                        print("\nQuery executed (no results): {}".format(query.strip()))
                except sqlite3.Error as e:
                    print("Error executing query: {}\nError: {}".format(query.strip(), e))
    except (sqlite3.Error, FileNotFoundError) as e:
        print("Error running queries: {}".format(e))

def main():
    # Initialize database
    init_db()
    # Run example queries
    print("\nRunning Queries from queries.sql:")
    run_query("queries.sql")

if __name__ == "__main__":
    main()