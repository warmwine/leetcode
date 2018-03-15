def length_of_longest_substring(text):
    size = len(text)
    char_dict = {}
    max_length = 0
    sub_start = 0
    if text:
        max_length = 1
        for i in range(0, size):
            char = text[i]
            if char in char_dict:
                if char_dict[char] >= sub_start:
                    length = i - sub_start
                    if length > max_length:
                        max_length = length
                    sub_start = char_dict[char]+1
            char_dict[char] = i
        length = size - sub_start
        if length > max_length:
            max_length = length
    return max_length


if __name__ == '__main__':
    print(length_of_longest_substring('abcabcbb'))
    print(length_of_longest_substring('bbbbbbb'))
    print(length_of_longest_substring('pwwkew'))
    print(length_of_longest_substring('aab'))
    print(length_of_longest_substring('ab'))
    print(length_of_longest_substring('dfdvdf'))
    print(length_of_longest_substring('tmmzuxt'))
    print(length_of_longest_substring('wobgrovw'))
