text = input("Enter a string or number: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")