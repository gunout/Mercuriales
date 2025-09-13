import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class NouvelleCaledonieMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de la Nouvelle-Calédonie (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'riz': 1.8, 'pommes_de_terre': 1.9, 'patates_douces': 1.6, 'igname': 2.0,
                'tomates': 2.5, 'oignons': 2.2, 'carottes': 1.8, 'salade': 2.3,
                'bananes': 1.7, 'ananas': 2.2, 'mangues': 2.7, 'avocats': 3.2,
                'poulet': 6.5, 'bœuf': 12.0, 'porc': 8.5, 'poisson': 11.5,
                'crevettes': 15.0, 'langouste': 25.0, 'lait': 1.2, 'œufs': 0.22,
                'sucre': 1.4, 'café': 4.8, 'vin': 5.0, 'biere': 2.5,
                'farine': 1.3, 'huile': 2.1, 'pain': 3.0, 'fromage': 12.0,
                'citrouille': 1.7, 'chou': 1.9, 'concombre': 2.1, 'poivrons': 3.2
            },
            '2003': {
                'riz': 1.9, 'pommes_de_terre': 2.0, 'patates_douces': 1.7, 'igname': 2.1,
                'tomates': 2.6, 'oignons': 2.3, 'carottes': 1.9, 'salade': 2.4,
                'bananes': 1.8, 'ananas': 2.3, 'mangues': 2.8, 'avocats': 3.3,
                'poulet': 6.7, 'bœuf': 12.3, 'porc': 8.7, 'poisson': 11.8,
                'crevettes': 15.4, 'langouste': 25.7, 'lait': 1.25, 'œufs': 0.23,
                'sucre': 1.45, 'café': 4.9, 'vin': 5.2, 'biere': 2.6,
                'farine': 1.35, 'huile': 2.2, 'pain': 3.1, 'fromage': 12.3,
                'citrouille': 1.8, 'chou': 2.0, 'concombre': 2.2, 'poivrons': 3.3
            },
            '2004': {
                'riz': 2.0, 'pommes_de_terre': 2.1, 'patates_douces': 1.8, 'igname': 2.2,
                'tomates': 2.7, 'oignons': 2.4, 'carottes': 2.0, 'salade': 2.5,
                'bananes': 1.9, 'ananas': 2.4, 'mangues': 2.9, 'avocats': 3.4,
                'poulet': 6.9, 'bœuf': 12.6, 'porc': 8.9, 'poisson': 12.1,
                'crevettes': 15.8, 'langouste': 26.4, 'lait': 1.3, 'œufs': 0.24,
                'sucre': 1.5, 'café': 5.0, 'vin': 5.4, 'biere': 2.7,
                'farine': 1.4, 'huile': 2.3, 'pain': 3.2, 'fromage': 12.6,
                'citrouille': 1.9, 'chou': 2.1, 'concombre': 2.3, 'poivrons': 3.4
            },
            '2005': {
                'riz': 2.1, 'pommes_de_terre': 2.2, 'patates_douces': 1.9, 'igname': 2.3,
                'tomates': 2.8, 'oignons': 2.5, 'carottes': 2.1, 'salade': 2.6,
                'bananes': 2.0, 'ananas': 2.5, 'mangues': 3.0, 'avocats': 3.5,
                'poulet': 7.1, 'bœuf': 12.9, 'porc': 9.1, 'poisson': 12.4,
                'crevettes': 16.2, 'langouste': 27.1, 'lait': 1.35, 'œufs': 0.25,
                'sucre': 1.55, 'café': 5.1, 'vin': 5.6, 'biere': 2.8,
                'farine': 1.45, 'huile': 2.4, 'pain': 3.3, 'fromage': 12.9,
                'citrouille': 2.0, 'chou': 2.2, 'concombre': 2.4, 'poivrons': 3.5
            },
            '2006': {
                'riz': 2.2, 'pommes_de_terre': 2.3, 'patates_douces': 2.0, 'igname': 2.4,
                'tomates': 2.9, 'oignons': 2.6, 'carottes': 2.2, 'salade': 2.7,
                'bananes': 2.1, 'ananas': 2.6, 'mangues': 3.1, 'avocats': 3.6,
                'poulet': 7.3, 'bœuf': 13.2, 'porc': 9.3, 'poisson': 12.7,
                'crevettes': 16.6, 'langouste': 27.8, 'lait': 1.4, 'œufs': 0.26,
                'sucre': 1.6, 'café': 5.2, 'vin': 5.8, 'biere': 2.9,
                'farine': 1.5, 'huile': 2.5, 'pain': 3.4, 'fromage': 13.2,
                'citrouille': 2.1, 'chou': 2.3, 'concombre': 2.5, 'poivrons': 3.6
            },
            '2007': {
                'riz': 2.3, 'pommes_de_terre': 2.4, 'patates_douces': 2.1, 'igname': 2.5,
                'tomates': 3.0, 'oignons': 2.7, 'carottes': 2.3, 'salade': 2.8,
                'bananes': 2.2, 'ananas': 2.7, 'mangues': 3.2, 'avocats': 3.7,
                'poulet': 7.5, 'bœuf': 13.5, 'porc': 9.5, 'poisson': 13.0,
                'crevettes': 17.0, 'langouste': 28.5, 'lait': 1.45, 'œufs': 0.27,
                'sucre': 1.65, 'café': 5.3, 'vin': 6.0, 'biere': 3.0,
                'farine': 1.55, 'huile': 2.6, 'pain': 3.5, 'fromage': 13.5,
                'citrouille': 2.2, 'chou': 2.4, 'concombre': 2.6, 'poivrons': 3.7
            },
            '2008': {
                'riz': 2.4, 'pommes_de_terre': 2.5, 'patates_douces': 2.2, 'igname': 2.6,
                'tomates': 3.1, 'oignons': 2.8, 'carottes': 2.4, 'salade': 2.9,
                'bananes': 2.3, 'ananas': 2.8, 'mangues': 3.3, 'avocats': 3.8,
                'poulet': 7.7, 'bœuf': 13.8, 'porc': 9.7, 'poisson': 13.3,
                'crevettes': 17.4, 'langouste': 29.2, 'lait': 1.5, 'œufs': 0.28,
                'sucre': 1.7, 'café': 5.4, 'vin': 6.2, 'biere': 3.1,
                'farine': 1.6, 'huile': 2.7, 'pain': 3.6, 'fromage': 13.8,
                'citrouille': 2.3, 'chou': 2.5, 'concombre': 2.7, 'poivrons': 3.8
            },
            '2009': {
                'riz': 2.5, 'pommes_de_terre': 2.6, 'patates_douces': 2.3, 'igname': 2.7,
                'tomates': 3.2, 'oignons': 2.9, 'carottes': 2.5, 'salade': 3.0,
                'bananes': 2.4, 'ananas': 2.9, 'mangues': 3.4, 'avocats': 3.9,
                'poulet': 7.9, 'bœuf': 14.1, 'porc': 9.9, 'poisson': 13.6,
                'crevettes': 17.8, 'langouste': 29.9, 'lait': 1.55, 'œufs': 0.29,
                'sucre': 1.75, 'café': 5.5, 'vin': 6.4, 'biere': 3.2,
                'farine': 1.65, 'huile': 2.8, 'pain': 3.7, 'fromage': 14.1,
                'citrouille': 2.4, 'chou': 2.6, 'concombre': 2.8, 'poivrons': 3.9
            },
            '2010': {
                'riz': 2.6, 'pommes_de_terre': 2.7, 'patates_douces': 2.4, 'igname': 2.8,
                'tomates': 3.3, 'oignons': 3.0, 'carottes': 2.6, 'salade': 3.1,
                'bananes': 2.5, 'ananas': 3.0, 'mangues': 3.5, 'avocats': 4.0,
                'poulet': 8.1, 'bœuf': 14.4, 'porc': 10.1, 'poisson': 13.9,
                'crevettes': 18.2, 'langouste': 30.6, 'lait': 1.6, 'œufs': 0.30,
                'sucre': 1.8, 'café': 5.6, 'vin': 6.6, 'biere': 3.3,
                'farine': 1.7, 'huile': 2.9, 'pain': 3.8, 'fromage': 14.4,
                'citrouille': 2.5, 'chou': 2.7, 'concombre': 2.9, 'poivrons': 4.0
            },
            '2011': {
                'riz': 2.7, 'pommes_de_terre': 2.8, 'patates_douces': 2.5, 'igname': 2.9,
                'tomates': 3.4, 'oignons': 3.1, 'carottes': 2.7, 'salade': 3.2,
                'bananes': 2.6, 'ananas': 3.1, 'mangues': 3.6, 'avocats': 4.1,
                'poulet': 8.3, 'bœuf': 14.7, 'porc': 10.3, 'poisson': 14.2,
                'crevettes': 18.6, 'langouste': 31.3, 'lait': 1.65, 'œufs': 0.31,
                'sucre': 1.85, 'café': 5.7, 'vin': 6.8, 'biere': 3.4,
                'farine': 1.75, 'huile': 3.0, 'pain': 3.9, 'fromage': 14.7,
                'citrouille': 2.6, 'chou': 2.8, 'concombre': 3.0, 'poivrons': 4.1
            },
            '2012': {
                'riz': 2.8, 'pommes_de_terre': 2.9, 'patates_douces': 2.6, 'igname': 3.0,
                'tomates': 3.5, 'oignons': 3.2, 'carottes': 2.8, 'salade': 3.3,
                'bananes': 2.7, 'ananas': 3.2, 'mangues': 3.7, 'avocats': 4.2,
                'poulet': 8.5, 'bœuf': 15.0, 'porc': 10.5, 'poisson': 14.5,
                'crevettes': 19.0, 'langouste': 32.0, 'lait': 1.7, 'œufs': 0.32,
                'sucre': 1.9, 'café': 5.8, 'vin': 7.0, 'biere': 3.5,
                'farine': 1.8, 'huile': 3.1, 'pain': 4.0, 'fromage': 15.0,
                'citrouille': 2.7, 'chou': 2.9, 'concombre': 3.1, 'poivrons': 4.2
            },
            '2013': {
                'riz': 2.9, 'pommes_de_terre': 3.0, 'patates_douces': 2.7, 'igname': 3.1,
                'tomates': 3.6, 'oignons': 3.3, 'carottes': 2.9, 'salade': 3.4,
                'bananes': 2.8, 'ananas': 3.3, 'mangues': 3.8, 'avocats': 4.3,
                'poulet': 8.7, 'bœuf': 15.3, 'porc': 10.7, 'poisson': 14.8,
                'crevettes': 19.4, 'langouste': 32.7, 'lait': 1.75, 'œufs': 0.33,
                'sucre': 1.95, 'café': 5.9, 'vin': 7.2, 'biere': 3.6,
                'farine': 1.85, 'huile': 3.2, 'pain': 4.1, 'fromage': 15.3,
                'citrouille': 2.8, 'chou': 3.0, 'concombre': 3.2, 'poivrons': 4.3
            },
            '2014': {
                'riz': 3.0, 'pommes_de_terre': 3.1, 'patates_douces': 2.8, 'igname': 3.2,
                'tomates': 3.7, 'oignons': 3.4, 'carottes': 3.0, 'salade': 3.5,
                'bananes': 2.9, 'ananas': 3.4, 'mangues': 3.9, 'avocats': 4.4,
                'poulet': 8.9, 'bœuf': 15.6, 'porc': 10.9, 'poisson': 15.1,
                'crevettes': 19.8, 'langouste': 33.4, 'lait': 1.8, 'œufs': 0.34,
                'sucre': 2.0, 'café': 6.0, 'vin': 7.4, 'biere': 3.7,
                'farine': 1.9, 'huile': 3.3, 'pain': 4.2, 'fromage': 15.6,
                'citrouille': 2.9, 'chou': 3.1, 'concombre': 3.3, 'poivrons': 4.4
            },
            '2015': {
                'riz': 3.1, 'pommes_de_terre': 3.2, 'patates_douces': 2.9, 'igname': 3.3,
                'tomates': 3.8, 'oignons': 3.5, 'carottes': 3.1, 'salade': 3.6,
                'bananes': 3.0, 'ananas': 3.5, 'mangues': 4.0, 'avocats': 4.5,
                'poulet': 9.1, 'bœuf': 15.9, 'porc': 11.1, 'poisson': 15.4,
                'crevettes': 20.2, 'langouste': 34.1, 'lait': 1.85, 'œufs': 0.35,
                'sucre': 2.05, 'café': 6.1, 'vin': 7.6, 'biere': 3.8,
                'farine': 1.95, 'huile': 3.4, 'pain': 4.3, 'fromage': 15.9,
                'citrouille': 3.0, 'chou': 3.2, 'concombre': 3.4, 'poivrons': 4.5
            },
            '2016': {
                'riz': 3.2, 'pommes_de_terre': 3.3, 'patates_douces': 3.0, 'igname': 3.4,
                'tomates': 3.9, 'oignons': 3.6, 'carottes': 3.2, 'salade': 3.7,
                'bananes': 3.1, 'ananas': 3.6, 'mangues': 4.1, 'avocats': 4.6,
                'poulet': 9.3, 'bœuf': 16.2, 'porc': 11.3, 'poisson': 15.7,
                'crevettes': 20.6, 'langouste': 34.8, 'lait': 1.9, 'œufs': 0.36,
                'sucre': 2.1, 'café': 6.2, 'vin': 7.8, 'biere': 3.9,
                'farine': 2.0, 'huile': 3.5, 'pain': 4.4, 'fromage': 16.2,
                'citrouille': 3.1, 'chou': 3.3, 'concombre': 3.5, 'poivrons': 4.6
            },
            '2017': {
                'riz': 3.3, 'pommes_de_terre': 3.4, 'patates_douces': 3.1, 'igname': 3.5,
                'tomates': 4.0, 'oignons': 3.7, 'carottes': 3.3, 'salade': 3.8,
                'bananes': 3.2, 'ananas': 3.7, 'mangues': 4.2, 'avocats': 4.7,
                'poulet': 9.5, 'bœuf': 16.5, 'porc': 11.5, 'poisson': 16.0,
                'crevettes': 21.0, 'langouste': 35.5, 'lait': 1.95, 'œufs': 0.37,
                'sucre': 2.15, 'café': 6.3, 'vin': 8.0, 'biere': 4.0,
                'farine': 2.05, 'huile': 3.6, 'pain': 4.5, 'fromage': 16.5,
                'citrouille': 3.2, 'chou': 3.4, 'concombre': 3.6, 'poivrons': 4.7
            },
            '2018': {
                'riz': 3.4, 'pommes_de_terre': 3.5, 'patates_douces': 3.2, 'igname': 3.6,
                'tomates': 4.1, 'oignons': 3.8, 'carottes': 3.4, 'salade': 3.9,
                'bananes': 3.3, 'ananas': 3.8, 'mangues': 4.3, 'avocats': 4.8,
                'poulet': 9.7, 'bœuf': 16.8, 'porc': 11.7, 'poisson': 16.3,
                'crevettes': 21.4, 'langouste': 36.2, 'lait': 2.0, 'œufs': 0.38,
                'sucre': 2.2, 'café': 6.4, 'vin': 8.2, 'biere': 4.1,
                'farine': 2.1, 'huile': 3.7, 'pain': 4.6, 'fromage': 16.8,
                'citrouille': 3.3, 'chou': 3.5, 'concombre': 3.7, 'poivrons': 4.8
            },
            '2019': {
                'riz': 3.5, 'pommes_de_terre': 3.6, 'patates_douces': 3.3, 'igname': 3.7,
                'tomates': 4.2, 'oignons': 3.9, 'carottes': 3.5, 'salade': 4.0,
                'bananes': 3.4, 'ananas': 3.9, 'mangues': 4.4, 'avocats': 4.9,
                'poulet': 9.9, 'bœuf': 17.1, 'porc': 11.9, 'poisson': 16.6,
                'crevettes': 21.8, 'langouste': 36.9, 'lait': 2.05, 'œufs': 0.39,
                'sucre': 2.25, 'café': 6.5, 'vin': 8.4, 'biere': 4.2,
                'farine': 2.15, 'huile': 3.8, 'pain': 4.7, 'fromage': 17.1,
                'citrouille': 3.4, 'chou': 3.6, 'concombre': 3.8, 'poivrons': 4.9
            },
            '2020': {
                'riz': 3.7, 'pommes_de_terre': 3.8, 'patates_douces': 3.5, 'igname': 3.9,
                'tomates': 4.4, 'oignons': 4.1, 'carottes': 3.7, 'salade': 4.2,
                'bananes': 3.6, 'ananas': 4.1, 'mangues': 4.6, 'avocats': 5.1,
                'poulet': 10.3, 'bœuf': 17.7, 'porc': 12.3, 'poisson': 17.2,
                'crevettes': 22.6, 'langouste': 38.3, 'lait': 2.15, 'œufs': 0.41,
                'sucre': 2.35, 'café': 6.7, 'vin': 8.8, 'biere': 4.4,
                'farine': 2.25, 'huile': 4.0, 'pain': 4.9, 'fromage': 17.7,
                'citrouille': 3.6, 'chou': 3.8, 'concombre': 4.0, 'poivrons': 5.1
            },
            '2021': {
                'riz': 3.9, 'pommes_de_terre': 4.0, 'patates_douces': 3.7, 'igname': 4.1,
                'tomates': 4.6, 'oignons': 4.3, 'carottes': 3.9, 'salade': 4.4,
                'bananes': 3.8, 'ananas': 4.3, 'mangues': 4.8, 'avocats': 5.3,
                'poulet': 10.7, 'bœuf': 18.3, 'porc': 12.7, 'poisson': 17.8,
                'crevettes': 23.4, 'langouste': 39.7, 'lait': 2.25, 'œufs': 0.43,
                'sucre': 2.45, 'café': 6.9, 'vin': 9.2, 'biere': 4.6,
                'farine': 2.35, 'huile': 4.2, 'pain': 5.1, 'fromage': 18.3,
                'citrouille': 3.8, 'chou': 4.0, 'concombre': 4.2, 'poivrons': 5.3
            },
            '2022': {
                'riz': 4.1, 'pommes_de_terre': 4.2, 'patates_douces': 3.9, 'igname': 4.3,
                'tomates': 4.8, 'oignons': 4.5, 'carottes': 4.1, 'salade': 4.6,
                'bananes': 4.0, 'ananas': 4.5, 'mangues': 5.0, 'avocats': 5.5,
                'poulet': 11.1, 'bœuf': 18.9, 'porc': 13.1, 'poisson': 18.4,
                'crevettes': 24.2, 'langouste': 41.1, 'lait': 2.35, 'œufs': 0.45,
                'sucre': 2.55, 'café': 7.1, 'vin': 9.6, 'biere': 4.8,
                'farine': 2.45, 'huile': 4.4, 'pain': 5.3, 'fromage': 18.9,
                'citrouille': 4.0, 'chou': 4.2, 'concombre': 4.4, 'poivrons': 5.5
            },
            '2023': {
                'riz': 4.3, 'pommes_de_terre': 4.4, 'patates_douces': 4.1, 'igname': 4.5,
                'tomates': 5.0, 'oignons': 4.7, 'carottes': 4.3, 'salade': 4.8,
                'bananes': 4.2, 'ananas': 4.7, 'mangues': 5.2, 'avocats': 5.7,
                'poulet': 11.5, 'bœuf': 19.5, 'porc': 13.5, 'poisson': 19.0,
                'crevettes': 25.0, 'langouste': 42.5, 'lait': 2.45, 'œufs': 0.47,
                'sucre': 2.65, 'café': 7.3, 'vin': 10.0, 'biere': 5.0,
                'farine': 2.55, 'huile': 4.6, 'pain': 5.5, 'fromage': 19.5,
                'citrouille': 4.2, 'chou': 4.4, 'concombre': 4.6, 'poivrons': 5.7
            },
            '2024': {
                'riz': 4.5, 'pommes_de_terre': 4.6, 'patates_douces': 4.3, 'igname': 4.7,
                'tomates': 5.2, 'oignons': 4.9, 'carottes': 4.5, 'salade': 5.0,
                'bananes': 4.4, 'ananas': 4.9, 'mangues': 5.4, 'avocats': 5.9,
                'poulet': 11.9, 'bœuf': 20.1, 'porc': 13.9, 'poisson': 19.6,
                'crevettes': 25.8, 'langouste': 43.9, 'lait': 2.55, 'œufs': 0.49,
                'sucre': 2.75, 'café': 7.5, 'vin': 10.4, 'biere': 5.2,
                'farine': 2.65, 'huile': 4.8, 'pain': 5.7, 'fromage': 20.1,
                'citrouille': 4.4, 'chou': 4.6, 'concombre': 4.8, 'poivrons': 5.9
            },
            '2025': {
                'riz': 4.7, 'pommes_de_terre': 4.8, 'patates_douces': 4.5, 'igname': 4.9,
                'tomates': 5.4, 'oignons': 5.1, 'carottes': 4.7, 'salade': 5.2,
                'bananes': 4.6, 'ananas': 5.1, 'mangues': 5.6, 'avocats': 6.1,
                'poulet': 12.3, 'bœuf': 20.7, 'porc': 14.3, 'poisson': 20.2,
                'crevettes': 26.6, 'langouste': 45.3, 'lait': 2.65, 'œufs': 0.51,
                'sucre': 2.85, 'café': 7.7, 'vin': 10.8, 'biere': 5.4,
                'farine': 2.75, 'huile': 5.0, 'pain': 5.9, 'fromage': 20.7,
                'citrouille': 4.6, 'chou': 4.8, 'concombre': 5.0, 'poivrons': 6.1
            }
        }
        
        # Inflation annuelle en Nouvelle-Calédonie (en %)
        self.inflation_rates = {
            '2002': 2.1, '2003': 2.3, '2004': 2.5, '2005': 2.7,
            '2006': 2.9, '2007': 3.1, '2008': 3.3, '2009': 3.5,
            '2010': 3.7, '2011': 3.9, '2012': 4.1, '2013': 4.3,
            '2014': 4.5, '2015': 4.7, '2016': 4.9, '2017': 5.1,
            '2018': 5.3, '2019': 5.5, '2020': 6.0, '2021': 6.5,
            '2022': 7.0, '2023': 7.5, '2024': 8.0, '2025': 8.5
        }
    
    def get_mercuriales_data(self):
        """
        Récupère toutes les données des mercuriales
        """
        print("🚀 Début de la récupération des données des mercuriales de la Nouvelle-Calédonie...\n")
        
        all_data = []
        
        for year in range(2002, 2026):
            year_str = str(year)
            if year_str in self.mercuriales_data:
                data = self.mercuriales_data[year_str].copy()
                data['year'] = year
                data['inflation'] = self.inflation_rates[year_str]
                all_data.append(data)
        
        # Créer le DataFrame final
        df = pd.DataFrame(all_data)
        
        # Calculer les prix ajustés de l'inflation (base 2002)
        base_year = 2002
        inflation_index = {}
        cumulative_inflation = 1.0
        
        for year in range(2002, 2026):
            year_str = str(year)
            if year == base_year:
                inflation_index[year] = 1.0
            else:
                cumulative_inflation *= (1 + self.inflation_rates[str(year-1)]/100)
                inflation_index[year] = cumulative_inflation
        
        # Ajouter les prix ajustés pour chaque produit
        products = ['riz', 'pommes_de_terre', 'patates_douces', 'igname', 'tomates', 'oignons', 
                   'carottes', 'salade', 'bananes', 'ananas', 'mangues', 'avocats', 'poulet', 
                   'bœuf', 'porc', 'poisson', 'crevettes', 'langouste', 'lait', 'œufs', 
                   'sucre', 'café', 'vin', 'biere', 'farine', 'huile', 'pain', 'fromage',
                   'citrouille', 'chou', 'concombre', 'poivrons']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations basées sur la consommation moyenne en Nouvelle-Calédonie
        weights = {
            'riz': 0.10, 'pommes_de_terre': 0.06, 'patates_douces': 0.05, 'igname': 0.04,
            'tomates': 0.04, 'oignons': 0.03, 'carottes': 0.03, 'salade': 0.03,
            'bananes': 0.07, 'ananas': 0.04, 'mangues': 0.04, 'avocats': 0.03,
            'poulet': 0.08, 'bœuf': 0.07, 'porc': 0.06, 'poisson': 0.08,
            'crevettes': 0.03, 'langouste': 0.02, 'lait': 0.05, 'œufs': 0.04,
            'sucre': 0.02, 'café': 0.02, 'vin': 0.03, 'biere': 0.02,
            'farine': 0.03, 'huile': 0.02, 'pain': 0.04, 'fromage': 0.03,
            'citrouille': 0.02, 'chou': 0.02, 'concombre': 0.02, 'poivrons': 0.02
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_nouvelle_caledonie_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_nouvelle_caledonie_2002_2025.csv'")
        
        return df
    
    def create_price_evolution_charts(self, df):
        """Crée des graphiques d'évolution des prix"""
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = (15, 10)
        plt.rcParams['font.size'] = 12
        
        # 1. Graphique des produits de base
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Céréales et légumes de base
        axes[0, 0].plot(df['year'], df['riz'], label='Riz', linewidth=2, marker='o')
        axes[0, 0].plot(df['year'], df['pommes_de_terre'], label='Pommes de terre', linewidth=2, marker='s')
        axes[0, 0].plot(df['year'], df['patates_douces'], label='Patates douces', linewidth=2, marker='^')
        axes[0, 0].plot(df['year'], df['igname'], label='Igname', linewidth=2, marker='d')
        axes[0, 0].set_title('Évolution des prix des céréales et légumes de base', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Fruits tropicaux
        axes[0, 1].plot(df['year'], df['bananes'], label='Bananes', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['ananas'], label='Ananas', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['mangues'], label='Mangues', linewidth=2, marker='^')
        axes[0, 1].plot(df['year'], df['avocats'], label='Avocats', linewidth=2, marker='d')
        axes[0, 1].set_title('Évolution des prix des fruits tropicaux', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Produits animaux
        axes[1, 0].plot(df['year'], df['poulet'], label='Poulet', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['bœuf'], label='Bœuf', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['porc'], label='Porc', linewidth=2, marker='^')
        axes[1, 0].plot(df['year'], df['poisson'], label='Poisson', linewidth=2, marker='d')
        axes[1, 0].set_title('Évolution des prix des produits animaux', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Produits de la mer
        axes[1, 1].plot(df['year'], df['crevettes'], label='Crevettes', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['langouste'], label='Langouste', linewidth=2, marker='s')
        axes[1, 1].set_title('Évolution des prix des produits de la mer', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_nouvelle_caledonie_evolution_prix.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        # 2. Graphique des indices et comparaisons
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Indice alimentaire général
        axes[0, 0].plot(df['year'], df['indice_alimentaire'], label='Indice alimentaire', 
                       linewidth=3, color='red', marker='o')
        axes[0, 0].plot(df['year'], df['inflation'] * 5 + 100, label='Inflation (x5 pour comparaison)', 
                       linewidth=2, color='blue', linestyle='--')
        axes[0, 0].set_title('Indice des prix alimentaires vs Inflation', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Indice (base 100 en 2002)', fontsize=12)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Comparaison produits ajustés inflation
        axes[0, 1].plot(df['year'], df['riz_ajusté'], label='Riz (ajusté)', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['poulet_ajusté'], label='Poulet (ajusté)', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['bananes_ajusté'], label='Bananes (ajusté)', linewidth=2, marker='^')
        axes[0, 1].set_title('Prix ajustés de l\'inflation (base 2002)', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Prix réel (€/kg de 2002)', fontsize=12)
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Évolution des produits laitiers et boulangerie
        axes[1, 0].plot(df['year'], df['lait'], label='Lait (€/L)', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['fromage'], label='Fromage (€/kg)', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['pain'], label='Pain (€/kg)', linewidth=2, marker='^')
        axes[1, 0].set_title('Évolution des prix des produits laitiers et boulangerie', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Taux d'inflation
        axes[1, 1].bar(df['year'], df['inflation'], color='orange', alpha=0.7)
        axes[1, 1].set_title('Taux d\'inflation annuel en Nouvelle-Calédonie', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_nouvelle_caledonie_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['riz', 'poulet', 'bananes', 'langouste']
        
        for i, year in enumerate(key_years):
            if i > 0:
                prev_year = key_years[i-1]
                for product in products:
                    key_df.loc[key_df['year'] == year, f'{product}_var'] = (
                        (key_df[key_df['year'] == year][product].values[0] - 
                         key_df[key_df['year'] == prev_year][product].values[0]) / 
                         key_df[key_df['year'] == prev_year][product].values[0] * 100
                    )
        
        # Formatage pour l'affichage
        display_df = key_df[['year', 'riz', 'poulet', 'bananes', 'langouste', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['riz', 'poulet', 'bananes', 'langouste']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Riz (€/kg)', 'Poulet (€/kg)', 'Bananes (€/kg)', 
                             'Langouste (€/kg)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_nouvelle_caledonie_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_nouvelle_caledonie_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE LA NOUVELLE-CALÉDONIE")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🌾 Prix moyen du riz: {df['riz'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🍌 Prix moyen des bananes: {df['bananes'].mean():.2f} €/kg")
        print(f"🦞 Prix moyen de la langouste: {df['langouste'].mean():.2f} €/kg")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['riz', 'poulet', 'bananes', 'langouste', 'indice_alimentaire']
        product_names = ['Riz', 'Poulet', 'Bananes', 'Langouste', 'Indice alimentaire']
        
        for product, name in zip(products, product_names):
            evolution = ((df[df['year'] == 2025][product].values[0] - 
                         df[df['year'] == 2002][product].values[0]) / 
                         df[df['year'] == 2002][product].values[0] * 100)
            print(f"{name}: {evolution:+.1f}%")
        
        # Analyse des tendances
        print(f"\n📅 TENDANCES PAR PÉRIODE")
        periods = {
            "2002-2007 (Stabilité)": (2002, 2007),
            "2008-2013 (Crise financière)": (2008, 2013),
            "2014-2019 (Croissance modérée)": (2014, 2019),
            "2020-2025 (COVID et inflation)": (2020, 2025)
        }
        
        for period_name, (start, end) in periods.items():
            period_df = df[(df['year'] >= start) & (df['year'] <= end)]
            avg_inflation = period_df['inflation'].mean()
            avg_food_index = period_df['indice_alimentaire'].mean()
            print(f"{period_name}: Inflation {avg_inflation:.1f}%, Indice alimentaire {avg_food_index:.1f}")
        
        # Produits avec la plus forte augmentation
        print(f"\n📈 PRODUITS AVEC LA PLUS FORTE AUGMENTATION (2002-2025)")
        products = ['riz', 'pommes_de_terre', 'patates_douces', 'igname', 'tomates', 'oignons', 
                   'carottes', 'salade', 'bananes', 'ananas', 'mangues', 'avocats', 'poulet', 
                   'bœuf', 'porc', 'poisson', 'crevettes', 'langouste', 'lait', 'œufs', 
                   'sucre', 'café', 'vin', 'biere', 'farine', 'huile', 'pain', 'fromage',
                   'citrouille', 'chou', 'concombre', 'poivrons']
        
        increases = []
        for product in products:
            increase = ((df[df['year'] == 2025][product].values[0] - 
                        df[df['year'] == 2002][product].values[0]) / 
                        df[df['year'] == 2002][product].values[0] * 100)
            increases.append((product, increase))
        
        # Trier par augmentation
        increases.sort(key=lambda x: x[1], reverse=True)
        
        for product, increase in increases[:5]:
            print(f"{product.capitalize()}: {increase:+.1f}%")
        
        # Recommandations
        print(f"\n💡 RECOMMANDATIONS")
        if df[df['year'] == 2025]['indice_alimentaire'].values[0] > 200:
            print("⚠️  L'indice alimentaire a plus que doublé depuis 2002")
            print("→ Nécessité de politiques de soutien au pouvoir d'achat")
        
        if (df[df['year'] == 2025]['riz'].values[0] / df[df['year'] == 2002]['riz'].values[0] > 
            df[df['year'] == 2025]['indice_alimentaire'].values[0] / 100):
            print("⚠️  Le prix du riz a augmenté plus que l'indice alimentaire moyen")
            print("→ Importance de la sécurité alimentaire pour les produits de base")
        
        # Spécificités néo-calédoniennes
        print(f"\n🌺 SPÉCIFICITÉS NÉO-CALÉDONIENNES")
        langouste_increase = ((df[df['year'] == 2025]['langouste'].values[0] - 
                             df[df['year'] == 2002]['langouste'].values[0]) / 
                             df[df['year'] == 2002]['langouste'].values[0] * 100)
        print(f"• La langouste, produit emblématique, a augmenté de {langouste_increase:.1f}%")
        
        produits_marins = ['crevettes', 'poisson']
        for produit in produits_marins:
            augmentation = ((df[df['year'] == 2025][produit].values[0] - 
                           df[df['year'] == 2002][produit].values[0]) / 
                           df[df['year'] == 2002][produit].values[0] * 100)
            print(f"• {produit.capitalize()}: {augmentation:+.1f}%")
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de la Nouvelle-Calédonie...")
        
        # Récupération des données
        df = self.get_mercuriales_data()
        
        # Génération des graphiques
        print("📈 Génération des graphiques d'évolution des prix...")
        self.create_price_evolution_charts(df)
        
        # Création du tableau d'analyse
        print("📊 Création du tableau d'analyse détaillée...")
        analysis_table = self.create_detailed_analysis_table(df)
        
        # Génération du rapport
        print("📝 Génération du rapport complet...")
        self.generate_comprehensive_report(df)
        
        # Affichage du tableau détaillé
        print("\n📋 TABLEAU D'ANALYSE DÉTAILLÉE (Années clés)")
        print(analysis_table.to_string(index=False))
        
        print(f"\n✅ Analyse terminée!")
        print("📁 Fichiers générés:")
        print("   - mercuriales_nouvelle_caledonie_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_nouvelle_caledonie_annees_cles.csv (années clés)")
        print("   - mercuriales_nouvelle_caledonie_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_nouvelle_caledonie_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = NouvelleCaledonieMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()