def check_for_word_match(sentence, word):
    words = sentence.split()
    for i, w in enumerate(words):
        if word in w:
            return i
    return "no match"


sentence = input("Enter a sentence: ")
word = input("Enter a word: ")

result = check_for_word_match(sentence, word)
print(f"Matching index: {result}")
