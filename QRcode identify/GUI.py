import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode
from pyzbar.pyzbar import decode
import io

def generate_qr_code():
    data = entry.get()
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img = img.resize((200, 200), Image.ANTIALIAS)
        img_tk = ImageTk.PhotoImage(img)
        qr_label.config(image=img_tk)
        qr_label.image = img_tk
        status_label.config(text="QR Code generated")
        return img

def decode_qr_code():
    img = generate_qr_code()
    if img:
        decoded_result = decode_qr_code_from_img(img)
        if decoded_result:
            status_label.config(text=f"QR Code Contents: {decoded_result}")
        else:
            status_label.config(text="Failed to decode QR Code or no QR code found in the image.")

def decode_qr_code_from_img(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    buffered.seek(0)
    decoded_objects = decode(Image.open(buffered))
    if decoded_objects:
        decoded_text = decoded_objects[0].data.decode('utf-8', 'ignore')
        return decoded_text
    return None


# 创建GUI窗口
root = tk.Tk()
root.title("QR Code Generator and Decoder")

# 创建GUI组件
label = tk.Label(root, text="Enter data for QR Code:")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

decode_button = tk.Button(root, text="Decode QR Code", command=decode_qr_code)
decode_button.pack()

qr_label = tk.Label(root)
qr_label.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# 运行GUI主循环
root.mainloop()
