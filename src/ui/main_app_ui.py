import tkinter as tk
from tkinter import ttk
class MainApp:
    WIDTH = 1000
    HEIGHT = 600
    WIDTH_CONTENT = round(0.7*WIDTH, 0)
    COLOR_BACKGROUND = "#F5F7FA"
    LEFT_FRAME_COLOR = "#FFFFFF"

    def __init__(self):
        # Khởi tạo cửa sổ chính - Initialize the main window
        self.root:tk.Tk = tk.Tk()
        
        # Tạo title cho cửa sổ - Create title for the main window
        self.root.title = "Học từ vựng - Quản lý"

        # Đặt kích thước ban đầu và vị trí (giữa màn hình) - Set initial size and position (center of screen)
        self.root.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Cho phép thay đổi kích thước - Allow resize 
        self.root.resizable(True, True)

        # Đặt màu nền cho ứng dụng - Set background color for the app
        self.root.configure(bg=self.COLOR_BACKGROUND)

        self.current_row = 0
        self.style = ttk.Style()
    
    def draw_app(self):
        # Tạo PanedWindow để chia cửa sổ thành hai phần - Create a PaneWindow to seperate the main window into two part
        self.paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, sashwidth=5, sashrelief="raised")
        self.paned_window.pack(fill="both", expand=True)

        
        # Tạo frame bên trái (70% độ rộng app) - Create left frame (70% width app)
        self.left_frame = tk.Frame(self.paned_window, borderwidth=10, relief="flat")
        self.paned_window.add(self.left_frame, width=self.WIDTH_CONTENT)  # 70% của 1000px - 70% of 1000px

        # Tạo inner_left_frame với padding - Create inner_left_frame with padding
        self.inner_left_frame = tk.Frame(self.left_frame, border=10, bg=self.LEFT_FRAME_COLOR)
        self.inner_left_frame.pack(padx=8, pady=8, fill="both", expand=True)  # Padding 20px xung quanh - Padding 20px around
        
        # Tạo frame con để chứa biểu mẫu và căn giữa
        self.form_frame = tk.Frame(self.inner_left_frame, bg=self.LEFT_FRAME_COLOR)
        self.form_frame.pack(expand=True, fill='y', pady=60)

        # Tạo frame bên phải (30% độ rộng app) - Create right frame (30% width app)
        self.right_frame = tk.Frame(self.paned_window, borderwidth=10, relief="flat")
        self.paned_window.add(self.right_frame, width=1000 - self.WIDTH_CONTENT)  # 30% của 1000px - 30% of 1000px
        
        # Thêm nhãn mẫu vào frame trái - Add label to the left frame
        tk.Label(self.form_frame, text="Form nhập từ vựng", font=("Arial", 24), bg=self.LEFT_FRAME_COLOR).grid(row=0, column=0, columnspan=2, pady=20)
        
        self.current_row += 1

        # Thêm nhãn mẫu vào frame phải - Add label to the right frame
        tk.Label(self.right_frame, text="Chủ đề", font=("Arial", 12)).pack(pady=20)
        
      
        self.create_input_form("Nhập chủ đề", 50)
        self.create_input_form("Nhập từ", 50)
        self.create_input_form("Nhập từ loại", 50)
        self.create_input_form("Nghĩa", 50)

        self.create_button()

   

    def create_input_form(self, label_text, entry_width):
        # Tạo style cho Entry và Label - Create style for Entry and Label
        
        self.style.theme_use('clam')  # Sử dụng theme 'clam' để giao diện hiện đại hơn - Use the 'clam' theme for a more modern UI
        
        # Tùy chỉnh kiểu cho Label - Customize the style for the Label
        self.style.configure("Custom.TLabel",
                        background="#ffffff",  
                        foreground="black",
                        font=("Arial", 12))
        
        # Tùy chỉnh kiểu cho Entry - Customize the style for the Entry
        self.style.configure("Custom.TEntry",
                        fieldbackground="white",  # Màu nền ô input - Background color of the input
                        foreground="black",       # Màu chữ - Text color
                        bordercolor="gray",       # Màu viền - Border color
                        borderwidth=1,            # Độ dày viền - Border thinkness
                        padding=5)                
        # Hiệu ứng khi focus vào ô input - Focusing effect for the input
        self.style.map("Custom.TEntry",
                fieldbackground=[("focus", "#e6f3ff")],  # Màu nền khi focus - Background color on focus
                bordercolor=[("focus", "#4a90e2")])      # Màu viền khi focus - Border color on focus

        # Tạo nhãn với kiểu tùy chỉnh - Create the label with the customized style
        label = ttk.Label(self.form_frame, text=label_text, style="Custom.TLabel")
        label.grid(row=self.current_row, column=0, padx=5, pady=5, sticky="w")

        # Tạo ô input với kiểu tùy chỉnh - Create the input with the customized style
        entry = ttk.Entry(self.form_frame, width=entry_width, style="Custom.TEntry")
        entry.grid(row=self.current_row, column=1, padx=5, pady=5, sticky="w")

        self.current_row += 1
    
        
    def create_button(self):
        # Tạo một kiểu dáng tùy chỉnh cho nút
        self.style.theme_use('clam')
        self.style.configure('Custom.TButton', background='lightblue', foreground='white', font=('Arial', 12))

        # Ánh xạ màu khi di chuột qua
        self.style.map('TButton',
            background=[('active', 'white')],
            foreground=[('active', 'lightblue')]
        )
        # Tạo nút với kiểu dáng tùy chỉnh
        ttk_button = ttk.Button(self.form_frame, text="Thêm vào", style='Custom.TButton',cursor="hand2", command=lambda:print('click'))
        
        # Đặt nút vào lưới, trải dài qua 2 cột và căn chỉnh theo chiều ngang
        ttk_button.grid(row=self.current_row, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        
        # Tăng giá trị current_row để chuẩn bị cho widget tiếp theo
        self.current_row += 1   
    
    def run(self):
        # Vẽ giao diện app - Create the UI of the app
        self.draw_app()
        # Chạy vòng lặp chính của ứng dụng - Run the main loop of the app
        self.root.mainloop()


