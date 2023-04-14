# python3

B = 341
Q = 1000211

def get_hash(pattern: str) -> int: #paņemu šo funkciju no prezentācijas, gunkcija atdeva element hash numuru, lai mēs talāk ar to darbotos.
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result

def read_input():
    text = input()
    if "I" in text:
        pattern = input()
        text = input()
    elif "F" in text:
        with open ("tests/06") as f:
            pattern = f.readline()
            text = f.readline()

    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    global B, Q
    # ir nepieciešams lai pec tām iet caur textu un salidzināt pettrnu un textu.
    pattern_len = len(pattern)
    text_len = len(text)

    multiplier = 1     
    #lai katram elementam būtu savs atšķirīgs hash numurs
    for i in range(1, pattern_len):
        multiplier = (B * multiplier) % Q
    
    pattern_hash = get_hash(pattern)
    text_hash = get_hash(text[:pattern_len])

    #salidiznu hashus un simvolus textaa un patternaa ar ciklu, ja sakrit tad ievietoju rezultējošā masīvā occurences, kas glab sākum poziciju pattern textā.
    occurrences = []
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+ pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = (B*(text_hash - ord(text[i])*multiplier) + ord(text[i+ pattern_len])) % Q
            
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

