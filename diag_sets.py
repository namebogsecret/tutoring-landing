# -*- coding: utf-8 -*-
"""Наборы вопросов блока «Диагностика за 10 минут» на страницах-ответах (answers/*).

Набор = экзамен/предмет страницы, сопоставление DIAG_SET_BY_SLUG явное (slug страницы → ключ набора);
язык вопросов = язык страницы. Вопрос: (текст, [4 варианта], индекс верного). Ровно 5 вопросов в наборе,
ровно один верный ответ. Все числа проверены вручную (см. комментарии у вопросов). Дроби пишутся символом U+2044 (⁄): сайтовый тест запрещает «цифра/цифра» в видимом тексте.
Стоп-слова сайта (tests/test_pillar_pages.py FORBIDDEN, EXTRA_FORBIDDEN) действуют и на этот текст.
"""

SETS = {
    # ── ЕГЭ физика ─────────────────────────────────────────────────────────
    "ege-physics": {
        "ru": [
            ("Равнодействующая сил, приложенных к телу массой 2 кг, равна 6 Н. Чему равно ускорение тела?",
             ["0,33 м/с²", "3 м/с²", "8 м/с²", "12 м/с²"], 1),                                   # a=F/m=3
            ("Идеальный газ нагрели при постоянном объёме так, что его абсолютная температура выросла в 2 раза. Как изменилось давление?",
             ["не изменилось", "уменьшилось в 2 раза", "выросло в 2 раза", "выросло в 4 раза"], 2),  # p~T
            ("К резистору сопротивлением 10 Ом приложено напряжение 5 В. Какая мощность выделяется на резисторе?",
             ["0,5 Вт", "2,5 Вт", "5 Вт", "50 Вт"], 1),                                           # U²/R=2,5
            ("Тело брошено вертикально вверх со скоростью 20 м/с. Сопротивлением воздуха пренебречь, g = 10 м/с². Какой максимальной высоты оно достигнет?",
             ["2 м", "10 м", "40 м", "20 м"], 3),                                                 # v²/2g=20
            ("Как изменится максимальная кинетическая энергия фотоэлектронов при увеличении частоты падающего света (выше красной границы) и неизменной интенсивности?",
             ["увеличится", "не изменится", "уменьшится", "станет равной нулю"], 0),              # Ekmax=hν−A
        ],
        "en": [
            ("The net force on a 2 kg body is 6 N. What is its acceleration?",
             ["0.33 m/s²", "8 m/s²", "3 m/s²", "12 m/s²"], 2),
            ("An ideal gas is heated at constant volume so that its absolute temperature doubles. What happens to the pressure?",
             ["it doubles", "it stays the same", "it halves", "it quadruples"], 0),
            ("A voltage of 5 V is applied across a 10 ohm resistor. What power is dissipated in it?",
             ["0.5 W", "5 W", "2.5 W", "50 W"], 2),
            ("A body is thrown vertically upward at 20 m/s. Ignore air resistance and take g = 10 m/s². What maximum height does it reach?",
             ["20 m", "2 m", "10 m", "40 m"], 0),
            ("The frequency of the light in the photoelectric effect is increased (above the threshold) with the intensity unchanged. What happens to the maximum kinetic energy of the photoelectrons?",
             ["it stays the same", "it decreases", "it increases", "it becomes zero"], 2),
        ],
    },
    # ── IGCSE Physics 0625 ─────────────────────────────────────────────────
    "igcse-physics": {
        "ru": [
            ("Автомобиль проехал 150 м за 10 с с постоянной скоростью. Чему равна его скорость?",
             ["1500 м/с", "15 м/с", "160 м/с", "140 м/с"], 1),                                    # 15
            ("Масса бруска 240 г, объём 30 см³. Чему равна плотность вещества?",
             ["0,125 г/см³", "270 г/см³", "8 г/см³", "7200 г/см³"], 2),                           # 8
            ("Какая из этих единиц измеряет энергию?",
             ["ньютон", "ватт", "паскаль", "джоуль"], 3),
            ("Два одинаковых резистора подключены параллельно. Как их общее сопротивление соотносится с сопротивлением одного резистора?",
             ["меньше", "больше", "равно", "равно сумме"], 0),                                    # R/2
            ("Длина волны 2 м, частота 5 Гц. Чему равна скорость волны?",
             ["2,5 м/с", "7 м/с", "10 м/с", "0,4 м/с"], 2),                                       # 10
        ],
        "en": [
            ("A car travels 150 m in 10 s at a constant speed. What is its speed?",
             ["15 m/s", "1500 m/s", "160 m/s", "140 m/s"], 0),
            ("A block has a mass of 240 g and a volume of 30 cm³. What is its density?",
             ["0.125 g/cm³", "270 g/cm³", "7200 g/cm³", "8 g/cm³"], 3),
            ("Which of these is a unit of energy?",
             ["newton", "joule", "watt", "pascal"], 1),
            ("Two identical resistors are connected in parallel. How does their combined resistance compare with one resistor on its own?",
             ["greater", "equal", "less", "equal to the sum of the two"], 2),
            ("A wave has a wavelength of 2 m and a frequency of 5 Hz. What is its speed?",
             ["2.5 m/s", "10 m/s", "7 m/s", "0.4 m/s"], 1),
        ],
    },
    # ── IB Physics (SL/HL) ─────────────────────────────────────────────────
    "ib-physics": {
        "ru": [
            ("Автомобиль разгоняется из состояния покоя с ускорением 2 м/с² в течение 5 с. Какой путь он пройдёт?",
             ["10 м", "5 м", "25 м", "50 м"], 2),                                                 # ½·2·25=25
            ("Тело массой 2,0 кг падает без начальной скорости с высоты 5,0 м (g = 9,81 м/с², сопротивлением воздуха пренебречь). Какова скорость у земли?",
             ["5,0 м/с", "9,9 м/с", "49 м/с", "98 м/с"], 1),                                      # √(2·9,81·5)=9,9
            ("Масса на пружине колеблется с периодом T. Массу увеличили в 4 раза. Каким станет период?",
             ["T/2", "T", "4T", "2T"], 3),                                                        # T~√m
            ("Период полураспада изотопа 6 ч. Сколько из 80 г изотопа останется нераспавшимся через 18 ч?",
             ["10 г", "20 г", "40 г", "5 г"], 0),                                                 # 80⁄8
            ("Какая из этих величин является векторной?",
             ["работа", "импульс", "мощность", "температура"], 1),
        ],
        "en": [
            ("A car accelerates uniformly from rest at 2 m/s² for 5 s. What distance does it travel?",
             ["25 m", "10 m", "5 m", "50 m"], 0),
            ("A 2.0 kg object is dropped from rest from a height of 5.0 m (g = 9.81 m/s², ignore air resistance). What is its speed just before it lands?",
             ["5.0 m/s", "49 m/s", "9.9 m/s", "98 m/s"], 2),
            ("A mass on a spring oscillates with period T. The mass is increased by a factor of 4. What is the new period?",
             ["T/2", "T", "4T", "2T"], 3),
            ("A radioactive isotope has a half-life of 6 h. How much of an 80 g sample remains undecayed after 18 h?",
             ["40 g", "20 g", "10 g", "5 g"], 2),
            ("Which of these quantities is a vector?",
             ["energy", "power", "momentum", "work"], 2),
        ],
    },
    # ── AP Physics (1, 2, C) ───────────────────────────────────────────────
    "ap-physics": {
        "ru": [
            ("Грузовик сталкивается с лёгким автомобилем. Как соотносятся модули сил, с которыми они действуют друг на друга во время столкновения?",
             ["сила на автомобиль больше", "сила на грузовик больше", "силы равны по модулю", "зависит от скоростей до удара"], 2),  # 3-й закон
            ("Скорость тела массой 2 кг изменилась с 3 м/с до 5 м/с. Какую работу совершила равнодействующая сила?",
             ["4 Дж", "16 Дж", "8 Дж", "34 Дж"], 1),                                             # ½·2·(25−9)=16
            ("Тележка массой 2 кг движется со скоростью 3 м/с и сталкивается с неподвижной тележкой массой 1 кг; после удара тележки сцепляются. Какова их общая скорость?",
             ["1 м/с", "1,5 м/с", "2 м/с", "3 м/с"], 2),                                          # 2·3/(2+1)=2
            ("Шарик на нити движется по горизонтальной окружности с постоянной по модулю скоростью. Куда направлена равнодействующая сил на шарик?",
             ["по касательной к окружности", "от центра", "вдоль нити к центру окружности", "равнодействующая равна нулю"], 2),
            ("Груз на пружине совершает гармонические колебания. Массу груза увеличили в 4 раза, пружина прежняя. Как изменился период колебаний?",
             ["не изменился", "уменьшился в 2 раза", "вырос в 2 раза", "вырос в 4 раза"], 2),    # T=2π√(m/k)~√m
        ],
        "en": [
            ("A truck collides with a small car. How do the magnitudes of the forces they exert on each other during the collision compare?",
             ["the force on the car is greater", "the forces are equal in magnitude", "the force on the truck is greater", "it depends on the speeds before impact"], 1),
            ("A 2 kg object speeds up from 3 m/s to 5 m/s. How much work does the net force do?",
             ["4 J", "8 J", "34 J", "16 J"], 3),
            ("A 2 kg cart moving at 3 m/s collides with a stationary 1 kg cart and the carts stick together. What is their common speed after the collision?",
             ["2 m/s", "1 m/s", "3 m/s", "1.5 m/s"], 0),                                         # 2·3/(2+1)=2
            ("A ball on a string moves in a horizontal circle at constant speed. What is the direction of the net force on the ball?",
             ["toward the centre of the circle", "tangent to the circle", "away from the centre", "the net force is zero"], 0),
            ("A mass on a spring undergoes simple harmonic motion. The mass is increased by a factor of 4 with the same spring. What happens to the period?",
             ["it doubles", "it stays the same", "it quadruples", "it is halved"], 0),           # T=2π√(m/k)~√m
        ],
    },
    # ── A-level Physics (Edexcel 9PH0) ─────────────────────────────────────
    "alevel-physics": {
        "ru": [
            ("Сила 4 Н перемещает тело на 3 м; угол между силой и перемещением 60°. Какую работу совершает сила?",
             ["3 Дж", "6 Дж", "10,4 Дж", "12 Дж"], 1),                                            # 4·3·0,5=6
            ("Что численно равно площади под графиком зависимости скорости от времени?",
             ["ускорению", "перемещению", "силе", "импульсу силы"], 1),
            ("Струна длиной L закреплена на обоих концах. Чему равна длина волны основной моды стоячей волны?",
             ["L/2", "L", "2L", "4L"], 2),
            ("Конденсатор ёмкостью 200 мкФ заряжен до 10 В. Какая энергия в нём запасена?",
             ["1 мДж", "20 мДж", "2 Дж", "10 мДж"], 3),                                           # ½·200e−6·100=0,01 Дж
            ("Тележка массой 2 кг со скоростью 3 м/с сталкивается с неподвижной тележкой массой 1 кг, и они сцепляются. Какова их общая скорость?",
             ["2 м/с", "3 м/с", "1 м/с", "1,5 м/с"], 0),                                          # 6⁄3=2
        ],
    },
    # ── Олимпиадная физика ─────────────────────────────────────────────────
    "olympiad-physics": {
        "ru": [
            ("Скорость катера относительно воды 5 м/с, скорость течения 3 м/с, ширина реки 100 м. За какое минимальное время катер может пересечь реку?",
             ["12,5 с", "20 с", "25 с", "50 с"], 1),                                              # 100⁄5
            ("Кусок льда плавает в стакане с водой. Как изменится уровень воды, когда лёд полностью растает?",
             ["повысится", "понизится", "не изменится", "зависит от температуры воды"], 2),
            ("Путник половину пути прошёл со скоростью 30 км/ч, вторую половину — со скоростью 60 км/ч. Чему равна средняя скорость на всём пути?",
             ["45 км/ч", "50 км/ч", "42 км/ч", "40 км/ч"], 3),                                    # 2·30·60⁄90=40
            ("Тело брошено под углом 45° к горизонту со скоростью 10 м/с, g = 10 м/с², сопротивлением пренебречь. Какова дальность полёта по горизонтали?",
             ["10 м", "5 м", "20 м", "7 м"], 0),                                                  # v²sin90/g=10
            ("Как период малых колебаний математического маятника зависит от длины l и ускорения свободного падения g (по соображениям размерности и закону маятника)?",
             ["пропорционален l/g", "пропорционален √(l/g)", "пропорционален √(g/l)", "пропорционален l·g"], 1),
        ],
    },
    # ── общий набор для страницы-профиля (все программы) ───────────────────
    "physics-general": {
        "en": [
            ("A 10 N net force acts on a 5 kg body. What is its acceleration?",
             ["50 m/s²", "0.5 m/s²", "2 m/s²", "15 m/s²"], 2),
            ("What is the kinetic energy of a 2 kg body moving at 3 m/s?",
             ["9 J", "6 J", "18 J", "3 J"], 0),
            ("A 12 V supply is connected across a 4 ohm resistor. What current flows?",
             ["48 A", "3 A", "8 A", "0.33 A"], 1),
            ("Sound travels at 340 m/s. What is the wavelength of a 170 Hz tone?",
             ["0.5 m", "170 m", "2 m", "510 m"], 2),
            ("A piece of ice floats in a glass of water. What happens to the water level when the ice melts completely?",
             ["it rises", "it falls", "it depends on the temperature", "it stays the same"], 3),
        ],
    },
    # ── IB Mathematics: Analysis and Approaches ────────────────────────────
    "ib-math": {
        "ru": [
            ("Решите уравнение 2^x = 32.",
             ["x = 4", "x = 5", "x = 16", "x = 6"], 1),
            ("Найдите f'(2) для f(x) = x³ − 3x.",
             ["6", "12", "9", "3"], 2),                                                           # 3x²−3 → 9
            ("Упростите ln 8 − ln 2.",
             ["ln 6", "ln 4", "ln 16", "3 ln 2 − 2"], 1),                                         # ln4
            ("Найдите сумму бесконечной геометрической прогрессии с первым членом 6 и знаменателем 1⁄3.",
             ["9", "18", "8", "расходится"], 0),                                                  # 6/(1−1⁄3)=9
            ("Векторы a = (1, 2, 3) и b = (4, −5, 2). Что верно?",
             ["они параллельны", "угол между ними острый", "они перпендикулярны", "угол между ними тупой"], 2),  # 4−10+6=0
        ],
        "en": [
            ("Solve 2^x = 32.",
             ["x = 5", "x = 4", "x = 16", "x = 6"], 0),
            ("Find f'(2) for f(x) = x³ − 3x.",
             ["6", "9", "12", "3"], 1),
            ("Simplify ln 8 − ln 2.",
             ["ln 6", "ln 16", "ln 4", "3 ln 2 − 2"], 2),
            ("Find the sum to infinity of a geometric series with first term 6 and common ratio 1⁄3.",
             ["18", "8", "it diverges", "9"], 3),
            ("Vectors a = (1, 2, 3) and b = (4, −5, 2). Which statement is true?",
             ["they are perpendicular", "they are parallel", "the angle between them is acute", "the angle between them is obtuse"], 0),
        ],
    },
    # ── AP Calculus AB/BC ──────────────────────────────────────────────────
    "ap-calc": {
        "ru": [
            ("Найдите производную функции f(x) = x² sin x.",
             ["2x cos x", "2x sin x + x² cos x", "x² cos x", "2x sin x − x² cos x"], 1),
            ("Чему равен предел sin(3x)/x при x → 0?",
             ["0", "1", "не существует", "3"], 3),
            ("Вычислите интеграл от 1 до e от (1/x) dx.",
             ["1", "e", "e − 1", "0"], 0),
            ("В какой точке функция f(x) = x² − 4x + 5 достигает минимума?",
             ["x = −2", "x = 0", "x = 2", "x = 4"], 2),                                          # f'=2x−4=0
            ("Радиус круга растёт со скоростью 2 см/с. С какой скоростью растёт площадь круга в момент, когда r = 3 см?",
             ["6π см²/с", "18π см²/с", "36π см²/с", "12π см²/с"], 3),                              # 2πr·r'=12π
        ],
        "en": [
            ("Find the derivative of f(x) = x² sin x.",
             ["2x cos x", "x² cos x", "2x sin x + x² cos x", "2x sin x − x² cos x"], 2),
            ("What is the limit of sin(3x)/x as x → 0?",
             ["3", "1", "0", "it does not exist"], 0),
            ("Evaluate the integral from 1 to e of (1/x) dx.",
             ["e", "e − 1", "0", "1"], 3),
            ("At which x does f(x) = x² − 4x + 5 attain its minimum?",
             ["x = 4", "x = 2", "x = 0", "x = −2"], 1),                                          # f'=2x−4=0
            ("The radius of a circle grows at 2 cm/s. How fast is the area growing when r = 3 cm?",
             ["6π cm²/s", "12π cm²/s", "18π cm²/s", "36π cm²/s"], 1),
        ],
    },
    # ── IGCSE Mathematics 0580 ─────────────────────────────────────────────
    "igcse-math": {
        "ru": [
            ("Решите уравнение 3x + 5 = 20.",
             ["x = 5", "x = 25⁄3", "x = 15", "x = 8"], 0),
            ("Раскройте скобки: (x + 3)(x − 3).",
             ["x² + 9", "x² − 6x − 9", "x² − 9", "x² + 6x − 9"], 2),
            ("Цена 80 снижена на 25%. Какой стала цена?",
             ["55", "60", "20", "65"], 1),                                                        # 60
            ("Катеты прямоугольного треугольника равны 6 и 8. Чему равна гипотенуза?",
             ["14", "48", "7", "10"], 3),
            ("В мешке 3 красных и 2 синих шара. Наугад достают один шар. Какова вероятность, что он красный?",
             ["3⁄5", "3⁄2", "2⁄5", "1⁄3"], 0),
        ],
        "en": [
            ("Solve 3x + 5 = 20.",
             ["x = 25⁄3", "x = 5", "x = 15", "x = 8"], 1),
            ("Expand (x + 3)(x − 3).",
             ["x² + 9", "x² − 6x − 9", "x² + 6x − 9", "x² − 9"], 3),
            ("A price of 80 is reduced by 25%. What is the new price?",
             ["55", "20", "60", "65"], 2),
            ("The two shorter sides of a right-angled triangle are 6 and 8. What is the length of the hypotenuse?",
             ["10", "14", "48", "7"], 0),
            ("A bag holds 3 red and 2 blue balls. One ball is taken at random. What is the probability that it is red?",
             ["3⁄2", "2⁄5", "3⁄5", "1⁄3"], 2),
        ],
    },
    # ── ЕГЭ математика (профиль) ───────────────────────────────────────────
    "ege-math": {
        "ru": [
            ("Найдите значение выражения log₂ 32 + log₃ 9.",
             ["5", "6", "11", "7"], 3),
            ("Найдите значение производной функции f(x) = x³ − 6x в точке x = 2.",
             ["6", "2", "12", "0"], 0),
            ("Симметричную монету бросают три раза. Какова вероятность, что орёл выпадет ровно два раза?",
             ["1⁄4", "3⁄8", "1⁄2", "1⁄8"], 1),
            ("Известно, что sin x = 0,6. Найдите cos 2x.",
             ["0,64", "0,8", "0,28", "−0,28"], 2),                                                # 1−2·0,36
            ("Диагональ куба равна 2√3. Найдите объём куба.",
             ["4", "12", "24", "8"], 3),                                                          # a=2
        ],
    },
}

# slug страницы-ответа → ключ набора (явно и детерминированно; язык берётся у страницы)
# ── Страницы n=411–414 (24.11.2026): вопросы по содержанию курса, решаются без внешних данных ──
SETS["ap-calc-ab"] = {"ru": [
    ("Чему равна производная функции f(x) = x³ − 4x в точке x = 2?",
     ["0", "4", "8", "12"], 2),                                                       # 3x²−4 = 8
    ("Чему равен предел (sin 3x)⁄x при x, стремящемся к 0?",
     ["0", "1", "3", "не существует"], 2),                                            # 3
    ("Чему равен определённый интеграл от 2x dx на отрезке от 0 до 3?",
     ["9", "6", "3", "18"], 0),                                                       # x² от 0 до 3 = 9
    ("Какой экстремум имеет функция f(x) = x³ − 3x в точке x = −1?",
     ["локальный минимум", "локальный максимум", "точку перегиба", "экстремума нет"], 1),   # f'=0, f''=−6<0
    ("Чему равна производная функции y = e^(2x)?",
     ["e^(2x)", "2x·e^(2x)", "2e^(2x)", "e^(2x)⁄2"], 2),
]}
SETS["ap-statistics"] = {"ru": [
    ("Чему равно среднее арифметическое набора 2, 4, 4, 6, 9?",
     ["4", "5", "6", "25"], 1),                                                       # 25 : 5
    ("Набор 3, 5, 7, 9, 100. Чему равна медиана?",
     ["7", "24,8", "9", "100"], 0),
    ("События A и B независимы, P(A) = 0,5, P(B) = 0,4. Чему равна вероятность того, что произойдут оба события?",
     ["0,9", "0,1", "0,2", "0,45"], 2),                                               # 0,2
    ("Коэффициент корреляции равен −0,9. Что это означает?",
     ["сильную отрицательную линейную связь", "слабую положительную связь", "отсутствие связи", "ошибку: он не бывает отрицательным"], 0),
    ("Как изменится стандартная ошибка выборочного среднего, если объём выборки вырастет в 4 раза (прочее неизменно)?",
     ["вырастет в 2 раза", "уменьшится в 4 раза", "уменьшится в 2 раза", "не изменится"], 2),   # σ⁄√n
]}
SETS["oge-physics"] = {"ru": [
    ("Тело движется равномерно со скоростью 5 м/с. Какой путь оно пройдёт за 12 с?",
     ["60 м", "2,4 м", "17 м", "120 м"], 0),
    ("Сила тока в проводнике 2 А, напряжение на нём 12 В. Чему равно сопротивление проводника?",
     ["24 Ом", "6 Ом", "10 Ом", "0,17 Ом"], 1),
    ("Сколько теплоты нужно, чтобы нагреть 2 кг воды на 10 °C? Удельная теплоёмкость воды 4200 Дж/(кг·°C).",
     ["8,4 кДж", "42 кДж", "84 кДж", "840 кДж"], 2),                                  # 2·4200·10
    ("Сила 100 Н действует перпендикулярно поверхности площадью 0,5 м². Чему равно давление?",
     ["50 Па", "200 Па", "100,5 Па", "20 Па"], 1),
    ("Какую минимальную работу нужно совершить, чтобы равномерно поднять груз массой 3 кг на высоту 2 м? Примите g = 10 м/с².",
     ["6 Дж", "15 Дж", "60 Дж", "30 Дж"], 2),                                         # mgh
]}
SETS["gcse-physics"] = {"ru": [
    ("Тело массой 4 кг движется с ускорением 3 м/с². Чему равна равнодействующая сила?",
     ["7 Н", "12 Н", "1,33 Н", "0,75 Н"], 1),
    ("Чему равна кинетическая энергия тела массой 2 кг при скорости 3 м/с?",
     ["6 Дж", "12 Дж", "9 Дж", "18 Дж"], 2),                                          # mv²⁄2
    ("Какой заряд проходит по цепи за 5 с при силе тока 3 А?",
     ["15 Кл", "8 Кл", "0,6 Кл", "1,67 Кл"], 0),
    ("Длина волны 0,5 м, частота 40 Гц. Чему равна скорость волны?",
     ["80 м/с", "20 м/с", "0,0125 м/с", "40,5 м/с"], 1),
    ("Ядро атома содержит 6 протонов и 8 нейтронов. Чему равно его массовое число?",
     ["6", "8", "14", "2"], 2),
]}

DIAG_SET_BY_SLUG = {
    # ЕГЭ физика
    "repetitor-fizika-ege-online": "ege-physics", "repetitor-fizika-ege-msu": "ege-physics",
    "podgotovka-ege-fizika-za-rubezhom": "ege-physics", "podgotovka-ege-fizika-2027-plan-po-mesyacam": "ege-physics",
    "russian-ege-physics-tutor-english-speaking": "ege-physics", "ege-physics-tutor-online": "ege-physics",
    "ege-physics-tutor-msu": "ege-physics", "ege-physics-preparation-abroad-online": "ege-physics",
    # IGCSE physics (страница 406 — физика + математика; набор по физике, математика — отдельный набор igcse-math)
    "repetitor-igcse-fizika-0625-na-russkom": "igcse-physics", "igcse-physics-0625-tutor-russian-speaking": "igcse-physics",
    "igcse-physics-0625-tutor-russian": "igcse-physics", "podgotovka-igcse-fizika-matematika-onlajn": "igcse-physics",
    # IB physics
    "repetitor-ib-physics-russkoyazychnyj": "ib-physics", "ib-physics-hl-tutor-online": "ib-physics",
    "ib-physics-tutor-russian-speaking": "ib-physics", "ib-physics-hl-ili-sl-chto-vybrat": "ib-physics",
    "ib-physics-hl-vs-sl-which-to-take": "ib-physics", "how-to-choose-ib-physics-hl-tutor": "ib-physics",
    # A-level (+IB) physics, русская страница
    "podgotovka-a-level-ib-fizika-onlajn": "alevel-physics",
    # AP physics
    "repetitor-ap-physics-na-russkom": "ap-physics", "ap-physics-1-tutor-online": "ap-physics",
    "ap-physics-tutor-russian-speaking": "ap-physics", "ap-physics-1-2-c-chem-otlichayutsya": "ap-physics",
    "ap-physics-1-vs-2-vs-c-which-to-take": "ap-physics", "how-to-choose-ap-physics-1-tutor": "ap-physics",
    "ap-physics-calculus-onlajn-programma-grafik-mayskie-ekzameny": "ap-physics",
    # UCAS/Oxford/Cambridge: ближайший набор — A-level/IB физика
    "podgotovka-fizika-zarubezhnye-vuzy-ucas-oxford-cambridge-onlajn": "alevel-physics",
    # олимпиадная
    "olimpiadnaya-fizika-podgotovka-tehnicheskie-vuzy-onlajn": "olympiad-physics",
    # страница-профиль репетитора
    "vladimir-podlevskikh-physics-tutor": "physics-general",
    # математика
    "repetitor-ib-math-aa-online-russkoyazychnyj": "ib-math", "best-ib-math-aa-hl-tutor-online": "ib-math",
    "repetitor-ap-calculus-na-russkom": "ap-calc", "best-ap-calculus-bc-tutor-online": "ap-calc",
    "repetitor-igcse-matematika-0580-na-russkom": "igcse-math", "igcse-maths-0580-tutor-russian-speaking": "igcse-math",
    "podgotovka-ege-matematika-profil-2027-plan": "ege-math",
    # страницы n=411-414 (24.11.2026)
    "ap-calculus-ab-tutor-online": "ap-calc-ab", "ap-statistics-tutor-online": "ap-statistics",
    "oge-fizika-podgotovka-onlajn": "oge-physics", "gcse-physics-aqa-8463-tutor-online": "gcse-physics",
}

N_QUESTIONS = 5


def diag_set(slug, lang):
    """(ключ набора, список вопросов) для страницы или None, если страница не покрыта."""
    key = DIAG_SET_BY_SLUG.get(slug)
    if key is None:
        return None
    return key, SETS[key][lang]
