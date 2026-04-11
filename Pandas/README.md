# Pandas Learning Folder

This folder contains beginner to intermediate Pandas practice files covering DataFrame basics, data selection, filtering, handling missing data, grouping & aggregation, and data export.

## What You Learn Here

- What rows, columns, and dtypes mean in a DataFrame
- How to inspect data with `shape`, `columns`, `dtypes`, and `info()`
- How to select single or multiple columns
- How to filter rows using boolean conditions
- How to combine multiple conditions
- How to save Pandas output to files
- How to think about missing data in a dataset
- **Handling missing data**: filling with mean, forward/backward fill, interpolation
- **GroupBy and aggregation**: grouping data and calculating statistics
- **Sorting and organizing data**: organizing by column values

## Prerequisites

- Python 3.x installed
- Pandas installed

Install Pandas:

```bash
pip install pandas
```

## Files in This Folder

### Core DataFrame Operations
- `about.txt`: Notes about Pandas basics and data analysis concepts
- `problem.txt`: Practice notes about columns, rows, dtypes, and missing data
- `data.txt`: Data-related notes and examples
- `topic.py`: Example showing DataFrame creation, shape, and columns
- `describe.py`: Practice with `describe()` and summary statistics
- `rows.py`: Row selection and filtering practice
- `adding.py`: Example for adding data or columns
- `removColum.py`: Example for removing a column from a DataFrame
- `selColumExample.py`: Example for selecting columns
- `save.py`: Saving DataFrame output to files
- `app.py`: Main practice script for DataFrame operations
- `problemexmple.py`: Problem-based example script

### Handling Missing Data (`Handling missing Data/`)
Advanced techniques for dealing with missing values (NaN, None):
- `missing.txt`: Notes and strategies for handling missing data
- `missing.py`: Forward/Backward fill techniques
- `handle2.py`: **Filling missing values with column mean** - replacing NaN with average values
- `inte.py`: **Interpolation methods** - linear, polynomial, nearest neighbor interpolation

**Key Concepts:**
- `fillna()` - Fill missing values with specific values or methods
- `interpolate()` - Estimate missing values based on surrounding data
- `select_dtypes()` - Select numeric columns only
- Different interpolation methods: `linear`, `polynomial`, `nearest`

### Sorting & Aggregation (`Sorting & Aggregation/`)
Grouping data and performing aggregate calculations:
- `groupby.py`: **GroupBy operations** - grouping data by columns and aggregating (`sum()`, `mean()`, `count()`, etc.)
- `sorting.py`: Sorting operations (ascending/descending)
- `sumarrySort.py`: Summary statistics and sorting combinations

**Key Concepts:**
- `groupby()` - Group rows by column values
- `.sum()`, `.mean()`, `.max()`, `.min()`, `.count()` - Aggregate functions
- `.agg()` - Apply multiple aggregations at once
- `sort_values()` - Sort by columns

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
# Core DataFrame Operations
python topic.py
python app.py
python describe.py
python rows.py
python save.py
python removColum.py
python selColumExample.py

# Handling Missing Data
python Handling\ missing\ Data\handle2.py    # Fill with mean
python Handling\ missing\ Data\inte.py       # Interpolation

# Sorting & Aggregation
python Sorting\ \&\ Aggregation\groupby.py   # GroupBy operations
python Sorting\ \&\ Aggregation\sorting.py   # Sorting examples
```

## Goal of This Folder

Build a strong foundation in Pandas data analysis so you can:
- Inspect and explore datasets with confidence
- Clean data and handle missing values effectively
- Group and aggregate data to extract insights
- Filter, transform, and export datasets for further analysis
