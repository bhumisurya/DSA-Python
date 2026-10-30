def non_repeating_ch(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in freq:
        if freq[ch] > 1:
            print(ch, end=" ")
    
print(non_repeating_ch("aabbgtyrhbvdhvhefgfvhvhsdbehfv"))
    