import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont
import random

class EmojiDisplay(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Colorful Emojis")
        self.geometry("400x300")
        
        # Create frame to hold emojis
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(expand=True, padx=20, pady=20)
        
        # Define emojis - using more colorful default emojis
        self.emojis = ["🌈", "🎨", "🌺", "🦚"]
        
        # Create labels for each emoji
        for i in range(2):
            for j in range(2):
                idx = i * 2 + j
                label = ctk.CTkLabel(
                    self.frame,
                    text=self.emojis[idx],
                    font=("Segoe UI Emoji", 48),
                    width=100,
                    height=100,
                    fg_color="transparent",  # Remove background color
                    corner_radius=0  # Remove rounded corners
                )
                label.grid(row=i, column=j, padx=10, pady=10)

if __name__ == "__main__":
    app = EmojiDisplay()
    app.mainloop()