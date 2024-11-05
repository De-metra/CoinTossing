import tkinter as tk
from PIL import Image, ImageTk
import random
import time

class CoinSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Симуляция подбрасывания монеты")
        
        # Загрузка изображений монеты
        self.images = [ImageTk.PhotoImage(Image.open(f"images/coin_{i}.png")) for i in range(1, 13)]
        self.orel_image = ImageTk.PhotoImage(Image.open("images/orel.png"))
        self.reshka_image = ImageTk.PhotoImage(Image.open("images/reshka.png"))
        
        # Создание холста для отображения монеты
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Кнопка для подбрасывания монеты
        self.flip_button = tk.Button(root, text="Подбросить монету", command=self.flip_coin)
        self.flip_button.pack()

        # Отображение монеты
        self.coin_image = self.canvas.create_image(150, 150, image=self.images[0])

    def flip_coin(self):
        # Анимация вращения монеты
        for _ in range(10):  # Количество вращений
            for img in self.images:
                self.canvas.itemconfig(self.coin_image, image=img)
                self.root.update()
                time.sleep(0.1)  # Задержка между изображениями для эффекта анимации
        
        # Показываем финальный результат
        final_result = random.choice(["Орел", "Решка"])
        if final_result == "Орел":
            self.canvas.itemconfig(self.coin_image, image=self.orel_image)
        else:
            self.canvas.itemconfig(self.coin_image, image=self.reshka_image)

if __name__ == "__main__":
    root = tk.Tk()
    coin_simulator = CoinSimulator(root)
    root.mainloop()
