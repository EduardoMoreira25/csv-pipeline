import csv

def read_csv(filepath):
    with open(filepath, newline='') as f:
        return list(csv.DictReader(f))

def transform(rows):
    return [row for row in rows if row.get('amount')]

def write_csv(rows, filepath):
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
