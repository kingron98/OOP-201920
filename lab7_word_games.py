# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 07-11-2019
# purpose: Lab 7 - Word Games

class WordGames:
    def __init__(self):
        self.mywords = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        print("User input was: "+self.mywords)


class WordDupli(WordGames):
    def word_play(self):
        print("User input was: " + self.mywords)
        print(self.mywords * 2)


class WordScramble(WordGames):
    def word_play(self):
        # print what was input
        print("The user input was: ", self.mywords)

        sentence = self.mywords.strip().split(" ")

        for i, word in enumerate(sentence):
            if len(word) > 3:
                temp_word = list(word)
                if ',' in temp_word:
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp

                else:
                    temp = temp_word[1]
                    temp_word[1] = temp_word[2]
                    temp_word[2] = temp

                temp_word = ''.join(temp_word)
                sentence[i] = temp_word

        sentence = ' '.join(sentence)
        print(sentence)


wg = WordDupli()