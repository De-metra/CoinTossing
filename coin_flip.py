import tkinter as tk
import random
import time

class CoinSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Симуляция подбрасывания монеты")
        
        # Создание холста для отображения монеты
        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        # Кнопка для подбрасывания монеты
        self.flip_button = tk.Button(root, text="Подбросить монету", command=self.flip_coin)
        self.flip_button.pack()

        # Текст для отображения результата
        self.result_text = self.canvas.create_text(150, 150, text="", font=("Arial", 30))

    def flip_coin(self):
        # Анимация вращения монеты
        for _ in range(10):  # Количество вращений
            self.canvas.itemconfig(self.result_text, text=random.choice(["Орел", "Решка"]))
            self.root.update()
            time.sleep(0.1)  # Задержка между "вращениями"
        
        # Показываем финальный результат
        final_result = random.choice(["Орел", "Решка"])
        self.canvas.itemconfig(self.result_text, text=final_result)

if __name__ == "__main__":
    root = tk.Tk()
    coin_simulator = CoinSimulator(root)
    root.mainloop()
