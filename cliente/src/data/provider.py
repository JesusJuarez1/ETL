##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: provider.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la conexión a la API donde
#   se encuentran los datos del sistema
#
#-------------------------------------------------------------------------
import requests

host = "http://orientdb"
port = "2480"
username = "root"
password = "N0gPa0hk2sbP"
database = "etl"

class Provider:

    @staticmethod
    def execute(query):
        response = requests.get(f"{host}:{port}/query/{database}/sql/{query}", auth=(username, password))
        return response