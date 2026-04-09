# Pandas Learning Folder

This folder contains beginner-friendly practice files for learning Pandas step by step.

## What You Learn Here

- What data manipulation and data analysis mean
- Why Pandas is useful
- Basic DataFrame concepts (rows, columns, dtypes)
- How to inspect data using methods like info(), shape, and columns
- How to select columns and filter rows
- How to save output to files

## Prerequisites

- Python 3.x installed
- Pandas installed

Install Pandas:

```bash
pip install pandas
```

## Files in This Folder

- about.txt: Notes about data manipulation, analysis, and Pandas basics
- problem.txt: Practice questions and concepts to check in a dataset
- data.txt: Data-related notes/examples
- app.py: Main practice script for DataFrame operations
- topic.py: Example showing DataFrame creation, shape, and columns
- describe.py: Practice with describe() and summary statistics
- rows.py: Row selection/filtering practice
- save.py: Saving DataFrame output to files
- problemexmple.py: Problem-based example script

## Generated Output Files

These files are also part of this Pandas practice workflow and are created by save/export examples.

- ../output.csv: CSV export output
- ../output.json: JSON export output
- ../output.xlsx: Excel export output

## Quick Example

```python
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari"],
    "Age": [28, 34, 22],
    "Salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df.shape)      # (rows, columns)
print(df.columns)    # column names
print(df.dtypes)     # data types of each column
print(df.info())     # complete structure summary
```

## Common Learning Notes

- Text columns are usually object dtype by default in many beginner examples.
- Numeric columns are commonly int64 or float64.
- Use boolean indexing for filtering rows.

## How to Run

From this Pandas folder:

```bash
python topic.py
python app.py
python describe.py
python rows.py
python save.py
```

## Goal of This Folder

Build a strong foundation in Pandas so you can clean data, analyze trends, and prepare datasets for real projects.
