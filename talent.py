import pandas as pd
import numpy as np

# Load your CSV file
df = pd.read_csv("mashaghel.csv")  # Replace with your file path if needed

# Identify client column (assumes it's the second column)
client_column = df.columns[1]
client_scores = df[client_column].values
occupations_df = df.iloc[:, 2:]  # All other columns are occupational categories

# Calculate Manhattan Distance and Variance
results = []
for col in occupations_df.columns:
    occupation_scores = occupations_df[col].values
    diffs = client_scores - occupation_scores
    manhattan = np.sum(np.abs(diffs))
    variance = np.var(diffs ** 2)
    results.append({
        'Occupational Category': col,
        'Manhattan Distance': manhattan,
        'Variance': variance
    })

# Create results DataFrame
results_df = pd.DataFrame(results)

# Normalize both metrics (min-max)
results_df['Norm_Manhattan'] = (
    results_df['Manhattan Distance'] - results_df['Manhattan Distance'].min()
) / (
    results_df['Manhattan Distance'].max() - results_df['Manhattan Distance'].min()
)

results_df['Norm_Variance'] = (
    results_df['Variance'] - results_df['Variance'].min()
) / (
    results_df['Variance'].max() - results_df['Variance'].min()
)

# Combine normalized values (equal weight)
results_df['Combined Score'] = results_df['Norm_Manhattan'] + results_df['Norm_Variance']

# Sort and get top 2 matches
top_2 = results_df.sort_values(by='Combined Score').head(2)

# Display result
print(top_2[['Occupational Category', 'Manhattan Distance', 'Variance', 'Combined Score']])