import sys

# Define the braille patterns for letters, numbers, and special symbols
braille_alphabet = {
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO",
    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",
    "cap": ".....O", "num": ".O.OOO", "space": "......"
}

# Function to translate Braille to English
def braille_to_english(braille):
    english = ""
    i = 0
    cap_next = False
    num_mode = False
    
    while i < len(braille):
        char_braille = braille[i:i+6]
        if char_braille == braille_alphabet["cap"]:
            cap_next = True
        elif char_braille == braille_alphabet["num"]:
            num_mode = True
        elif char_braille == braille_alphabet["space"]:
            english += " "
            num_mode = False
        else:
            for letter, pattern in braille_alphabet.items():
                if pattern == char_braille:
                    if cap_next:
                        english += letter.upper()
                        cap_next = False
                    else:
                        english += letter
                    break
        i += 6

    return english

# Function to translate English to Braille
def english_to_braille(english):
    braille = ""
    for char in english:
        if char.isupper():
            braille += braille_alphabet["cap"]
            char = char.lower()
        if char.isdigit():
            braille += braille_alphabet["num"]
            braille += braille_alphabet[char]
        elif char == " ":
            braille += braille_alphabet["space"]
        else:
            braille += braille_alphabet[char]
    return braille

# Main function to determine input type and translate accordingly
def main():
    input_str = " ".join(sys.argv[1:])
    
    # Determine if input is Braille or English
    if all(c in ".O" for c in input_str.replace(" ", "")) and len(input_str.replace(" ", "")) % 6 == 0:
        output_str = braille_to_english(input_str.replace(" ", ""))
    else:
        output_str = english_to_braille(input_str)
    
    print(output_str.replace(" ", ""))

if __name__ == "__main__":
    main()
