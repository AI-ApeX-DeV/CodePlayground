def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            return i
    return -1

# Test the function with an example
text = "Hello, world!"
pattern = "world"
result = naive_string_match(text, pattern)
if result == -1:
    print("Pattern not found in the text.")
else:
    print("Pattern found at index", result)
