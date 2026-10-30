def longest(sentence):
    words = sentence.split()

    if not words:
        return None
    return max(words, key=len)

print(longest("BHumika Devendra Suryawanshi"))