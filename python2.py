def count_character_frequency(input_string):
   
    frequency = {}
    for char in input_string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

# Example usage
input_string = input("Enter a string: ")
frequency = count_character_frequency(input_string)

print("\nCharacter frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")

