import pandas

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
alphabets_data = pandas.read_csv('nato_phonetic_alphabet.csv')
print(alphabets_data)
phonetic_dict = {row.letter:row.code for (index, row) in alphabets_data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input('Enter the word: ').upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print('Sorry, please enter only letters in alphabets.')
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()



