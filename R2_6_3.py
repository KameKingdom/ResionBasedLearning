import zipfile
import json
import tkinter as tk

root = tk.Tk()
root.geometry("2000x1000+0+0")
root.title("北村研領域実習R2_6_2")

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

def draw_lines(data):
    people_num = len(data["people"])
    for i in range(people_num):
        content = data["people"][i]["pose_keypoints_2d"]
        neck_x = content[3*1 + 0]
        neck_y = content[3*1 + 1]
        right_shoulder_x = content[3*2 + 0]
        right_shoulder_y = content[3*2 + 1]
        left_shoulder_x = content[3*5 + 0]
        left_shoulder_y = content[3*5 + 1]
        canvas.create_line(int(right_shoulder_x), int(right_shoulder_y), int(neck_x), int(neck_y), width=2)
        canvas.create_line(int(left_shoulder_x), int(left_shoulder_y), int(neck_x), int(neck_y), width=2)

def animate(zip_file):
    file_names = zip_file.namelist()
    index = 0
    
    def update_animation():
        nonlocal index
        
        if index < len(file_names):
            file_name = file_names[index]
            
            with zip_file.open(file_name, 'r') as file:
                data = json.load(file)
                if isinstance(data, dict):
                    canvas.delete("all")
                    draw_lines(data)
                    
            index += 1
            root.after(500, update_animation)  # 1秒後に再度呼び出す
        
    update_animation()

with zipfile.ZipFile("kabeposter.zip", 'r') as zip_file:
    animate(zip_file)

root.mainloop()
