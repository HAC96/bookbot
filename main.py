from stats import word_count, sorted_char_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    num_words = word_count(filepath)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_char_count(filepath):
        char, num = dict["char"], dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()
