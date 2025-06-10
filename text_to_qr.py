import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode

qr_image = None
qr_display = None
text_input = None

def generate_qr():
    global qr_image, qr_display

    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Enter something....")
        return

    qr = qrcode.make(text)
    qr_image = qr

    img = qr.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)

    qr_display.configure(image=img_tk)
    qr_display.image = img_tk

def save_qr():
    if not qr_image:
        messagebox.showwarning("Generate a QR code first")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG Image", "*.png")])
    if file_path:
        qr_image.save(file_path)
        messagebox.showinfo("Saved", "QR Code saved to: "+file_path)

def clear_all():
    global qr_image
    text_input.delete("1.0", tk.END)
    qr_display.configure(image='')
    qr_display.image = None
    qr_image = None

root = tk.Tk()
root.title("Text to QR Code Generator")
root.geometry("600x700")
root.configure(bg="#f0f0f0")

text_label = tk.Label(root, text="Enter your text below:", font=("Arial", 12,"bold"), bg="#f0f0f1")
text_label.pack(pady=(10, 0))

text_input = tk.Text(root, height=10, font=("Arial", 12), wrap=tk.WORD)
text_input.pack(padx=20, pady=10, fill=tk.BOTH)

button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

generate_btn = tk.Button(button_frame, text="Generate QR", command=generate_qr,bg="#4CAF50", fg="white", width=15)
generate_btn.grid(row=0, column=0, padx=10)

save_btn = tk.Button(button_frame, text="Save QR", command=save_qr,bg="blue", fg="white", width=15)
save_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_all, bg="#f44336", fg="white", width=15)
clear_btn.grid(row=0, column=2, padx=10)

qr_label_title = tk.Label(root, text="QR Code Output", font=("Sans-Serief", 12, "bold"), bg="#f0f0f0")
qr_label_title.pack(pady=(20, 5))

qr_display = tk.Label(root, bg="white", width=200, height=200, bd=2, relief="sunken")
qr_display.pack(pady=10)

root.mainloop()
