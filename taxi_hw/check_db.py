import duckdb

con = duckdb.connect("taxi_hw_v3.duckdb")

# 1. See all column names and their types
print("--- Column Info ---")
print(con.execute("DESCRIBE ny_taxi_data.rides").df())

# 2. See a sample of 5 rows (transposed so it's easy to read)
print("\n--- Data Sample (First 5 rows) ---")
# .df() makes it a pretty Pandas-style table
print(con.execute("SELECT sum(tip_amt) FROM ny_taxi_data.rides").df().T)