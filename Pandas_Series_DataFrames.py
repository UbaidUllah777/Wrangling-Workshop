import pandas as pd
import numpy as np
import psycopg2

# A Series in Pandas is a one-dimensional labeled array capable of holding any data type 
# (integers, strings, floating point numbers, Python objects, etc.). It is similar to a column in a spreadsheet or a database table. 
# Each element in a Series has an associated label, known as its index, which allows for fast lookups and alignment of data. 
# Series are a fundamental data structure in Pandas and are often used as building blocks for more complex data structures like 
# DataFrames.  

pd_series = pd.Series([1, 2, 3, 4, 5])
# A DataFrame in Pandas is a two-dimensional labeled data structure with columns of potentially different types.
pd_dataframe = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.0, 5.5, 6.1],
    'C': ['p', 'q', 'r']
})
# A DataFrame is similar to a spreadsheet or SQL table, or a dictionary of Series objects.
# It is a primary data structure in Pandas and is used for storing and manipulating tabular data.   
# A DataFrame can be thought of as a collection of Series that share the same index.
# The index of a DataFrame is a set of labels that uniquely identify each row, allowing for easy data alignment and retrieval.  
# DataFrames can be created from various data sources, including lists, dictionaries, and NumPy arrays.
# DataFrames can also be created from external data sources like CSV files, Excel spreadsheets, and SQL databases.
# The DataFrame constructor can take various parameters to customize the creation of the DataFrame, such as specifying the index,
# column names, and data types.


import random
from faker import Faker

fake = Faker()
positions = [
    'Software Engineer', 'Data Analyst', 'DevOps Engineer', 'ML Engineer', 'QA Engineer',
    'Backend Developer', 'Frontend Developer', 'Cloud Architect', 'SysAdmin', 'Data Scientist'
]

# Prepare to generate 50 employee records
# Each record will include a name, position, start date, and salary
for i in range(50):
    name = fake.name().replace("'", "''")  # Escape single quotes
    position = random.choice(positions)
    # Use datetime.date objects instead of strings for start_date and end_date
    start_date = fake.date_between(start_date=pd.to_datetime("2015-01-01").date(), end_date=pd.to_datetime("2024-06-01").date())
    salary = random.randint(60000, 200000)
    print(f"INSERT INTO employees (name, position, start_date, salary) VALUES ('{name}', '{position}', '{start_date}', {salary});")


# Replace with your Neon connection details
conn_str = "postgresql://neondb_owner:npg_WuBb0k8gTHlf@ep-patient-wave-a8zje19m-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

# Connect to the database
conn = psycopg2.connect(conn_str)

# Query the table and load into Pandas
df = pd.read_sql_query("SELECT * FROM employees;", conn)

conn.close()

# Show the DataFrame
print(df.head())


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming df is already loaded
df['start_year'] = pd.DatetimeIndex(df['start_date']).year

# Calculate mean salary for each position per year
pivot = df.pivot_table(index='position', columns='start_year', values='salary', aggfunc='mean')

# Plot grouped bar chart
pivot.plot(kind='bar', figsize=(12, 6))
plt.title('Average Salary by Position and Start Year')
plt.xlabel('Position')
plt.ylabel('Average Salary ($)')
plt.legend(title='Start Year')
plt.tight_layout()
plt.show()

