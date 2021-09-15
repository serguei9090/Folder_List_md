#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
import time

print("""
*************************************************************************
* Crear Listado de Carpetas, Ingrese el nombre del Txt que quiere tener.*
* Creado por Market                                                     *
* Prestamos servicio de creacio nde Catalogos PDF y Web para su Banco   *
* Whatsapp:+53 52472074                                                 *
*************************************************************************      
"""
)

file_name = input('nombre del archivo:')
txt_file = file_name + "-" + time.strftime("%d-%m-%Y")+".txt"

for dirname in os.listdir(os.getcwd()):
        with open(txt_file, 'a', newline='', encoding='utf-8') as file_txt:
            if os.path.isdir(dirname):
                file_txt.writelines(dirname)
                file_txt.writelines('\n')


        