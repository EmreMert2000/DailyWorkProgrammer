import tkinter as tk
import db_manager
import calendar_view

def open_add_note():
    def save_note():
        content = note_text.get("1.0", tk.END).strip()
        date = cal.get_date()
        if content:
            db_manager.add_note(content, date)
            add_note_window.destroy()

    add_note_window = tk.Toplevel(root)
    add_note_window.title("Yeni Not")
    
    tk.Label(add_note_window, text="Notunuzu Yazın:").pack(pady=10)
    note_text = tk.Text(add_note_window, height=10, width=30)
    note_text.pack(pady=10)

    cal = calendar_view.Calendar(add_note_window)
    cal.pack(pady=10)

    tk.Button(add_note_window, text="Kaydet", command=save_note).pack(pady=10)

root = tk.Tk()
root.title("Yapışkan Notlar")
root.geometry("400x400")

db_manager.create_tables()

tk.Button(root, text="Takvimi Aç", command=calendar_view.open_calendar).pack(pady=20)
tk.Button(root, text="Yeni Not Ekle", command=open_add_note).pack(pady=20)

root.mainloop()
