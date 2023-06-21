import tkinter as tk

root = tk.Tk()
root.geometry("500x500+0+0")
root.title("北村研領域実習R2_5")

canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)


class Human:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.face_size = 50
        self.speed = 1

    def write(self):
        canvas.create_oval(self.x - self.face_size, self.y - self.face_size, self.x + self.face_size, self.y + self.face_size, width=2)
        body_len = 200
        canvas.create_line(self.x, self.y + self.face_size, self.x, self.y + self.face_size + body_len, width=2)
        arm_len = 70
        for i in [-1, 1]:
            canvas.create_line(self.x, self.y + self.face_size + (body_len // 3), self.x + (arm_len * i), self.y + self.face_size + (body_len // 3) + arm_len, width=2)
            canvas.create_line(self.x, body_len - self.face_size + body_len, self.x + arm_len * i, body_len - self.face_size + arm_len + body_len, width=2)

    def move(self):
        if self.x > 500 or self.x < 0:
            self.speed *= -1
        self.x += self.speed


def animate():
    canvas.delete("all")
    human.move()
    human.write()
    root.after(10, animate)


human = Human(100, 100)
animate()
root.mainloop()
