from diclogic import add_word, view_all_words, view_all_counts, view_words_with_count
def pres():
    exit = False
    while not exit:
        print("\nMenu:")
        print('0. Exit')
        print("1. Add a word")
        print("2. View all words")
        print("3. View all words and their count")
        print("4. View words with a specific count")
        
        choice = int(input("Enter your choice: "))

        if choice == 1:
            word = input("Enter a word: ")
            v= add_word(word)
            print(v)
            print("Word added successfully!")

            
        elif choice == 2:
            word_counts = view_all_words(word)
            print("Words are:", word_counts)

        elif choice == 3:
            count= view_all_counts(word)
            print(count)
        
        elif choice == 4:
                count = int(input("Enter the count to filter by: "))
                v =view_words_with_count(count)
                print(v)
       
        elif choice == 0:
            exit = True

        
