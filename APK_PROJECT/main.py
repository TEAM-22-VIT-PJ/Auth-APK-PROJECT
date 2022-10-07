import os
import math
import random
import smtplib
from plyer import filechooser
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton,MDIconButton
from kivy.app import App
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.button import MDFlatButton,MDIconButton
import mysql.connector as mysql
sql=mysql.connect(host="localhost",user="apk_project",passwd="Tanishq@2017",database="apk_project")
if sql.is_connected()== True:
    print("systems online")
    cr=sql.cursor()
else :
    print("connection not established")
################################################
def login():#login function 
    global Id
    Id=int(input('enter you id'))
    Pass=input('enter your password')
def pop_up():
    content = Button(text='Alright!!')
    popup = Popup(title='ACCOUNT STATUS',content=Label(text='Account Created successfully'),size_hint=(None, None), size=(400, 400),auto_dismiss=True)
    content.bind(on_press=popup.dismiss)
    popup.open()
def pop_up2():
    content = Button(text='Alright!!')
    popup = Popup(title='taking to 2fa',content=Label(text='Account login successfully'),size_hint=(None, None), size=(400, 400),auto_dismiss=True)
    content.bind(on_press=popup.dismiss)
    popup.open()
def pop_up3():
    content = Button(text='Alright!!')
    popup = Popup(title='OPT',content=Label(text='2fA verified'),size_hint=(None, None), size=(400, 400),auto_dismiss=True)
    content.bind(on_press=popup.dismiss)
    popup.open()
def pop_up4():
    content = Button(text='Alright!!')
    popup = Popup(title='taking to 2fa',content=Label(text='2FA NOT VERIFIED'),size_hint=(None, None), size=(400, 400),auto_dismiss=True)
    content.bind(on_press=popup.dismiss)
    popup.open()
def Create(a,b,c):
    global UserName
    global PassWord
    global EmailID
    s=0
    cr.execute('select Max(SNO) from login_cred')
    code=cr.fetchall()
    for i in code:#a check loop to determine if their is any data in server's database
        for j in i:
            print(j)
            if j==None:
                s=1204000
            else:
                s=int(j)+1
    cr.execute('INSERT INTO login_cred VALUES("{}","{}","{}","{}")'.format(a,b,c,s))
    sql.commit()
    print('account created successfully: ')
    
Window.size=(412,732)
class WelcomeScreen(Screen):
    pass
class LoginPage(Screen):
    pass
class AfterLogin(Screen):
    pass
class RegisterPage(Screen):
    pass
class MenuScreen(Screen):
    pass
class RecievedScreen(Screen):
    pass
class MainApp(MDApp):
    def current_Screen():
        sm.current='home'
    def logger(self):
        global u_ser
        global passwd
        u_ser=self.root.get_screen('login').ids.email.text
        passwd=self.root.get_screen('login').ids.password.text
        cr.execute("select password from login_cred where email='{}'".format(u_ser))
        data=cr.fetchall()
        for i in data:
            for j in i:
                if j==passwd:
                    pop_up2()
        print(u_ser,passwd)
        global OTP
        digits="0123456789"
        OTP =""
        for i in range(6):
            OTP+= digits[math.floor(random.random()*10)]
            otp = str(OTP) +" is your OTP"
            new_otp = otp
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('aj.mrfya@gmail.com','gzcodqfajxsaehrp')
        server.sendmail('aj.mrfya@gmail.com',u_ser, new_otp)
        server.quit()
    def clear(self):
        self.root.get_screen('login').ids.welcome_label.text = "WELCOME"
        self.root.get_screen('login').ids.user.text = ""
        self.root.get_screen('login').ids.password.text = ""
    def logger_re(self):
        global new_otp
        global EmailID
        UserName=self.root.get_screen('register').ids.user.text
        PassWord=self.root.get_screen('register').ids.password.text
        EmailID=self.root.get_screen('register').ids.email.text
        print(UserName,PassWord,EmailID)
        Create(UserName,PassWord,EmailID)
        pop_up()
    def Verify_2FA(self):
        otp_=self.root.get_screen('afterlogin').ids.OPT.text
        if OTP==otp_:
            pop_up3()
            sm.current='menu'
        else:
            pop_up4()
            sm.current='home'
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)
    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='home'))
        sm.add_widget(LoginPage(name='login'))
        sm.add_widget(RegisterPage(name='register'))
        sm.add_widget(AfterLogin(name="afterlogin"))
        sm.add_widget(MenuScreen(name='menu'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return sm
if __name__=='__main__':
    MainApp().run()