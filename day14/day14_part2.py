import sys

with open(sys.argv[1], 'r') as fid:
    lines = [line.strip() for line in fid.readlines()]

rows = lines

# forgot to change my calculate_load function to not also assume shift for a while
def calculate_load(columns):
    total_load = 0
    for column in columns:
        for i, token in enumerate(column):
              if token == 'O':
                total_load += len(column) - i
    
    return total_load

def shift(columns):
    new_columns = []
    for column in columns:
        new_column = []
        start = 0
        for i, token in enumerate(column):
            if token == '#':
                new_column.append(token)
                start = i + 1
            elif token == 'O':
                new_column.insert(start, 'O')
            else:
                new_column.append(token)
        new_columns.append(''.join(new_column))

    return new_columns

def cycle(columns):
    columns = shift([''.join(line[i] for line in columns) for i in range(len(columns[0]))])
    columns = shift([''.join(line[i] for line in columns) for i in range(len(columns[0]))])
    columns = shift([''.join(reversed(column)) for column in shift([''.join(line[i] for line in columns) for i in reversed(range(len(columns[0])))])])
    columns = [str(''.join(reversed(column))) for column in shift([''.join(line[i] for line in columns) for i in reversed(range(len(columns[0])))])]
    return columns

seen_rows = {}
diff = 0
end = 0
found_end = False
for i in range(1000000000):
    rows = cycle(rows)

    if found_end and i % diff == end:
        break
        
    if not found_end and ''.join(rows) in seen_rows:
        diff = i - seen_rows[''.join(rows)]
        start = i % diff
        end = (1000000000 - 1) % diff
        found_end = True
        

    seen_rows[''.join(rows)] = i

print(calculate_load([''.join(line[i] for line in rows) for i in range(len(rows[0]))]))
