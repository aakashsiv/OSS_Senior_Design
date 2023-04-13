# The given code reads a CSV file into a Pandas DataFrame named "df", 
# filters out the rows that have certain values in the "Last Funding Type" column, 
# and saves the resulting filtered DataFrame to a new CSV file.
import pandas as pd

df = pd.read_csv('myCSV.csv')

# Filter out rows that contain "Post-IPO Equity" or "Post-IPO Debt" or "Secondary Market" categories in the "Last Funding Type" column
df = df[~df['Last Funding Type'].isin(['Post-IPO Equity', 'Post-IPO Debt', 'Secondary Market'])]

# Save the filtered DataFrame to a new CSV file
df.to_csv('csvNew.csv', index=False)
