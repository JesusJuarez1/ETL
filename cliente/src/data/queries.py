##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: queries.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define las consultas que permiten obtener información 
#   y realizar el llenado de datos del tablero
#
#-------------------------------------------------------------------------
class Queries:

    @staticmethod
    def get_total_products():
        return "SELECT COUNT(description) FROM Product"

    @staticmethod
    def get_total_providers():
        return "SELECT SUM(pid) FROM (SELECT COUNT(pid) as pid FROM Provider GROUP BY pid)"

    @staticmethod
    def get_total_locations():
        return "SELECT SUM(name) FROM (SELECT COUNT(name) as name FROM Location GROUP BY name)"

    @staticmethod
    def get_total_orders():
        return "SELECT COUNT(invoice) FROM Order"

    @staticmethod
    def get_total_sales():
        return "SELECT SUM(total.asFloat()) FROM Order"

    @staticmethod
    def get_providers_per_location():
        return "SELECT COUNT(name), name FROM (SELECT expand(out('belongs').include('@rid', 'name')) as name from Provider) WHERE name <> 'United Kingdom' GROUP BY name"

    @staticmethod
    def get_sales_per_location():
        return "SELECT SUM(total.asFloat()), country FROM Order WHERE country <> 'United Kingdom' GROUP BY country"

    @staticmethod
    def get_orders_per_location():
        return "SELECT COUNT(invoice), country FROM Order WHERE country <> 'United Kingdom' GROUP BY country"

    @staticmethod
    def get_best_sellers():
        return "SELECT invoice, SUM(total.asFloat()) as total FROM Order GROUP BY invoice ORDER BY total DESC LIMIT 5"

    @staticmethod
    def get_worst_sales():
        return "SELECT invoice, SUM(total.asFloat()) as total FROM Order GROUP BY invoice ORDER BY total LIMIT 5"

    @staticmethod
    def get_most_selled_products():
        return "SELECT product, COUNT(product) FROM (SELECT first(in('bought').description) as product FROM Order) GROUP BY product ORDER BY COUNT DESC"