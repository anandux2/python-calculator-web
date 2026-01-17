import tkinter as tk
from tkinter import messagebox

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Premium Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
       
        display_frame = tk.Frame(self.root, width=400, height=100, bd=0, highlightbackground="#333", highlightthickness=1, bg="#1e1e1e")
        display_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        input_field = tk.Entry(display_frame, font=('Outfit', 36, 'bold'), textvariable=self.input_text, width=50, bg="#1e1e1e", fg="#ffffff", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0, sticky="nsew", padx=20, pady=40)
        display_frame.grid_rowconfigure(0, weight=1)
        display_frame.grid_columnconfigure(0, weight=1)

       
        btns_frame = tk.Frame(self.root, width=400, height=500, bg="#1e1e1e")
        btns_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '%', '0', '.', '='
        ]

        row = 0
        col = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            
            if button == "=":
                bg_color = "#4CAF50" 
                fg_color = "white"
            elif button in ['C', '(', ')', '/', '*', '-', '+', '%']:
                bg_color = "#333333"
                fg_color = "#4CAF50"
            else:
                bg_color = "#252525"
                fg_color = "white"

            btn = tk.Button(btns_frame, text=button, font=('Outfit', 18), fg=fg_color, width=10, height=3, bd=0, bg=bg_color, cursor="hand2",
                            activebackground="#444444", activeforeground="white", command=action)
            btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(5):
            btns_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            btns_frame.grid_columnconfigure(i, weight=1)

    def on_button_click(self, item):
        if item == "C":
            self.expression = ""
            self.input_text.set("")
        elif item == "=":
            try:
                # Replace special characters for eval
                expr_to_eval = self.expression.replace('%', '/100')
                result = str(eval(expr_to_eval))
                self.input_text.set(result)
                self.expression = result
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.input_text.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.input_text.set("")
        else:
            self.expression += str(item)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()
