import sys


def main():
    temp = []
    occurs = []
    done = []
    with open("dictionary.txt", "r") as file:
        reader = file.read()
        poss = str(reader).split("\n")
        word = sys.argv[1].lower()
        print(f"First Word: {word}")

        while True:
            res = input("Result: ").lower()
            if res == 'ggggg':
                print(f"Congrats! {word} was correct!")
                break

            else:
                for i,j in enumerate(res):
                    if j == 'g':
                        done.append(i)
                        for k in poss:
                            if word[i] == k[i]:
                                temp.append(k)
                        poss = list(temp)
                        temp.clear()

                    if j == 'b':
                        for k in poss:
                            if word[i] not in k:
                                temp.append(k)
                        poss = list(temp)
                        temp.clear()

                    if j == 'y':
                        for k in poss:
                            for l, m in enumerate(k):
                                if word[i] == m and l not in done and word[i] != k[i]:
                                    temp.append(k)
                        poss = list(temp)
                        temp.clear()


        print(poss)





main()


