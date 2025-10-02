def get_book_text(path):
    with open(path) as f:
        return f.read()

def book_words(text):
    word_count = len(text.split())
    return word_count

def count_characters(text):  
    lowercase_text = text.lower()
    char_count = {}
    for char in lowercase_text:
        if char.isalpha():
            if char in char_count:  
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def get_count_value(item):
    return item[1]

def sort_character_counts(char_count):
    sorted_chars = sorted(char_count.items(), key=get_count_value, reverse=True)
    return sorted_chars

def print_report(book_path):
    text = get_book_text(book_path)
    
    word_count = book_words(text)
    char_count = count_characters(text)
    sorted_chars = sort_character_counts(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    
    print("============= END ===============")