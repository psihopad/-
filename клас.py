import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os
from PyQt5 import uic, QtWidgets, QtGui, QtCore
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi('untitled.ui')
        palette = QtGui.QPalette()
        img = QtGui.QImage('фон3.jpg')
        scaled = img.scaled(self.ui.size())
        palette.setBrush(QtGui.QPalette.Window, QtGui.QBrush(scaled))
        self.ui.setPalette(palette)
        self.ui.setWindowTitle('Акції та знижки')
        self.ui.show()
        self.ui.pushButton.setIcon(QtGui.QIcon('грош.png'))
        self.ui.pushButton_2.setIcon(QtGui.QIcon('атб.png'))
        self.ui.pushButton_3.setIcon(QtGui.QIcon('фуршет.png'))
        self.ui.pushButton.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton_2.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton_3.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton_7.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton.setIconSize(QtCore.QSize(75, 75))
        self.ui.pushButton_2.setIconSize(QtCore.QSize(75, 75))
        self.ui.pushButton_3.setIconSize(QtCore.QSize(75, 75))
        self.ui.pushButton_7.setIconSize(QtCore.QSize(75, 75))
        self.ui.pushButton.clicked.connect(self.click_1)
        self.ui.pushButton_2.clicked.connect(self.click_2)
        self.ui.pushButton_3.clicked.connect(self.click_3)
        self.ui.pushButton_7.clicked.connect(self.click_4)

    def click_1(self):
        if requests.ConnectionError:
            while True:
                try:
                    Grosh(self)
                    self.ui.close()
                    break
                except requests.ConnectionError:
                    msgWarn = QtWidgets.QMessageBox()
                    msgWarn.setIcon(QtWidgets.QMessageBox.Warning)
                    msgWarn.setWindowTitle("Помилка підключення")
                    msgWarn.setWindowIcon(QtGui.QIcon('ерор.jpg'))
                    msgWarn.setText("Для виконання цієї дії потрібне підключення до Інтернету. Перевірте підключення і повторіть спробу")
                    msgWarn.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msgWarn.exec_()
                    break
        else:
            self.ui.close()

    def click_3(self):
        if requests.ConnectionError:
            while True:
                try:
                    Furshet(self)
                    self.ui.close()
                    break
                except requests.ConnectionError:
                    msgWarn = QtWidgets.QMessageBox()
                    msgWarn.setIcon(QtWidgets.QMessageBox.Warning)
                    msgWarn.setWindowTitle("Помилка підключення")
                    msgWarn.setWindowIcon(QtGui.QIcon('ерор.jpg'))
                    msgWarn.setText(
                        "Для виконання цієї дії потрібне підключення до Інтернету. Перевірте підключення і повторіть спробу")
                    msgWarn.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msgWarn.exec_()
                    break
        else:
            self.ui.close()
    def click_2(self):
        if requests.ConnectionError:
            while True:
                try:
                    Atb(self)
                    self.ui.close()
                    break
                except requests.ConnectionError:
                    msgWarn = QtWidgets.QMessageBox()
                    msgWarn.setWindowTitle("Помилка підключення")
                    msgWarn.setWindowIcon(QtGui.QIcon('ерор.jpg'))
                    msgWarn.setIcon(QtWidgets.QMessageBox.Warning)
                    msgWarn.setText("Для виконання цієї дії потрібне підключення до Інтернету. Перевірте підключення і повторіть спробу")
                    msgWarn.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msgWarn.exec_()
                    break
        else:
            self.ui.close()

    def click_4(self):
        self.ui.close()
class Grosh(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """Получаем страницу"""
        super(Grosh, self).__init__(parent)
        self.i = 0
        self.lis_img = []
        self.url = 'http://grosh.ua/buyers/promo/'
        self.label = QtWidgets.QLabel()
        self.ui = uic.loadUi('таблиця-грош.ui')
        self.ui.setWindowTitle('Грош')
        self.ui.setWindowIcon(QtGui.QIcon('грош.png'))
        self.ui.pushButton.clicked.connect(self.click_1)
        self.ui.pushButton.setIcon(QtGui.QIcon('назад.png'))
        self.ui.pushButton.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton_2.clicked.connect(self.click_2)
        self.ui.pushButton_2.setStyleSheet("background-color: #bfba4e")
        self.parse()
        self.ui.show()
    def parse(self):
        self.page = requests.get(self.url, headers={'User-Agent': UserAgent().chrome})  # получаем страницу
        self.page.raise_for_status()  # статус запроса
        self.page = self.page.text
        self.soup = BeautifulSoup(self.page, "lxml")
        link = self.soup.find('div', {'class': 'carousel-inner promoSlider'})
        links = link.find_all('a', {'class': 'carousel-item'})
        for i in links:
            try:
                self.img1 = i.img.get('src')
                img = 'http://grosh.ua' + self.img1

            except AttributeError:
                img = None

            self.lis_img.append(img)

        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(len(self.lis_img))
        self.ui.tableWidget.setHorizontalHeaderLabels(["Зображення продукту"])

        os.chdir(os.getcwd()+ r'\Grosh_foto')

        for k in self.lis_img:
            if self.i < len(self.lis_img):
                filename = '{}.jpg'.format(self.i)
                self.r = requests.get(k)
                if self.r.status_code == 200:
                    with open(filename, 'wb') as imgfile:
                        imgfile.write(self.r.content)
                        self.i += 1
                        continue
            else:
                break
        num = 0
        for i in range(len(self.lis_img)):
            self.label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(os.getcwd() + '/{}.jpg'.format(i))
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
            self.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(1100)
            self.ui.tableWidget.verticalHeader().setDefaultSectionSize(600)
            self.ui.tableWidget.setCellWidget(int(i), 0, self.label)
            num += 1
        os.chdir(os.path.split(os.getcwd())[0])

    def click_1(self):
        MainWindow(self)
        self.ui.close()

    def click_2(self):
        self.ui.close()

class Furshet(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        """Получаем страницу"""
        super(Furshet, self).__init__(parent)

        self.url = 'https://furshet.ua/actions?page=%s'
        self.lis_img = []
        self.urls = []
        self.name_list = []
        self.price_list = []
        self.old_list = []
        self.i = 0
        self.ui = uic.loadUi('таблиця.ui')
        self.ui.setWindowTitle('Фуршет')
        self.ui.setWindowIcon(QtGui.QIcon('фуршет.png'))
        self.ui.pushButton.clicked.connect(self.click_1)
        self.ui.pushButton.setIcon(QtGui.QIcon('назад.png'))
        self.ui.pushButton.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton_2.clicked.connect(self.click_2)
        self.ui.pushButton_2.setStyleSheet("background-color: #bfba4e")
        self.parse()
        self.ui.show()

    def parse(self):
        self.page = requests.get(self.url, headers={'User-Agent': UserAgent().opera})  # получаем страницу
        self.page.raise_for_status()  # статус запроса
        self.soup = BeautifulSoup(self.page.text, "html.parser")
        self.divs = self.soup.find('div', {'class': 'item-list'})
        self.pages = self.divs.find('a', {'title': 'Перейти до сторінки 3'}).text
        for url in [self.url % i for i in range(1)]:
            self.pag = requests.get(url, headers={'User-Agent': UserAgent().opera})
            self.pag.raise_for_status()
            self.soups = BeautifulSoup(self.pag.text, "html.parser")
            for j in self.soups.findAll('div', {'class': "actions-list__action swiper-slide"}):
                try:
                    img = j.img['src'].split('.pagespeed')[0]
                except AttributeError:
                    img = None
                self.lis_img.append(img)
                try:
                    name = j.find('div', {'class': 'desc'}).text.replace('\n', ' ')
                except AttributeError:
                    name = None
                self.name_list.append(name)
                try:
                    price = j.find_all('div', {'class': 'cost'})[-1]
                    price = price.text.replace('\n', '')
                    price = price[0:-3] + ',' + price[-3:-1]
                    price = price + ' грн'
                except AttributeError:
                    price = ''
                self.price_list.append(price)
                try:
                    old_price = j.find('div', {'class': 'del-cost'}).text
                    old_price = old_price[0:-3] + ',' + old_price[-3:-1]
                    old_price = old_price + ' грн'
                except AttributeError:
                    old_price = ''
                self.old_list.append(old_price)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(len(self.lis_img))
        self.ui.tableWidget.setHorizontalHeaderLabels(["Зображення продукту", "Назва продукту", "Акційна ціна продукту", "Початкова ціна продукту"])
        self.ui.tableWidget.resizeColumnsToContents()
        num = 0
        for i in self.name_list:
            item = QtWidgets.QTableWidgetItem(str(i))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
            item.setFont(QtGui.QFont("Times New Roman", 12))
            self.ui.tableWidget.setItem(num, 1, item)
            num += 1
        nu = 0
        for j in self.price_list:
            item = QtWidgets.QTableWidgetItem(str(j))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
            item.setFont(QtGui.QFont("Times New Roman", 12))
            self.ui.tableWidget.setItem(nu, 2, item)
            nu += 1
        n = 0
        for k in self.old_list:
            item = QtWidgets.QTableWidgetItem(str(k))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
            item.setFont(QtGui.QFont("Times New Roman", 12))
            self.ui.tableWidget.setItem(n, 3, item)
            n += 1
        os.chdir(os.getcwd()+'/Furshet_foto')

        for k in self.lis_img:
            if self.i < len(self.lis_img):
                filename = '{}.png'.format(self.i)
                self.r = requests.get(k)
                if self.r.status_code == 200:
                    with open(filename, 'wb') as imgfile:
                        imgfile.write(self.r.content)
                        self.i += 1
                        continue
            else:
                break
        num = 0
        for i in range(len(self.lis_img)):
            self.label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(os.getcwd() + '/{}.png'.format(i))
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
            self.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(250)
            self.ui.tableWidget.verticalHeader().setDefaultSectionSize(200)
            self.ui.tableWidget.setCellWidget(int(i), 0, self.label)
            num += 1
        os.chdir(os.path.split(os.getcwd())[0])

    def click_2(self):
        self.ui.close()

    def click_1(self):
        MainWindow(self)
        self.ui.close()

class Atb(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        """Получаем страницу"""
        super(Atb, self).__init__(parent)

        self.ui = uic.loadUi('таблиця.ui')
        self.ui.setWindowIcon(QtGui.QIcon('атб.png'))
        self.ui.setWindowTitle('АТБ')
        self.ui.pushButton.clicked.connect(self.click_1)
        self.ui.pushButton.setIcon(QtGui.QIcon('назад.png'))
        self.ui.pushButton.setStyleSheet("background-color: #bfba4e")
        self.ui.pushButton_2.clicked.connect(self.click_2)
        self.ui.pushButton_2.setStyleSheet("background-color: #bfba4e")
        self.lis_img = []
        self.urls = []
        self.name_list = []
        self.price_list = []
        self.old_list = []
        self.i = 0
        self.ui.show()
        self.parse()

    def parse(self):
        self.url = 'https://www.atbmarket.com/hot/akcii/economy/'
        self.page = requests.get(self.url, headers={'User-Agent': UserAgent().chrome})  # получаем
        self.page.raise_for_status()  # статус запроса
        self.soup = BeautifulSoup(self.page.text, "lxml")
        self.link = self.soup.find('ul', {'class': "promo_list promo_type2"})
        self.links = self.link.find_all('li')
        for i in self.links:
            try:
                a = i.find('a', {'class': 'promo_image_link'})
                img1 = a.img['src']

                img = 'https://www.atbmarket.com/' + img1
            except AttributeError:
                img = None
            self.lis_img.append(img)
            try:
                name = i.find('span', {'class': 'promo_info_text'}).text.replace('\n', '').replace('       ',
                                                                                                   ' ').strip()
            except AttributeError:
                name = None
            self.name_list.append(name)
            try:
                price = i.find('div', {'class': 'promo_price'})
                price = ''.join(str(price).replace('<span>', '.').replace('</span>', '').strip().split()[2::2]).replace(
                    'class="currency">', ' ')
            except AttributeError:
                price = ''
            self.price_list.append(price)
            try:
                old_price = i.find('span', {'class': 'promo_old_price'}).text
                old_price = old_price + ' грн'
            except AttributeError:
                old_price = ''
            self.old_list.append(old_price)
        self.ui.tableWidget.setColumnCount(4)
        self.ui.tableWidget.setRowCount(len(self.lis_img))
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Зображення продукту", "Назва продукту", "Акційна ціна продукту", "Початкова ціна продукту"])
        self.ui.tableWidget.resizeColumnsToContents()
        num = 0
        for i in self.name_list:
            item = QtWidgets.QTableWidgetItem(str(i))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
            item.setFont(QtGui.QFont("Times New Roman", 12))
            self.ui.tableWidget.setItem(num, 1, item)
            num += 1
        nu = 0
        for j in self.price_list:
            item = QtWidgets.QTableWidgetItem(str(j))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
            item.setFont(QtGui.QFont("Times New Roman", 12))
            self.ui.tableWidget.setItem(nu, 2, item)
            nu += 1
        n = 0
        for k in self.old_list:
            item = QtWidgets.QTableWidgetItem(str(k))
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            item.setForeground(QtGui.QBrush(QtGui.QColor('blue')))
            item.setFont(QtGui.QFont("Times New Roman", 12))
            self.ui.tableWidget.setItem(n, 3, item)
            n += 1
        # .setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        os.chdir(os.getcwd() + r'/Atb_foto')
        print(os.getcwd())

        for k in self.lis_img:
            if self.i < len(self.lis_img):
                filename = '{}.jpg'.format(self.i)
                self.r = requests.get(k)
                if self.r.status_code == 200:
                    with open(filename, 'wb') as imgfile:
                        imgfile.write(self.r.content)
                        self.i += 1
                        continue
            else:
                break
        num = 0
        for i in range(len(self.lis_img)):
            self.label = QtWidgets.QLabel()
            pixmap = QtGui.QPixmap(os.getcwd() + r'/{}.jpg'.format(i))
            self.label.setPixmap(pixmap)
            self.label.setScaledContents(True)
            self.label.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
            self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(250)
            self.ui.tableWidget.verticalHeader().setDefaultSectionSize(200)
            self.ui.tableWidget.setCellWidget(int(i), 0, self.label)
            num += 1
        os.chdir(os.path.split(os.getcwd())[0])


    def click_1(self):
        MainWindow(self)
        self.ui.close()

    def click_2(self):
        self.ui.close()

def createFolder():
    path = os.getcwd()
    print(path)
    folder_name = ['Grosh_foto', 'Furshet_foto', 'Atb_foto']
    for i in folder_name:
        fullpath = os.path.join(path, i)
        if not os.path.exists(fullpath):
            os.mkdir(fullpath)

if __name__ == "__main__":
    createFolder()
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())
