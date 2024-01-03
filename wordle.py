import sys


def main():
    temp = []
    done = []
    counter = 1
    if len(sys.argv[1]) == 5:
        dictionary = "dictionary.txt"
    else:
        dictionary = "bigdictionary.txt"
    with open(dictionary, "r") as file:
        reader = file.read()
        poss = str(reader).split("\n")
        word = sys.argv[1].lower()
        print(f"First Word: {word}")
        for i in poss:
            if len(i) == len(word):
                temp.append(i)
        poss = list(temp)
        temp.clear()

        while True:
            res = input("Result: ").lower()
            if res == 'g' * len(word):
                print(f"Congrats! {word} was correct in {counter} guesses!")
                break

            else:
                for i,j in enumerate(res):
                    if j == 'g':
                        done.append(i)
                        for k in poss:
                            if word[i] == k[i]:
                                temp.append(k)

                    if j == 'b':
                        occurs = word.count(word[i])
                        for k in poss:
                            if k.count(word[i]) < occurs:
                                temp.append(k)

                    if j == 'y':
                        for k in poss:
                            for l, m in enumerate(k):
                                if word[i] == m and l not in done and m != k[i]:
                                    temp.append(k)

                    poss = list(temp)
                    temp.clear()
                    if len(poss) == 0:
                        print("Error: No match found")
                        return

                word = poss[0]
                print(f"Next Word: {word}")
                counter += 1









main()


