# Симуляция подбрасывания монеты 
Проект симулирует подбрасывание монеты с анимацией и выводом результата (Орел или Решка).

### Описание
Программа реализована на Python с использованием библиотеки _tkinter_ для графического интерфейса. При нажатии на кнопку "Подбросить монету" запускается анимация вращения, после чего отображается результат подбрасывания (Орел или Решка).

### Требования
Для работы программы необходимы:
+ Python 3.7 или выше
+ Библиотека _Pillow_ для работы с изображениями

### Установка
1. Скачайте и установите Python с официального сайта (если Python еще не установлен).
2. Установите библиотеку Pillow:
    `pip install Pillow`

### Настройка
Поместите изображения монеты в папку проекта. В программе используются следующие изображения:
+ coin_1.png - coin_12.png для анимации вращения.
+ orel.png и reshka.png для отображения финального результата.
Проверьте, что все изображения находятся в одной папке с файлом программы и что названия файлов соответствуют требованиям программы.

### Запуск
1. Сохраните код программы в файл, например, `coin_flip.py`.
2. Откройте терминал или командную строку, перейдите в директорию с проектом, и запустите программу командой:
    `python coin_flip.py`

### Использование
+ Откроется окно с кнопкой "Подбросить монету".
+ Нажмите кнопку, чтобы начать анимацию вращения монеты.
+ После завершения анимации отобразится результат: "Орел" или "Решка".

### Структура папки
Ваша папка с проектом должна выглядеть следующим образом:
> /папка_проекта
│
├── coin_simulator.py      # файл программы
├── coin_1.png             # изображение монеты для анимации
├── coin_2.png
├── ...
├── coin_12.png
├── orel.png               # изображение для результата "Орел"
└── reshka.png             # изображение для результата "Решка"

### Примечания
Программа использует метод after для создания анимации, чтобы интерфейс оставался отзывчивым.
Если программа не запускается, проверьте наличие всех необходимых изображений в директории.

### Лицензия
Этот проект находится в свободном доступе и может использоваться без ограничений.