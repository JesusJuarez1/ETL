##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: dashboard_controller.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la funcionalidad del componente
#
#-------------------------------------------------------------------------
from src.data.repository import Repository
import json

class DashboardController:

    @staticmethod
    def load_products():
        response = Repository.get_products()
        if response.status_code != 200:
            return {"products": 0}
        
        json_response = json.loads(response.text)
        return {
            "products": json_response["result"][0]["COUNT"]
        }

    @staticmethod
    def load_providers():
        response = Repository.get_providers()
        if response.status_code != 200:
            return {"providers": 0}
        
        json_response = json.loads(response.text)
        return {
            "providers": json_response["result"][0]["SUM"]
        }

    @staticmethod
    def load_locations():
        response = Repository.get_locations()
        if response.status_code != 200:
            return {"locations": 0}
        
        json_response = json.loads(response.text)
        return {
            "locations": json_response["result"][0]["SUM"]
        }

    @staticmethod
    def load_orders():
        response = Repository.get_orders()
        if response.status_code != 200:
            return {"orders": 0}
        
        json_response = json.loads(response.text)
        return {
            "orders": json_response["result"][0]["COUNT"]
        }

    @staticmethod
    def load_sales():
        response = Repository.get_sales()
        if response.status_code != 200:
            return {"sales": 0}
        
        json_response = json.loads(response.text)
        return {
            "sales": json_response["result"][0]["SUM"]
        }

    @staticmethod
    def load_providers_per_location():
        response = Repository.get_providers_by_location()
        if response.status_code != 200:
            return {
                "providers": [],
                "location": []
            }
        result = {
            "providers": [],
            "location": []
        }
        json_response = json.loads(response.text)
        for entry in json_response["result"]:
            result["providers"].append(entry["COUNT"])
            result["location"].append(entry["name"])
        return result

    @staticmethod
    def load_sales_per_location():
        response = Repository.get_sales_by_location()
        if response.status_code != 200:
            return {
                "sales": [],
                "location": []
            }
        result = {
            "sales": [],
            "location": []
        }
        json_response = json.loads(response.text)
        for entry in json_response["result"]:
            result["sales"].append(entry["SUM"])
            result["location"].append(entry["country"])
        return result

    @staticmethod
    def load_orders_per_location():
        response = Repository.get_orders_by_location()
        if response.status_code != 200:
            return {
                "orders": [],
                "location": []
            }
        result = {
            "orders": [],
            "location": []
        }
        json_response = json.loads(response.text)
        for entry in json_response["result"]:
            result["orders"].append(entry["COUNT"])
            result["location"].append(entry["country"])
        return result

    @staticmethod
    def load_best_sellers():
        response = Repository.get_best_sellers()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)
        for product in json_response["result"]:
            result.append({
                "invoice": product["invoice"],
                "total": product["total"]
            })
        return result

    @staticmethod
    def load_worst_sales():
        response = Repository.get_worst_sales()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)
        for product in json_response["result"]:
            result.append({
                "invoice": product["invoice"],
                "total": product["total"]
            })
        return result

    @staticmethod
    def load_most_selled_products():
        response = Repository.get_most_selled_products()
        if response.status_code != 200:
            return []
        result = []
        json_response = json.loads(response.text)
        for product in json_response["result"]:
            result.append({
                "product": product["product"],
                "times": product["COUNT"]
            })
        return result