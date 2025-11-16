alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    for letter in original_text:

        if encode_or_decode == "decode":
            shift_amount *= -1

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        # Using modulo to wrap around.
        # If shifted_position < len(alphabet), it stays the same.
        # If it's >= len(alphabet), this brings it back into the 0–25 range.

        output_text += alphabet[shifted_position]
        
    print(f"Here is the encoded result {output_text}")

caesar(text, shift, direction)