import tkinter as tk
from PIL import Image, ImageTk  # Import Pillow để hỗ trợ .jpg

def on_button_click():
    label.config(text="Bạn đã nhấn nút!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giao diện Tkinter")

# Đảm bảo đường dẫn hình ảnh đúng
image = Image.open("Users/acer/Documents/Code/Test/BasicProject/project python/project_6_UDU/download.png")
photo = ImageTk.PhotoImage(image)

# Thêm nhãn hiển thị hình ảnh
label = tk.Label(root, image=photo)
label.image = photo  # Giữ tham chiếu đến hình ảnh để tránh bị xóa
label.pack()

# Thêm nút bấm
button = tk.Button(root, text="Nhấn vào đây", command=on_button_click)
button.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
