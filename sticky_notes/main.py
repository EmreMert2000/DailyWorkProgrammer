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

    # Yeni Not Penceresi
    add_note_window = tk.Toplevel(root)
    add_note_window.title("Yeni Not")
    add_note_window.geometry("700x700")  # Kare boyut
    add_note_window.resizable(False, False)  # Pencere boyutunun değişmemesini sağla

    
    tk.Label(add_note_window, text="Notunuzu Yazın:", font=("Arial", 14, "bold"), bg="#0000FF", fg="white").grid(row=0, column=0, pady=20, padx=10)

   
    note_text = tk.Text(add_note_window, height=10, width=40, font=("Arial", 12), bd=2, relief="solid", wrap=tk.WORD)
    note_text.grid(row=1, column=0, pady=10, padx=10)

    
    cal = calendar_view.get_calendar(add_note_window)
    cal.grid(row=2, column=0, pady=10, padx=10)

  
    ttk.Button(add_note_window, text="Kaydet", command=save_note, style="TButton").grid(row=3, column=0, pady=20, padx=10)

# Ana Pencere
root = tk.Tk()
root.title("Yapışkan Notlar")
root.geometry("500x500")  
root.resizable(False, False)  
root.configure(bg="#f0f0f0")  


style = ttk.Style()
style.configure("TButton", font=("Arial", 12), width=20, padding=10, background="#4CAF50", foreground="white", relief="flat")
style.map("TButton", background=[("active", "#45a049")])


db_manager.create_tables()


ttk.Button(root, text="Takvimi Aç", command=calendar_view.open_calendar).grid(row=0, column=0, pady=20, padx=10, sticky="ew")
ttk.Button(root, text="Yeni Not Ekle", command=open_add_note).grid(row=1, column=0, pady=20, padx=10, sticky="ew")


root.mainloop()