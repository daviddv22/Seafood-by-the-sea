import sqlite3
import pandas as pd
from scipy.stats import kruskal, ttest_ind, levene, pearsonr, chi2_contingency

def perform_kruskal_wallis_test(data):
    regions = data['region'].unique()
    prices_by_region = [data[data['region'] == region]['int_price'].values for region in regions]
    return kruskal(*prices_by_region)

def perform_levene_ttest(df):
    cheap_group = df[df['int_price'].isin([1, 2])]
    exp_group = df[df['int_price'].isin([3, 4, 5])]
    levene_result = levene(cheap_group['rating'], exp_group['rating'])
    ttest_result = ttest_ind(cheap_group['rating'], exp_group['rating'])
    ch2_squared = chi2_contingency(cheap_group['rating'], exp_group['rating'])
    return levene_result, ttest_result, ch2_squared

def perform_pearson_correlation(df):
    grouped_data = df.groupby('distance').median()
    return pearsonr(grouped_data.index, grouped_data['int_price'])

def main():
    # Connect to databases
    with sqlite3.connect('databases/wholedata.db') as wholedata, \
         sqlite3.connect('databases/oceanDistance.db') as distancedata:

        # Hypothesis 1
        distance_df = pd.read_sql_query('SELECT name, region FROM oceanDistance', distancedata)
        price_df = pd.read_sql_query('SELECT name, int_price FROM resturants WHERE int_price IS NOT NULL', wholedata)
        merged_df = pd.merge(distance_df, price_df, on='name')
        kruskal_result = perform_kruskal_wallis_test(merged_df)
        print("Kruskal-Wallis H test result:", kruskal_result)

        # Hypothesis 2
        df = pd.read_sql_query('SELECT * FROM resturants', wholedata)
        df['rating'] = df['rating'].astype(float)
        levene_result, ttest_result, ch2_squared = perform_levene_ttest(df)
        print("Levene's test result:", levene_result)
        print("Chi-square test result:", ch2_squared)
        print("T-test result:", ttest_result)

        # Hypothesis 3
        distance_data_3 = pd.read_sql_query('SELECT name, distance FROM oceanDistance', distancedata)
        merged_data_3 = pd.merge(price_df, distance_data_3, on='name')
        merged_data_3['distance'] = merged_data_3['distance'].astype(float)
        pearson_corr, p_value = perform_pearson_correlation(merged_data_3)
        print("Pearson correlation coefficient:", pearson_corr)
        print("p-value:", p_value)

if __name__ == "__main__":
    main()