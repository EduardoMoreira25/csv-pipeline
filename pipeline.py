import csv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
logger = logging.getLogger(__name__)

def read_csv(filepath):
    logger.info(f"Reading input from {filepath}")
    with open(filepath, newline='') as f:
        return list(csv.DictReader(f))

def validate(rows):
    for row in rows:
        try:
            if row.get('amount')/1:
                print('Its a number!')
        except Exception as e:
            print(f"Not a number:\n{e}")

def transform(rows):
    logger.info(f"Transforming {len(rows)} rows")
    return [
        {k: v.strip() for k, v in row.items()}
        for row in rows
        if row.get('amount')
    ]

def write_csv(rows, filepath):
    logger.info(f"Writing {len(rows)} rows to {filepath}")
    if not rows:
        return
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    rows = read_csv('data/input.csv')
    cleaned = transform(rows)
    write_csv(cleaned, 'data/output.csv')