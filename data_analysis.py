import pandas as pd

# Load the dataset
df = pd.read_csv(r'C:\Users\user\Downloads\Crash_Reporting_-_Drivers_Data.csv', low_memory=False)

# Display basic information about the dataset
print(df.info())

# Display the first few rows of the dataset
print(df.head())

# Display summary statistics for numeric columns
print(df.describe())

# Display unique values in the 'Weather' column
print(df['Weather'].unique())

# Check for missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

# Data cleaning: Fill missing values with the mode of each column
df['Route Type'] = df['Route Type'].fillna(df['Route Type'].mode()[0])
df['Surface Condition'] = df['Surface Condition'].fillna(df['Surface Condition'].mode()[0])
df['Weather'] = df['Weather'].fillna(df['Weather'].mode()[0])
df['Driver Substance Abuse'] = df['Driver Substance Abuse'].fillna(df['Driver Substance Abuse'].mode()[0])
df['Traffic Control'] = df['Traffic Control'].fillna(df['Traffic Control'].mode()[0])
df['Vehicle Movement'] = df['Vehicle Movement'].fillna(df['Vehicle Movement'].mode()[0])

# Check for missing values in each column after filling missing values
missing_values_after_fill = df.isnull().sum()
print("Columns with missing values after filling:")
print(missing_values_after_fill[missing_values_after_fill > 0])

# Save the cleaned DataFrame to a CSV file
df.to_csv(r'C:\Users\user\pythoncode\cleaned_data.csv', index=False)


