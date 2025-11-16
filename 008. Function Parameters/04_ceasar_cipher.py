alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]

def caesar(original_text, shift_amount, encode_or_decode):
    """
    Encrypts or decrypts text using the Caesar cipher.
    
    Parameters:
    - original_text: string to encode or decode
    - shift_amount: number of letters to shift
    - encode_or_decode: "encode" or "decode"
    """
    output_text = ""
    
    # Reverse shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    # Normalize shift to avoid large numbers
    shift_amount %= len(alphabet)

    for letter in original_text:
        if letter not in alphabet:
            # Keep non-alphabet characters unchanged
            output_text += letter
            continue
        
        shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
        output_text += alphabet[shifted_position]
    
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Main program loop
running = True

while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid option! Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message: ").lower()
    
    # Ensure the user enters a valid number
    try:
        shift = int(input("Type the shift number: "))
    except ValueError:
        print("Please enter a valid number for the shift.")
        continue

    caesar(text, shift, direction)

    again = input("Type 'yes' if you want to go again. Otherwise, type 'no' to quit: ").lower()
    if again == "no":
        running = False
        print("Thank you!")
