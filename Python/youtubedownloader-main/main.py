# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 18:42:57 2020

@author: DELL
"""

""" TeknoBol Youtube Downloader """

#Kütüphane tanımlamaları
import sys
import time
import pytube
import os,sys


from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore # timer için

from TeknobolYoutube import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_TeknobolYoutubeDowndloader()
ui.setupUi(MainWindow)
MainWindow.show()

def VideoIndir():
    ui.statusbar.showMessage(" ")

    link = ui.lineEdit.text()
    yt=pytube.YouTube(link)
    name=yt.title
    ui.progressBar.setValue(25)
    ui.label_3.setText(name)
#    viewss=yt.views
#    ui.label_5.setText(viewss)
#    link2=yt.watch_url
#    ui.label_4.setText(link2)
#    rating=yt.rating
#    ui.label_6.setText(rating)
    ui.progressBar.setValue(55)
    ys = yt.streams.get_highest_resolution()
    
    print(ys)
    #Starting download
    ui.statusbar.showMessage("   İndiriliyor...")

    ys.download()
    ui.progressBar.setValue(100)
    ui.statusbar.showMessage("   İndirme tamamlandı.")
#    time.sleep(0.3)
    Temizle()
    
def MP3():
    ui.statusbar.showMessage(" ")
    link_mp3 = ui.lineEdit_2.text()
    yt_mp3=pytube.YouTube(link_mp3)
    name_mp3=yt_mp3.title
    ui.progressBar_2.setValue(25)
    ui.label_5.setText(name_mp3)
    #sadece ses olarak mp4 indirir, görüntü olmaz
    ys_mp3 = yt_mp3.streams.get_audio_only()
    ui.progressBar_2.setValue(58)
    print(ys_mp3)

    ui.statusbar.showMessage("   İndiriliyor...")

    ys_mp3.download()
    ui.progressBar_2.setValue(79)
    ui.statusbar.showMessage("   İndirme tamamlandı.")
    #mp4 olarak indirildi, mp3'e çevirme işlemi yapacağız.

    folder =  "../TeknobolYoutubeDownloader/"
    folder2= folder+name_mp3
    folder3=folder2+'.mp4'

    liste=os.listdir(folder)
    print(liste)
    ui.progressBar_2.setValue(100)
    infilename=os.path.join(folder3)

    newname=infilename.replace('mp4', '.mp3')
    os.rename(infilename, newname)
    

    Temizle()
    
    
def Temizle():
    ui.statusbar.showMessage("   İndirme tamamlandı.")
    time.sleep(0.3)
    ui.statusbar.showMessage("   Önceki indirme tamamlandı. Yeni indirme için uzantıyı yazın.")
    ui.progressBar.setValue(0)
    ui.progressBar_2.setValue(0)
    ui.lineEdit_2.setText(" ")
    ui.lineEdit.setText(" ")
    ui.label_3.setText(" ")
    ui.label_5.setText(" ")
    #ui.statusbar.showMessage("   ")

#buton tanımlamaları
ui.pushButton.clicked.connect(VideoIndir)
ui.pushButton_2.clicked.connect(MP3)
#sys.exit(app.exec_())