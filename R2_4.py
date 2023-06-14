import tkinter as tk

root = tk.Tk()
root.geometry("500x500+0+0")
root.title("北村研領域実習R2_4")

# Canvasの作成
canvas = tk.Canvas(root)
# Canvasを配置
canvas.pack(fill = tk.BOTH, expand = True)

center_x = 250
center_y = 250
face_size = 50
# 顔の描画
canvas.create_oval(center_x - face_size, 100 - face_size, center_x + face_size, 100 + face_size, width = 2)

body_len = 200
# 胴体の描画
canvas.create_line(center_x, 150, center_x, 150 + body_len, width = 2)

arm_len = 70
# 腕の描画
for i in [-1, 1]:
    canvas.create_line(center_x, 200, center_x + arm_len * i, 200 + arm_len, width = 2)
    canvas.create_line(center_x, 150 + body_len, center_x + arm_len * i, 150 + arm_len + body_len, width = 2)


root.mainloop()