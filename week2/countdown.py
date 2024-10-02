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

def askLetters() -> str:
    tmp = []
    for i in range(9):
        tmp.append(input(f"letter {i+1} --> "))
    tmp = sorted(tmp)
    letters = "".join(tmp)
    print(letters)
    return letters

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


# for vowels and consonants version
def findValidWords(wordList: list[str], desiredVowelsAndConsonants: tuple[int, int]) -> list[str]:
    validWords = []
    for word in wordList:
        if wordIsValid(word, desiredVowelsAndConsonants):
            validWords.append(word)
    return validWords

# for letters version
def findFullyValidWords(wordList: list[str], letters: str) -> list[str]:
    validWords = []
    for word in wordList:
        if sorted(word) == letters:
            validWords.append(word)
    return validWords
    # TODO: NEED TO CHECK FOR WORDS WHICH ARE CONTAINED WITHIN LETTERS, NOT JUST 9 FOR 9 MATCHES


def main():
    # desiredVowelsAndConsonants = askVowelsAndConsonants()
    # wordList = getWords(FILE_PATH)
    # validWords = findValidWords(wordList, desiredVowelsAndConsonants)
    # print(validWords)

    letters = askLetters()

    return
    

if __name__ == "__main__":
    main()
