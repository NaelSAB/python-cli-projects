import pandas

nato_phonetic_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter: row.code for index, row in nato_phonetic_alphabet_data.iterrows()}

enter_word = input("enter the word to change it to NATO: ").upper()
list_nato = [dict_nato[letter] for letter in enter_word]
print(list_nato)
