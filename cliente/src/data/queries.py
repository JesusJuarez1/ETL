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
from datetime import datetime

class Queries:

    @staticmethod
    def get_total_products():
        return """
            {
                response(func: has(description)) {
                    count(uid)
                }
            }
        """

    @staticmethod
    def get_total_providers():
        return """
            {
                response(func: has(pid)) {
                    count(uid)
                }
            }
        """
    
    @staticmethod
    def get_total_providers_by_date(start_date: datetime, end_date: datetime):
        return '''
            {{
                response(func: has(pid)) @filter(
                    ge(date, "{start_d}") AND 
                    le(date, "{end_d}")
                ) {{
                    count(uid)
                }}
            }}
        '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())
    

    


        
    
    

    @staticmethod
    def get_total_locations():
        return """
            {
                response(func: has(name)) {
                    count(uid)
                }
            }
        """

    ## ORDENES POR FECHA
    @staticmethod
    def get_total_orders(start_date: datetime, end_date: datetime):
        return '''
            {{
                response(func: has(invoice)) @filter(
                    ge(date, "{start_d}") AND 
                    le(date, "{end_d}")
                ) {{
                    count(uid)
                }}
            }}
        '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())
        
    

    @staticmethod
    def get_total_sales():
        return """
            {
                var(func: has(invoice)) {
                    t as total
                }

                response() {
                    total: sum(val(t))
                }
            }
        """

    @staticmethod
    def get_providers_per_location():
        return """
            {
                response(func: has(name)) {
                    name
                    providers: ~belongs {
                        count(uid)
                    }
                }
            }
        """
    
    def get_providers_per_location_by_date():
        return """
            {
                response(func: has(name)) {
                    name
                    providers: ~belongs {
                        count(uid)
                    }
                }
            }
        """

    @staticmethod
    def get_sales_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: ~sold {
                            price
                            quantity: count(bought)
                        }
                    }
                }
            }
        """
    
    @staticmethod
    def get_sales_per_location_by_date(start_date: datetime, end_date: datetime):
        return '''
                {{
                    response(func: has(name)){{
                    name
                    providers: ~belongs {{
                        sold: ~sold {{
                            price
                            quantity: count(bought) @filter( ge(date, "{start_d}") AND le(date, "{end_d}"))
                        }}
                    }}
                }}
            }}
    '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())


        

    @staticmethod
    def get_orders_per_location():
        return """
            {
                response(func: has(name)){
                    name
                    providers: ~belongs {
                        sold: count(~sold)
                    }
                }
            }
        """

    @staticmethod
    def get_best_sellers():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_worst_sales():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderasc: val(c)){
                    description
                    times: val(c)
                    price
                }
            }
        """

    @staticmethod
    def get_most_selled_products():
        return """
            {
                var(func: has(description)) {
                    c as count(bought) 
                }
                    
                response(func: has(description), orderdesc: val(c)){
                    description
                    times: val(c)
                }
            }
        """
        
    
    @staticmethod
    def get_best_sellers_by_date(start_date: datetime, end_date: datetime):
        return '''
            {{
                var(func: has(description)) {{
                    c as count(bought)@filter(
                        ge(date, "{start_d}") AND 
                        le(date, "{end_d}")
                    )
                }}
                    
                response(func: has(description), orderdesc: val(c)){{
                    description
                    times: val(c)
                    price
                }}
            }}
        '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())
        
    @staticmethod
    def get_worst_sales_by_date(start_date: datetime, end_date: datetime):
        return '''
            {{
                var(func: has(description)) {{
                    c as count(bought)@filter(
                        ge(date, "{start_d}") AND 
                        le(date, "{end_d}")
                    )
                }}
                    
                response(func: has(description), orderasc: val(c)){{
                    description
                    times: val(c)
                    price
                }}
            }}
        '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())
    
    @staticmethod
    def get_total_sales_by_date(start_date: datetime, end_date: datetime):
        return '''
            {{
                var(func: has(invoice)) @filter( ge(date, "{start_d}") AND le(date, "{end_d}")){{
                    t as total 
                }}

                response() {{
                    total: sum(val(t))
                }}
            }}
        '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())
    
    @staticmethod
    def get_most_selled_products_by_date(start_date: datetime, end_date: datetime):
        return '''
            {{
                var(func: has(description)) {{
                    c as count(bought) @filter(
                        ge(date, "{start_d}") AND 
                        le(date, "{end_d}")
                    )
                }}

                response(func: has(description), orderdesc: val(c)){{
                    description
                    times: val(c)
                }}
            }}
        '''.format(start_d=start_date.isoformat(), end_d=end_date.isoformat())