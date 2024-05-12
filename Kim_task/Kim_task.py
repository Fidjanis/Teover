from random import randint
from random import uniform
import math
from functions import *


def task_1():
    quantity_stud = randint(10, 20)
    answer = "1. \n"
    print(quantity_stud)
    text = f"1. Студенты трех групп (по {int(quantity_stud)} человек в каждой) выбирают трех человек для участия в профсоюзной конференции: руководителя делегации, докладчика и содокладчика." \
           "Какова вероятность того, что:\n"
    text += "a) для этого будут выбраны старосты первой, второй и третьей групп соответственно\n"
    otvet1 = (1 / (quantity_stud ** 3))
    answer += f"a) {otvet1}\n"
    text += f"б) докладчиком и содокладчиком будут выбраны старосты?\n"
    otvet2 = (1 / (quantity_stud ** 2))
    answer += f"б) {otvet2}\n"
    return text, answer


def task_2():  #хз что с этим делать
    whole = randint(5, 13) * 5
    rus = int(whole / 5 + 5)
    france = int(whole / 6)
    sur = whole - rus - france
    print(rus, france, sur, whole)
    choice0 = (randint(6, rus - 2))
    choice1 = choice0 - randint(1, choice0 - 4)
    choice2 = int(choice0 / 2)
    print(choice0, choice1, choice2)
    answer = "2. \n"
    text = f"2. В Зеленом зале художественного салона развешаны картины: {int(rus)} натюрмортов русских художников, {int(france)} полотен французских импрессионистов и {int(sur)} картины представителей сюрреализма." \
           f"Воры в темноте наугад снимают {choice0} картин. Какова вероятность того, что среди этих картин:\n"
    text += f"а) {choice1}  натюрморта\n"
    answer += f"а) {round(combination(rus, choice1)[1] / combination(whole, choice0)[1], 12)}\n"
    text += f"б) по {choice2} картины импрессионистов и сюрреалистов\n"
    answer += f"б) {round((combination(france, choice2)[1] / combination(whole, choice0)[1]) * (combination(sur, choice2)[1] / combination(whole, choice0)[1]), 12)}\n"
    return text, answer


def task_3():
    text = "3.Пусть X - число очков, выпавших на верхней грани игральной кости при однократном подбрасывании." \
           "События: А - Х кратно трем; В - Х нечетно; D - Х кратно двум; Е - Х дробно; Н - Х больше шести. " \
           "Постройте множество элементарных исходов и выявите состав подмно- жеств, соответствующих событиям: \n" \
           "А) B;\n " \
           "Б) E ∪ D\n" \
           "B) A ∩ B \n" \
           "Г) E ∩ H\n"
    answer = "3. \n" \
             "А) B={1,3,5} \n" \
             "Б) E ∪ D = {2,4,6}\n" \
             "В) A ∩ B = {3}\n" \
             "Г) E ∩ H = Ø\n"
    return text, answer


def task_4():
    melon = randint(6, 9) / 10
    cream = randint(4, 7) / 10
    answer = "4. \n"
    text = f"4.Кошка Фуша выбирает из предложенных ей продук- тов сметану с вероятностью 0,7, дыню - с вероятностью 0,95." \
           "Какова вероятность того, что сегодня: \n"
    text += " a) кошка Фуша выберет только дыню;\n"
    a1 = (melon * (1 - cream))
    answer += f"a) {round(a1, 4)}\n"
    text += "б) не выберет ни дыню, ни сметану;\n"
    a2 = ((1 - melon) * (1 - cream))
    answer += f"б) {round(a2, 4)}\n"
    text += "c) выберет либо дыню, либо сметану?\n"
    a3 = (melon + cream) - (melon * cream)
    answer += f"c) {round(a3, 4)}\n"
    return text, answer


def task_5():
    water1 = randint(6, 9) / 10
    water2 = randint(5, 8) / 10
    answer = "5. \n"
    text = f"5. Иван Иванович покупает бутылку минеральной воды «Карачинская» с вероятностью {water1}, а «Омская-1» - с вероятностью {water2}." \
           "Сегодня он купил 3 бутылки минеральной воды. Какова вероятность, что «Омской-1» он купил больше, чем «Карачинской»?\n"
    a1 = (pow(water2, 3))
    a2 = (combination(3, 2)[1] * water1 * (1 - water1) * (water2 ** 2) * (1 - water2))
    answer += f"{round(a1 + a2, 6)}\n"
    return text, answer


def task_6():
    words = ['ТЮЛЬПАН', 'АКУЛА', 'ЮРА', 'СУДЬБА', 'ЁЖИК']
    choice = randint(0, 4)
    text = f"6. На семи карточках написаны буквы "
    for j in range(0, len(words[choice])):
        text += f"{words[choice][j]}"
        if j != len(words[choice]) and j != len(words[choice]) - 1:
            text += ", "
    text += f". Карточки тщательно перемешивают, затем берут по одной и кладут последовательно рядом. Какова вероятность того, что получится слово «{words[choice]}»?\n"
    a = (1 / (choice ** choice))
    answer = "6. \n" \
             f"{round(1 / math.factorial(len(words[choice])), 5)}\n"
    return text, answer


def task_7():
    rab = randint(2, 4) / 10
    bez = rab / 4
    kom = 1 - rab - bez
    rabv = randint(4, 7) / 10
    bezv = round(randint(3, 5) / 10, 2)
    komv = round(randint(1, 4) / 10, 2)
    answer = "7. \n"
    text = f"7. В один из кризисных годов {rab * 100}% выпускников одной из групп университета путей сообщения устроились работать по специальности, " \
           f" {bez * 100}% не нашли работу и {kom * 100}% занялись коммерцией. Вероятность того, что выпускник, работающий по специальности, " \
           f"ближайшее лето проведет на курорте Боровое, равна {rabv}, для неработающего выпускника эта вероятность составляет {bezv}, " \
           f"для коммерсанта - {komv}. Первый позвонивший вам выпускник этой группы с горечью сообщил, что лето вынужден провести на Канарских островах." \
           "Какова вероятность, что он работает по специальности?\n"
    a1 = ((rabv * rab) + (bezv * bez) + (komv * kom))
    a2 = ((rabv * rab) / a1)
    answer += f"{round(a2, 4)}\n"
    return text, answer


def task_8():
    # Вероятности сидеть рядом с каждым из студентов
    p_Furman = randint(3, 6) / 10
    p_Mokin = p_Furman / 1.5
    p_Sitnikov = 1 - p_Mokin - p_Furman
    answer = "8. \n"
    # Вероятности быть выгнанным доцентом Заблоцкой в зависимости от того, с кем сидел Щукин
    p_expulsion_Furman = randint(4, 7) / 10
    p_expulsion_Mokin = p_expulsion_Furman / 5
    p_expulsion_Sitnikov = 1 - p_expulsion_Mokin - p_expulsion_Furman
    text = f"8.На лекции по математике студент Щукин с вероятностью {p_Furman} садится рядом с Фурманом," \
           f"с вероятностью {p_Mokin} - с Мокиным, с вероятностью {p_Sitnikov} - с Ситниковым." \
           f"В первом случае вероятность того, что доцент Заблоцкая выгонит Щукина с лекции, равна {p_expulsion_Furman}," \
           f"во втором случае - {p_expulsion_Mokin}, в третьем - {p_expulsion_Sitnikov}. Сегодня студент Щукин дослушал лекцию до конца. С кем рядом вероятнее всего он сидел?\n"
    # Рассчитаем общие вероятности быть выгнанным для каждого из студентов
    p_expulsion = p_Furman * p_expulsion_Furman + p_Mokin * p_expulsion_Mokin + p_Sitnikov * p_expulsion_Sitnikov

    # Вероятность, что Щукин досидит лекцию до конца
    p_stay = 1 - p_expulsion

    # Найдем вероятность сидеть рядом с каждым студентом, учитывая, что Щукин досидел лекцию
    p_stay_Furman = p_Furman * p_expulsion_Furman / p_stay
    p_stay_Mokin = p_Mokin * p_expulsion_Mokin / p_stay
    p_stay_Sitnikov = p_Sitnikov * p_expulsion_Sitnikov / p_stay

    # Определим с кем вероятнее всего Щукин сидел
    max_probability = max(p_stay_Furman, p_stay_Mokin, p_stay_Sitnikov)
    if max_probability == p_stay_Furman:
        answer += f"{round(max_probability, 4)} Furman\n"
    elif max_probability == p_stay_Mokin:
        answer += f"{round(max_probability, 4)} Mokin\n"
    else:
        answer += f"{round(max_probability, 4)} Sitnikov\n"
    return text, answer


def task_9():
    n = randint(5, 10)
    falshivka = randint(2, 12)
    proknulo = randint(2, 4)
    text = f"Пара одинаковых игральных костей бросается {int(n)} раз." \
           f"Какова вероятность того, что сумма очков, выпавших на обеих костях, равная {int(falshivka)}, повторится {int(proknulo)}?\n"
    a = (combination(n, proknulo)[1] * ((1 / 36) ** proknulo) * ((35 / 36) ** (n - proknulo)))
    answer = "9. \n"
    answer += f"{round(a, 6)}\n"
    return text, answer


def task_10():
    answer = "10. \n"
    n = randint(100, 150)
    p = randint(5, 9) / 10
    k = randint(50, 70)
    skail = randint(10, 20)
    text = f"Имеется {int(n)} станков, работающих независимо друг от друга." \
           f"Каждый из них включен в течение {p} рабочего времени. Какова вероятность того, что в произвольный момент окажутся включенными:" \
           f"a) {k} станков; б) от {k} до {k + skail} станков?\n"
    x = (k - n * p) / (n * p * (1 - p))
    y = (k + skail - n * p) / (n * p * (1 - p))
    otvet = local_lapl(x)
    answer += f'a) {otvet}\n'
    answer += f'б) {round(integr_lapl(round(y, 2)) - integr_lapl(round(x, 2)), 5)}\n'
    return text, answer


def task_11():
    answer = "11. \n"
    n = randint(1000, 2000)
    p = randint(1, 9) / 1000
    k = randint(1, 10)
    text = f"Радиоаппаратура состоит из {n} электроэлементов. Вероятность отказа одного элемента в течение одного года " \
           f"работы равна {p} и не зависит от состояния других элементов. Какова вероятность отказа не менее {k} электроэлементов за год?\n"
    lam = n * p
    a = (lam ** k) / (math.factorial(k)) * math.exp(-lam)
    answer += f"{round(a, 4)}\n"
    return text, answer


def task_12():
    answer = "12. \n"
    p1 = randint(70, 95) / 100
    p2 = randint(70, 95) / 100
    text = f"Каждые сутки со станции отправляются по два скорых поезда. Вероятность своевременного прибытия их " \
           f"на конечный пункт составляет соответственно {p1} и {p2}. Составить ряд распределения числа поездов, " \
           "которые прибудут в пункт назначения без опоздания. Найти M(X), D(X), G(X), F(X) этой случайной величины." \
           "Построить график F(X).\n"
    x0 = (1-p1)*(1-p2)
    x1 = ((1-p2)*p1)+((1-p1)*p2)
    x2 = p1*p2
    arr = {0: x0, 1: x1, 2: x2}
    m = discr_math_expectation(arr)
    d = discr_dispersion(arr)
    sig = math.sqrt(d)
    answer += "xi   |0|     |1|     |2|\n"
    answer += f"pi   |{round(x0, 3)}| |{round(x1, 3)}| |{round(x2, 3)}|\n"
    answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}, σ(X)={round(sig, 3)}\n"
    answer += f"F(x)= 0 при X<0\n"
    answer += f"F(x)= {round(x0, 3)} при 0<=X<1\n"
    answer += f"F(x)= {round(x1, 3)} при 1<=X<2\n"
    answer += f"F(x)= {round(x2, 3)} при 2<=X\n"
    return text, answer


def task_13():
    answer = "13. \n"
    n = randint(1, 3)
    p = randint(1, 6)/10
    text = f"Случайная величина Х - число попаданий мячом в корзину при {n} броске. "\
            f"Вероятность попадания равна {p}. Составить ряд распределения случайной величины Х. Найти M(X) и D(X).\n"
    if n == 1:
        x0 = 1-p
        x1 = p
        arr = {0: x0, 1: x1}
        m = discr_math_expectation(arr)
        d = discr_dispersion(arr)
        answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}\n"
    elif n == 2:
        x0 = (1-p)**n
        x1 = 2*((1-p)*p)
        x2 = p**2
        arr = {0: x0, 1: x1, 2: x2}
        m = discr_math_expectation(arr)
        d = discr_dispersion(arr)
        answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}\n"
    elif n == 3:
        x0 = round((1-p)**3,3)
        x1 = round(3*(((1-p)**2)*p),3)
        x2 = round(3*((pow(p, 2))*(1-p)),3)
        x3 = round(p**3,3)
        arr = {0: x0, 1: x1, 2: x2, 3: x3}
        m = discr_math_expectation(arr)
        d = discr_dispersion(arr)
        answer += f"M(X)={round(m, 3)}, D(X)={round(d, 3)}\n"
    return text, answer


def task_14():
    answer = '13. \n'
    n = randint(100, 200)
    k = randint(1, 9) / 100
    text = f"Вероятность выпуска бракованного изделия равна {k}. "\
            f"Выпущено {n} изделий. Составить ряд распределения числа бракованных изделий. "\
            "Найти М(X) этой случайной величины.\n"
    answer += "Ряд распределения:\n"
    m = n * k
    arr = [0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 7):
        p = combination(n, i)[1] * k ** i * (1 - k) ** (n - i)
        arr[i] = p
    answer += "|0|     |1|     |2|     |3|     |4|     |5|     |6|      ...\n"
    for i in range(0, 7):
        answer += f"|{round(arr[i], 3)}| "
    answer += "    ...\n"
    answer += f"M(x)={round(m, 5)}\n"
    return text, answer


