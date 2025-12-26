import tkinter as tk
from tkinter import messagebox

def calculate_share():
    try:
        bill_total = float(entry_bill.get())  
        num_people = int(entry_people.get()) 
        
        if num_people <= 0:
            messagebox.showwarning("Error", "تعداد نفرات باید بیشتر از 0 باشه!")
            return
        
        share = bill_total / num_people  
        messagebox.showinfo("Result", f"سهم هر نفر: {share} تومان")  
    except ValueError:
        messagebox.showwarning("Error", "لطفا عدد وارد کنید!")

root = tk.Tk()
root.title("ماشین حساب دُنگ")
root.geometry("300x200")

tk.Label(root, text="مبلغ صورتحساب: ").grid(row=0, column=0, padx=10, pady=10)
entry_bill = tk.Entry(root)
entry_bill.grid(row=0, column=1)

tk.Label(root, text="تعداد نفرات: ").grid(row=1, column=0, padx=10, pady=10)
entry_people = tk.Entry(root)
entry_people.grid(row=1, column=1)

btn_calculate = tk.Button(root, text="محاسبه سهم", command=calculate_share)
btn_calculate.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
