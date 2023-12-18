# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os , sys, psutil
print("Famille du système d'exploitation : ", os.uname().sysname)
print("Ordre des octets : ", sys.byteorder, "endian")
print("Encodage des caractères : ",  sys.getfilesystemencoding())
print("Nom de l'hôte de la machine : ", os.uname().nodename)
print("Architecture du CPU : ", os.uname().machine)
print("Version du kernel : ", os.uname().release)
print("Architecture du CPU : ", os.system("python3 --version"))
print("Nombre de coeurs du processeur :", os.cpu_count())
print("Processeurs physiques : ", psutil.cpu_count(logical=False))
print("Processeurs logiques : ", psutil.cpu_count(logical=True))
print("Fréquence des CPUs : ", psutil.cpu_freq(percpu=True))
print("Informations sur les montages ext4 du système : ", psutil.disk_partitions())
print("Infos TCP : ", psutil.net_connections(kind='tcp'))