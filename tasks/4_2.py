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
    img = tk.PhotoImage(data=draw(shader, WIDTH, HEIGHT)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def is_inside_circle(x, y, r):
    distance_squared = (int(x) - WIDTH//2)**2 + (int(y) - HEIGHT//2)**2
    if distance_squared <= r**2:
        return True
    else:
        return False


def get_circle_color(x, y, offset):
    x_center = WIDTH//2 + offset
    y_center = HEIGHT//2 + offset

    distance = ((x - x_center)**2 + (y - y_center)**2)**0.5
    if distance < WIDTH // 4:
        return (1 - distance / (WIDTH//4))
    return 0


def shader(x, y):
    ans = (0, 0, 0)

    ans = tuple([ans[i] + (0, get_circle_color(x * WIDTH, y * HEIGHT, -4), 0)[i] for i in range(3)])
    ans = tuple([ans[i] + (get_circle_color(x * WIDTH, y * HEIGHT, 4), 0, 0)[i] for i in range(3)])
    return ans


main(shader)
