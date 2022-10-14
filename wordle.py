import random

if __name__ == "__main__":
    # User input
    user_input = input()

    # define answer
    word_file = open("words.txt","r")
    dictionary_w = word_file.read().splitlines()
    word_file.close()

    # print(dictionary_w)
    answer = random.sample(dictionary_w,1)[0]
    print(answer)

    # compare user_input and answer
    for i in range (len(user_input)):
        if user_input[i] == answer[i]:
            print("A")
        elif user_input[i] in answer:
            print("B")
        else:
            print("X")