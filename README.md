# csv-pipeline

A lightweight Python pipeline that reads raw sales data, validates and transforms it, and writes clean output.

## What it does

1. Reads `data/input.csv`
2. Validates that the `amount` field is numeric
3. Strips whitespace from all fields
4. Writes clean rows to `data/output.csv`

## Usage
```bash
python pipeline.py
```
## Environment variables
| Variable | Description | Required |
|----------|-------------|----------|
| DB_HOST  | Database hostname | Yes |
| LOG_LEVEL | Logging verbosity | No (default: INFO) |

## Project structure
```
csv-pipeline/
├── pipeline.py      # main pipeline logic
├── data/
│   └── input.csv    # sample input data
└── README.md
```

## Requirements

Python 3.8+
