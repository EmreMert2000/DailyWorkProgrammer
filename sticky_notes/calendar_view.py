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
       
        notes_window.geometry("500x400")
        notes_window.resizable(False, False)

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
                frame = tk.Frame(notes_window, bg="#f7f7f7")
                frame.pack(pady=10, padx=10, fill="x")

                note_content = tk.Text(frame, wrap="word", width=40, height=3, font=("Arial", 12))
                note_content.insert("1.0", note[1])
                note_content.pack(side="left", padx=5, pady=5)
                
                def save_changes(note_id=note[0]):
                    new_content = note_content.get("1.0", "end").strip()
                    db_manager.update_note(note_id, new_content)

                def delete_note_action(note_id=note[0]):
                    db_manager.delete_note(note_id)
                    frame.destroy()

                tk.Button(frame, text="Kaydet", command=save_changes, bg="#4CAF50", fg="white").pack(side="left", padx=5)
                tk.Button(frame, text="Sil", command=delete_note_action, bg="#F44336", fg="white").pack(side="left", padx=5)
        else:
            tk.Label(notes_window, text="Bu tarihte not bulunamadı.", font=("Arial", 14), fg="red", bg="#f7f7f7").pack(pady=30)

    root = tk.Toplevel()
    root.title("Takvim")
    
    root.geometry("400x400")
    root.resizable(False, False)

    tk.Label(root, text="Bir Tarih Seçin:", font=("Arial", 12)).pack(pady=20)
    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(pady=20)

    ttk.Button(root, text="Notları Göster", command=show_notes).pack(pady=20)
