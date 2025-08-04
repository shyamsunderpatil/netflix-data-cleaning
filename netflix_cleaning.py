import pandas as pd

# Load dataset
df = pd.read_csv(r'C:\Users\shyamsunder\OneDrive\Documents\elevate intership\netflix_titles.csv')

# Step 1: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 2: Handle missing values
fills = {
    'director': 'Not Specified',
    'cast': 'Not Specified',
    'country': 'Not Specified',
    'rating': df['rating'].mode()[0]
}
df.fillna(fills, inplace=True)

# Fix date_added separately with cleaning
df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'], format='%B %d, %Y', errors='coerce')

# Step 3: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 4: Extract numeric and unit from 'duration'
df['duration_num'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['duration_unit'] = df['duration'].str.extract(r'([A-Za-z ]+)$').iloc[:, 0].str.strip()

# Step 5: Standardize text fields
for col in ['type', 'rating', 'country']:
    df[col] = df[col].str.strip().str.title()

# Step 6: Save cleaned dataset
df.to_csv(r'C:\Users\shyamsunder\OneDrive\Documents\elevate intership\netflix_titles_cleaned.csv', index=False)

print("✅ Data cleaning complete. Cleaned file saved as 'netflix_titles_cleaned.csv'")
