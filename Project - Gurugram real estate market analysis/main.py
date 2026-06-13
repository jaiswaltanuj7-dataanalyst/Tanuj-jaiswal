import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print(data.head())

# Check for missing values
print(data.isnull().sum())

# Clean and convert numeric columns
if 'Rate per sqft' in data.columns:
    data['Rate per sqft'] = (
        data['Rate per sqft']
        .astype(str)
        .str.replace(',', '', regex=False)
        .str.strip()
    )
    data['Rate per sqft'] = pd.to_numeric(data['Rate per sqft'], errors='coerce')

numeric_cols = data.select_dtypes(include=[np.number]).columns
if len(numeric_cols) > 0:
    data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())

# Summary statistics
print(data.describe())

# Correlation matrix
correlation_matrix = data[numeric_cols].corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.tight_layout()
plt.show()

# Choose valid columns for plots
x_col = 'Area' if 'Area' in data.columns else numeric_cols[0]
y_col = 'Price' if 'Price' in data.columns else numeric_cols[1] if len(numeric_cols) > 1 else numeric_cols[0]

# Scatter plot of two variables
plt.figure(figsize=(8, 6))
sns.scatterplot(x=x_col, y=y_col, data=data)
plt.title(f'Scatter Plot of {x_col} vs {y_col}')
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.tight_layout()
plt.show()

# Box plot to check for outliers
box_col = 'Price' if 'Price' in data.columns else x_col
plt.figure(figsize=(8, 6))
sns.boxplot(x=data[box_col])
plt.title(f'Box Plot of {box_col}')
plt.xlabel(box_col)
plt.tight_layout()
plt.show()

# Histogram of a variable
hist_col = 'Area' if 'Area' in data.columns else box_col
plt.figure(figsize=(8, 6))
sns.histplot(data[hist_col].dropna(), bins=30, kde=True)
plt.title(f'Histogram of {hist_col}')
plt.xlabel(hist_col)
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

