##!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------
# Archivo: application.py
# Capitulo: Flujo de Datos
# Autor(es): Perla Velasco & Yonathan Mtz. & Jorge Solís
# Version: 1.0.0 Noviembre 2022
# Descripción:
#
#   Este archivo define la aplicación que sirve la UI y la lógica 
#   del componente
#
#-------------------------------------------------------------------------
from src.view.dashboard import Dashboard
import dash_bootstrap_components as dbc
import dash
from datetime import datetime
from dash.dependencies import Input, Output, State

app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

app.title = "ETL"

dashboard = Dashboard()

app.layout = dashboard.document(min_date_allowed=datetime(2010, 1, 1), max_date_allowed=datetime.now())

@app.callback(
    Output(component_id='output-container-date-picker-range', component_property='children'),
    [Input(component_id='Update-button', component_property='n_clicks')],
    [State(component_id='date-picker-range', component_property='start_date'),
    State(component_id='date-picker-range', component_property='end_date')]
)
def update(n_clicks, start_date:datetime, end_date:datetime):
    if start_date != None and end_date != None:
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M:%S000Z')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M:%S000Z')
        return dashboard.document(min_date_allowed=start_date, max_date_allowed=end_date)