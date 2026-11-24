# Product Category Analysis

## 1. Dataset Overview

The Olist products dataset (`olist_products_dataset.csv`) contains **32,951 product records** across 9 columns. It provides information about product categories, descriptions, dimensions, weight and photos.

The `product_category_name_translation.csv` dataset contains **71 Portuguese-to-English category translations**. This will allow us to present category names in English during analysis and visualisation.

## 2. Data Quality Findings

- No duplicate rows were identified in the products dataset.
- 610 records have missing product category names.
- 610 records also have missing product name length, description length and photo quantity.
- 2 records have missing product weight and dimensions.
- The translation dataset contains no missing values or duplicate rows.

Missing category information may affect category-level analysis, so these records will need to be investigated during data cleaning.

## 3. Product Characteristics

| Metric | Average |
|---|---:|
| Product name length | 48.48 characters |
| Product description length | 771.50 characters |
| Number of photos | 2.19 |
| Product weight | 2,276.47 g |
| Product length | 30.82 cm |
| Product height | 16.94 cm |
| Product width | 23.20 cm |

The median product weight is 700 g, compared with an average of approximately 2.28 kg. This suggests that some heavier products may be influencing the average.

## 4. Business Relevance

Product category information will be important for understanding:

- Which categories generate the most revenue.
- Which categories sell the most products.
- Which categories perform best across different months.
- Which categories receive the highest average customer review scores.
- Whether product categories have different delivery or freight cost patterns.

## 5. Next Steps

The product dataset will be joined with the order items dataset using `product_id`. The category translation dataset will then be joined using `product_category_name`.

This will allow us to analyse actual sales activity by product category rather than relying only on product catalogue information.

**Important:** Missing category values and category names without English translations should be checked before the final analysis. We should not automatically remove these records because they may still contain valid sales information.