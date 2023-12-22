import re

def word_frequency(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower())
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Test case
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
