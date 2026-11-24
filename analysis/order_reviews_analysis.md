### Order Reviews Dataset Inspection

- Total records: 99,224
- Total columns: 7
- Duplicate rows: 0
- Unique review IDs: 98,410
- Unique order IDs: 98,673

**Missing values:**
- Review titles: 87,656
- Review messages: 58,247
- Review scores and timestamps: 0

**Review score statistics:**
- Average score: 4.09 / 5
- Median score: 5
- Highest score: 5
- Lowest score: 1

**Initial findings:**
- Five-star reviews are the most common, with 57,328 records.
- Four-star reviews are the second most common, with 19,142 records.
- The average review score indicates generally positive customer feedback.
- Many customers submitted ratings without written comments.
- Repeated review and order identifiers require further investigation before joining datasets.

**Further analysis:** Customer satisfaction by product category and the relationship between delivery delays and review scores will be investigated using SQL.