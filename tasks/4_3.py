import math
import tkinter as tk


WIDTH = 256
HEIGHT = 256

def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def get_circle_color(x, y, x_center, y_center, radius):
    distance = ((x - x_center)**2 + (y - y_center)**2)**0.5
    if distance < radius:
        return True
    return False


def tuple_summa(a, b):
    return tuple([a[i] + b[i] for i in range(3)])


def compare_with_line(x, y, k, b=0):
    line_y = k*x + b
    if y > line_y:
        return True
    return False


def shader(x, y):
    if get_circle_color(x * WIDTH, y * HEIGHT, WIDTH//2, HEIGHT//2, WIDTH // 4):
        if get_circle_color(x * WIDTH, y * HEIGHT, WIDTH//8 * 4.7, HEIGHT//8 * 3, WIDTH // 18):
            return 0, 0, 0
        if not compare_with_line((x * WIDTH) - WIDTH//2, (HEIGHT - y * HEIGHT) - HEIGHT//2, 0.5):
            if compare_with_line((x * WIDTH) - WIDTH//2, (HEIGHT - y * HEIGHT) - HEIGHT//2, -0.5):
                return 0, 0, 0
        return 1, 1, 0
    return 0, 0, 0


main(shader)
