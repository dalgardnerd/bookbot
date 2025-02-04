def open_file(file_path):
    with open(file_path) as f:
        return f.read()

def count_characters(text):
    character_count = {}
    for character in text:
        if character.lower() not in character_count:
            character_count[character.lower()] = 1
        else:
            character_count[character.lower()] += 1
    return character_count

def print_book_report(path, word_count, character_count):
    #print(f'--- Begin report of {path} ---')
    #print(f'{word_count} words found in the document')
    #for key, value in character_count:
    #    print(f'The {key} character was found {value} times')
    #print('--- End report ---')
    print(character_count)

def main():
    path = "books/frankenstein.txt"
    text = open_file(path)
    word_count = len(text.split())
    character_count = count_characters(text)
    print_book_report(path, word_count, character_count)
main()


