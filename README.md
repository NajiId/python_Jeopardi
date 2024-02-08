# Jeopardy Data Analysis

This project involves analyzing Jeopardy data using Python and the Pandas library. The script reads a dataset from a CSV file containing Jeopardy questions and answers, cleans the data, and performs various analyses.

## Requirements

- Python 3.x
- Pandas

## Usage

1. Clone the repository or download the Python script.

2. Ensure you have Python installed on your system.

3. Install the required libraries by running:

    ```bash
    pip install pandas
    ```

4. Run the Python script `jeopardy.py`.

## Functionality

The Python script performs the following tasks:

1. **Loading and Cleaning Data**:
   - Reads the Jeopardy dataset from a CSV file.
   - Cleans the column names by converting them to lowercase and stripping whitespace.
   - Renames specific columns for better readability.

2. **Filtering Data**:
   - Provides two filtering functions (`filter_data` and `my_filter`) to search for specific keywords in the questions.
   - Compares the results of both filtering functions to identify any differences.

3. **Statistical Analysis**:
   - Calculates the mean value of numerical answers.
   - Determines the count of unique answers.

4. **Question Comparison**:
   - Analyzes the usage of the word "Computer" in questions from the 90s and the 2000s.

5. **Category Analysis**:
   - Identifies whether the category "Literature" is more common in Single Jeopardy or Double Jeopardy rounds.

## Running the Script

Execute the Python script `jeopardy.py` in your preferred Python environment.

## Additional Notes

- The script sets the Pandas display option to show the full content of DataFrame columns for better readability.

## Acknowledgments

The Jeopardy dataset used in this project is for educational purposes only.

