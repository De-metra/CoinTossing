import tkinter as tk
from PIL import Image, ImageTk
import random

class CoinSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Симуляция подбрасывания монеты")
        
        # Загрузка изображений монеты и сохранение в атрибуте экземпляра
        self.images = [ImageTk.PhotoImage(Image.open(f"images/coin_{i}.png")) for i in range(1, 13)]
        self.orel_image = ImageTk.PhotoImage(Image.open("images/orel.png"))
        self.reshka_image = ImageTk.PhotoImage(Image.open("images/reshka.png"))
        
        # Создание холста для отображения монеты
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Кнопка для подбрасывания монеты
        self.flip_button = tk.Button(root, text="Подбросить монету", command=self.start_flip)
        self.flip_button.pack()

        # Отображение монеты
        self.coin_image = self.canvas.create_image(150, 150, image=self.images[0])

        # Счетчик для анимации
        self.animation_index = 0

    def start_flip(self):
        # Блокировка кнопки на время анимации
        self.flip_button.config(state="disabled")
        
        # Запуск анимации вращения
        self.animate_flip()

    def animate_flip(self):
        # Смена изображения в анимации
        self.canvas.itemconfig(self.coin_image, image=self.images[self.animation_index])
        self.animation_index = (self.animation_index + 1) % len(self.images)
        
        # Продолжение анимации или отображение конечного результата
        if self.animation_index != 0 or random.choice([True, False]):  # Случайное число для остановки
            self.root.after(100, self.animate_flip)  # Продолжаем анимацию через 100 мс
        else:
            # Вывод финального результата
            final_result = random.choice(["Орел", "Решка"])
            if final_result == "Орел":
                self.canvas.itemconfig(self.coin_image, image=self.orel_image)
            else:
                self.canvas.itemconfig(self.coin_image, image=self.reshka_image)
            # Доступность кнопки после завершения анимации
            self.flip_button.config(state="normal")

if __name__ == "__main__":
    root = tk.Tk()
    coin_simulator = CoinSimulator(root)
    root.mainloop()
