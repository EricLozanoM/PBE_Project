import tkinter as tk
from tkinter import scrolledtext
from rpi_lcd import LCD  
import sys

class LCDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LCD Display Control")
        
        self.text_input = scrolledtext.ScrolledText(root, width=20, height=4, wrap=tk.WORD, bg='blue', fg='white', insertbackground='white')
        self.text_input.grid(column=0, row=0, padx=10, pady=10)

        self.display_button = tk.Button(root, text="Display", command=self.display_text)
        self.display_button.grid(column=0, row=1, padx=10, pady=10)

        self.lcd = LCD()
    
    def validate_input(self, event):
        current_text = self.text_input.get("1.0", tk.END).strip()

        if len(current_text) > 80:
            self.text_input.delete("1.0", tk.END)  
            self.text_input.insert("1.0", current_text[:80])  


    def display_text(self):
        user_input = self.text_input.get("1.0", tk.END).strip() 

        self.lcd.clear()
        
        input_lines = user_input.split('\n')
        for i in range(min(len(input_lines), 4)):
            line_text = input_lines[i]
            self.lcd.text(line_text, i + 1)

if __name__ == "__main__":
    root = tk.Tk()
    app = LCDApp(root)
    root.mainloop()
