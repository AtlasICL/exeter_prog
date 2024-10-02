FILE_PATH = "C://eaca/prog/week2/words.txt"
VOWELS = ['a', 'e', 'i', 'o', 'u']


def getWords(filePath: str) -> list[str]:
    wordList = []
    with open(filePath, 'r') as file:
        for line in file:
            if len(line) > 10: # TODO: why 10 and not 9?
                continue
            wordList.append(line.strip().lower())
    return wordList


def askVowelsAndConsonants() -> tuple[int, int]:
    vowelCount: int = 0
    for i in range(9):
        cin = input(f"char {i+1} (v)owel or (c)onsonant? --> ")
        if cin == 'v':
            vowelCount += 1
    return (vowelCount, 9-vowelCount)


def vowelCount(word: str) -> int:
    vowelCount = 0
    for letter in word:
        if letter in VOWELS:
            vowelCount += 1
    return vowelCount


def consonantCount(word: str) -> int:
    consonantCount = 0
    for letter in word:
        if letter not in VOWELS:
            consonantCount += 1
    return consonantCount


def wordIsValid(word: str, desiredVowelsAndConsonants: tuple[int, int]) -> bool:
    if vowelCount(word) > desiredVowelsAndConsonants[0]:
        return False
    if consonantCount(word) > desiredVowelsAndConsonants[1]:
        return False
    return True


def findValidWords(wordList: list[str], desiredVowelsAndConsonants: tuple[int, int]) -> list[str]:
    validWords = []
    for word in wordList:
        if wordIsValid(word, desiredVowelsAndConsonants):
            validWords.append(word)
    return validWords


def main():
    desiredVowelsAndConsonants = askVowelsAndConsonants()
    wordList = getWords(FILE_PATH)
    validWords = findValidWords(wordList, desiredVowelsAndConsonants)
    print(validWords)
    return
    

if __name__ == "__main__":
    main()
