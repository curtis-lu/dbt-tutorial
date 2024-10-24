import duckdb

# Connect to DuckDB (create a database if it doesn't exist, or use in-memory ':memory:')
con = duckdb.connect('dev.duckdb')

# Create the schema if it doesn't exist
con.execute("CREATE SCHEMA IF NOT EXISTS jaffle_shop")

# Drop the table if it already exists
con.execute("DROP TABLE IF EXISTS jaffle_shop.customers")

# Drop the table if it already exists
con.execute("DROP TABLE IF EXISTS jaffle_shop.orders")

# Load CSV file into a table
con.execute("""
    CREATE TABLE jaffle_shop.customers AS
    SELECT * FROM read_csv_auto('./source/raw_customers.csv')
""")

# Verify data loading
result = con.execute("SELECT * FROM jaffle_shop.customers LIMIT 10").fetchdf()

# Display the first 10 rows
print(result)

# Load CSV file into a table
con.execute("""
    CREATE TABLE jaffle_shop.orders AS
    SELECT * FROM read_csv_auto('./source/raw_orders.csv')
""")

# Verify data loading
result = con.execute("SELECT * FROM jaffle_shop.orders LIMIT 10").fetchdf()

# Display the first 10 rows
print(result)