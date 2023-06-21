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

with zipfile.ZipFile("kabeposter.zip", 'r') as zip_file:
    for file_name in zip_file.namelist():
        if int(file_name.split('_')[1]) == 0:
            with zip_file.open(file_name, 'r') as file:
                data = json.load(file)
                if isinstance(data, dict):
                    draw_lines(data)

root.mainloop()