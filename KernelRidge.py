import numpy as np
import sqlite3
import tensorflow as tf
from sklearn.kernel_ridge import KernelRidge
from sklearn.metrics import r2_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import KFold
import plotly.express as px

RANDOM_SEED = 10
REGION_MAPPING = {'North': 1, 'South': 2, 'East': 3, 'West': 4, '': 5, 'Central': 6, 
                  'Northeast': 7, 'Northwest': 8, 'Southeast': 9, 'Southwest': 10, 'Midwest': 11}

def get_data_from_db(query, db_path):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        return cur.execute(query).fetchall()

def preprocess_data(distances, regions, prices, labels, review_counts):
    # Processing regions and prices
    processed_regions = [REGION_MAPPING.get(region, 5) for region in regions]
    processed_prices = [2 if price == 'N/A' else 1 if price == '$' else 2 if price == '$$' else 3 if price == '$$$' else 4 for price in prices]
    
    # One-hot encoding
    price_one_hot = tf.one_hot(processed_prices, depth=5).numpy()
    region_one_hot = tf.one_hot(processed_regions, depth=11).numpy()
    
    # Normalizing review counts
    review_counts = np.array(review_counts)
    normalized_reviews = (review_counts - np.mean(review_counts)) / np.std(review_counts)
    
    # Creating the feature matrix
    return np.hstack((price_one_hot, np.array(distances)[:, None], normalized_reviews[:, None], region_one_hot))

def train_and_evaluate_model(X, Y, model, n_splits=5):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=RANDOM_SEED)
    total_accuracy = 0

    for train_index, test_index in kf.split(X):
        X_train, Y_train = X[train_index], Y[train_index]
        X_test, Y_test = X[test_index], Y[test_index]

        model.fit(X_train, Y_train)
        y_pred = model.predict(X_test)

        accuracy = r2_score(y_pred, Y_test)
        n = X_train.shape[0]
        k = X_train.shape[1]
        adj_r_squared = 1 - ((1 - accuracy) * (n - 1) / (n - k - 1))

        print(f"Fold {i+1} - R-squared: {accuracy}, Adjusted R-squared: {adj_r_squared}")
        total_accuracy += adj_r_squared

    return total_accuracy / n_splits

def plot_confusion_matrix(Y, y_pred, title, filename):
    cf_matrix = confusion_matrix(Y, y_pred)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cf_matrix[2:], annot=True, fmt='', cmap='viridis', xticklabels=['0', '1', '2', '3', '4', '5'], \
            yticklabels=['True Negative', 'False Negative','True Positive', 'False Positive'])
    plt.title(title)
    plt.savefig(filename)
    plt.clf()

def save_choreograph():
    # create choropleth of all states and their ratings
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    
    x = cur2.execute('SELECT state, rating FROM resturants')
    state_ratings = {}
    for state, rating in x:
        if state not in state_ratings:
            state_ratings[state] = [rating]
        else:
            state_ratings[state].append(rating)
    y = []
    for state in state_ratings:
        y.append(np.mean(state_ratings[state]))
    
    y.append(3)
    fig = px.choropleth(locations=states, locationmode="USA-states", color=y,
                        scope="usa", color_continuous_scale="Viridis",
                        title="Average Rating of Restaurants in Each State")
    fig.update_layout(
        title={
            'text': "Average Rating of Restaurants in Each State",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(
        title_font_family="Times New Roman",
        title_font_color="black",
        title_font_size=24)
    fig.update_layout(
        font_family="Times New Roman",
        font_color="black",
        font_size=18)
    fig.update_layout(
        coloraxis_colorbar=dict(
            
            title="Rating",
            thicknessmode="pixels", thickness=50,
            lenmode="pixels", len=300,
            yanchor="top", y=1,
            ticks="outside", ticksuffix="",
            dtick=0.5
        )
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.write_image("analysis_deliverable/choropleth.png")

    # create choropleth of all states and their prices
    states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    
    x = cur2.execute('SELECT state FROM resturants')
    state_prices = {}
    for state, price in zip(x, price_points):
        if state not in state_prices:
            state_prices[state] = [price]
        else:
            state_prices[state].append(price)
    y = []
    for state in state_prices:
        y.append(np.mean(state_prices[state]))

    y.append(2)
    fig = px.choropleth(locations=states, locationmode="USA-states", color=y,
                        scope="usa", color_continuous_scale="Viridis",
                        title="Average Price of Restaurants in Each State")
    fig.update_layout(
        title={
            
            'text': "Average Price of Restaurants in Each State",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
    fig.update_layout(
        title_font_family="Times New Roman",
        title_font_color="black",
        title_font_size=24)
    fig.update_layout(
        font_family="Times New Roman",
        font_color="black",
        font_size=18)
    fig.update_layout(
        coloraxis_colorbar=dict(
        
            
            title="Price",
            thicknessmode="pixels", thickness=50,
            lenmode="pixels", len=300,
            yanchor="top", y=1,
            ticks="outside", ticksuffix="",
            dtick=0.5
        )
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig.write_image("analysis_deliverable/choropleth2.png")


def main():
    # Fetching and preprocessing data
    distances_data = get_data_from_db('SELECT distance, region FROM oceanDistance', './databases/oceanDistance.db')
    distances, regions = zip(*distances_data)

    ratings_data = get_data_from_db('SELECT rating, price, review_count FROM resturants', './databases/wholedata.db')
    labels, prices, review_counts = zip(*ratings_data)

    X = preprocess_data(distances, regions, prices, labels, review_counts)
    Y = np.array(labels, dtype=float)

    # Training and evaluating model
    model = KernelRidge(alpha=1.0, kernel='poly')
    average_accuracy = train_and_evaluate_model(X, Y, model)
    print(f"Average accuracy of Kernel Ridge regression model: {average_accuracy}")

    # Plotting confusion matrix
    y_pred = model.predict(X).astype(int)

    y_pred[y_pred > 5] = 0
    y_pred[y_pred < 0] = 0

    Y = Y.astype(int)
    Y[Y > 5] = 0
    Y[Y < 0] = 0

    plot_confusion_matrix(Y, y_pred, 'Confusion Matrix for Kernel Ridge Regression Model', 'confusion_matrix.png')

if __name__ == "__main__":
    main()
