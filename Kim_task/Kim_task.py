from random import randint
from random import uniform
import math
from functions import *


def task_1():
    quantity_stud = randint(15, 25)
    answer = "1. \n"
    text = f"1. Студенты трех групп (по {int(quantity_stud)} человек в каждой) выбирают трех человек для участия в профсоюзной конференции: руководителя делегации, докладчика и содокладчика." \
           "Какова вероятность того, что:\n"
    text += "a) для этого будут выбраны старосты первой, второй и третьей групп соответственно\n"
    otvet1 = (1 / (quantity_stud ** 3))
    answer += f"a) {otvet1}\n"
    text += f"б) докладчиком и содокладчиком будут выбраны старосты?\n"
    otvet2 = (1 / (quantity_stud ** 2))
    answer += f"б) {otvet2}\n"
    return text, answer


def task_2():
    whole = randint(5, 13) * 5
    rus = int(whole / 5 + 10)
    france = int(whole / 5)
    sur = whole - rus - france
    choice0 = int(whole / (randint(2, 4)))
    choice1 = choice0 - (randint(1, 3))
    choice2 = choice1 - 1
    answer = "2. \n"
    text = f"2. В Зеленом зале художественного салона развешаны картины: {int(rus)} натюрмортов русских художников, {int(france)} полотен французских импрессионистов и {int(sur)} картины представителей сюрреализма." \
           f"Воры в темноте наугад снимают {choice0} картин. Какова вероятность того, что среди этих картин:\n"
    text += f"а) {choice1}  натюрморта\n"
    answer += f"а) {combination(rus, choice1)}/{combination(whole, choice0)}\n"
    text += f"б) по {choice2} картины импрессионистов и сюрреалистов\n"
    answer += f"б) {(combination(france, choice2) / combination(whole, choice0)) * (combination(sur, choice2) / combination(whole, choice0))}\n"
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
    a1 = (combination(3, 3) * (water2 ** 3) * ((1 - water2) ** 0))
    a2 = (combination(3, 2) * water1 * (1 - water1) * (water2 ** 2) * (1 - water2))
    answer += f"{a1 + a2}\n"
    return text, answer


def task_6():
    text = "6. На семи карточках написаны буквы А, Л, Н, П, Т, Ю, Б. Карточки тщательно перемешивают, " \
           "затем берут по одной и кладут последовательно рядом. Какова вероятность того, что получится слово «ТЮЛЬПАН»?"
    a = (1 / (7 ** 7))
    answer = "6. \n" \
             f"{round(a, 6)}\n"
    return text, answer


def task_7():
    rab = randint(2, 5) / 10
    bez = rab / 4
    kom = 1 - rab - bez
    rabv = randint(6, 8) / 10
    bezv = rabv / 1.5
    komv = 1 - rabv - bezv
    answer = "7. \n"
    text = f"7. В один из кризисных годов {rab * 10}% выпускников одной из групп университета путей сообщения устроились работать по специальности, " \
           f" {bez * 10} не нашли работу и {kom * 10} занялись коммерцией. Вероятность того, что выпускник, работающий по специальности, " \
           f"ближайшее лето проведет на курорте Боровое, равна {rabv}, для неработающего выпуск- ника эта вероятность составляет {bezv}, " \
           f"для коммерсанта - {komv}. Первый позвонивший вам выпускник этой группы с горечью сообщил, что лето вынужден провести на Канарских островах." \
           "Какова вероятность, что он работает по спе- циальности?\n"
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
        answer += f"{round(max_probability,4)} Furman\n"
    elif max_probability == p_stay_Mokin:
        answer += f"{round(max_probability,4)} Mokin\n"
    else:
        answer += f"{round(max_probability,4)} Sitnikov\n"
    return text, answer
