# Требуется реализовать функцию longest_words(file),
# которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

def longest_words(file):
    with open(file, "r", encoding='utf-8') as data:
        file_words = data.read().split()
        max_word = len(max(file_words, key=len))
        for word in file_words:
            if len(word) == max_word:
                print(word)

longest_words("article.txt")

