from collections import Counter
from typing import List

# remove parentheses
def trim(token: str) -> str:
    while token.startswith('('):
        token = token[1:]
    while token.endswith(')'):
        token = token[:-1]
    return token

def compute_accuracy(reference: str, translation: str) -> float:
    translated_tokens = translation.split(' ')
    reference_tokens = reference.split(' ')
    trimmed_translated_tokens = [trim(token) for token in translated_tokens]
    trimmed_reference_tokens = [trim(token) for token in reference_tokens]

    # precision = correct / output-length
    # recall = correct / reference-length
    # f = p * q * 2 / (p + q)
    correct = list((Counter(trimmed_reference_tokens) & Counter(trimmed_translated_tokens)).elements())
    overlap = len(correct)
    # return if denom is 0
    if overlap == 0:
        return 0
    precision = overlap / len(trimmed_translated_tokens)
    recall = overlap / len(trimmed_reference_tokens)
    f = precision * recall * 2 / (precision + recall)
    return round(f, 3)

def read_file() -> List[str]:
    with open('data/generated_daide_clean.txt', 'r') as f:
        lines = f.read()
        entries = lines.split('\n\n')
    
    for entry in entries:
        english, reference, translation = entry.split('\n')
        print(compute_accuracy(reference, translation))
    return lines

if __name__ == '__main__':
    lines = read_file()
    