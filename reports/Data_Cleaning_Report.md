# Day 1 — Data Cleaning and Preprocessing

**Prepared by:** AJMAL K H  
**Domain:** Data Analytics  
**Tools:** Python, Pandas, Excel, Jupyter Notebook

## 1. Objective
Inspect and clean a raw sales dataset containing common data-quality problems, then produce a reliable dataset suitable for downstream analysis.

## 2. Dataset
A deliberately messy practice sales dataset was created for this learning task. It contains missing values, a duplicate record, inconsistent whitespace/capitalization, mixed date formats, and numeric fields stored as text.

## 3. Issues Identified
- Missing email, quantity, and unit-price values
- One exact duplicate row
- Leading/trailing whitespace
- Inconsistent capitalization
- Mixed date formats
- Numeric values stored as strings

## 4. Cleaning Methodology
The workflow used `df.info()`, `df.isnull().sum()`, and `df.duplicated().sum()` for initial inspection. Text fields were trimmed and standardized. Emails were normalized to lowercase. Dates were parsed using mixed-format handling with day-first interpretation, while numeric fields were converted to numeric types. Missing values were handled according to column context. Exact duplicate rows were removed. A `Total_Sales` field was calculated as `Quantity × Unit_Price`.

## 5. Validation Results
| Metric | Before | After |
|---|---:|---:|
| Rows | 21 | 20 |
| Missing values | 3 | 0 |
| Duplicate rows | 1 | 0 |

## 6. Deliverables
- Raw dataset
- Cleaned dataset
- Change log
- Pandas cleaning script
- Jupyter notebook
- README
- LinkedIn post draft

## 7. Conclusion
The final dataset contains no missing values or duplicate rows and has standardized text and corrected data types. The workflow is documented and reproducible, providing a clean foundation for analysis.

> Note: This is a practice dataset created specifically for the Day 1 learning task and is not an official external dataset.
