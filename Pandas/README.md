# Pandas Learning Folder

This folder contains beginner-friendly Pandas practice files focused on DataFrame basics, selecting data, filtering rows, saving output, and handling missing data.

## What You Learn Here

- What rows, columns, and dtypes mean in a DataFrame
- How to inspect data with `shape`, `columns`, `dtypes`, and `info()`
- How to select single or multiple columns
- How to filter rows using boolean conditions
- How to combine multiple conditions
- How to save Pandas output to files
- How to think about missing data in a dataset

## Prerequisites

- Python 3.x installed
- Pandas installed

Install Pandas:

```bash
pip install pandas
```

## Files in This Folder

- `about.txt`: Notes about Pandas basics and data analysis concepts
- `problem.txt`: Practice notes about columns, rows, dtypes, and missing data
- `data.txt`: Data-related notes and examples
- `app.py`: Main practice script for DataFrame operations
- `topic.py`: Example showing DataFrame creation, shape, and columns
- `describe.py`: Practice with `describe()` and summary statistics
- `rows.py`: Row selection and filtering practice
- `adding.py`: Example for adding data or columns
- `removColum.py`: Example for removing a column from a DataFrame
- `selColumExample.py`: Example for selecting columns
- `save.py`: Saving DataFrame output to files
- `problemexmple.py`: Problem-based example script
- `Handling missing Data/`: Notes and practice files for missing-value handling
  - `missing.txt`: Notes about handling missing data
  - `missing.py`: Practice script for missing-data techniques

## Generated Output Files

These files are created by the save/export examples in this folder:

- `../output.csv`: CSV export output
- `../output.json`: JSON export output
- `../output.xlsx`: Excel export output

## Quick Example

```python
import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Hari"],
    "Age": [28, 34, 22],
    "Salary": [50000, 60000, 45000]
}

df = pd.DataFrame(data)

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
```

## Common Learning Notes

- Text columns are usually `object` dtype by default.
- Numeric columns are commonly `int64` or `float64`.
- Use square brackets for selecting columns.
- Use boolean indexing for filtering rows.

## How to Run

From this Pandas folder:

```bash
python topic.py
python app.py
python describe.py
python rows.py
python save.py
python removColum.py
python selColumExample.py
```

## Goal of This Folder

Build a strong foundation in Pandas so you can inspect, clean, filter, and export datasets with confidence.
