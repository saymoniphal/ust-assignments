# word_frequency.py
"""
Compute a frequency of words from input string.
Returns a sorted list of tuple (word, frequency)
"""
def count_words(st: str) -> dict[str, int]:
    word_counts = {}
    for word in st.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    l = [(k, v) for k, v in word_counts.items()]
    return sorted(l)

def print_words_freq(st: str) -> None:
    for wc in count_words(st):
        print(wc)