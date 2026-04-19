import pandas as pd

def analyze_missing_and_skew(df):
    """
    Performs missing value analysis, imputes missing numeric values with mean,
    calculates skewness for numeric columns, and returns the required lists.

    Parameters:
    df (pd.DataFrame): Input DataFrame (can contain numeric and non-numeric columns)

    Returns:
    list: [list of columns with missing values (alphabetically),
           list of skewness values for numeric columns (ascending, rounded to 2 decimals)]
    """
    # Step 1: Create a copy
    df_copy = df.copy()

    # Step 2: Identify columns with missing values
    missing_cols = sorted(df_copy.columns[df_copy.isna().any()].tolist())

    # Step 3: Select numeric columns only
    numeric_cols = df_copy.select_dtypes(include='number').columns

    # Step 4: Fill missing numeric values with mean
    for col in numeric_cols:
        mean_val = df_copy[col].mean()
        df_copy[col].fillna(mean_val, inplace=True)

    # Step 5: Calculate skewness for numeric columns
    skew_values = df_copy[numeric_cols].skew().sort_values().round(2).tolist()

    # Step 6: Return result
    return [missing_cols, skew_values]

# -----------------------------
# Example usage
data = pd.DataFrame({
    'Age': [25, 30, None, 35, 40, None, 28, 45],
    'Salary': [50000, None, 75000, 60000, None, 55000, 65000, 80000],
    'Experience': [2, 5, 8, 3, None, 4, 6, 10],
    'Rating': [4.5, 3.8, 4.2, None, 4.7, 3.9, 4.1, 4.8],
})


df = pd.DataFrame(data)
result = analyze_missing_and_skew(df)
print(result)
