# Import pandas library
import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Print the entire DataFrame
print(df)

# Print the mean age
print("Mean age:", df['Age'].mean())

# Select data where the age is greater than 30
print(df[df['Age'] > 30])
