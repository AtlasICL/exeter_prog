FILE_PATH = "C://eaca/exe/exeter_prog/week2/words.txt"
VOWELS = ['a', 'e', 'i', 'o', 'u']


def getWords(filePath: str) -> list[str]:
    wordList = []
    with open(filePath, 'r') as file:
        for line in file:
            wordList.append(line.strip().lower())
    return wordList


def askLetters() -> str:
    tmp = []
    for i in range(9):
        tmp.append(input(f"letter {i+1} --> "))
    tmp = sorted(tmp)
    letters = "".join(tmp)
    return letters


def isSubstring(substringCandidate: str, mainString: str) -> bool:
    counts = [0]*26
    for char in mainString:
        counts[ord(char) - ord('a')] += 1
    for char in substringCandidate:
        index = ord(char) - ord('a')
        counts[index] -= 1
        if counts[index] < 0:
            return False
    return True


def displayResults(validWords: list[str]) -> None:
    print(f"There were {len(validWords)} words found with the letters provided.")
    bestAnswers = sorted(validWords, key=len, reverse=True)
    bestWords = []
    try:
        i = 0
        while i < 5:
            bestWords.append(bestAnswers[i])
            i += 1
        print(f"Here are the best answers: {bestWords}")
    except IndexError:
        pass


def main():
    letters = askLetters()
    wordList = getWords(FILE_PATH)
    validWords = [word for word in wordList if isSubstring(word, letters)]
    displayResults(validWords)
    

if __name__ == "__main__":
    main()
