def remove_duplicate_words():

    user_input = input("enter a sentance:").strip()
    
    if user_input.isdigit():
        print("invalid input; int not allowed")
        return
    
    words = user_input.split()
    seen = set()
    unique_words = []
    
    for word in words:
        if word not in seen:
            seen.add(word)
            unique_words.append(word)

    result = " ".join(unique_words)
    print("result :", result)
    
remove_duplicate_words()