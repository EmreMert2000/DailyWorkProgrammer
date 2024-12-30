import tkinter as tk
from tkinter import ttk, messagebox
import db_manager
import calendar_view

def open_add_note():
    def save_note():
        content = note_text.get("1.0", tk.END).strip()
        date = cal.get_date()
        if content:
            db_manager.add_note(content, date)
            messagebox.showinfo("Başarılı", "Not başarıyla kaydedildi!")
            add_note_window.destroy()
        else:
            messagebox.showwarning("Hata", "Boş not kaydedilemez!")

    add_note_window = tk.Toplevel(root)
    add_note_window.title("Yeni Not")
    add_note_window.geometry("400x400")
    add_note_window.resizable(True, True)  

    tk.Label(add_note_window, text="Notunuzu Yazın:", font=("Arial", 12)).grid(row=0, column=0, pady=10, padx=10)
    note_text = tk.Text(add_note_window, height=10, width=40)
    note_text.grid(row=1, column=0, pady=10, padx=10)

    cal = calendar_view.get_calendar(add_note_window)
    cal.grid(row=2, column=0, pady=10, padx=10)

    ttk.Button(add_note_window, text="Kaydet", command=save_note).grid(row=3, column=0, pady=10, padx=10)

root = tk.Tk()
root.title("Yapışkan Notlar")
root.geometry("400x400")
root.resizable(True, True)  

style = ttk.Style()
style.configure("TButton", font=("Arial", 10))

db_manager.create_tables()


ttk.Button(root, text="Takvimi Aç", command=calendar_view.open_calendar).grid(row=0, column=0, pady=20, padx=10, sticky="ew")
ttk.Button(root, text="Yeni Not Ekle", command=open_add_note).grid(row=1, column=0, pady=20, padx=10, sticky="ew")

root.mainloop()
