import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import db_manager

def open_calendar():
    def show_notes():
        selected_date = cal.get_date()
        notes = db_manager.get_notes_by_date(selected_date)
        notes_window = tk.Toplevel(root)
        notes_window.title(f"Notlar - {selected_date}")

        if notes:
            for note in notes:
                tk.Label(notes_window, text=f"- {note[1]}", wraplength=300, justify="left", font=("Arial", 10)).pack(pady=5)
        else:
            tk.Label(notes_window, text="Bu tarihte not bulunamadı.", font=("Arial", 10), fg="red").pack(pady=10)

    root = tk.Toplevel()
    root.title("Takvim")
    root.geometry("400x400")

    tk.Label(root, text="Bir Tarih Seçin:", font=("Arial", 12)).pack(pady=10)
    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)

    ttk.Button(root, text="Notları Göster", command=show_notes).pack(pady=10)

def get_calendar(parent):
    return Calendar(parent, selectmode="day", date_pattern="yyyy-mm-dd")
