# ============================================================
# SECTION 1: IMPORT LIBRARIES
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path


# ============================================================
# SECTION 2: LOAD DATASET AND CREATE OUTPUT DIRECTORY
# ============================================================

# Load the dataset
file_path = Path(__file__).resolve().parent.parent / "Dataset" / "boardgames1.csv"
df = pd.read_csv(file_path)

# Create a folder for output figures
output_dir = Path(__file__).resolve().parent.parent / "Figures"
output_dir.mkdir(exist_ok=True)

# Display dataset information
print("Dataset shape:", df.shape)

# Display relevant columns
print(df[["name", "sortindex", "average"]].head(10))


# ============================================================
# SECTION 3: DATA CLEANING
# ============================================================

# Extract relevant columns
rankings = df[["sortindex", "average"]].copy()

# Check for missing values
print("\nMissing values:")
print(rankings.isnull().sum())

# Remove missing and invalid values
rankings = rankings.dropna()
rankings = rankings[rankings["sortindex"] > 0]
rankings = rankings[rankings["average"].between(1, 10)]

# Display data cleaning results
print("\nData Cleaning Results:")
print(f"Original number of games: {len(df)}")
print(f"Valid number of games: {len(rankings)}")
print(f"Excluded games: {len(df) - len(rankings)}")

# Extract rankings and ratings
rank = rankings["sortindex"]
rating = rankings["average"]


# ============================================================
# SECTION 4: DESCRIPTIVE STATISTICS
# ============================================================

print("\nDescriptive Statistics:")
print(rankings.describe())


# ============================================================
# SECTION 5: CORRELATION ANALYSIS
# ============================================================

# Pearson correlation
pearson_r, pearson_p = stats.pearsonr(rank, rating)

# Spearman correlation
spearman_r, spearman_p = stats.spearmanr(rank, rating)

# Display Pearson correlation results
print("\nPearson Correlation:")
print(f"Correlation coefficient: {pearson_r:.4f}")
print(f"P-value: {pearson_p:.4e}")

# Display Spearman correlation results
print("\nSpearman Correlation:")
print(f"Correlation coefficient: {spearman_r:.4f}")
print(f"P-value: {spearman_p:.4e}")


# ============================================================
# SECTION 6: LINEAR REGRESSION ANALYSIS
# ============================================================

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(rank, rating)

# Calculate coefficient of determination
r_squared = r_value ** 2

# Display regression results
print("\nLinear Regression:")
print(f"Slope: {slope:.8f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_squared:.4f}")
print(f"P-value: {p_value:.4e}")

# Calculate regression line
regression_line = slope * rank + intercept


# ============================================================
# SECTION 7: CHI-SQUARE GOODNESS-OF-FIT TEST
# ============================================================

# Define rating intervals
bins = np.arange(1, 11, 1)

# Calculate observed frequencies
observed, bin_edges = np.histogram(rating, bins=bins)

# Calculate expected frequencies for a uniform distribution
expected = np.full(len(observed),
                   len(rating) / len(observed))

# Perform chi-square test
chi_stat, chi_p = stats.chisquare(observed, expected)

# Define significance level
alpha = 0.05

# Display chi-square test results
print("\nChi-Square Goodness-of-Fit Test:")
print("Observed frequencies:", observed)
print("Expected frequencies:", expected)
print(f"Chi-square statistic: {chi_stat:.4f}")
print(f"Degrees of freedom: {len(observed) - 1}")
print(f"P-value: {chi_p:.4e}")

# Evaluate the null hypothesis
if chi_p < alpha:
    print("Reject the null hypothesis.")
else:
    print("Fail to reject the null hypothesis.")


# ============================================================
# SECTION 8: RATING DISTRIBUTION PERCENTAGES
# ============================================================

# Calculate rating distribution percentages
percentages = observed / len(rating) * 100

print("\nRating Distribution Percentages:")

for i in range(len(observed)):
    print(f"{bins[i]}-{bins[i+1]}: {percentages[i]:.2f}%")

# Percentage of games rated from 5 to below 8
middle_percentage = sum(observed[4:7]) / len(rating) * 100

print(f"\nGames rated from 5 to below 8: {middle_percentage:.2f}%")


# ============================================================
# SECTION 9: OBSERVED VS. EXPECTED DISTRIBUTION PLOT
# ============================================================

plt.figure(figsize=(10, 6))

# Calculate the centers of each rating interval
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Plot observed frequencies
plt.bar(bin_centers - 0.2, observed, width=0.4,
        label="Observed Frequencies", color="steelblue")

# Plot expected frequencies
plt.bar(bin_centers + 0.2, expected, width=0.4,
        label="Expected Frequencies", color="orange")

# Configure figure labels and title
plt.xlabel("Average User Rating Interval")
plt.ylabel("Number of Board Games")
plt.title("Observed vs. Uniform Distribution of User Ratings")

plt.xticks(bin_centers,
           [f"{i}-{i+1}" for i in range(1, 10)])

plt.legend()
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# Save figure
plt.savefig(output_dir / "Q2_rating_distribution.png", dpi=300)


# ============================================================
# SECTION 10: LINEAR REGRESSION SCATTERPLOT
# ============================================================

plt.figure(figsize=(10, 6))

# Plot observed ratings
plt.scatter(rank, rating, s=5, alpha=0.3,
            label="Observed Ratings")

# Plot linear regression
plt.plot(rank, regression_line, color="red",
         linewidth=2, label="Linear Regression")

# Configure figure labels and title
plt.xlabel("Board Game Rank")
plt.ylabel("Average User Rating (1-10)")
plt.title("Board Game Rankings vs. Average User Ratings")

plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Save figure
plt.savefig(output_dir / "Q2_linear_regression.png", dpi=300)


# ============================================================
# SECTION 11: DISPLAY FIGURES
# ============================================================

plt.show()