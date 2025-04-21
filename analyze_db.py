import sqlite3

def init_db():
    conn = sqlite3.connect("ecommerce.db")
    with open("data/init_db.sql") as f:
        conn.executescript(f.read())
    conn.close()

def run_query(query_file):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    with open(query_file) as f:
        query = f.read()
    cursor.executescript(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    conn.close()

def main():
    # Initialize database
    init_db()
    # Run example queries
    print("Basic Queries:")
    run_query("queries.sql")
    

if __name__ == "__main__":
    main()