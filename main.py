def main():
    with open('books/frankenstein.txt', 'r') as f:
        file_contents = f.read()
    count_word(file_contents)
    characters_dict = count_characters(file_contents)
    organized_dict = sort_dict(characters_dict)
    print(organized_dict)
    
def count_word(complete_textfile):
    splited_text = complete_textfile.split()
    counted_words = len(splited_text)

def count_characters(complete_textfiles):
    charactersDict = {}
    lowered_case = complete_textfiles.lower()
    for i in lowered_case:
        if i.isalpha():
            charactersDict[i] = charactersDict.get(i, 0) + 1
    return charactersDict

def sort_dict(characters_dict):
    new = dict(sorted(characters_dict.items()))
    for letter, count in new.items():
        print(f'The {letter} character was found {count} times')

main()