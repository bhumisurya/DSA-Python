def freq_word(sentence):
    words = sentence.lower().split()
    freq = {}

    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

print(freq_word("Bhumika PG Devendra AI Suryawanshi AI AI "))