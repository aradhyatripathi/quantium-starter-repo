import pandas as pd
import glob

# Read all CSV files
files = glob.glob('data/*.csv')
dfs = []

for file in files:
    df = pd.read_csv(file)
    dfs.append(df)

# Combine all files
df = pd.concat(dfs, ignore_index=True)

# Keep only Pink Morsel
df = df[df['product'] == 'pink morsel']

# Create sales column
df['price'] = df['price'].str.replace('$', '').astype(float)
df['sales'] = df['price'] * df['quantity']

# Keep only required columns
df = df[['sales', 'date', 'region']]

# Save output
df.to_csv('data/daily_sales_data.csv', index=False)

print("Done!", len(df), "rows")