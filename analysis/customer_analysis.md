# Customer Analysis 

## 1. Customer Georaphical Distribuation 

### Customer Disturbuation by state 
The five states with the heighest number of customer records are: 
____________________________
| State | Customer Records |
|-------|------------------|
|  SP   |      41746       | 
|  RJ   |      12852       |
|  MG   |      11635       |
|  RS   |      5466        |
|  PR   |      5045        |
____________________________
** Observation ** 
Sao Paulo (SP) has the highest number of customer record, with 41,746, followed by Rio de Janerio (RJ) with 12, 852

### Geographical Reach
- Distinct cities: 4,119
- Total customer records: 99,441
- Unique customers: 96,096

** Observation ** 
The dataset represents customers acroess 4,119 different cites, indacting a geographical distribuation 

### Business Insights 
- São Paulo represents the largest concentration of customer records.
- Olist serves customers across a large number of Brazilian cities.
- Customer records and unique customers are different measures and should not be treated interchangeably.

## 2. Data Quiality Assessment 
## Missing values 

The dataset was inspected using Pandas' df.info().sum() method.
The results showed that all five columns contained 99,441 non-null values, indicating that no missing values were identified.
## Duplicated records 

The dataset was inspected using Pandas' df.duplicated() method to identify duplicate rows.
The result returned 0 duplicate records, indicating that no identical rows were found in the customers dataset.

### Customer Identifier Analysis

The dataset contains 99,441 distinct `customer_id` values and 96,096 distinct `customer_unique_id` values.

This indicates that some customer records are associated with the same unique customer identifier.

**Finding:** There are 3,345 more customer records than unique customers. This highlights the importance of using `customer_unique_id` when analysing customer behaviour and repeat purchases.

*Note: The number of repeat customers will be investigated further using the orders dataset.*