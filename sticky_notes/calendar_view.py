import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
import db_manager

def open_calendar():
    def show_notes():
        selected_date = cal.get_date()
        notes = db_manager.get_notes_by_date(selected_date)

       
        notes_window = tk.Toplevel(root)
        notes_window.title(f"Notlar - {selected_date}")
        notes_window.geometry("600x400")

       
        try:
            bg_image = Image.open("assets/notes.png")
            bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)  
            bg_photo = ImageTk.PhotoImage(bg_image)

            bg_label = tk.Label(notes_window, image=bg_photo)
            bg_label.image = bg_photo 
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            tk.Label(notes_window, text="Arka plan resmi bulunamadı.", font=("Arial", 12), fg="red").pack(pady=30)

        
        if notes:
            for note in notes:
                tk.Label(notes_window, text=f"- {note[1]}", wraplength=300, justify="left", font=("Arial", 14), bg="#f7f7f7").pack(pady=10)
        else:
            tk.Label(notes_window, text="Bu tarihte not bulunamadı.", font=("Arial", 14), fg="red", bg="#f7f7f7").pack(pady=30)

    root = tk.Toplevel()
    root.title("Takvim")
    root.geometry("400x400")

    tk.Label(root, text="Bir Tarih Seçin:", font=("Arial", 12)).pack(pady=20)
    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)

    ttk.Button(root, text="Notları Göster", command=show_notes).pack(pady=20)

def get_calendar(parent):
    return Calendar(parent, selectmode="day", date_pattern="yyyy-mm-dd")
