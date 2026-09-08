# Day 1 — Data Cleaning and Preprocessing

## Overview
This project demonstrates a practical data-cleaning workflow using **Python, Pandas, and Excel**.

The dataset is a deliberately messy **practice sales dataset** created for this Day 1 task. It contains realistic data-quality issues such as missing values, duplicate rows, inconsistent capitalization/whitespace, mixed date formats, and numeric fields stored as text.

## Objective
Prepare the raw dataset for reliable downstream analysis by identifying, documenting, and resolving common data-quality problems.

## Tools
- Python
- Pandas
- Excel
- Jupyter Notebook

## Data Quality Issues
1. Missing email, quantity, and unit-price values
2. An exact duplicate row
3. Leading/trailing whitespace
4. Inconsistent capitalization
5. Mixed date formats
6. Numeric values stored as strings
7. Need for a validated derived metric (`Total_Sales`)

## Cleaning Approach
- Inspected structure with `df.info()`
- Audited missing values with `df.isnull().sum()`
- Audited duplicates with `df.duplicated().sum()`
- Trimmed whitespace
- Standardized text casing
- Normalized email casing
- Converted dates and numeric fields
- Handled missing values according to column context
- Removed exact duplicate records
- Calculated `Total_Sales`
- Re-ran validation checks after cleaning

## Files
- `data/raw_dataset.csv` — original messy practice dataset
- `data/cleaned_dataset.csv` — cleaned output
- `data/data_cleaning_workbook.xlsx` — Raw Data, Cleaned Data, and Change Log sheets
- `scripts/data_cleaning.py` — reproducible Pandas cleaning script
- `notebooks/data_cleaning.ipynb` — notebook version of the workflow
- `reports/Data_Cleaning_Report.pdf` — project report
- `screenshots/cleaning_validation.png` — before/after validation evidence
- `LinkedIn_Post_Draft.txt` — prepared LinkedIn post text

## Validation
The final dataset was checked for:
- Remaining missing values
- Remaining duplicate rows
- Corrected data types
- Consistent text formatting

## Results
- Rows: **21 → 20**
- Missing values: **3 → 0**
- Duplicate rows: **1 → 0**

## Note
This is a practice dataset prepared specifically for the Day 1 learning task. It should not be represented as an official Kaggle, Superstore, or Titanic dataset.
