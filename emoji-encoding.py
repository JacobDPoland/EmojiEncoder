import customtkinter as ctk
import tkinter as tk

# UTF-8 to Emoji mapping
utf8_to_emoji = {chr(i): chr(0x1F600 + i) for i in range(128)}
emoji_to_utf8 = {v: k for k, v in utf8_to_emoji.items()}

def encode_text(text):
    return ''.join(utf8_to_emoji.get(char, char) for char in text)

def decode_text(text):
    return ''.join(emoji_to_utf8.get(char, char) for char in text)

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
root.title("UTF-8 to Emoji Encoder/Decoder")

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