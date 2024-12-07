# Data Exploration and Wrangling Assignment

## Objective

The goal of this assignment is to evaluate your understanding of Data Exploration and Data Wrangling concepts. You will apply standard Python libraries to clean, explore, and analyze a provided dataset.

## Assignment Overview

In this assignment, you are provided with a dataset containing 1000 records of personal information. The dataset has various inconsistencies, missing values, and data quality issues. You will need to:

1. **Analyze the Dataset**  
   - Identify and summarize the inconsistencies or issues present in each column.
   - Provide insights into the distribution of key attributes (e.g., Age, Gender, Income).

2. **Clean and Fix the Dataset**  
   - Handle missing values appropriately.
   - Fix inconsistencies in formatting (e.g., non-standard number formats, malformed email addresses).
   - Ensure all columns adhere to valid data types and formats.

3. **Generate Insights**  
   - After cleaning, create a summary of trends and patterns in the data.
   - Highlight any relationships or correlations between variables such as Age, Weekly Wage, and Job Status.

## Dataset Overview

The dataset includes the following columns:

- **ID**: Unique 7-character alphanumeric identifiers. May contain duplicates.
- **Name**: Full names with random capitalization and missing middle names.
- **Date of Birth**: Two date formats with some missing values.
- **Age**: Derived from DOB but has missing or inconsistent entries.
- **Gender**: M/F/O.
- **Body Mass Index (BMI)**: Includes some missing data.
- **Address**: Concatenated address strings.
- **Weekly Wage**: Ranges from 100 to 10,000, including dirty formats like "5K".
- **Job Status**: Student, Employed, or Unemployed.
- **Profession**: Relevant for employed individuals, with some inconsistencies.
- **Annual Income**: Ranges from 5,000 to 500,000, with dirty formats and missing values.
- **Email Address**: Valid and malformed emails.
- **Contact Number**: 11-digit numbers with some non-standard formats.
- **Marital Status**: Married/Unmarried.
- **# of Dependants**: Numeric values with occasional non-standard text entries.
- **Avg Monthly Expenditure**: Ranges from 50 to 500,000, including dirty formats.

## Instructions

### 1. Dataset File
The dataset is located in the `data` directory under the name `data.csv`. You need to read it into a pandas dataframe.

### 2. Environment Setup
Make sure you have the following libraries installed:
```bash
pip install pandas numpy matplotlib
```

### 3. Solution Approach
Follow the steps provided in the notebook to:
- Import necessary libraries.
- Load the dataset and start analyzing.
- Clean and fix the dataset by handling missing values and correcting formats.
- Generate insights through data visualization and statistical analysis.

### 4. Test Cases
Each step is provided with public test cases to verify your solution. However, there are also hidden test cases that will be used to assess your solution.

### 5. Important Instructions
- **Do not delete any of the existing cells** in the notebook. These cells are part of the structure, and modifying them can affect the integrity of the assignment.
- Your **submission** should include the completed notebook, and it **must execute without any errors**. Make sure all code cells run successfully from top to bottom.