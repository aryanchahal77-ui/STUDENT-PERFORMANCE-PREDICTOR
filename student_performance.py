import pandas as pd

# List of student data
students = [
    ('Ayesha', 34, 'Sydeny', 'Australia'),
    ('Asif', 30, 'Delhi', 'India'),
    ('Imran', 31, 'Mumbai', 'India'),
    ('Yaseen', 32, 'Bangalore', 'India'),
    ('Rahmath', 16, 'New York', 'US'),
    ('Needha', 17, 'Las Vegas', 'US')
]

# Create DataFrame
df = pd.DataFrame(
    students,
    columns=['Name', 'Age', 'City', 'Country'],
    index=['a', 'b', 'c', 'd', 'e', 'f']
)

# Display DataFrame
print(df)
