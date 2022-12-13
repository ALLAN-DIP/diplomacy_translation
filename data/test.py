with open('data/annotated_daide.txt', 'r') as f:
    count = 0
    data = f.read()
    entries = data.split('\n\n')
    for entry in entries:
        lines = entry.split('\n')
        last_line = lines[-1]
        if last_line.startswith('daide'):
            count += 1
    print(len(entries))
    print(count)