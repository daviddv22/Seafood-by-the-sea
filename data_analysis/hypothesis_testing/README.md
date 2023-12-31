# Hypothesis Testing
## 1. region and Kruskal-Wallace H test: (null hypothesis: median price is the same per region, alternative hypothesis: median price is not the same per region)
Assumptions:
1. The samples are independent.
2. The distributions of each sample are identical except for the median.
3. The data should be continuous.
4. The samples are randomly selected.
5. The sample size is at least 5. \
statistic: 13.870920422610434 \
p-value: 0.003086222435632776 
- What is your interpretation of the results?
  - the region where a restaurant is located leads to statistically significant differences in price.
- Do you accept or deny the hypothesis?
  - we reject the null hypothesis.
- Intuitively, how do you react to the results?
  - intuitively, it makes sense that regions have different average prices for seafood, as their distances from the coast (transport costs, etc.) would vary.
- Are you confident in the results? 
  - yes.

## 2. rating and T-test: price point affects rating ( /$-$$ and $$$-$$$$$ groups and compare means)
Assumptions:
1. The ratings for each restaurant are independent.
2. The distribution of ratings are approximately normal.
3. The variance of ratings of each price group is approximately equal. \
statistic: -2.9738240558240285 \
p-value: 0.0030434156524699546 
- What is your interpretation of the results? 
  - price level does affect the rating. 
- Do you accept or deny the hypothesis? 
  - we accept the hypothesis.
- Intuitively, how do you react to the results? 
  - intuitively, it makes sense that people's internalization of price influences their overall rating (there is the belief that higher prices = higher quality = better). 
- Are you confident in the results? 
  - yes - we were not certain if we should instead be looking at whether rating affects price point, since our focus is price point; however, intuitively this wouldn't make any sense.

## 3. distance from ocean and Pearson Test:  there is a negative correlation between price point and distance from ocean (the higher the price point, the lower the distance from the ocean)
Assumptions:
1. The relationship between the price point and distance is linear.
2. Both price point and distance are normally distributed.
3. The variance of the residuals are constant across all levels of predictor variables.
4. The observations are independent. \
correlation coefficient: -0.0677816949963931 \
p-value: 0.09495515965411612 
- What is your interpretation of the results? 
  - negative correlation - there is no correlation between price and distance from the ocean.
- Do you accept or deny the hypothesis? 
  - we deny the hypothesis. 
- Intuitively, how do you react to the results? 
  - a few considerations here - we initially thought that price point would be higher closer to the ocean because restaurants may be more inclined to have higher prices for "higher quality seafood", but there is also the consideration that prices may be lower since restaurants that are closer to the ocean may have easier access to seafood resources.... considering these two points, it makes sense that there would be no conclusive correlation. 
- Are you confident in the results? 
  - yes. 

## Did you find the results corresponded with your initial belief of the data? If yes/no, why do you think this was the case?
### 1. region:
Yes, intuitively we believed that regions would have different average prices for seafood.
### 2. rating:
We weren't surprised by the results (as explained in the prior section); however, objectively, rating and price point shouldn't necessarily have a significant effect on one another if the reviewer is just considering the quality of the food; but it makes sense with the criticism levels of our modern food-savvy society. Price may influence rating when reviewers consider whether the price is worth the quality or restaurant ambiance.
### 3. distance from ocean:
After thinking about it, yes, as there were two perceptions of the data to consider (explained in the prior section).

## Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?
### 1. region:
Yes, the Kruskal-Wallis H test is an appropriate tool for analyzing whether the median price is the same per region or not. The Kruskal-Wallis H test is a non-parametric test used to compare the medians of more than two independent groups, and it does not assume that the data is normally distributed or has equal variances.
In this case, since we are comparing the median price across multiple regions, the Kruskal-Wallis H test is a suitable choice. The test statistic and p-value indicate that there is a statistically significant difference in median price across the regions. The low p-value suggests that we can reject the null hypothesis that the median price is the same across all regions.
### 2. rating:
T-Test: used to interpret whether something affects another variable
Yes, the t-test is an appropriate tool for analyzing the hypothesis that price point affects rating by comparing the means of two groups ( /$-$$ and $$$-$$$$$). The t-test is commonly used to compare the means of two groups and determine if there is a statistically significant difference between them. In this case, we are comparing the means of two groups based on their price point and testing if there is a significant difference in their ratings. The resulting t-test statistic and p-value can help us determine if there is a significant difference between the groups, and support or reject our hypothesis.
### 3. distance from ocean:
We considered the Kruskal-Wallis H test for price vs distance from ocean as well, but after thinking about it, Kruskal-Wallis H test is usually used to compare the medians of two or more independent groups. Since we specifically wanted to look at the correlation between two continuous variables (price point and distance from the ocean), the Pearson correlation coefficient seemed more appropriate. The Pearson correlation coefficient let us quantify the strength and direction of the relationship between the price point and the distance from the ocean. Our result showed that there was a weak negative correlation between price point and distance from the ocean. However, the p-value was above 0.05 (the typical significance level), which means that the observed correlation could be due to chance.
Was the data adequate for your analysis? If not what aspects of the data was problematic and how could you have remedied that?
interpretation of null values
remedy: we did not consider the null values, such as a null price point or no region.

************************************************************************************
### Machine Learning Models:

### Kernel Ridge Regression:
- Q1: Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
- A1: After testing multiple regression model, we found that the Kernel Ridge Regression model from sklearn.kernel_ridge to be the most accurate model. From this model, we got a R-squared score of -0.132, which is not a good score as it should be close to 1. However, I think the reason why the score is so low is because we either do not have enough data. For a linear regression model, we have gotten a R-squared score of ~-37 which signals that relationship between the data is not linear. This was much lower than other regression models such as linear regression model, SVMs, or knn models with much lower R-squared scores.


- Q2:What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?
    - A2:After testing multiple regression model, we found that the Kernel Ridge Regression model from sklearn.kernel_ridge to be the most accurate model. From this model, we got a R-squared score of -0.132, which is not a good score as it should be close to 1. However, I think the reason why the score is so low is because we either do not have enough data. For a linear regression model, we have gotten a R-squared score of ~-37 which signals that relationship between the data is not linear.
        
    - However, we still get predictions that make some sense, such as the rating of the example above with a distance of 2.1 miles from the ocean, a price point of 2, and a review count of 1000.1. The predicted rating is 4.1, which is a reasonable rating from what we have experimented with thus far. We are not satisfied with the prediction accuracy because we think that the accuracy can be improved if we have more data. We may attempt to obtain more data in the future to improve the accuracy of the model.

    - Intuitively, we were a little surprised by the results because we thought that the distance from the ocean would have a larger impact on the rating of the restaurant. However, we think that the model predicts this as it is likely the case that we do not have enough data to make a good prediction. We are not confident in the results because of the low and negative r-squared score and lack of variability in the predictions.

### NN:
- Q1:Why did you use this statistical test or ML algorithm? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?
    - A1: We used an NN because we wanted see if there was some non-linear function we could learn over the longitude and latitude coordinates to determine rating. 
    We can think of there being some surface over the united states defining where the best seafood restaurants, and hopefully this nn will help us approximate exactly what that surface is. Since we are trying to make a rating, we use mse as our metric for our model, using k-folds validation. We compare this against our linear model to see if it gives us a better surface than a simple linear one. In order to feed the price rarings into our model, we had some descisions to make. We could have put the relative price ratings in as a number, but this seemed unintuitive, and we didn't want to throw away all the data points with no price rating. Thus, we one-hot encoded our price ratings, include the 'n/a' entires, to solve these problems, essentiall letting the nn decide for us what to do with each rating. 

- Q2: What is your interpretation of the results? Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?
        
    - A2: Attempting to learn relationship between the data with a neural network, we found the average accuracy to be around .34. This was somewhat unsatisfactory but significantly better than our SVR model. We believe that this accuracy makes sense as it learns the relationship between the variables rather than trying to fit a line to the data. Additionally, we believe the lower accuracy was a result of the lack of data. We only had 1000 data points to train on, which is not a lot. For this model, if we have more data, we believe that we can achieve a higher accuracy.

    - Intuitively, we expected these results as we knew this model could learn relationships between the features and we did believe that our features had an impact on the rating of a restaurant. We are more confident in the results of this model than the SVR model as we believe that the features we chose to input into the model did have an impact on the rating of the restaurant. However, it is likely the case that we do not have enough data to make a good prediction. We are not confident in the results because of the relatively low accuracy.

### Machine Learning Models
- Q1: Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?
    - A3: Although we received a relatively low r-squared score, we still found that the prediction results still corresponded with our initial belief in the data. We believed that the distance from the ocean and its price point would have a significant impact on the rating of the restaurant. We did not expect our r-squared score to be as low as it was but we believe that the reason for this is because we do not have enough data and something that can be addressed the future. For our neural network, we achieved better results because of the nature of neural networks learning features that we as human may not be able to discern. We were able to reach an accuracy of ~35% which was better than expected due to the performance of our SVR model. This model faces the same issue of the lack of data, and we believe that if we had more data we would be able to achieve a higher accuracy. In conclusion, we found that using a neural network to predict the rating of the model was the best machine learning model that we attempted. Furthermore, with more data both model could have achieved a higher accuracy and performance and something we may try to address before the end of this project. 

- Q2: Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?
    - A4: Yes, we believe that the tools for analysis that we chose was appropriate. We tested many models to see what best fit out data. We tried a clustering model, but that did not make too much sense with our hypothesis. We then tried a KNN model, however, the results were not very good. We then tried a simple linear regression model, which seemed to predict okay but had a r-squared score of ~ -37 which was quite low. We tried to remedy this by adding regularization using the Ridge, Lasso, and SVM models, however, the improvement was not great. Ultimately, we concluded that the relationship of our data was not linear and a non-linear model was required. This lead us to use a KernelRidge model, a model that does Ridge regression (which includes regularization) with a non-linear function. This model was able to predict the rating of the restaurant with a r-squared score of ~ -0.132, which was the best score of the models that we experimented thus far. We believe that this model was the best model for the data we currently had, and was an appropriate for the analysis.

- Q3: Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?
    - A5: Although we believe that the features we chose was adequate for our analysis, we believe as a whole our data was not adequate for our machine learning analysis. This is because machine learning requires a lot of data. However, we only had ~1000 data points. which we believe was not enough data for our models to accurately predict the rating of a restaurant from our features. We believe that if we had more data, we would have been able to achieve a higher r-squared score and a more accurate prediction and remedy these issues. Other than our lack of data points, we believe that our data structure was adequate for our analysis.
