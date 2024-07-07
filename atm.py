import customtkinter as ctk
from tkinter import simpledialog,messagebox

class ATM:
    def __init__(self, balance=0, pin=0000):
        self.balance = balance
        self.pin = pin

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrawal successful. Current balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. Current balance: {self.balance}"

    def change_pin(self, new_pin):
        self.pin = new_pin
        return "PIN changed successfully."

class ATMApp:
    def __init__(self, root, atm):
        self.atm = atm
        self.root = root
        self.root.title("ATM Machine ")
        self.root.geometry("400x400")

        ctk.set_appearance_mode("dark")  
        ctk.set_default_color_theme("dark-blue") 
        
        self.main_frame = ctk.CTkFrame(master=root)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.pin_label = ctk.CTkLabel(master=self.main_frame, text="Enter PIN", font=("Arial", 24))
        self.pin_label.pack(pady=20)

        self.pin_entry = ctk.CTkEntry(master=self.main_frame, show="*", width=200, font=("Arial", 20))
        self.pin_entry.pack(pady=10)

        self.pin_button = ctk.CTkButton(master=self.main_frame, text="Enter", command=self.enter_pin)
        self.pin_button.pack(pady=10)

    def enter_pin(self):
        pin = self.pin_entry.get()
        if not pin.isdigit():
            messagebox.showerror("Error", "PIN should be numeric.")
            return
        if int(pin) != self.atm.pin:
            messagebox.showerror("Error", "Incorrect PIN. Please try again.")
        else:
            self.show_menu()

    def show_menu(self):
        self.clear_frame(self.main_frame)

        self.menu_label = ctk.CTkLabel(master=self.main_frame, text="Menu", font=("Arial", 24))
        self.menu_label.pack(pady=20)

        ctk.CTkButton(master=self.main_frame, text="Check Balance", command=self.check_balance).pack(pady=10)
        ctk.CTkButton(master=self.main_frame, text="Withdraw", command=self.withdraw).pack(pady=10)
        ctk.CTkButton(master=self.main_frame, text="Deposit", command=self.deposit).pack(pady=10)
        ctk.CTkButton(master=self.main_frame, text="Change PIN", command=self.change_pin).pack(pady=10)
        ctk.CTkButton(master=self.main_frame, text="Exit", command=self.root.quit).pack(pady=10)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def check_balance(self):
        self.clear_frame(self.main_frame)

        balance = self.atm.check_balance()
        balance_label = ctk.CTkLabel(master=self.main_frame, text=f"Current balance: {balance}", font=("Arial", 24))
        balance_label.pack(pady=20)

        back_button = ctk.CTkButton(master=self.main_frame, text="Back", command=self.show_menu)
        back_button.pack(pady=10)

    def withdraw(self):
        self.clear_frame(self.main_frame)

        amount_label = ctk.CTkLabel(master=self.main_frame, text="Enter the amount to withdraw:", font=("Arial", 18))
        amount_label.pack(pady=20)

        amount_entry = ctk.CTkEntry(master=self.main_frame, width=200, font=("Arial", 20))
        amount_entry.pack(pady=10)

        withdraw_button = ctk.CTkButton(master=self.main_frame, text="Withdraw", command=lambda: self.perform_withdraw(amount_entry))
        withdraw_button.pack(pady=10)

        back_button = ctk.CTkButton(master=self.main_frame, text="Back", command=self.show_menu)
        back_button.pack(pady=10)

    def perform_withdraw(self, amount_entry):
        amount = amount_entry.get()
        if amount.isdigit():
            amount = float(amount)
            result = self.atm.withdraw(amount)
            messagebox.showinfo("Withdraw", result)
        else:
            messagebox.showerror("Error", "Invalid amount.")
        self.show_menu()

    def deposit(self):
        self.clear_frame(self.main_frame)

        amount_label = ctk.CTkLabel(master=self.main_frame, text="Enter the amount to deposit:", font=("Arial", 18))
        amount_label.pack(pady=20)

        amount_entry = ctk.CTkEntry(master=self.main_frame, width=200, font=("Arial", 20))
        amount_entry.pack(pady=10)

        deposit_button = ctk.CTkButton(master=self.main_frame, text="Deposit", command=lambda: self.perform_deposit(amount_entry))
        deposit_button.pack(pady=10)

        back_button = ctk.CTkButton(master=self.main_frame, text="Back", command=self.show_menu)
        back_button.pack(pady=10)

    def perform_deposit(self, amount_entry):
        amount = amount_entry.get()
        if amount.isdigit():
            amount = float(amount)
            result = self.atm.deposit(amount)
            messagebox.showinfo("Deposit", result)
        else:
            messagebox.showerror("Error", "Invalid amount.")
        self.show_menu()

    def change_pin(self):
        self.clear_frame(self.main_frame)

        pin_label = ctk.CTkLabel(master=self.main_frame, text="Enter your new PIN:", font=("Arial", 18))
        pin_label.pack(pady=20)

        pin_entry = ctk.CTkEntry(master=self.main_frame, width=200, font=("Arial", 20))
        pin_entry.pack(pady=10)

        change_button = ctk.CTkButton(master=self.main_frame, text="Change PIN", command=lambda: self.perform_change_pin(pin_entry))
        change_button.pack(pady=10)

        back_button = ctk.CTkButton(master=self.main_frame, text="Back", command=self.show_menu)
        back_button.pack(pady=10)

    def perform_change_pin(self, pin_entry):
        new_pin = pin_entry.get()
        if new_pin.isdigit() and len(new_pin) == 4:
            new_pin = int(new_pin)
            result = self.atm.change_pin(new_pin)
            messagebox.showinfo("Change PIN", result)
        else:
            messagebox.showerror("Error", "PIN must be a 4-digit number.")
        self.show_menu()

if __name__ == "__main__":
    root = ctk.CTk()
    atm = ATM(1000, 1234)
    app = ATMApp(root, atm)
    root.mainloop()
