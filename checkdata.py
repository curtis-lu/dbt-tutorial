import duckdb

# Connect to DuckDB (create a database if it doesn't exist, or use in-memory ':memory:')
con = duckdb.connect('dev.duckdb')

# Verify the data loading
result = con.execute("SELECT * FROM customers LIMIT 10").fetchdf()

# Display the first 10 rows
print(result)