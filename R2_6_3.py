import zipfile
import json
import tkinter as tk

root = tk.Tk()
root.geometry("2000x1000+0+0")
root.title("北村研領域実習R2_6_2")

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

def location(pos, data, i):
    content = data["people"][i]["pose_keypoints_2d"]
    return int(content[3 * pos + 0]), int(content[3 * pos + 1])

def draw_lines(data):
    people_num = len(data["people"])
    for i in range(people_num):
        canvas.create_line(location(0, data, i), location(1, data, i), width=2)
        canvas.create_line(location(1, data, i), location(2, data, i), width=2)
        canvas.create_line(location(2, data, i), location(3, data, i), width=2)
        canvas.create_line(location(3, data, i), location(4, data, i), width=2)
        canvas.create_line(location(1, data, i), location(5, data, i), width=2)
        canvas.create_line(location(5, data, i), location(6, data, i), width=2)
        canvas.create_line(location(6, data, i), location(7, data, i), width=2)
        canvas.create_line(location(1, data, i), location(8, data, i), width=2)
        canvas.create_line(location(8, data, i), location(9, data, i), width=2)
        canvas.create_line(location(9, data, i), location(10, data, i), width=2)
        canvas.create_line(location(10, data, i), location(11, data, i), width=2)
        canvas.create_line(location(8, data, i), location(12, data, i), width=2)
        canvas.create_line(location(12, data, i), location(13, data, i), width=2)
        canvas.create_line(location(13, data, i), location(14, data, i), width=2)

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
                    print(data)
                    canvas.delete("all")
                    draw_lines(data)

            index += 1
            root.after(500, update_animation)
        else:
            zip_file.close()  # 追加: アニメーション終了時にzipファイルを閉じる

    update_animation()

zip_file = zipfile.ZipFile("kabeposter.zip", 'r')
animate(zip_file)

root.mainloop()
