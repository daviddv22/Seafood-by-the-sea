# Tech Report
<!-- Link to data https://github.com/csci1951a-spring-2023/final-project-little-mermaids/blob/main/data/yelp-data-whole.json -->
## Data Size
Out of the 944 restaurants in wholedatabase.db, 247 records have an N/A value for prices. The records with N/A price values can only be used to evaluate the correlation between the rating of seafood restaurants with a coast versus inland. Thus, when looking at restaurant ratings, considering that around 20% of the data points will be used for validating the results (around 190 records), the actual number of data points that will be analyzed will be lower. On the other hand, when looking at the correlation between the price of seafood restaurants with a coast versus inland, we will have 697 data points. Regardless, even if we use around 20% (around 140 records) for validation, the data will provide a reasonable amount of information for computing both correlations.

## Attributes
The data includes information about a restaurant, such as its name, address, city, state, zip code, rating, price point, and the review count (see Data Specs in the project README).

## Data Reputability
Data was collected using the Yelp API and web scraping of Tripadvisor.

Yelp is a popular review platform with a fairly long history. It also has a large and loyal user base, making it a reliable source of data. The sample may exhibit some level of sampling bias, as the results are based on user-generated content and may be influenced by various factors, such as the popularity of the restaurant or the preferences of the Yelp user base; however, the website does have thorough regulation of its reviewing process.

TripAdvisor is a well-known travel website that provides a platform for travelers to post reviews and ratings of hotels, restaurants, and attractions. The website has a large user base and allows users to rate and review establishments on a scale of 1 to 5. While TripAdvisor's rating system is based on user-generated content, the website does have mechanisms in place to prevent fake reviews and ratings. For example, the website uses algorithms to identify and remove suspicious content and also employs a team of content moderators to manually review questionable content.

## Data Cleaning
Given the requirements for a review on Yelp's platform, the data is generally quite clean. Duplicate rows (i.e restaurants) may be a consideration in an outdated database or if we were to collect information from more than one source. The data from TripAdvisor was scraped and set into the same format as that collected from the Yelp API.

In terms of cleaning mechanisms, we checked for duplicate rows of restaurants and considered only requesting the data with a valid price field and dropping restaurants with an N/A value. Currently, our wholedatabase.db still contains restaurants with N/A pricepoints, as we are still considering whether these may be of any use to us. Aside from this column, there is only one other field that contains a missing value; however, since this field is not vital to our project goals this was overlooked.

## Data Distribution
Rating values - users of Yelp and TripAdvisor can only rate in terms of ints on a 1-5 scale:

MIN: 1.0, MAX: 5.0

The distribution of the ratings column is quite a symmetric distribution, skewed slightly right if anything, for wholedata.db:
average: 4.0879
median: 4.0
Mode: 4.0

We'd also like to consider the distribution for the price points column. Price is currently a text, as it gives a string of dollar signs where more signs represent higher price. To be more usable for us, we may want to convert this to an int, equivalent to the amount of dollar signs. This can be very easily mapped to the database. After we do this, we can determine its distribution in a similar fashion as above.

## Additional Considerations
We need to add coastal/inland column and determine metrics for sorting the data for this. What should be our distinctions between what's considered coastal vs inland?

Can differences in price point be due to differing transport costs to restaurants more inland?

We need to keep in mind that ratings involve more than just the quality of the seafood (not a negative, but our primary question does seem to focus on seafood; must remember that seafood restaurants also may contain other items that may be more popular than the actual seafood items - may skew the ratings for a restaurant).

Does portraying ratings through their means (the typical method for ratings) skew our analysis in any way?

Since values for yelp ratings are set to the nearest whole/half rating, this doesn't yield accurate means per restaurant. Given the small rating scale of 1-5, it may overgeneralize ratings... will we need these nuances in the ratings (more accurate rating averages) for better consideration?

## Next Steps
We obtained most of the data that is necessary to make an analysis. We will still need to calculate the distance
of a resturant to the sea and reformat some of our data points such as pricing into an interger value. After 
data reformating, we can begin to analyze and test our question on the impact of a restaurant's location on its reviews, rating, and price as our data collection has not impacted the type of analysis we will perform. 