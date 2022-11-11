from collections import Counter

def trim(token):
    while token.startswith('('):
        token = token[1:]
    while token.endswith(')'):
        token = token[:-1]
    return token

def compute_accuracy(reference, translation):
    translated_tokens = translation.split(' ')
    reference_tokens = reference.split(' ')
    trimmed_translated_tokens = [trim(token) for token in translated_tokens]
    trimmed_reference_tokens = [trim(token) for token in reference_tokens]

    # precision = correct / output-length
    # recall = correct / reference-length
    # f = p * q * 2 / (p + q)
    correct = list((Counter(trimmed_reference_tokens) & Counter(trimmed_translated_tokens)).elements())
    precision = len(correct) / len(trimmed_translated_tokens)
    recall = len(correct) / len(trimmed_reference_tokens)
    f = precision * recall * 2 / (precision + recall)
    return f

def read_file():
    count = 1
    with open('data/generated_daide_clean.txt', 'r') as f:
        lines = f.read()
        entries = lines.split('\n\n')
    
    for entry in entries:
        english, reference, translation = entry.split('\n')
        print(count)
        count += 1
    return lines

if __name__ == '__main__':
    lines = read_file()
    