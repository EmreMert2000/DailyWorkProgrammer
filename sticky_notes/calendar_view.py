import tkinter as tk
from tkcalendar import Calendar
import db_manager

def open_calendar():
    def show_notes():
        selected_date = cal.get_date()
        notes = db_manager.get_notes_by_date(selected_date)
        notes_window = tk.Toplevel(root)
        notes_window.title(f"Notlar - {selected_date}")
        for note in notes:
            tk.Label(notes_window, text=note[1], wraplength=300, justify="left").pack(pady=5)

    root = tk.Tk()
    root.title("Takvim")
    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)

    tk.Button(root, text="Notları Göster", command=show_notes).pack(pady=10)
    root.mainloop()
