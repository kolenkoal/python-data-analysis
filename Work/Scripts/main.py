# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:23:48 2022

@author: Alexander
"""
import csv
from tkinter import ttk
import os
from tkinter import *
from tkinter import messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.lines as mlines

os.chdir(r'../Data/')

"""
Класс, вызывающийся главной функцией, 
который содержит все функции, которые 
выполняются в программе
"""


class Window:
    """
        Главная функция класса, к которой обращаются все функции
        приложения и в который вызывается окно, устанавливается
        геометрия, задний фон, деление на вкладки, после чего
        устанавливаются определённые кнопки
    """

    def __init__(self):
        # Создание самого окна
        self.window = Tk()
        self.window.title("Исследование зависимости роста человека по странам")
        self.width = 1200
        self.height = 700
        self.background = '#F0F7E7'

        self.window.geometry(f'{self.getScreenWidth()}x{self.getScreenHeight()}')
        self.window.resizable(False, False)

        self.notebook = ttk.Notebook(self.window)
        self.notebook.place(x=0, y=0)

        self.frame1 = ttk.Frame(master=self.notebook, width=self.window.winfo_screenwidth(),
                                height=self.window.winfo_screenheight())
        self.frame1.pack(fill='both', expand=True)
        self.frame2 = ttk.Frame(master=self.notebook, width=self.window.winfo_screenwidth(),
                                height=self.window.winfo_screenheight())
        self.frame2.pack(fill='both', expand=True)
        self.frame3 = ttk.Frame(master=self.notebook, width=self.window.winfo_screenwidth(),
                                height=self.window.winfo_screenheight())
        self.frame3.pack(fill='both', expand=True)
        self.notebook.add(self.frame1, text="График")
        self.notebook.add(self.frame2, text='База Данных')
        self.notebook.add(self.frame3, text='Текстовый отчет')

        # self.icon = PhotoImage(file=r"C:\Users\Alexander\.spyder-py3\Python\icon.png")
        self.icon = PhotoImage(file=r'icon.png')
        self.window.iconphoto(False, self.icon)

        self.theFont = ("Book Antiqua", int(8 * self.coefficient1), "bold", "roman")

        self.exitButton = Button(master=self.frame1, text="ВЫХОД", font=self.theFont,
                                 command=self.window.destroy).place(
            x=40 * self.coefficient1,
            y=620 * self.coefficient2,
            width=129 * self.coefficient1,
            height=44 * self.coefficient2)
        self.countries = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola',
                          'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria',
                          'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
                          'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia',
                          'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria',
                          'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
                          'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
                          'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia' 'Cuba',
                          'Cyprus', 'Czechia', 'Democratic Republic of Congo', 'Denmark', 'Djibouti',
                          'Dominica', 'Dominican Republic', 'East Asia and Pacific',
                          'Europe and Central Asia', 'Latin America and Caribbean',
                          'Middle East and North Africa', 'North America', 'South Asia',
                          'Sub-Saharan Africa', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
                          'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France',
                          'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece',
                          'Greenland', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana',
                          'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia',
                          'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
                          'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia',
                          'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Lithuania', 'Luxembourg',
                          'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta',
                          'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
                          'Micronesia (country)', 'Moldova', 'Mongolia', 'Montenegro', 'Morocco',
                          'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands',
                          'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'North Korea',
                          'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama',
                          'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal',
                          'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis',
                          'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa',
                          'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles',
                          'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands',
                          'Somalia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'Sudan',
                          'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
                          'Tanzania', 'Thailand', 'Timor', 'Togo', 'Tokelau', 'Tonga',
                          'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda',
                          'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States',
                          'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'World', 'Yemen',
                          'Zambia', 'Zimbabwe']

        self.graphs = {
            "Сравнение среднего роста мужчин и женщин по всему миру": {'Возраст': None,
                                                                       'Функция': 'bar_chart_for_mean_height'},
            "Изменение прироста роста мужчин и женщин за 100 лет": {'Континент': None,
                                                                    'Функция': 'scatter_for_increase_in_percent'},
            "Изменение прироста роста женщин в стране": {'Страна': None, 'Функция': 'plot_for_changing'},
            "Сравнение изменения среднего роста мужчин и женщин по стране": {'Страна': None,
                                                                             'Функция': 'plot_for_changing_mean_male_female_height'},
            "Как зависит рост и индекс развития": {'Год': None, 'Континент': None, 'Функция': 'scatter_for_dev_index'},
            "Как зависит рост и смертность детей(данные собраны со всех возрастов)": {'Год': None, 'Континент': None,
                                                                                      'Функция': 'scatter_for_childRate'},
            "Как изменяется рост мужчин и женщин глобально": {'Функция': 'plot_for_global_change_in_height'},
            "Как изменился рост по континенту": {'Год начала': None, 'Год конца': None,
                                                 'Функция': 'inclined_map_for_change_over_century'},
            "На сколько в среднем рост мужчин выше женщин": {'Год': None,
                                                             'Функция': 'scatter_for_mean_height_betw_mal_fem'},
            "Ящик с усами": {'Возрасты': [], 'Годы': [],
                             'Функция': 'boxplot_for_height'},
            "Зависимость роста от животного белка по всему миру": {'Год': None, 'Функция': 'scatter_for_calories'},
            "Зависимость роста от животного белка по континенту": {'Год': None,
                                                                   'Функция': 'scatter_for_calories_per_country'},
            "Каково распределение роста мужчин и женщин по миру": {'Разделители': None,
                                                                   'Функция': 'hist_for_mean_height'}
        }

        self.welcomeLabel = Label(master=self.frame1, font=self.theFont,
                                  text="Выберите график, который хотите построить").place(
            x=700 * self.coefficient1, y=10 * self.coefficient2,
            height=32 * self.coefficient2,
            width=400 * self.coefficient1)
        self.theChoice = StringVar(master=self.frame1)
        self.theChoice.set(list(self.graphs.keys())[0])
        self.graphChoice = OptionMenu(self.frame1, self.theChoice, *list(self.graphs.keys()))
        self.graphChoice.config(font=self.theFont)
        self.graphChoice.place(x=680 * self.coefficient1, y=40 * self.coefficient2, width=445 * self.coefficient1,
                               height=35 * self.coefficient2)
        self.acceptButton = Button(master=self.frame1, text="Выбрать", font=self.theFont,
                                   command=lambda: self.chooseOption()).place(
            x=830 * self.coefficient1, y=100 * self.coefficient2,
            width=135 * self.coefficient1,
            height=40 * self.coefficient2)

        self.window.mainloop()

    """
        Получает ширину и длину экрана монитора пользователя 
        для установления геометрии в полный экран и определяет 
        коэффициент для того, чтобы приложение и его 
        вид был максимально оптимизирован для 
        просмотра пользователем
    """

    def getScreenWidth(self):
        screenWidth = self.window.winfo_screenwidth()
        self.coefficient1 = screenWidth / self.width
        return screenWidth

    def getScreenHeight(self):
        screenHeight = self.window.winfo_screenheight()
        self.coefficient2 = screenHeight / self.height
        return screenHeight

    """
    Функция получает на вход массив, Проходит по 
    нему и возвращает список необходимых функций 
    и значений, необходимых для построения графика
    """

    def getData(self, theChoiceOM):
        for i in self.graphs.keys():
            if i == theChoiceOM:
                return list(self.graphs[i])

    """
    Выбирает функцию, зависит от 
    действий пользователя (введённых им данных)
    """

    def chooseOption(self):
        self.flag = False
        self.flagEdit = False
        theChoiceOM = self.theChoice.get()
        self.dataForGraph = []
        self.dataForGraph = self.getData(theChoiceOM)
        self.result = list()

        counter = 0
        for item in self.frame1.winfo_children():
            counter += 1
            if counter > 4:
                item.destroy()
        for item in self.frame2.winfo_children():
            item.destroy()

        if len(self.dataForGraph) == 1:
            if self.dataForGraph[0] == 'Функция':
                Label(master=self.frame1, font=self.theFont,
                      text="Чтобы построить этот график, дополнительные данные вводить не нужно").place(
                    x=700 * self.coefficient1, y=190 * self.coefficient2, height=30 * self.coefficient2,
                    width=410 * self.coefficient1)
                Label(master=self.frame1, text="Нажмите 'Нарисовать', когда захотите увидеть график",
                      font=self.theFont).place(
                    x=700 * self.coefficient1,
                    y=260 * self.coefficient2,
                    height=30 * self.coefficient2,
                    width=410 * self.coefficient1)
                self.result.append((self.dataForGraph[0], self.graphs[theChoiceOM]['Функция']))
                self.drawButton = Button(master=self.frame1, text="Нарисовать", font=self.theFont,
                                         command=lambda: self.draw()).place(x=750 * self.coefficient1,
                                                                            y=550 * self.coefficient2,
                                                                            width=243 * self.coefficient1,
                                                                            height=60 * self.coefficient2)

            else:
                Label(master=self.frame1, text="Введите " + "'" + self.dataForGraph[
                    0] + "'" + " , а затем нажмите 'Нарисовать'", font=self.theFont).place(x=690 * self.coefficient1,
                                                                                           y=200 * self.coefficient2,
                                                                                           height=30 * self.coefficient2,
                                                                                           width=420 * self.coefficient1)

                Label(master=self.frame1, text=self.dataForGraph[0], font=self.theFont).place(x=660 * self.coefficient1,
                                                                                              y=270 * self.coefficient2,
                                                                                              height=30 * self.coefficient2,
                                                                                              width=100 * self.coefficient1)
                entry = Entry(master=self.frame1, width=30, font=self.theFont)
                entry.place(width=180 * self.coefficient1, height=30 * self.coefficient2, y=270 * self.coefficient2,
                            x=940 * self.coefficient1)
                self.result.append((self.dataForGraph[0], entry))
                self.submitButton = Button(master=self.frame1, text="Ввести", font=self.theFont,
                                           command=lambda: self.collectDataEntries()).place(
                    width=111, height=39, x=830 * self.coefficient1, y=350)
        elif len(self.dataForGraph) == 2:
            Label(master=self.frame1, text="Введите " + "'" + self.dataForGraph[
                0] + "'" + " , а затем нажмите 'Нарисовать'", font=self.theFont).place(x=690 * self.coefficient1,
                                                                                       y=200 * self.coefficient2,
                                                                                       height=30 * self.coefficient2,
                                                                                       width=420 * self.coefficient1)

            Label(master=self.frame1, text=self.dataForGraph[0], font=self.theFont).place(x=660 * self.coefficient1,
                                                                                          y=270 * self.coefficient2,
                                                                                          height=30 * self.coefficient2,
                                                                                          width=100 * self.coefficient1)
            entry = Entry(master=self.frame1, width=30, font=self.theFont)
            entry.place(width=180 * self.coefficient1, height=30 * self.coefficient2, y=270 * self.coefficient2,
                        x=940 * self.coefficient1)
            for num, i in enumerate(self.dataForGraph):
                if num <= 0:
                    self.result.append((self.dataForGraph[num], entry))
                else:
                    self.result.append((self.dataForGraph[num], self.graphs[theChoiceOM]['Функция']))
            self.submitButton = Button(master=self.frame1, text="Ввести", font=self.theFont,
                                       command=lambda: self.collectDataEntries()).place(
                width=111 * self.coefficient1, height=39 * self.coefficient2, x=830 * self.coefficient1,
                y=350 * self.coefficient2)

        elif len(self.dataForGraph) == 3:
            Label(master=self.frame1, text="Введите " + "'" + self.dataForGraph[
                0] + "'" + " и '" + self.dataForGraph[1] + "' " + " , а затем нажмите 'Нарисовать'",
                  font=self.theFont).place(
                x=675 * self.coefficient1, y=170 * self.coefficient2,
                height=30 * self.coefficient2,
                width=465 * self.coefficient1)

            start = 220

            for num, i in enumerate(self.dataForGraph):
                if (num <= 1):
                    Label(master=self.frame1, text=i, font=self.theFont).place(x=660 * self.coefficient1,
                                                                               y=start * self.coefficient2,
                                                                               height=30 * self.coefficient2,
                                                                               width=100 * self.coefficient1)
                    entry = Entry(master=self.frame1, width=30, font=self.theFont)
                    entry.place(width=180 * self.coefficient1, height=25 * self.coefficient2,
                                y=start * self.coefficient2, x=940 * self.coefficient1)
                    start += 50
                    self.result.append((i, entry))
                else:
                    self.result.append((i, self.graphs[theChoiceOM]['Функция']))
            self.submitButton = Button(master=self.frame1, text="Ввести", font=self.theFont,
                                       command=lambda: self.collectDataEntries()).place(
                width=111 * self.coefficient1, height=39 * self.coefficient2, x=830 * self.coefficient1,
                y=350 * self.coefficient2)

    """
        Функция получает значения, введенные пользователем в поле ввода, 
        проверяет входные данные на правильное введение. 
        Появляется кнопка, по нажатию которой приложение 
        строит график, выводит базу данных
        """

    def collectDataEntries(self):
        if not self.flag and not self.flagEdit:
            counter = 0
            for item in self.frame1.winfo_children():
                counter += 1

                if counter >= 9 and len(self.result) == 2:
                    item.destroy()
                if counter >= 11 and len(self.result) == 3:
                    item.destroy()
            for item in self.frame2.winfo_children():
                item.destroy()
            for item in self.frame3.winfo_children():
                item.destroy()
            flag = False
            flag1 = False
            self.result1 = dict()

            for name, entry in self.result:

                try:
                    if len(self.result) == 3:
                        if name == "Возрасты":
                            if entry.get() == '':
                                flag1 = True
                            else:
                                a = entry.get().split(',')
                                if len(a) != 4:
                                    flag1 = True
                                for age in a:
                                    if age == '' or not age.isdigit() or int(age) < 5 or int(age) > 19:
                                        flag1 = True
                                        break
                            if flag1:
                                self.warningLabel1 = Label(master=self.frame1, font=self.theFont,
                                                           text="Введите 4 возраста от 5 до 19 через запятую").place(
                                    x=750 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=320 * self.coefficient1)

                        if name == "Годы":
                            if entry.get() == '':
                                flag = True
                            else:
                                a = entry.get().split(',')
                                if len(a) != 4:
                                    flag = True
                                for age in a:
                                    if age == '' or not age.isdigit() or int(age) < 1985 or int(age) > 2019:
                                        flag = True
                                        break
                            if flag:
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите 4 года от 1985 до 2019 через запятую").place(
                                    x=670 * self.coefficient1, y=500 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=470 * self.coefficient1)

                        if name == "Год начала":

                            minYear = 1896
                            maxYear = 1996
                            if entry.get() == '' or not entry.get().isdigit():
                                flag1 = True
                            if entry.get() != '' and entry.get().isdigit():
                                if int(entry.get()) < minYear or int(entry.get()) > maxYear:
                                    flag1 = True
                            if flag1:
                                self.warningLabel1 = Label(master=self.frame1, font=self.theFont,
                                                           text="Введите значение для года начала от " + str(
                                                               minYear) + " до " + str(maxYear)).place(
                                    x=750 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=320 * self.coefficient1)
                            if not flag1:
                                self.startyear = int(entry.get())
                        if name == "Год конца":
                            minYear = self.startyear + 1
                            maxYear = 1996
                            if entry.get() == '' or not entry.get().isdigit():
                                flag = True
                            if entry.get() != '' and entry.get().isdigit():
                                if int(entry.get()) < minYear or int(entry.get()) > maxYear:
                                    flag = True
                            if flag:
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите значение для года окончания от " + str(
                                                              minYear) + " до " + str(maxYear)).place(
                                    x=750 * self.coefficient1, y=500 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=320 * self.coefficient1)
                        if name == "Год":
                            if self.result[2][1] == 'scatter_for_dev_index':
                                minYear = 1980
                                maxYear = 1996
                                if entry.get() == '' or not entry.get().isdigit():
                                    flag1 = True
                                if entry.get() != '' and entry.get().isdigit():
                                    if int(entry.get()) < minYear or int(entry.get()) > maxYear:
                                        flag1 = True
                                if flag1:
                                    self.warningLabel1 = Label(master=self.frame1, font=self.theFont,
                                                               text="Введите значение для года от " + str(
                                                                   minYear) + " до " + str(maxYear)).place(
                                        x=750 * self.coefficient1, y=500 * self.coefficient2,
                                        height=32 * self.coefficient2,
                                        width=300 * self.coefficient1)
                            elif self.result[2][1] == 'scatter_for_childRate':
                                minYear = 1962
                                maxYear = 1996
                                if entry.get() == '' or not entry.get().isdigit():
                                    flag1 = True
                                if entry.get() != '' and entry.get().isdigit():
                                    if int(entry.get()) < minYear or int(entry.get()) > maxYear:
                                        flag1 = True
                                if flag1:
                                    self.warningLabel1 = Label(master=self.frame1, font=self.theFont,
                                                               text="Введите значение для года от " + str(
                                                                   minYear) + " до " + str(maxYear)).place(
                                        x=750 * self.coefficient1, y=500 * self.coefficient2,
                                        height=32 * self.coefficient2,
                                        width=300 * self.coefficient1)
                        if name == "Континент":

                            if entry.get() == "Africa" or entry.get() == "Oceania" or entry.get() == "North America" \
                                    or entry.get() == "South America" or entry.get() == "Asia" \
                                    or entry.get() == "Europe":
                                flag = False

                            else:
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите настоящее название континента").place(
                                    x=750 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=300 * self.coefficient1)
                                flag = True

                    elif len(self.result) == 2:

                        if name == "Год":
                            if self.result[1][1] == 'scatter_for_mean_height_betw_mal_fem':
                                minYear = 1896
                                maxYear = 1996
                                if entry.get() == '' or not entry.get().isdigit():
                                    flag = True
                                if entry.get() != '' and entry.get().isdigit():

                                    if int(entry.get()) < minYear or int(entry.get()) > maxYear:
                                        flag = True
                                if flag:
                                    self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                              text="Введите значение для года от " + str(
                                                                  minYear) + " до " + str(maxYear)).place(
                                        x=750 * self.coefficient1, y=500 * self.coefficient2,
                                        height=32 * self.coefficient2,
                                        width=300 * self.coefficient1)
                            if self.result[1][1] == ('scatter_for_calories' or 'scatter_for_calories_per_country'):
                                minYear = 1966
                                maxYear = 1996
                                if entry.get() == '' or not entry.get().isdigit():
                                    flag = True
                                elif entry.get() != '' and entry.get().isdigit():

                                    if int(entry.get()) < minYear or int(entry.get()) > maxYear:
                                        self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                                  text="Введите значение для года от " + str(
                                                                      minYear) + " до " + str(maxYear)).place(
                                            x=750 * self.coefficient1, y=500 * self.coefficient2,
                                            height=32 * self.coefficient2,
                                            width=300 * self.coefficient1)
                                        flag = True
                        if name == "Разделители":
                            if entry.get() == '' or not entry.get().isdigit():
                                flag = True
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите целое число разделителей (чем больше, тем лучше)").place(
                                    x=700 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=400 * self.coefficient1)
                            elif entry.get() != '' and entry.get().isdigit():
                                flag = False

                        if name == "Возраст":
                            if entry.get() == '' or not entry.get().isdigit():
                                flag = True
                            elif entry.get() != '' and entry.get().isdigit():

                                if int(entry.get()) < 5 or int(entry.get()) > 18:
                                    flag = True
                            if flag:
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите значение для возраста от 5 до 18").place(
                                    x=750 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=300 * self.coefficient1)
                        if name == "Континент":
                            if entry.get() == "Africa" or entry.get() == "Oceania" or entry.get() == "North America" \
                                    or entry.get() == "South America" or entry.get() == "Asia" \
                                    or entry.get() == "Europe":

                                flag = False

                            else:
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите настоящее название континента").place(
                                    x=750 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=300 * self.coefficient1)
                                flag = True
                        if name == "Страна":
                            flag = True

                            for country in self.countries:
                                if entry.get() == country:
                                    flag = False
                            if flag:
                                self.warningLabel = Label(master=self.frame1, font=self.theFont,
                                                          text="Введите настоящее название страны").place(
                                    x=750 * self.coefficient1, y=450 * self.coefficient2,
                                    height=32 * self.coefficient2,
                                    width=300 * self.coefficient1)


                except:
                    continue

            if flag or flag1:
                return None
            elif not flag and len(self.result) == 2:

                counter = 0
                for item in self.frame1.winfo_children():
                    counter += 1
                    if counter >= 9:
                        item.destroy()
                for item in self.frame2.winfo_children():
                    item.destroy()
                for name, entry in self.result:
                    self.result1[name] = entry.get() if name != 'Функция' else entry
            elif not flag and not flag1 and len(self.result) == 3:
                counter = 0
                for item in self.frame1.winfo_children():

                    counter += 1
                    if counter >= 11:
                        item.destroy()
                for item in self.frame2.winfo_children():
                    item.destroy()

                for name, entry in self.result:
                    self.result1[name] = entry.get() if name != 'Функция' else entry
            if (not flag and len(self.result) == 2) or (not flag and not flag1 and len(self.result) == 3):
                self.drawButton = Button(master=self.frame1, text="Нарисовать", font=self.theFont,
                                         command=lambda: self.draw()).place(x=750 * self.coefficient1,
                                                                            y=550 * self.coefficient2,
                                                                            width=243 * self.coefficient1,
                                                                            height=60 * self.coefficient2)
            return self.result1

        elif self.flag and not self.flagEdit:
            flag = False
            self.result2 = dict()

            for name, entry in self.resultDB:

                try:
                    if name == "Sex":
                        if entry.get() != "Boys" and entry.get() != "Girls":
                            messagebox.showerror("Пол", "Вы должны указать пол 'Boys' или 'Girls'")
                            flag = True
                            break
                    if name == "Year" or name == "Age group" or name == "Mean height" \
                            or name == "Mean height lower 95% uncertainty interval " \
                            or name == "Mean height upper 95% uncertainty interval" \
                            or name == "Mean height standard error" or name == "Mean male height (cm)" \
                            or name == "Mean female height (cm)" or name == "Year-on-year change in female height (%)" \
                            or name == "Year-on-year change in male height (%)" \
                            or name == "Human Development Index (UNDP)" or name == "Mortality rate" \
                            or name == "Calories from animal protein (FAO (2017))":
                        if entry.get() == '' or not entry.get().isdigit():
                            if entry.get() % 1 != 0:
                                messagebox.showerror("Ошибка значения", "Укажите число в поле " + name)
                                flag = True
                                break

                    if entry.get() == '':
                        flag = True
                except:
                    continue
            if flag:
                return None
            else:
                for name, entry in self.resultDB:
                    self.result2[name] = entry.get()
            if not flag:
                self.addingButton = Button(master=self.frame2, text="Добавить", font=self.theFont,
                                           command=lambda: self.addingRow()).place(x=890 * self.coefficient1,
                                                                                   y=450 * self.coefficient2,
                                                                                   width=200 * self.coefficient1,
                                                                                   height=60 * self.coefficient2)
            return self.result2
        elif self.flagEdit:
            flag = False
            self.result3 = dict()

            for name, entry in self.resultDBE:
                # print(name,entry)

                try:
                    if name == "Sex":
                        if entry.get() != "Boys" and entry.get() != "Girls":
                            messagebox.showerror("Пол", "Вы должны указать пол 'Boys' или 'Girls'")
                            flag = True
                            break
                    if name == "Year" or name == "Age group" or name == "Mean height" \
                            or name == "Mean height lower 95% uncertainty interval " \
                            or name == "Mean height upper 95% uncertainty interval" \
                            or name == "Mean height standard error" or name == "Mean male height (cm)" \
                            or name == "Mean female height (cm)" or name == "Year-on-year change in female height (%)" \
                            or name == "Year-on-year change in male height (%)" \
                            or name == "Human Development Index (UNDP)" or name == "Mortality rate" \
                            or name == "Calories from animal protein (FAO (2017))":
                        if entry.get() == '' or not entry.get().isdigit():
                            for i in entry.get():
                                if not i.isdigit() and i != '.':
                                    messagebox.showerror("Ошибка значения", "Укажите число в поле " + name)
                                    flag = True
                                    break
                            # if entry.get() % 1 != 0:
                            #     messagebox.showerror("Ошибка значения", "Укажите число в поле " + name)
                            #     flag = True
                            #     break

                    if entry.get() == '':
                        flag = True
                except:
                    continue
            if flag:
                return None
            else:
                for name, entry in self.resultDBE:
                    self.result3[name] = entry.get()
            if not flag:
                self.addingButton = Button(master=self.frame2, text="Добавить", font=self.theFont,
                                           command=lambda: self.edittingRow()).place(x=890 * self.coefficient1,
                                                                                     y=450 * self.coefficient2,
                                                                                     width=200 * self.coefficient1,
                                                                                     height=60 * self.coefficient2)
            return self.result3

    """
    Строит график, который потом выводится в приложении
    """

    def draw(self):
        for item in self.frame2.winfo_children():
            item.destroy()
        for item in self.frame3.winfo_children():
            item.destroy()
        a, b = self.result[0]
        if (b != 'plot_for_global_change_in_height'):
            self.function = f"self.{self.result1['Функция']}"

            if (self.result1['Функция'] == 'boxplot_for_height'):
                for i in self.result1:
                    if i != 'Функция':
                        self.result1[i] = self.result1[i].split(',')
                        for index in range(len(self.result1[i])):
                            self.result1[i][index] = int(self.result1[i][index])

                function = eval(self.function)(self.result1)
            else:
                function = eval(self.function)(self.result1)
            self.toolbarFrame = Frame(master=self.frame1)
            self.toolbar = NavigationToolbar2Tk(self.canvas, self.toolbarFrame)
            self.toolbarFrame.place(
                x=190 * self.coefficient1,
                y=512 * self.coefficient2,
                width=250 * self.coefficient1,
                height=30 * self.coefficient2)

        else:
            data = f"self.{b}"
            function = eval(data)()

    def treeMaker(self, columns_headers, dataset):
        self.scroll = ttk.Scrollbar(master=self.frame2)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.tree = ttk.Treeview(master=self.frame2, yscrollcommand=self.scroll.set, columns=columns_headers,
                                 show='headings', height=int(10 * self.coefficient2))

        self.columns = columns_headers

        datasetCopy = []
        counter = 0

        for i in columns_headers:
            datasetCopy.append(dataset[i].to_numpy())
            self.tree.column(counter, width=int(100 * self.coefficient1), minwidth=25, anchor=CENTER, stretch=True)
            self.tree.heading(counter, text=i)
            counter += 1

        self.rowCounter = 0

        finalData = list(zip(*datasetCopy))

        for i in range(len(finalData)):
            self.rowCounter += 1
            self.tree.insert(parent='', index=END, values=finalData[i])

        ttk.Style().configure('Treeview', background="silver", foreground="black", fieldbackground="silver")
        ttk.Style().configure('Treeview.Heading', font=(('Calibri', 12, 'bold')))
        self.table = ttk.Treeview(master=self.frame2, show='headings', height=40)
        self.scroll.config(command=self.tree.yview)
        self.tree.pack(anchor=N, expand=1, side=TOP, fill=X, pady=30 * self.coefficient2)
        self.makeRowButton = Button(master=self.frame2, text="Добавить новую строку", font=self.theFont,
                                    command=lambda: self.makeRow()).place(x=100 * self.coefficient1,
                                                                          y=250 * self.coefficient2,
                                                                          width=200 * self.coefficient1,
                                                                          height=40 * self.coefficient2)
        self.deleteButton = Button(master=self.frame2, text="Удалить выбранные строки", font=self.theFont,
                                   command=lambda: self.removeRows()).place(x=100 * self.coefficient1,
                                                                            y=350 * self.coefficient2,
                                                                            width=200 * self.coefficient1,
                                                                            height=40 * self.coefficient2)
        self.updateButton = Button(master=self.frame2, text="Обновить базу данных", font=self.theFont,
                                   command=lambda: self.updateDB()).place(x=100 * self.coefficient1,
                                                                          y=550 * self.coefficient2,
                                                                          width=200 * self.coefficient1,
                                                                          height=40 * self.coefficient2)
        self.editButton = Button(master=self.frame2, text="Изменить выбранную строку", font=self.theFont,
                                 command=lambda: self.EditTree()).place(x=100 * self.coefficient1,
                                                                        y=450 * self.coefficient2,
                                                                        width=200 * self.coefficient1,
                                                                        height=40 * self.coefficient2)

    """
    Функция удаляет выбранные 
    пользователем строки из базы данных
    """
    def removeRows(self):
        selected = self.tree.selection()
        for i in selected:
            self.tree.delete(i)

    """
    Функция изменяет базу данных, но изменяет сами .csv файлы, 
    поменять данные обратно можно будет только вручную
    """
    def updateDB(self):
        if self.currentDB[2].columns[0] == 'Country' and self.currentDB[2].columns[1] != 'Code':
            with open(self.currentDB[0], 'w', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=';')
                csvwriter.writerow((self.currentDB[2].columns)[:-2])
                for row_id in self.tree.get_children():
                    row = self.tree.item(row_id)['values'][:-2]
                    csvwriter.writerow(row)
            with open(self.currentDB[1], 'a', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=';')
                csvwriter.writerow(
                    [self.tree.item(list(self.tree.get_children())[-1])['values'][x] for x in [-2, 0, -1]])
        elif self.currentDB[2].columns[0] == 'Country' and self.currentDB[2].columns[1] == 'Code':
            with open(self.currentDB[0], 'w', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=';')
                csvwriter.writerow((self.currentDB[2].columns)[:-1])
                for row_id in self.tree.get_children():
                    row = self.tree.item(row_id)['values'][:-1]
                    csvwriter.writerow(row)
            with open(self.currentDB[1], 'a', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=';')
                csvwriter.writerow(
                    [self.tree.item(list(self.tree.get_children())[-1])['values'][x] for x in [1, 0, -1]])
        elif self.currentDB[2].columns[0] == 'Code':
            with open(self.currentDB[0], 'w', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=';')
                csvwriter.writerow((self.currentDB[2].columns)[:-2])
                for row_id in self.tree.get_children():
                    row = self.tree.item(row_id)['values'][:-2]
                    csvwriter.writerow(row)
            with open(self.currentDB[1], 'a', newline='') as myfile:
                csvwriter = csv.writer(myfile, delimiter=';')
                csvwriter.writerow(
                    [self.tree.item(list(self.tree.get_children())[-1])['values'][x] for x in [0, -2, -1]])


    """
    Создает строку в базе данных: 
    выводятся необходимые параметры, 
    чтобы ввести строку, добавляются в treeView
    """
    def makeRow(self):
        start = 280
        self.resultDB = list()
        counter = 0
        for item in self.frame2.winfo_children():
            counter += 1
            if counter > 7:
                item.destroy()

        for i in self.columns:
            Label(master=self.frame2, text=i, font=self.theFont).place(x=400 * self.coefficient1,
                                                                       y=start * self.coefficient2,
                                                                       width=250 * self.coefficient1,
                                                                       height=20 * self.coefficient2)
            entry = Entry(master=self.frame2, font=self.theFont)
            entry.place(x=700 * self.coefficient1, y=start * self.coefficient2, width=100 * self.coefficient1,
                        height=20 * self.coefficient2)
            start += 30 * 10 / len(self.columns)
            self.resultDB.append((i, entry))
        self.flag = True
        self.submitButton2 = Button(master=self.frame2, text="Проверить", font=self.theFont,
                                    command=lambda: self.collectDataEntries()).place(
            width=200 * self.coefficient1, height=60 * self.coefficient2, y=300 * self.coefficient2,
            x=890 * self.coefficient1)

    def addingRow(self):
        temperate = []

        for i in self.result2.values():
            temperate.append(i)
        self.tree.insert(parent='', index='end', iid=self.rowCounter, text="", values=temperate)
        self.rowCounter += 1
        messagebox.showinfo("Добавление в дерево", "Строка добавлена в конец таблицы")

    """
    Функция изменяет базу данных
    """
    def EditTree(self):
        selected = self.tree.focus()
        value = self.tree.item(selected, 'values')
        # print(value)
        counter = 0
        for item in self.frame2.winfo_children():
            counter += 1
            if counter > 7:
                item.destroy()

        start = 280
        self.resultDBE = list()
        # print(self.columns)
        counter = 0
        for i in self.columns:
            Label(master=self.frame2, text=i, font=self.theFont).place(x=400 * self.coefficient1,
                                                                       y=start * self.coefficient2,
                                                                       width=250 * self.coefficient1,
                                                                       height=20 * self.coefficient2)
            entry = Entry(master=self.frame2, font=self.theFont)
            entry.insert(0, value[counter])
            entry.place(x=700 * self.coefficient1, y=start * self.coefficient2, width=100 * self.coefficient1,
                        height=20 * self.coefficient2)
            start += 30 * 10 / len(self.columns)
            counter += 1
            self.resultDBE.append((i, entry))
        self.flagEdit = True
        self.submitButton2 = Button(master=self.frame2, text="Проверить", font=self.theFont,
                                    command=lambda: self.collectDataEntries()).place(
            width=200 * self.coefficient1, height=60 * self.coefficient2, y=300 * self.coefficient2,
            x=890 * self.coefficient1)

    """
    Функция изменяет строку в базе данных
    """
    def edittingRow(self):
        selected = self.tree.focus()
        temperate = []
        for i in self.result3.values():
            temperate.append(i)
        self.tree.item(selected, text="", values=temperate)

    """
    Функция создаёт график, который отображает 
    средний рост мужчин и женщин начиная с 18 лет
    """
    def bar_chart_for_mean_height(self, data):
        dataset = pd.read_csv('FemMaleheight.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')

        width = 0.35

        def autolabel(rects):
            for rect in rects:
                height = rect.get_height()
                ax.text(rect.get_x() + rect.get_width() / 2., 1.02 * height,
                        '%d' % int(height),
                        ha='center', va='bottom')

        dataset = dataset.merge(code)
        self.currentDB = ['FemMaleheight.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        selector = (dataset['Age group'] == int(data['Возраст']))
        self.text_table = pd.pivot_table(dataset[selector], index='Continent', columns='Sex', values='Mean height',
                                         aggfunc=np.mean)

        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        # print(text_table)
        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)
        first_bar = ax.bar(np.arange(len(self.text_table.index)) - width / 2, height=self.text_table['Boys'],
                           width=width,
                           label='Boys')
        second_bar = ax.bar(np.arange(len(self.text_table.index)) + width / 2, height=self.text_table['Girls'],
                            width=width,
                            label='Girls')
        ax.set_xticks(np.arange(len(self.text_table.index)))
        ax.set_xticklabels(self.text_table.index)

        ax.set_xlabel('Континент', fontsize=12)
        ax.set_ylabel('Средний рост по континенту', fontsize=12)
        ax.set_title(f"Каков средний рост мужчин и женщин для определенного возраста ({data['Возраст']}) ?",
                     fontsize=15)
        ax.legend(loc='upper right')
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)

    """
    Следующие две функция создают график, которые отображают изменения 
    прибавки роста у женщин в процентах каждый год. 
    """
    def scatter_for_increase_in_percent(self, data):
        dataset = pd.read_csv("РостМужчинИЖенщин.csv", delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')
        dataset = dataset.merge(code)

        selector = (dataset['Continent'] == data['Континент']) & ((dataset['Year'] == 1896) | (dataset['Year'] == 1996))
        self.currentDB = ["РостМужчинИЖенщин.csv", 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        self.text_table = pd.DataFrame()
        for i in ['Mean male height (cm)', 'Mean female height (cm)']:
            count = 2
            text_table = pd.pivot_table(dataset[selector], index=['Country'], columns='Year', values=i)

            for num, cnr in enumerate(text_table.index):
                new_row = {
                    f"{i}": abs(
                        (text_table.iloc[num][1896] - text_table.iloc[num][1996]) / text_table.iloc[num][1896] * 100)
                }
                self.text_table = self.text_table.append(new_row, ignore_index=True)
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        lenght = int(len(self.text_table) / 2)

        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)
        ax.scatter(self.text_table.iloc[lenght:2 * lenght]['Mean female height (cm)'],
                   self.text_table.iloc[:lenght]['Mean male height (cm)'],
                   color='red')
        ax.set_title(' Как относится изменение роста мужчин и женщин?', fontsize=15)

        ax.set_xlabel('Изменение в мужском росте (%)', fontsize=12)
        ax.set_ylabel('Изменение в женском росте (%)', fontsize=12)
        ax.set_xticks([x for x in range(0, 10)])
        ax.set_yticks([x for x in range(0, 10)])
        ax.grid()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Функция создаёт график, который отображает изменения 
    прибавки роста у женщин в процентах каждый год. 
    """
    def plot_for_changing(self, data):
        change_in_height_dataset = pd.read_csv("ОтносительноеИзменениеРоста.csv", delimiter=';')
        code_for_country = pd.read_csv('Код.csv', delimiter=';')

        dataset = change_in_height_dataset.merge(code_for_country)
        self.currentDB = ["ОтносительноеИзменениеРоста.csv", 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        selector = dataset['Country'] == data['Страна']
        self.text_table = dataset[selector].loc[:, ["Year", "Year-on-year change in female height (%)"]]
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        fig, ax = plt.subplots()
        fig.set_size_inches(6 * self.coefficient1, 5 * self.coefficient2)

        color = 'r' if self.text_table["Year-on-year change in female height (%)"].iloc[0] > \
                       self.text_table["Year-on-year change in female height (%)"].iloc[-1] else 'g'
        ax.plot(self.text_table['Year'], self.text_table["Year-on-year change in female height (%)"], color=color,
                marker='o',
                markersize=3)
        ax.set_title(f"Увеличение среднего роста женщин подходит к концу ? ({data['Страна']})", fontsize=17)
        ax.set_xlabel('Год', fontsize=13)
        ax.set_ylabel('Ежегодное изменение в росте', fontsize=13)
        ax.set_xticks([x for x in range(1900, 2000, 10)])
        ax.grid()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Функция создаёт график, который показывает 
    взаимосвязь между Индексом человеческого 
    развития страны и средним ростом мужчин в 
    разбивке по годам рождения.
    """
    def plot_for_changing_mean_male_female_height(self, data):
        dataset = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')
        list_of_country = ['Mean male height (cm)', 'Mean female height (cm)']
        list_of_country_ru = ['Средний рост мужчин (см)', 'Средний рост женщин (см)']
        dataset = dataset.merge(code)
        self.currentDB = ['РостМужчинИЖенщин.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        fig, ax = plt.subplots(2, 1, figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        selector = dataset['Country'] == data['Страна']
        self.text_table = dataset

        ax[0].set_title(f"Как изменялся средний рост в определенной стране ? ({data['Страна']})", fontsize=15)
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)

        for ax, i in zip(ax.flat, [0, 1]):
            ax.plot(dataset[selector]['Year'], dataset[selector][list_of_country[i]], color='g', marker='o',
                    markersize=3)
            ax.set_ylabel(list_of_country_ru[i], fontsize=12)
            ax.set_xticks([x for x in range(1900, 2000, 10)])
            ax.grid()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)

    def scatter_for_dev_index(self, data):
        """
        Соединен с прошлыми функциями, которые собирают данные

        Parameters
        ----------
        data : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        human_devIndex = pd.read_csv("HumanDev_new.csv", delimiter=';')
        code_for_country = pd.read_csv('Код.csv', delimiter=';')
        test = pd.read_csv('test_2.csv', delimiter=';')
        dataset = human_devIndex.merge(code_for_country)
        dataset = dataset.merge(test)
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        selector = (dataset["Continent"] == 'Africa') & (dataset["Year"] == 1980)
        # selector = (dataset["Continent"] == data['Континент']) & (dataset["Year"] == data['Год'])
        dataset = dataset[selector].loc[:, ["Human Development Index (UNDP)", "Mean male height (cm)"]]
        self.text_table = dataset[
            ~dataset["Human Development Index (UNDP)"].isna() & ~dataset["Mean male height (cm)"].isna()]
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)

        fig, ax = plt.subplots(figsize=(8 * self.coefficient1, 7 * self.coefficient2))
        ax.scatter(self.text_table['Human Development Index (UNDP)'], self.text_table['Mean male height (cm)'],
                   color='g')
        ax.set_title(
            f"Как зависит человеческий рост от Индекса развития человека(UNDP) ? {data['Континент'], data['Год']}",
            fontsize=17)
        ax.set_xlabel('Индекс развития человека(UNDP)', fontsize=15)
        ax.set_ylabel('Средний мужской рост (см)', fontsize=15)

        ax.set_xticks([x / 10 for x in range(0, 10, 1)])
        ax.grid()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)

    """
     Функция принимает базу данных и создаёт график.
     Здоровье – особенно в детском возрасте – 
     также влияет на рост человека. Болезни в детском 
     возрасте могут ограничивать рост, поскольку они 
     снижают доступность питательных веществ и повышают 
     метаболические потребности. Дети, борющиеся с болезнями, 
     имеют более высокие потребности в питании в период, когда 
     питательные вещества менее доступны. Таким образом, высокие 
     показатели заболеваемости должны приводить к снижению 
     среднего роста. Эта взаимосвязь проиллюстрирована на этом графике.
     """
    def scatter_for_childRate(self, data):
        """
        Соединен с предыдущими функциям, которые собирают данные

        Parameters
        ----------
        data : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        childMort_rate_per_mean_height = pd.read_csv("СмертностьДетей.csv", delimiter=';')
        code_for_country = pd.read_csv('Код.csv', delimiter=';')

        dataset = childMort_rate_per_mean_height.merge(code_for_country)
        self.currentDB = ["СмертностьДетей.csv", 'Код.csv', dataset.dropna()]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset.dropna())
        selector = (dataset['Continent'] == data['Континент']) & (dataset["Year"] == int(data['Год']))

        self.text_table = dataset[selector].loc[:, ["Mortality rate", "Mean male height (cm)", "Country"]]
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)

        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        ax.scatter(self.text_table['Mean male height (cm)'], self.text_table['Mortality rate'], color='r', marker='o',
                   linewidth=1)
        ax.set_title(
            'Как зависит средний рост человека от смертности детей от 5 лет ? ' + f" ({data['Континент']}, {data['Год']})",
            fontdict={'fontsize': 15})
        ax.set_xlabel('Средний рост человека(cm)', fontsize=12)
        ax.set_ylabel('Смертность детей', fontsize=12)
        ax.grid()
        ax.tick_params(labelsize=15)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Функция принимает базу данных и создаёт график.
    Данный график отображает глобальное изменение в 
    росте людей с течением времени. Позволяет отследить,
    уменьшаются или увеличиваются люди в росте глобально. 
    Может быть полезно для ученых футуристов пытающихся 
    предсказать внешний вид человека с течением времени.
    """
    def plot_for_global_change_in_height(self):
        dataset = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')

        dataset = dataset.merge(code)
        self.currentDB = ['РостМужчинИЖенщин.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        self.text_table = pd.pivot_table(dataset, index='Year', aggfunc=np.mean)
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        ax.plot(self.text_table.index, self.text_table['Mean male height (cm)'], marker='o', label='Boys')
        ax.plot(self.text_table.index, self.text_table['Mean female height (cm)'], marker='o', linewidth=1,
                label='Girls')
        ax.set_xticks([x for x in range(1896, 2000, 10)])
        ax.set(xlabel='Year', ylabel='Mean height over the century in the world',
               title='How has height changed globally?')

        ax.set_title('Как изменяется рост глобально по миру ?', fontsize=15)
        ax.set_xlabel('Год', fontsize=12)
        ax.set_ylabel('Средний рост', fontsize=12)
        ax.legend(fontsize=12)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Данный график отображает изменение в росте 
    людей в рамках одного века. Позволяет отследить,
    уменьшаются или увеличиваются люди в росте глобально.
    Может быть полезно для ученых футуристов пытающихся
    предсказать внешний вид человека с течением времени.
    Функция принимает базу данных и рисует график в приложении
    """
    def inclined_map_for_change_over_century(self, data):
        dataset = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')
        self.currentDB = ['РостМужчинИЖенщин.csv', 'Код.csv', dataset]

        dataset = dataset.merge(code)
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        selector = (dataset['Year'] == int(data['Год начала'])) | (dataset['Year'] == int(data['Год конца']))
        self.text_table = pd.pivot_table(dataset[selector], index='Continent', columns='Year',
                                         values='Mean female height (cm)', aggfunc=np.mean)
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)

        def newline(p1, p2):
            ax = plt.gca()
            l = mlines.Line2D([p1[0], p2[0]], [p1[1], p2[1]], color='red' if p1[1] - p2[1] > 0 else 'green', marker='o',
                              markersize=2)
            ax.add_line(l)
            return l

        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        ax.vlines(x=1, ymin=self.text_table[int(data['Год начала'])].min(),
                  ymax=self.text_table[int(data['Год начала'])].max(),
                  color='black',
                  alpha=0.7, linewidth=1)
        ax.vlines(x=3, ymin=self.text_table[int(data['Год конца'])].min(),
                  ymax=self.text_table[int(data['Год конца'])].max(),
                  color='black',
                  alpha=0.7, linewidth=1)
        ax.scatter(y=self.text_table[int(data['Год начала'])], x=np.repeat(1, self.text_table.shape[0]), s=10,
                   color='black',
                   alpha=0.7)
        ax.scatter(y=self.text_table[int(data['Год конца'])], x=np.repeat(3, self.text_table.shape[0]), s=10,
                   color='black',
                   alpha=0.7)
        for p1, p2, c in zip(self.text_table[int(data['Год начала'])], self.text_table[int(data['Год конца'])],
                             self.text_table.index[:10]):
            newline([1, p1], [3, p2])
            ax.text(1 - 0.05, p1, c + ', ' + str(round(p1, 2)), horizontalalignment='right', verticalalignment='center',
                    fontdict={'size': 8})
            ax.text(3 + 0.05, p2, c + ', ' + str(round(p2, 2)), horizontalalignment='left', verticalalignment='center',
                    fontdict={'size': 8})
        ax.set_title("Каково изменение в среднем росте по континентам ?", fontdict={'size': 15})

        ax.set_xticks([1, 3])
        ax.set_xticklabels([int(data['Год начала']), int(data['Год конца'])])
        ax.set_yticklabels([])

        plt.gca().spines["top"].set_alpha(.0)
        plt.gca().spines["bottom"].set_alpha(.0)
        plt.gca().spines["right"].set_alpha(.0)
        plt.gca().spines["left"].set_alpha(.0)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Функция, принимающая базу данных и рисующая график
    График иллюстрирует разницу между средним 
    ростом мужчин и женщин по всему миру. 
    """
    def scatter_for_mean_height_betw_mal_fem(self, data):
        dataset = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')
        dataset = dataset.merge(code)
        self.currentDB = ['РостМужчинИЖенщин.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        list_country = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        colors = ['red', 'blue', 'green', 'indigo', 'dimgray', 'orangered', 'black']
        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)
        for cnr, i in zip(list_country, colors):
            selector = (dataset['Year'] == int(data['Год'])) & (dataset['Continent'] == cnr)

            ax.scatter(dataset[selector]['Mean female height (cm)'], dataset[selector]['Mean male height (cm)'],
                       color=i, label=cnr)

        # selector = dataset['Year'] == data['year']
        # text_table = pd.pivot_table(dataset[selector], index=['Country'], aggfunc=np.mean)

        # ax.scatter(text_table['Mean female height (cm)'], text_table['Mean male height (cm)'])
        self.text_table = dataset
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        ax.set_xticks([x for x in range(150, 181, 5)])
        ax.set_yticks([x for x in range(150, 181, 5)])
        ax.plot([x for x in range(150, 181)], [y for y in range(150, 181)])

        ax.set(xlabel='Female height', ylabel='Male height', title='How much taller are men than women?')
        ax.legend()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """ 
    Строит график вида “box and whiskers” изменения роста 
    мужчин и женщин. Данный график отображает средний рост мужчин 
    и женщин начиная с 18 лет, чтобы исключать ненужные для 
    статистики выбросы связанные с учетом роста новорожденных детей. 
    Такая статистика может быть необходима для ученых ,которые 
    пытаются отследить закономерность изменения роста с течением времени.
    Функция принимает базу данных и рисует график в приложении
    """
    def boxplot_for_height(self, data):
        dataset = pd.read_csv('FemMaleheight.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')

        dataset = dataset.merge(code)
        self.currentDB = ['FemMaleheight.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        colors = ['#0000FF', '#0FFF00',
                  '#FFFF00', '#FF00FF']

        fig = plt.figure(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        ax = fig.add_subplot(111)
        selector = [[] for _ in range(4)]
        count = 0
        for age, year in zip(data['Возрасты'], data['Годы']):
            selector[count] = (dataset['Age group'] == age) & (dataset['Year'] == year)
            count += 1

        data1 = dataset[selector[0]]['Mean height']
        data2 = dataset[selector[1]]['Mean height']
        data3 = dataset[selector[2]]['Mean height']
        data4 = dataset[selector[3]]['Mean height']

        data_all = [data1, data2, data3, data4]

        self.text_table = data1

        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        bp = ax.boxplot(x=data_all, vert=0, showmeans=True, notch=True, patch_artist=True)
        for patch, color in zip(bp['boxes'], colors):
            patch.set(facecolor=color)
        for whisker in bp['whiskers']:
            whisker.set(color='#8B008B',
                        linewidth=1.5,
                        linestyle=':')

        for cap in bp['caps']:
            cap.set(color='#8B008B',
                    linewidth=2)

        for flier in bp['fliers']:
            flier.set(marker='D',
                      color='#FF00FF',
                      alpha=0.5)

        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.set_title('Распределение данных по квартилям', fontsize=15)
        ax.set_ylabel('Представители выбранного возраста', fontsize=12)
        ax.set_xlabel('Средний рост (см)', fontsize=12)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Питание является одним из сильнейших факторов, 
    определяющих рост человека.Люди преобразуют химическую энергию, 
    запасенную в макроэлементных компонентах пищи, в энергию. 
    Потребление энергии с пищей должно сбалансировать расход энергии, 
    обусловленный метаболическими функциями и физической активностью, 
    плюс дополнительные затраты энергии, такие как рост в детстве.
    Люди могут адаптироваться к постоянному низкому потреблению энергии с пищей или недоеданию, 
    снижая скорость роста, что приводит к задержке роста и ограничивает рост взрослого человека. 
    Таким образом недостаточное потребление энергии с пищей в популяции приводит к низкому 
    среднему росту взрослого человека
    Функция принимает базу данных и рисует график в приложении
    """
    def scatter_for_calories(self, data):
        dataset = pd.read_csv('calories.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')

        dataset = dataset.merge(code).dropna()
        self.currentDB = ['calories.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        # print(dataset.Continent.unique())
        list_country = dataset.Continent.unique()
        colors = ['red', 'blue', 'green', 'indigo', 'dimgray', 'orangered', 'black']

        fig, ax = plt.subplots(figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        for cnr, i in zip(list_country, colors):
            selector = (dataset['Year'] == int(data['Год'])) & (dataset['Continent'] == cnr)
            ax.scatter(dataset[selector]['Mean male height (cm)'],
                       dataset[selector]['Calories from animal protein (FAO (2017))'], color=i, label=cnr)
        ax.legend(fontsize=10)
        self.text_table = dataset
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)

        ax.set_title('Влияет ли употребление белка на средний рост ?' + f" {data['Год']}", fontsize=15)
        ax.set_xlabel('Средний рост (см)', fontsize=12)
        ax.set_ylabel('Дневное норма употребления животного белка', fontsize=12)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)

    def scatter_for_calories_per_country(self, data):
        dataset = pd.read_csv('calories.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')
        self.currentDB = ['calories.csv', 'Код.csv', dataset]

        dataset = dataset.merge(code).dropna()
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(6 * self.coefficient1, 5 * self.coefficient2), dpi=100)

        list_country = dataset.Continent.unique()
        colors = ['red', 'blue', 'green', 'indigo', 'dimgray', 'orangered', 'black']
        for ax, cnr, color in zip(ax.flat, list_country, colors):
            ax.set_title(f'Получение калорий в {cnr}', fontsize=10, pad=0)
            selector = (dataset['Year'] == int(data['Год'])) & (dataset['Continent'] == cnr)
            ax.scatter(dataset[selector]['Mean male height (cm)'],
                       dataset[selector]['Calories from animal protein (FAO (2017))'], color=color)
            ax.set_yticks([x for x in range(50, 301, 50)])
            ax.set_ylabel('Норма каллорий', fontsize=12)
            ax.tick_params(length=0, direction='in')
        self.text_table = dataset
        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)
    """
    Данный график – гистограмма ,которая отображает 
    средний рост мужчин и женщин начиная с 18 лет, 
    чтобы исключать ненужные для статистики выбросы 
    связанные с учетом роста новорожденных детей. 
    Такая статистика может быть необходима для ученых,
    которые пытаются отследить закономерность изменения 
    роста с течением времени.
    Функция принимает базу данных и рисует график в приложении
    """
    def hist_for_mean_height(self, data):
        dataset = pd.read_csv('РостМужчинИЖенщин.csv', delimiter=';')
        code = pd.read_csv('Код.csv', delimiter=';')

        dataset = dataset.merge(code)
        self.currentDB = ['РостМужчинИЖенщин.csv', 'Код.csv', dataset]
        columns_headers = list(dataset.columns.values)

        self.treeMaker(columns_headers, dataset)
        self.text_table = dataset

        with pd.option_context('display.max_columns',
                               None):  # more options can be specified also
            Label(master=self.frame3, text=self.text_table, justify='left', font=self.theFont).pack(side=TOP, pady=20,
                                                                                                    fill=X)
        fig, ax = plt.subplots(2, 1, figsize=(6 * self.coefficient1, 5 * self.coefficient2))
        ax[0].set_title('Каково распределение роста в мире ?', fontsize=15)
        tags = ['Mean male height (cm)', 'Mean female height (cm)']
        for ax, i in zip(ax.flat, tags):
            N, bins, patches = ax.hist(dataset[i], bins=int(data['Разделители']))

            fracs = N / N.max()

            norm = colors.Normalize(fracs.min(), fracs.max())

            for thisfrac, thispatch in zip(fracs, patches):
                color = plt.cm.viridis(norm(thisfrac))
                thispatch.set(facecolor=color)
                ax.hist(dataset['Mean male height (cm)'], bins=int(data['Разделители']), density=True)
            ax.set_ylabel('Количество представителей в группе', fontsize=12)
            ax.set_xlabel('Количество разбиений на группы', fontsize=15)
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame1)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=25)


if __name__ == "__main__":
    window = Window()
