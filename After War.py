def remover(sentence):
    return ''.join(char for char in sentence if char.isalpha() or char == ' ')
def find_similar_words(n, sentence, word):
    sentence = remover(sentence)
    words = sentence.split()
    similar_words = []
    for w in words:
        w = remover(w)
        similarity = calculate_similarity(word, w)
        if similarity <= n:
            similar_words.append(w)
    return similar_words
def calculate_similarity(word1, word2):
    len1 = len(word1)
    len2 = len(word2)
    if len1 < len2:
        word1 += "_" * (len2 - len1)
    elif len2 < len1:
        word2 += "_" * (len1 - len2)
    similarity = sum(c1 != c2 for c1, c2 in zip(word1, word2))
    return similarity
n = int(input())
sentence = input()
word = input()
result = find_similar_words(n, sentence, word)
for res in result:
    print(res)
