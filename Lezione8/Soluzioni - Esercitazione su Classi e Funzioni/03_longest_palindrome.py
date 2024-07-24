
def count_char(s: str):
    counter_dict = dict()
    for c in s:
        if c not in counter_dict:
            counter_dict[c] = 1
        else:
            counter_dict[c] += 1

    return counter_dict


def longest_palindrome(s: str) -> int:
    counter_dict = count_char(s)
    length = 0
    odd = False
    for val in counter_dict.values():
        if val % 2 == 0:
            length += val
        else:
            length += val - 1
            odd = True

    if odd:
        length += 1

    return length


print(longest_palindrome("abccccdd"))
print(longest_palindrome("a"))
print(longest_palindrome("Aa"))
print(longest_palindrome("abccccba")) 
print(longest_palindrome("abcabcabc"))