# -*- coding: utf-8 -*-

"""
Функции, необходимые для работы над базой данных и проектом.

"""
import pandas as pd
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from math import isnan


def checkihgStringOrFloat(data):
    """
    Проверка параметра, полученного на вход, на строку или число с плавающей точкой.

    Параметры:
    data - параметр, который проверяется с помощью данной функции

    :return:
    float(data): параметр в виде числа с плавающей точкой, которое используется в дальнейшем.
    or
    str(data): параметр в виде строки, которое используется в дальнейшем.
    """
    try:
        return float(data)
    except ValueError:
        return str(data)


def checkingStringOrInt(data):
    """
    Проверка параметра, полученного на вход, на строку или целое число.
    Автор: Коленько А. С.

    Параметры:
    data - параметр, который проверяется с помощью данной функции

    :return:
    int(data): параметр в виде целого числа, которое используется в дальнейшем.
    or
    str(data): параметр в виде строки, которое используется в дальнейшем.
    """
    try:
        return int(data)
    except ValueError:
        return str(data)


def tochechniyGraph():
    """
    Создание точечного графика с помощью базы данных, полученной из файла ОтносительноеИзменениеРоста.csv,
    разделителем которого является ";"

    Параметры:

    :return:
    Точечный график "Процентное увеличение среднего роста мужчин по сравнению с женщинами за столетие" с осями:
            Ось абцисс и ординат: Увеличение среднего женского роста (в процентах)

    """
    dataBase = pd.read_csv('ОтносительноеИзменениеРоста.csv', delimiter=';')
    relativeChangeInHeight = np.array(dataBase)
    X = relativeChangeInHeight[0:, 1]
    Y = relativeChangeInHeight[0:, 2]
    b = mcolors.BASE_COLORS
    num_set = np.random.randint(1, len(mcolors.BASE_COLORS), len(X))
    col = [list(b.keys())[i] for i in num_set]

    X = relativeChangeInHeight[0:, 1]
    Y = relativeChangeInHeight[0:, 2]

    plt.title("Percentage increase in mean male vs. female height over a century")
    plt.scatter(X, Y, s=10, c=col, linewidths=0.2)
    plt.gca().set(xlim=(0, 15), ylim=(0, 15),
                  xlabel="Increase in mean female height (%)", ylabel='Increase in mean female height (%)')


def barAndPieGraph():
    """
    Получение двух графиков: столбчатый и круговой на основе таблиц: РостМужчинИЖенщин.csv и Код.csv
    Параметры:

    :return:
    Два графика:
    Столбчатый график "Средний рост на разных континентах" с осями:
            Ось абцисс: Континент
            Ось ординат: Средний рост на данном континенте
    Круговой график "Процент представителей с разных континентов" с осями:
            Ось абцисс: Континент
            Ось ординат: Процент прдеставителей
    """
    secondDataBase = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
    thirdDataBase = pd.read_csv('Код.csv', delimiter=';')

    CodeContinent = np.array(thirdDataBase)
    HeightManAndWoman = np.array(secondDataBase)

    codes = CodeContinent[0:, 0]
    continents = CodeContinent[0:, 2]
    manHeight = HeightManAndWoman[0:, 1]
    dictionary = dict()

    for continent in continents:
        dictionary[continent] = list()
    for code, height, continent in zip(codes, manHeight, continents):
        dictionary[continent].append(height)

    for i in dictionary:
        dictionary[i] = len(dictionary[i])
    clean_dict = {k: dictionary[k] for k in dictionary if type(k) == str}
    keys = clean_dict.keys()
    values = clean_dict.values()
    explode = (0.1, 0, 0.15, 0, 0.2, 0)

    fig, ax = plt.subplots()
    plt.bar(keys, values, color='g', width=0.5)
    fig.autofmt_xdate()
    plt.title("Mean height in different continents")
    plt.gca().set(xlabel='Continent', ylabel='Height')

    fig, ax = plt.subplots()
    explode = (0, 0.1, 0.1, 0, 0, 0)
    plt.title("Percentage of representatives from different continents ")
    ax.pie(values, labels=keys,
           autopct='%.3f%%',
           shadow=True,
           explode=explode,
           wedgeprops={'lw': 0.5, 'ls': '--', 'edgecolor': "k"},
           rotatelabels=False,
           )
    ax.axis("Equal")


def text_report_for_change_in_female_height(change_in_height_dataset_filename, country, filename,
                                            code_for_country_filename):
    """
    Функция получения базы данных и файла для определенной страны на основе данных об изменении роста среди женщин

    :param change_in_height_dataset_filename: Файл в формате .csv - изменение роста женщин, необходимый для получения первой базы данных
    :param country: Название страны, относительно которой получить данные об изменении роста
    :param filename: Название файла - Слияние двух БД, результат выполнения функции
    :param code_for_country_filename: Файл в формате .csv, необходимый получения кода страны для занесения в новую БД

    :return: Файл в формате .csv - Новая база данных, полученная на основе двух вышеописанных таблиц, превращенных в БД.
    """
    change_in_height_dataset = pd.read_csv(change_in_height_dataset_filename, delimiter=';')
    code_for_country = pd.read_csv(code_for_country_filename, delimiter=';')

    united_dataset = change_in_height_dataset.merge(code_for_country, index=False)

    selector = united_dataset['Entity'] == country
    change_in_female_height = united_dataset[selector].loc[:, ["Year", "Year-on-year change in female height (%)"]]

    return change_in_female_height.to_csv(filename)


text_report_for_change_in_female_height("ОтносительноеИзменениеРоста.csv", "Albania", "ChangeFemaleHeight.csv",
                                        "Код.csv")


def text_report_for_mean_male_height(mean_height_dataset_filename, country, filename, code_for_country_filename):
    """
    Функция получения базы данных и файла для определенной страны на основе данных об изменении роста среди мужчин

    :param mean_height_dataset_filename: Файл в формате .csv - изменение роста мужчин, необходимый для получения первой
     базы данных
    :param country: Название страны, относительно которой получить данные об изменении роста
    :param filename: Название файла - Слияние двух БД, результат выполнения функции
    :param code_for_country_filename:  Файл в формате .csv, необходимый получения кода страны для занесения в новую БД

    :return: Файл в формате .csv - Новая база данных, полученная на основе двух вышеописанных таблиц, превращенных в БД.
    """
    change_in_mean_height = pd.read_csv(mean_height_dataset_filename, delimiter=';')
    code_for_country = pd.read_csv(code_for_country_filename, delimiter=';')

    united_dataset = change_in_mean_height.merge(code_for_country)

    selector = united_dataset['Entity'] == country
    mean_male_height = united_dataset[selector].loc[:, ["Year", "Mean male height (cm)"]]

    return mean_male_height.to_csv(filename)


text_report_for_mean_male_height("РостМужчинИЖенщин.csv", "Albania", "MeanMaleHeight.csv", "Код.csv")


def text_report_for_human_devIndex(human_development_filename, code_for_country_filename, year, continent, filename):
    """
    Функция получения базы данных и файла для определенного континента на основе данных об изменении индекса развития
    континента
    :param human_development_filename: Файл в формате .csv - изменение индекса развития континента,
    необходимый для получения первой базы данных
    :param code_for_country_filename: Файл в формате .csv, необходимый получения кода страны для занесения в новую БД
    :param year: Аргумент необходимый для выбора определенного года, чтобы проанализировать изменение индекса развития
    на континенте
    :param continent: Континент, относительно которого составлять БД
    :param filename: Название файла - Слияние двух БД, результат выполнения функции

    :return: Файл в формате .csv - Новая база данных, полученная на основе двух вышеописанных таблиц, превращенных в БД.
    """
    human_devIndex = pd.read_csv(human_development_filename, delimiter=';')
    code_for_country = pd.read_csv(code_for_country_filename, delimiter=';')

    united_dataset = human_devIndex.merge(code_for_country)

    selector = united_dataset["Continent"] == continent & united_dataset["Year"] == year
    finale_dataset = united_dataset[selector].loc[:, ["Human Development Index (UNDP)", "Mean male height (cm)"]]

    return finale_dataset.to_csv(filename)


text_report_for_human_devIndex("HumanDev_new.csv", "Код.csv", 2002, "South America", "HumanDevWithHeight.csv")

human_devIndex = pd.read_csv("HumanDev_new.csv", delimiter=';')
code_for_country = pd.read_csv("Код.csv", delimiter=';')

united_dataset = human_devIndex.merge(code_for_country)

selector = (united_dataset["Continent"] == "South America") & (united_dataset["Year"] == 1991) & (
    ~united_dataset.isna())
finale_dataset = united_dataset[selector].loc[:, ["Human Development Index (UNDP)", "Mean male height (cm)"]]


def text_report_for_mean_height_alltime(childMort_rate_dataset, filename, continent, code_for_country_dataset):
    """
    Создание таблицы с помощью pivot_table для отображения среднего роста мужчин за все представленное
    время в определенной стране, распределенных по континентам

    :param childMort_rate_dataset: Файл в формате .csv - среднего роста мужчин за все представленное
    время в определенной стране
    :param filename: Название файла - Слияние двух БД, результат выполнения функции
    :param continent: Континент, относительно которого составлять БД
    :param code_for_country_dataset: Файл в формате .csv, необходимый получения кода страны для занесения в новую БД
    :return:
    Файл в формате .csv - Новая база данных, полученная на основе двух вышеописанных таблиц, превращенных в БД.
    """
    childMort_rate_per_mean_height = pd.read_csv(childMort_rate_dataset, delimiter=';')
    code_for_country = pd.read_csv(code_for_country_dataset, delimiter=';')

    united_dataset = childMort_rate_per_mean_height.merge(code_for_country)

    # Использование pivot_table

    text_table = pd.pivot_table(united_dataset, index='Entity', columns='Continent', values='Mean male height (cm)',
                                aggfunc='mean')
    return text_table.to_csv(filename)


text_report_for_mean_height_alltime("РостМужчинИЖенщин.csv", "MeanHeightPerCont.csv", "Frun", "Код.csv")
