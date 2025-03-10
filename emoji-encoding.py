import random
import customtkinter as ctk
import tkinter as tk
import emoji

# Get a list of available single-character emojis
all_emojis = list(emoji.EMOJI_DATA.keys())

# Filter emojis to exclude variations and ensure they display well
filtered_emojis = [e for e in all_emojis if len(e) == 1 and e.isprintable()]

# Set random seed to keep mapping consistent across runs
random.seed(42)

# Dictionary to store dynamically assigned mappings
char_to_emoji = {}
emoji_to_char = {}

def get_or_assign_emoji(char):
    """Assigns an emoji to a character if it hasn't been assigned yet."""
    if char not in char_to_emoji:
        if not filtered_emojis:
            raise ValueError("Ran out of unique emojis!")
        chosen_emoji = filtered_emojis.pop(random.randint(0, len(filtered_emojis) - 1))
        char_to_emoji[char] = chosen_emoji
        emoji_to_char[chosen_emoji] = char
    return char_to_emoji[char]

def encode_text(text):
    """Encodes text by replacing each character with an assigned emoji."""
    return ''.join(get_or_assign_emoji(char) for char in text)

def decode_text(text):
    """Decodes text back to its original form using the stored mapping."""
    return ''.join(emoji_to_char.get(char, char) for char in text)

def on_encode():
    input_text = text_entry.get("1.0", tk.END).strip()
    encoded_text = encode_text(input_text)
    text_entry.delete("1.0", tk.END)
    text_entry.insert(tk.END, encoded_text)

def on_decode():
    input_text = text_entry.get("1.0", tk.END).strip()
    decoded_text = decode_text(input_text)
    text_entry.delete("1.0", tk.END)
    text_entry.insert(tk.END, decoded_text)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(text_entry.get("1.0", tk.END).strip())

# Initialize the main window
root = ctk.CTk()
root.title("Emoji Encoder/Decoder")

# Text entry box
text_entry = ctk.CTkTextbox(root, width=400, height=200, font=("Segoe UI Emoji", 12))
text_entry.pack(pady=20)

# Encode button
encode_button = ctk.CTkButton(root, text="Encode", command=on_encode)
encode_button.pack(pady=10)

# Decode button
decode_button = ctk.CTkButton(root, text="Decode", command=on_decode)
decode_button.pack(pady=10)

# Copy button
copy_button = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()