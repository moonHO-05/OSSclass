def get_all_substrings(string):
    length = len(string)
    return [string[i:j] for i in range(length) for j in range(i + 1, length + 1)]

sample = "abc"
print(get_all_substrings(sample))
