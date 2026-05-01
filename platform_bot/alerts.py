import tkinter as tk
import winsound
from platform_bot.config import ALERT_SOUND


def play_alert():
    try:
        winsound.PlaySound(str(ALERT_SOUND), winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception:
        pass


def show_alert(message: str):
    play_alert()

    window = tk.Tk()
    window.title("🚨 Route Detected")
    window.geometry("900x350")
    window.attributes("-topmost", True)
    window.configure(bg="white")

    window.after(100, lambda: window.focus_force())

    tk.Label(
        window,
        text=message,
        wraplength=780,
        font=("Arial", 26, "bold"),
        bg="white"
    ).pack(pady=30)

    tk.Button(
        window,
        text="OK",
        font=("Arial", 22, "bold"),
        command=window.destroy
    ).pack(pady=20)

    window.mainloop()