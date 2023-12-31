# Data spec
## Assumptions
1. All fields are present, except for the image_url field in the user dictionary, which may be missing
2. All fields have the specified data types
3. The review field is not required

## Attributes
### 1. Id
- Type of data: string
- Default value: N/A
- Range of value: Yelp's unique identifier for each business
- Simplified analysis of the distribution of values: Each business has a unique ID assigned by Yelp.
- Are these values unique? Yes, each business has a unique ID assigned by Yelp.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? Yes, the ID can be used along with other attributes to 
detect and remove duplicate records.
- Is this a required value? Yes, it is a required value as it uniquely identifies each business.
- Do you plan to use this attribute/feature in the analysis? Yes, this attribute will be used to join business information with reviews data.
- Does this feature include potentially sensitive information? No, it does not include any sensitive information.
### 2. Name
- Type of data: string
- Default value: N/A
- Range of value: The name of the business
- Simplified analysis of the distribution of values: Business names are mostly unique, while often two businesses have the same name. There are four names
that have more than 5 duplicates. Overall, the distribution seems to be pretty even (most business names are unique).
- Are these values unique? Business names can be unique or non-unique.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? Yes, the name can be used along with other attributes 
to detect and remove duplicate records, although other attributes might be more helpful since there can be multiple businesses with the same name.
- Is this a required value? Yes, it is a required value as it identifies the name of the business.
- Do you plan to use this attribute/feature in the analysis? Yes, this attribute will be used to identify businesses and analyze their ratings, reviews, 
and other attributes.
- Does this feature include potentially sensitive information? No, it does not include any sensitive information.
### 3. Address
- Type of data: string
- Default value: N/A
- Range of value: The street address of the business
- Simplified analysis of the distribution of values: There are 2 addresses that are used by 3 businesses and 11 used by 2 businesses. Overall, the 
distribution seems pretty even (most addresses are unique).
- Are these values unique? Addresses can be unique or non-unique.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? Yes, the address can be used along with other attributes
to detect and remove duplicate records.
- Is this a required value? Yes, it is a required value as it identifies the physical location of the business.
- Do you plan to use this attribute/feature in the analysis? Yes, this attribute will be used to identify businesses and analyze their ratings, reviews, 
and  other attributes.
- Does this feature include potentially sensitive information? No, it does not include any sensitive information.
### 4. City
- Type of data: string
- Default value: N/A
- Range of value: The city in which the business is located
- Simplified analysis of the distribution of values: Some cities have more businesses than others (> 10 businesses), so the distribution could be 
non-uniform without a particular trend as of now, although the distribution type could not be determined now.
- Are these values unique? City names can be non-unique.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? No, since the city might not be a unique identifier 
and multiple restaurants can exist in the same state.
- Is this a required value? Yes, it is a required value as it identifies the city in which the business is located.
- Do you plan to use this attribute/feature in the analysis? Yes, this attribute will be used to analyze businesses by city, to help determine whether the 
business is inland or with a coast.
- Does this feature include potentially sensitive information? No, it does not include any sensitive information.
### 5. State
- Type of data: string
- Default value: N/A
- Range of value: 2-character abbreviation for US states (e.g. "AL" for Alabama)
- Simplified analysis of the distribution of values: The distribution of values will depend on the number of restaurants in each state, but some states 
have more restaurants than others, making the distribution non-uniform.
- Are these values unique?: Yes, each state abbreviation should be unique.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?: No, since state is not a unique identifier 
and multiple restaurants can exist in the same state.
- Is this a required value?: Yes, since it is necessary to identify the location of the restaurant.
- Do you plan to use this attribute/feature in the analysis? If so, how?: Yes, we can use state as a grouping variable to analyze trends in restaurant 
ratings and prices across different regions of the US (particularly inland versus with a coast).
- Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?: No, state abbreviations are publicly 
available information.
### 6. Zip code
- Type of data: string
- Default value: N/A
- Range of value: 5-digit US zip code (e.g. "35243") (theoretically "00000" to "99999")
- Simplified analysis of the distribution of values: The distribution of values will depend on the location of the restaurants, but we can assume that 
some zip codes will have more restaurants than others, making the distribution non-uniform.
- Are these values unique?: No, since multiple restaurants can exist in the same zip code.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?: Yes, we can use zip code in combination 
with restaurant name and address to identify possible duplicate records.
- Is this a required value?: Yes, since it is necessary to identify the location of the restaurant.
- Do you plan to use this attribute/feature in the analysis? If so, how?: Yes, we can use zip code as a grouping variable to analyze trends in restaurant 
ratings and prices across different regions of the US (particularly inland versus with a coast)..
- Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?: Yes, zip codes can be used to identify 
the general location of a person or business. To handle this issue, we can either remove zip code information or aggregate data at a higher level 
(e.g. city or state) to protect individual privacy.
### 7. Rating
- Type of data: float
- Default value: N/A
- Range of value: 0-5, in increments of 0.5 (e.g. 4.5)
- Simplified analysis of the distribution of values: The distribution of values will depend on the quality of the restaurants, but we can assume that most 
restaurants will have a rating between 3 and 4.5 stars. 
- Are these values unique?: No, multiple restaurants can have the same rating.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? If so, how?: No, since rating is not a unique
identifier and multiple restaurants can have the same rating.
- Is this a required value?: Yes, since it is an important measure of the quality of the restaurant.
- Do you plan to use this attribute/feature in the analysis? If so, how?: Yes, we can use rating as a variable to analyze the factors that contribute to 
the quality of a restaurant along with price in our project.
- Does this feature include potentially sensitive information? If so, how do you suggest handling such issues?: No, restaurant ratings are publicly 
available information.
### 8. Price
- Type of data: String
- Default value: N/A
- Range of value: "$" - "$$$$$" (1-5 dollar signs)
- Simplified analysis of the distribution of values: The distribution of values is likely to be skewed to the left, with the majority of restaurants 
falling in the $ to $$ range.
- Are these values unique? No, there may be multiple restaurants with the same price.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? No, price alone is not sufficient to detect duplicate 
records.
- Is this a required value? No, some restaurants may not have a price listed. In our data, there are some data points with an N/A value as the price.
- Do you plan to use this attribute/feature in the analysis? Yes, price will be used as a feature in the analysis to explore the relationship between 
price and other attributes such as rating and review count.
- Does this feature include potentially sensitive information? No, price is not sensitive information.
### 9. Review count
- Type of data: Integer
- Default value: 0
- Range of value: 1 - 8320 (depends on the popularity of the restaurant)
- Simplified analysis of the distribution of values: The distribution of values is likely to be highly skewed to the right, with a few very popular 
restaurants having a disproportionately high number of reviews.
- Are these values unique? Yes, each restaurant has a unique review count.
- Will you use this value (maybe in composition with others) to detect possible duplicate records? No, review count alone is not sufficient to detect 
duplicate records.
- Is this a required value? No, some restaurants may not have a review count listed.
- Do you plan to use this attribute/feature in the analysis? Yes, review count will be used as a feature in the analysis to explore the relationship 
between review count and other attributes such as rating and price.
- Does this feature include potentially sensitive information? No, review count is not sensitive information.
