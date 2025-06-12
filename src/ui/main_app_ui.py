import tkinter as tk

class MainApp:
    WIDTH = 1000
    HEIGHT = 600
    WIDTH_CONTENT = 0.7*WIDTH
    def __init__(self):
        # Khởi tạo cửa sổ chính - Initialize the main window
        self.root:tk.Tk = tk.Tk()
        
        # Tạo title cho cửa sổ - Create title for the main window
        self.root.title = "Học từ vựng - Quản lý"

        # Đặt kích thước ban đầu và vị trí (giữa màn hình) - Set initial size and position (center of screen)
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Cho phép thay đổi kích thước - Allow resize 
        self.root.resizable(True, True)

        # Tạo PanedWindow để chia cửa sổ thành hai phần - Create a PaneWindow to seperate the main window into two part
        self.paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, sashwidth=5, sashrelief="raised")
        self.paned_window.pack(fill="both", expand=True)


         # Tạo frame bên trái (70%)
        self.left_frame = tk.Frame(self.paned_window, bg="lightblue")
        self.paned_window.add(self.left_frame, width=round(self.WIDTH_CONTENT))  # 70% của 350px
        
        # Tạo frame bên phải (30%)
        self.right_frame = tk.Frame(self.paned_window, bg="lightgray")
        self.paned_window.add(self.right_frame, width=round(1000 - self.WIDTH_CONTENT))  # 30% của 350px
        
        # Thêm nhãn mẫu vào frame trái (sẽ thay bằng form nhập từ)
        tk.Label(self.left_frame, text="Form nhập từ vựng", font=("Arial", 12), bg="lightblue").pack(pady=20)
        
        # Thêm nhãn mẫu vào frame phải (sẽ thay bằng danh sách từ hoặc khác)
        tk.Label(self.right_frame, text="Thông tin bổ sung", font=("Arial", 12), bg="lightgray").pack(pady=20)
        
        # Nút thoát tạm thời
        self.exit_button = tk.Button(self.root, text="Thoát", command=self.root.quit)
        self.exit_button.pack(pady=5)


    def create_input_form(self):
        pass
    
    def run(self):
        # Chạy vòng lặp chính của ứng dụng
        self.root.mainloop()


