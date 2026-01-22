def star_pattern():
    user_input = input("Enter one alphabate: ").strip()
    print("user_input", user_input)
    
    if len(user_input) != 1 or not user_input.isalpha():
        print("invalid input")
        return
    
    char = user_input
    row = ord(char.lower()) - ord('a') + 1
    print("row: ", row)
    
    for i in range(1, row + 1):
        print(char * i)
    
    # reverse
    for i in range(row, 0, -1):
        print(char * i)
    
    
star_pattern()