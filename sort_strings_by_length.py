def sort_strings_by_length(input): 
    return sorted(input, key=len)

strings = ["a", "ab", "abc", "abcd", "abcde", "abcdef"]
sorted_strings = sort_strings_by_length(strings)
print(sorted_strings)