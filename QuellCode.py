import tkinter as tk
import webbrowser

UPDATE_URL = "https://github.com/Smopga/Sulfer-AntiVirus"

def fake_update():
    # „Update Feature“ tut nichts echtes – nur Link öffnen
    webbrowser.open(UPDATE_URL)

# Fenster erstellen
window = tk.Tk()
window.title("Sulfer AntiVirus")
window.geometry("400x250")
window.resizable(False, False)
window.configure(bg="#0d0d0d")

# Coming Soon Text
label = tk.Label(
    window,
    text="🚧 Coming Soon 🚧",
    font=("Arial", 20, "bold"),
    fg="#00ff99",
    bg="#0d0d0d"
)
label.pack(pady=40)

# Update Button (Fake Feature)
update_button = tk.Button(
    window,
    text="Check for Updates",
    font=("Arial", 12),
    fg="#0d0d0d",
    bg="#00ff99",
    command=fake_update
)
update_button.pack(pady=10)

# Start GUI
window.mainloop()
