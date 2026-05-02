import sys

def parse_cipher_csv(payload):
    values = []
    token = ""
    
    for c in payload:
        if '0' <= c <= '9':
            token += c
        elif token:
            values.append(int(token))
            token = ""
    
    if token:
        values.append(int(token))
    
    return values

def decrypt_with_key(cipher, key):
    out = []
    for i in range(len(cipher)):
        decrypted_char = cipher[i] ^ ord(key[i % len(key)])
        out.append(chr(decrypted_char))
    return ''.join(out)

def text_score(text):
    score = 0
    
    for c in text:
        uc = ord(c)
        if uc < 9 or uc > 126:
            return -1000000
        if c == ' ':
            score += 3
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            score += 2
    
    def count_occurrences(needle):
        cnt = 0
        pos = 0
        while True:
            pos = text.find(needle, pos)
            if pos == -1:
                break
            cnt += 1
            pos += len(needle)
        return cnt
    
    score += 40 * count_occurrences(" the ")
    score += 25 * count_occurrences(" and ")
    score += 20 * count_occurrences(" of ")
    score += 20 * count_occurrences(" to ")
    
    return score

def ascii_sum(text):
    total = 0
    for c in text:
        total += ord(c)
    return total

def solve(file_path):
    try:
        with open(file_path, 'r') as input_file:
            cipher_data = input_file.read()
    except Exception:
        raise RuntimeError(f"Could not open cipher file: {file_path}")
    
    cipher = parse_cipher_csv(cipher_data)
    
    best_score = float('-inf')
    best_text = ""
    
    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                key = chr(a) + chr(b) + chr(c)
                text = decrypt_with_key(cipher, key)
                score = text_score(text)
                if score > best_score:
                    best_score = score
                    best_text = text
    
    return ascii_sum(best_text)

def run_checkpoints():
    key = "abc"
    plain = "hello world"
    cipher = []
    
    for i in range(len(plain)):
        cipher.append(ord(plain[i]) ^ ord(key[i % len(key)]))
    
    if decrypt_with_key(cipher, key) != plain:
        return False
    
    return True

def main():
    file_path = "resources/documents/0059_cipher.txt"
    run_checkpoints_flag = True
    
    # Parse command line arguments
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--file="):
            file_path = arg[7:]
    
    if run_checkpoints_flag and not run_checkpoints():
        sys.exit(2)
    
    try:
        result = solve(file_path)
        print(result)
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
        sys.exit(3)

if __name__ == "__main__":
    main()
