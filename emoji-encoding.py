import random
import customtkinter as ctk
import tkinter as tk
import emoji

# Get a list of available single-character emojis
all_emojis = list(emoji.EMOJI_DATA.keys())

# Filter emojis to exclude variations and ensure they display well
filtered_emojis = [e for e in all_emojis if len(e) == 1 and e.isprintable()]

# Use a consistent random seed
random.seed(42)
random.shuffle(filtered_emojis)  # Ensures emojis are assigned in the same order each run

# Create a fixed mapping for standard ASCII characters
all_chars = [chr(i) for i in range(32, 127)]  # Printable ASCII characters
char_to_emoji = {char: filtered_emojis[i] for i, char in enumerate(all_chars) if i < len(filtered_emojis)}
emoji_to_char = {v: k for k, v in char_to_emoji.items()}

def encode_text(text):
    """Encodes text by replacing each character with an assigned emoji."""
    return ''.join(char_to_emoji.get(char, char) for char in text)

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
