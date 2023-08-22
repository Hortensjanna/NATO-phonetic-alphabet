
import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

users_word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in users_word]
print(output_list)
