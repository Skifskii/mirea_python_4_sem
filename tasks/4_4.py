import math
import tkinter as tk
import datetime


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


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def next_prime_above(a):
    """Return the next prime number above a."""
    if a <= 1:
        return 2
    prime = a + 1
    while True:
        if is_prime(prime):
            return prime
        prime += 1


def shader(x, y):
    a = 3
    m = (datetime.datetime.now().microsecond % (1000 * (int(x * WIDTH)) + 1)) + 1

    result = ((int((a*y*(x*WIDTH + 256) + next_prime_above(m * y**2) + y)) + 1) % m) % 2

    return result, result, result


main(shader)
