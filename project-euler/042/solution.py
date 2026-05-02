import sys
import os

def parse_string_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return False, ""
    tail = arg[len(prefix):]
    if not tail:
        return False, ""
    return True, tail

def parse_arguments(args):
    options = {
        "words_file": "resources/documents/0042_words.txt",
        "run_checkpoints": True
    }
    
    i = 1
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            options["run_checkpoints"] = False
            i += 1
            continue
        
        found, value = parse_string_after_prefix(arg, "--words-file=")
        if found:
            options["words_file"] = value
            i += 1
            continue
        
        print(f"Unknown argument: {arg}", file=sys.stderr)
        return None, False
    
    return options, True

def parse_csv_words(payload):
    words = []
    current = ""
    inside_quotes = False
    
    for c in payload:
        if c == '"':
            inside_quotes = not inside_quotes
            if not inside_quotes:
                words.append(current)
                current = ""
            continue
        
        if inside_quotes:
            current += c
    
    return words

def word_value(word):
    value = 0
    for c in word:
        if 'A' <= c <= 'Z':
            value += ord(c) - ord('A') + 1
    return value

def triangle_set_up_to(limit):
    triangles = set()
    n = 1
    while True:
        t = n * (n + 1) // 2
        if t > limit:
            break
        triangles.add(t)
        n += 1
    return triangles

def solve(words_file):
    try:
        with open(words_file, 'r') as f:
            content = f.read()
    except Exception as e:
        raise RuntimeError(f"Could not open words file: {words_file}")
    
    words = parse_csv_words(content)
    
    max_word_value = 0
    for w in words:
        current_value = word_value(w)
        if current_value > max_word_value:
            max_word_value = current_value
    
    triangles = triangle_set_up_to(max_word_value)
    
    count = 0
    for w in words:
        if word_value(w) in triangles:
            count += 1
    
    return count

def run_checkpoints():
    if word_value("SKY") != 55:
        print("Checkpoint failed for SKY value", file=sys.stderr)
        return False
    
    triangles = triangle_set_up_to(100)
    if 55 not in triangles or 54 in triangles:
        print("Checkpoint failed for triangle-number set", file=sys.stderr)
        return False
    
    return True

def main():
    args = sys.argv
    options, success = parse_arguments(args)
    
    if not success:
        sys.exit(1)
    
    if options["run_checkpoints"] and not run_checkpoints():
        sys.exit(2)
    
    try:
        result = solve(options["words_file"])
        print(result)
    except Exception as ex:
        print(str(ex), file=sys.stderr)
        sys.exit(3)

if __name__ == "__main__":
    main()
