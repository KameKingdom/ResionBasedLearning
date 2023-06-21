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


lines = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (1, 5),
    (5, 6),
    (6, 7),
    (1, 8),
    (8, 9),
    (9, 10),
    (10, 11),
    (11, 22),
    (8, 12),
    (12, 13),
    (13, 14),
    (14, 19),
]


def draw_lines(data):
    people_num = len(data["people"])
    for i in range(people_num):
        for line in lines:
            start = location(line[0], data, i)
            end = location(line[1], data, i)
            if start != (0, 0) and end != (0, 0):
                canvas.create_line(start, end, width=2)

def animate(zip_file):
    file_names = zip_file.namelist()
    index = 0

    def update_animation():
        nonlocal index

        if index < len(file_names):
            file_name = file_names[index]

            with zip_file.open(file_name, "r") as file:
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


zip_file = zipfile.ZipFile("kabeposter.zip", "r")
animate(zip_file)

root.mainloop()
