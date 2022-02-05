from importlib.resources import path
from numpy import source
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from os.path import dirname, realpath
import time
import json

class  JsonManager:
    def abrir_ticket():
        with open("data-flow/ticket_bovespa.json") as ticket_bovespa:
            dados = json.load(ticket_bovespa)
            
JsonManager.abrir_ticket()
