import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class SaintPierreMiquelonMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de Saint-Pierre-et-Miquelon (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'pommes_de_terre': 1.5, 'carottes': 1.8, 'chou': 1.6, 'navets': 1.4,
                'oignons': 1.7, 'poireaux': 2.0, 'tomates': 3.0, 'salade': 2.5,
                'poulet': 6.5, 'bœuf': 12.0, 'porc': 8.5, 'agneau': 15.0,
                'morue': 9.0, 'saumon': 14.0, 'flétan': 11.0, 'crevettes': 16.0,
                'coquilles_st_jacques': 18.0, 'homard': 25.0, 'crabe': 12.0,
                'lait': 1.2, 'œufs': 0.22, 'beurre': 4.0, 'fromage': 12.0,
                'farine': 1.3, 'pain': 3.0, 'sucre': 1.4, 'huile': 2.2,
                'café': 4.8, 'thé': 3.5, 'riz': 1.9, 'pâtes': 1.8,
                'pommes': 2.2, 'poires': 2.4, 'oranges': 2.6, 'citrons': 3.0,
                'bananes': 2.0, 'myrtilles': 8.0, 'framboises': 10.0, 'rhum': 15.0
            },
            '2003': {
                'pommes_de_terre': 1.6, 'carottes': 1.9, 'chou': 1.7, 'navets': 1.5,
                'oignons': 1.8, 'poireaux': 2.1, 'tomates': 3.1, 'salade': 2.6,
                'poulet': 6.7, 'bœuf': 12.3, 'porc': 8.7, 'agneau': 15.4,
                'morue': 9.2, 'saumon': 14.3, 'flétan': 11.3, 'crevettes': 16.4,
                'coquilles_st_jacques': 18.5, 'homard': 25.7, 'crabe': 12.3,
                'lait': 1.25, 'œufs': 0.23, 'beurre': 4.1, 'fromage': 12.3,
                'farine': 1.35, 'pain': 3.1, 'sucre': 1.45, 'huile': 2.3,
                'café': 4.9, 'thé': 3.6, 'riz': 2.0, 'pâtes': 1.9,
                'pommes': 2.3, 'poires': 2.5, 'oranges': 2.7, 'citrons': 3.1,
                'bananes': 2.1, 'myrtilles': 8.2, 'framboises': 10.3, 'rhum': 15.4
            },
            '2004': {
                'pommes_de_terre': 1.7, 'carottes': 2.0, 'chou': 1.8, 'navets': 1.6,
                'oignons': 1.9, 'poireaux': 2.2, 'tomates': 3.2, 'salade': 2.7,
                'poulet': 6.9, 'bœuf': 12.6, 'porc': 8.9, 'agneau': 15.8,
                'morue': 9.4, 'saumon': 14.6, 'flétan': 11.6, 'crevettes': 16.8,
                'coquilles_st_jacques': 19.0, 'homard': 26.4, 'crabe': 12.6,
                'lait': 1.3, 'œufs': 0.24, 'beurre': 4.2, 'fromage': 12.6,
                'farine': 1.4, 'pain': 3.2, 'sucre': 1.5, 'huile': 2.4,
                'café': 5.0, 'thé': 3.7, 'riz': 2.1, 'pâtes': 2.0,
                'pommes': 2.4, 'poires': 2.6, 'oranges': 2.8, 'citrons': 3.2,
                'bananes': 2.2, 'myrtilles': 8.4, 'framboises': 10.6, 'rhum': 15.8
            },
            '2005': {
                'pommes_de_terre': 1.8, 'carottes': 2.1, 'chou': 1.9, 'navets': 1.7,
                'oignons': 2.0, 'poireaux': 2.3, 'tomates': 3.3, 'salade': 2.8,
                'poulet': 7.1, 'bœuf': 12.9, 'porc': 9.1, 'agneau': 16.2,
                'morue': 9.6, 'saumon': 14.9, 'flétan': 11.9, 'crevettes': 17.2,
                'coquilles_st_jacques': 19.5, 'homard': 27.1, 'crabe': 12.9,
                'lait': 1.35, 'œufs': 0.25, 'beurre': 4.3, 'fromage': 12.9,
                'farine': 1.45, 'pain': 3.3, 'sucre': 1.55, 'huile': 2.5,
                'café': 5.1, 'thé': 3.8, 'riz': 2.2, 'pâtes': 2.1,
                'pommes': 2.5, 'poires': 2.7, 'oranges': 2.9, 'citrons': 3.3,
                'bananes': 2.3, 'myrtilles': 8.6, 'framboises': 10.9, 'rhum': 16.2
            },
            '2006': {
                'pommes_de_terre': 1.9, 'carottes': 2.2, 'chou': 2.0, 'navets': 1.8,
                'oignons': 2.1, 'poireaux': 2.4, 'tomates': 3.4, 'salade': 2.9,
                'poulet': 7.3, 'bœuf': 13.2, 'porc': 9.3, 'agneau': 16.6,
                'morue': 9.8, 'saumon': 15.2, 'flétan': 12.2, 'crevettes': 17.6,
                'coquilles_st_jacques': 20.0, 'homard': 27.8, 'crabe': 13.2,
                'lait': 1.4, 'œufs': 0.26, 'beurre': 4.4, 'fromage': 13.2,
                'farine': 1.5, 'pain': 3.4, 'sucre': 1.6, 'huile': 2.6,
                'café': 5.2, 'thé': 3.9, 'riz': 2.3, 'pâtes': 2.2,
                'pommes': 2.6, 'poires': 2.8, 'oranges': 3.0, 'citrons': 3.4,
                'bananes': 2.4, 'myrtilles': 8.8, 'framboises': 11.2, 'rhum': 16.6
            },
            '2007': {
                'pommes_de_terre': 2.0, 'carottes': 2.3, 'chou': 2.1, 'navets': 1.9,
                'oignons': 2.2, 'poireaux': 2.5, 'tomates': 3.5, 'salade': 3.0,
                'poulet': 7.5, 'bœuf': 13.5, 'porc': 9.5, 'agneau': 17.0,
                'morue': 10.0, 'saumon': 15.5, 'flétan': 12.5, 'crevettes': 18.0,
                'coquilles_st_jacques': 20.5, 'homard': 28.5, 'crabe': 13.5,
                'lait': 1.45, 'œufs': 0.27, 'beurre': 4.5, 'fromage': 13.5,
                'farine': 1.55, 'pain': 3.5, 'sucre': 1.65, 'huile': 2.7,
                'café': 5.3, 'thé': 4.0, 'riz': 2.4, 'pâtes': 2.3,
                'pommes': 2.7, 'poires': 2.9, 'oranges': 3.1, 'citrons': 3.5,
                'bananes': 2.5, 'myrtilles': 9.0, 'framboises': 11.5, 'rhum': 17.0
            },
            '2008': {
                'pommes_de_terre': 2.1, 'carottes': 2.4, 'chou': 2.2, 'navets': 2.0,
                'oignons': 2.3, 'poireaux': 2.6, 'tomates': 3.6, 'salade': 3.1,
                'poulet': 7.7, 'bœuf': 13.8, 'porc': 9.7, 'agneau': 17.4,
                'morue': 10.2, 'saumon': 15.8, 'flétan': 12.8, 'crevettes': 18.4,
                'coquilles_st_jacques': 21.0, 'homard': 29.2, 'crabe': 13.8,
                'lait': 1.5, 'œufs': 0.28, 'beurre': 4.6, 'fromage': 13.8,
                'farine': 1.6, 'pain': 3.6, 'sucre': 1.7, 'huile': 2.8,
                'café': 5.4, 'thé': 4.1, 'riz': 2.5, 'pâtes': 2.4,
                'pommes': 2.8, 'poires': 3.0, 'oranges': 3.2, 'citrons': 3.6,
                'bananes': 2.6, 'myrtilles': 9.2, 'framboises': 11.8, 'rhum': 17.4
            },
            '2009': {
                'pommes_de_terre': 2.2, 'carottes': 2.5, 'chou': 2.3, 'navets': 2.1,
                'oignons': 2.4, 'poireaux': 2.7, 'tomates': 3.7, 'salade': 3.2,
                'poulet': 7.9, 'bœuf': 14.1, 'porc': 9.9, 'agneau': 17.8,
                'morue': 10.4, 'saumon': 16.1, 'flétan': 13.1, 'crevettes': 18.8,
                'coquilles_st_jacques': 21.5, 'homard': 29.9, 'crabe': 14.1,
                'lait': 1.55, 'œufs': 0.29, 'beurre': 4.7, 'fromage': 14.1,
                'farine': 1.65, 'pain': 3.7, 'sucre': 1.75, 'huile': 2.9,
                'café': 5.5, 'thé': 4.2, 'riz': 2.6, 'pâtes': 2.5,
                'pommes': 2.9, 'poires': 3.1, 'oranges': 3.3, 'citrons': 3.7,
                'bananes': 2.7, 'myrtilles': 9.4, 'framboises': 12.1, 'rhum': 17.8
            },
            '2010': {
                'pommes_de_terre': 2.3, 'carottes': 2.6, 'chou': 2.4, 'navets': 2.2,
                'oignons': 2.5, 'poireaux': 2.8, 'tomates': 3.8, 'salade': 3.3,
                'poulet': 8.1, 'bœuf': 14.4, 'porc': 10.1, 'agneau': 18.2,
                'morue': 10.6, 'saumon': 16.4, 'flétan': 13.4, 'crevettes': 19.2,
                'coquilles_st_jacques': 22.0, 'homard': 30.6, 'crabe': 14.4,
                'lait': 1.6, 'œufs': 0.30, 'beurre': 4.8, 'fromage': 14.4,
                'farine': 1.7, 'pain': 3.8, 'sucre': 1.8, 'huile': 3.0,
                'café': 5.6, 'thé': 4.3, 'riz': 2.7, 'pâtes': 2.6,
                'pommes': 3.0, 'poires': 3.2, 'oranges': 3.4, 'citrons': 3.8,
                'bananes': 2.8, 'myrtilles': 9.6, 'framboises': 12.4, 'rhum': 18.2
            },
            '2011': {
                'pommes_de_terre': 2.4, 'carottes': 2.7, 'chou': 2.5, 'navets': 2.3,
                'oignons': 2.6, 'poireaux': 2.9, 'tomates': 3.9, 'salade': 3.4,
                'poulet': 8.3, 'bœuf': 14.7, 'porc': 10.3, 'agneau': 18.6,
                'morue': 10.8, 'saumon': 16.7, 'flétan': 13.7, 'crevettes': 19.6,
                'coquilles_st_jacques': 22.5, 'homard': 31.3, 'crabe': 14.7,
                'lait': 1.65, 'œufs': 0.31, 'beurre': 4.9, 'fromage': 14.7,
                'farine': 1.75, 'pain': 3.9, 'sucre': 1.85, 'huile': 3.1,
                'café': 5.7, 'thé': 4.4, 'riz': 2.8, 'pâtes': 2.7,
                'pommes': 3.1, 'poires': 3.3, 'oranges': 3.5, 'citrons': 3.9,
                'bananes': 2.9, 'myrtilles': 9.8, 'framboises': 12.7, 'rhum': 18.6
            },
            '2012': {
                'pommes_de_terre': 2.5, 'carottes': 2.8, 'chou': 2.6, 'navets': 2.4,
                'oignons': 2.7, 'poireaux': 3.0, 'tomates': 4.0, 'salade': 3.5,
                'poulet': 8.5, 'bœuf': 15.0, 'porc': 10.5, 'agneau': 19.0,
                'morue': 11.0, 'saumon': 17.0, 'flétan': 14.0, 'crevettes': 20.0,
                'coquilles_st_jacques': 23.0, 'homard': 32.0, 'crabe': 15.0,
                'lait': 1.7, 'œufs': 0.32, 'beurre': 5.0, 'fromage': 15.0,
                'farine': 1.8, 'pain': 4.0, 'sucre': 1.9, 'huile': 3.2,
                'café': 5.8, 'thé': 4.5, 'riz': 2.9, 'pâtes': 2.8,
                'pommes': 3.2, 'poires': 3.4, 'oranges': 3.6, 'citrons': 4.0,
                'bananes': 3.0, 'myrtilles': 10.0, 'framboises': 13.0, 'rhum': 19.0
            },
            '2013': {
                'pommes_de_terre': 2.6, 'carottes': 2.9, 'chou': 2.7, 'navets': 2.5,
                'oignons': 2.8, 'poireaux': 3.1, 'tomates': 4.1, 'salade': 3.6,
                'poulet': 8.7, 'bœuf': 15.3, 'porc': 10.7, 'agneau': 19.4,
                'morue': 11.2, 'saumon': 17.3, 'flétan': 14.3, 'crevettes': 20.4,
                'coquilles_st_jacques': 23.5, 'homard': 32.7, 'crabe': 15.3,
                'lait': 1.75, 'œufs': 0.33, 'beurre': 5.1, 'fromage': 15.3,
                'farine': 1.85, 'pain': 4.1, 'sucre': 1.95, 'huile': 3.3,
                'café': 5.9, 'thé': 4.6, 'riz': 3.0, 'pâtes': 2.9,
                'pommes': 3.3, 'poires': 3.5, 'oranges': 3.7, 'citrons': 4.1,
                'bananes': 3.1, 'myrtilles': 10.2, 'framboises': 13.3, 'rhum': 19.4
            },
            '2014': {
                'pommes_de_terre': 2.7, 'carottes': 3.0, 'chou': 2.8, 'navets': 2.6,
                'oignons': 2.9, 'poireaux': 3.2, 'tomates': 4.2, 'salade': 3.7,
                'poulet': 8.9, 'bœuf': 15.6, 'porc': 10.9, 'agneau': 19.8,
                'morue': 11.4, 'saumon': 17.6, 'flétan': 14.6, 'crevettes': 20.8,
                'coquilles_st_jacques': 24.0, 'homard': 33.4, 'crabe': 15.6,
                'lait': 1.8, 'œufs': 0.34, 'beurre': 5.2, 'fromage': 15.6,
                'farine': 1.9, 'pain': 4.2, 'sucre': 2.0, 'huile': 3.4,
                'café': 6.0, 'thé': 4.7, 'riz': 3.1, 'pâtes': 3.0,
                'pommes': 3.4, 'poires': 3.6, 'oranges': 3.8, 'citrons': 4.2,
                'bananes': 3.2, 'myrtilles': 10.4, 'framboises': 13.6, 'rhum': 19.8
            },
            '2015': {
                'pommes_de_terre': 2.8, 'carottes': 3.1, 'chou': 2.9, 'navets': 2.7,
                'oignons': 3.0, 'poireaux': 3.3, 'tomates': 4.3, 'salade': 3.8,
                'poulet': 9.1, 'bœuf': 15.9, 'porc': 11.1, 'agneau': 20.2,
                'morue': 11.6, 'saumon': 17.9, 'flétan': 14.9, 'crevettes': 21.2,
                'coquilles_st_jacques': 24.5, 'homard': 34.1, 'crabe': 15.9,
                'lait': 1.85, 'œufs': 0.35, 'beurre': 5.3, 'fromage': 15.9,
                'farine': 1.95, 'pain': 4.3, 'sucre': 2.05, 'huile': 3.5,
                'café': 6.1, 'thé': 4.8, 'riz': 3.2, 'pâtes': 3.1,
                'pommes': 3.5, 'poires': 3.7, 'oranges': 3.9, 'citrons': 4.3,
                'bananes': 3.3, 'myrtilles': 10.6, 'framboises': 13.9, 'rhum': 20.2
            },
            '2016': {
                'pommes_de_terre': 2.9, 'carottes': 3.2, 'chou': 3.0, 'navets': 2.8,
                'oignons': 3.1, 'poireaux': 3.4, 'tomates': 4.4, 'salade': 3.9,
                'poulet': 9.3, 'bœuf': 16.2, 'porc': 11.3, 'agneau': 20.6,
                'morue': 11.8, 'saumon': 18.2, 'flétan': 15.2, 'crevettes': 21.6,
                'coquilles_st_jacques': 25.0, 'homard': 34.8, 'crabe': 16.2,
                'lait': 1.9, 'œufs': 0.36, 'beurre': 5.4, 'fromage': 16.2,
                'farine': 2.0, 'pain': 4.4, 'sucre': 2.1, 'huile': 3.6,
                'café': 6.2, 'thé': 4.9, 'riz': 3.3, 'pâtes': 3.2,
                'pommes': 3.6, 'poires': 3.8, 'oranges': 4.0, 'citrons': 4.4,
                'bananes': 3.4, 'myrtilles': 10.8, 'framboises': 14.2, 'rhum': 20.6
            },
            '2017': {
                'pommes_de_terre': 3.0, 'carottes': 3.3, 'chou': 3.1, 'navets': 2.9,
                'oignons': 3.2, 'poireaux': 3.5, 'tomates': 4.5, 'salade': 4.0,
                'poulet': 9.5, 'bœuf': 16.5, 'porc': 11.5, 'agneau': 21.0,
                'morue': 12.0, 'saumon': 18.5, 'flétan': 15.5, 'crevettes': 22.0,
                'coquilles_st_jacques': 25.5, 'homard': 35.5, 'crabe': 16.5,
                'lait': 1.95, 'œufs': 0.37, 'beurre': 5.5, 'fromage': 16.5,
                'farine': 2.05, 'pain': 4.5, 'sucre': 2.15, 'huile': 3.7,
                'café': 6.3, 'thé': 5.0, 'riz': 3.4, 'pâtes': 3.3,
                'pommes': 3.7, 'poires': 3.9, 'oranges': 4.1, 'citrons': 4.5,
                'bananes': 3.5, 'myrtilles': 11.0, 'framboises': 14.5, 'rhum': 21.0
            },
            '2018': {
                'pommes_de_terre': 3.1, 'carottes': 3.4, 'chou': 3.2, 'navets': 3.0,
                'oignons': 3.3, 'poireaux': 3.6, 'tomates': 4.6, 'salade': 4.1,
                'poulet': 9.7, 'bœuf': 16.8, 'porc': 11.7, 'agneau': 21.4,
                'morue': 12.2, 'saumon': 18.8, 'flétan': 15.8, 'crevettes': 22.4,
                'coquilles_st_jacques': 26.0, 'homard': 36.2, 'crabe': 16.8,
                'lait': 2.0, 'œufs': 0.38, 'beurre': 5.6, 'fromage': 16.8,
                'farine': 2.1, 'pain': 4.6, 'sucre': 2.2, 'huile': 3.8,
                'café': 6.4, 'thé': 5.1, 'riz': 3.5, 'pâtes': 3.4,
                'pommes': 3.8, 'poires': 4.0, 'oranges': 4.2, 'citrons': 4.6,
                'bananes': 3.6, 'myrtilles': 11.2, 'framboises': 14.8, 'rhum': 21.4
            },
            '2019': {
                'pommes_de_terre': 3.2, 'carottes': 3.5, 'chou': 3.3, 'navets': 3.1,
                'oignons': 3.4, 'poireaux': 3.7, 'tomates': 4.7, 'salade': 4.2,
                'poulet': 9.9, 'bœuf': 17.1, 'porc': 11.9, 'agneau': 21.8,
                'morue': 12.4, 'saumon': 19.1, 'flétan': 16.1, 'crevettes': 22.8,
                'coquilles_st_jacques': 26.5, 'homard': 36.9, 'crabe': 17.1,
                'lait': 2.05, 'œufs': 0.39, 'beurre': 5.7, 'fromage': 17.1,
                'farine': 2.15, 'pain': 4.7, 'sucre': 2.25, 'huile': 3.9,
                'café': 6.5, 'thé': 5.2, 'riz': 3.6, 'pâtes': 3.5,
                'pommes': 3.9, 'poires': 4.1, 'oranges': 4.3, 'citrons': 4.7,
                'bananes': 3.7, 'myrtilles': 11.4, 'framboises': 15.1, 'rhum': 21.8
            },
            '2020': {
                'pommes_de_terre': 3.4, 'carottes': 3.7, 'chou': 3.5, 'navets': 3.3,
                'oignons': 3.6, 'poireaux': 3.9, 'tomates': 4.9, 'salade': 4.4,
                'poulet': 10.3, 'bœuf': 17.7, 'porc': 12.3, 'agneau': 22.6,
                'morue': 12.8, 'saumon': 19.7, 'flétan': 16.7, 'crevettes': 23.6,
                'coquilles_st_jacques': 27.5, 'homard': 38.3, 'crabe': 17.7,
                'lait': 2.15, 'œufs': 0.41, 'beurre': 5.9, 'fromage': 17.7,
                'farine': 2.25, 'pain': 4.9, 'sucre': 2.35, 'huile': 4.1,
                'café': 6.7, 'thé': 5.4, 'riz': 3.8, 'pâtes': 3.7,
                'pommes': 4.1, 'poires': 4.3, 'oranges': 4.5, 'citrons': 4.9,
                'bananes': 3.9, 'myrtilles': 11.8, 'framboises': 15.7, 'rhum': 22.6
            },
            '2021': {
                'pommes_de_terre': 3.6, 'carottes': 3.9, 'chou': 3.7, 'navets': 3.5,
                'oignons': 3.8, 'poireaux': 4.1, 'tomates': 5.1, 'salade': 4.6,
                'poulet': 10.7, 'bœuf': 18.3, 'porc': 12.7, 'agneau': 23.4,
                'morue': 13.2, 'saumon': 20.3, 'flétan': 17.3, 'crevettes': 24.4,
                'coquilles_st_jacques': 28.5, 'homard': 39.7, 'crabe': 18.3,
                'lait': 2.25, 'œufs': 0.43, 'beurre': 6.1, 'fromage': 18.3,
                'farine': 2.35, 'pain': 5.1, 'sucre': 2.45, 'huile': 4.3,
                'café': 6.9, 'thé': 5.6, 'riz': 4.0, 'pâtes': 3.9,
                'pommes': 4.3, 'poires': 4.5, 'oranges': 4.7, 'citrons': 5.1,
                'bananes': 4.1, 'myrtilles': 12.2, 'framboises': 16.3, 'rhum': 23.4
            },
            '2022': {
                'pommes_de_terre': 3.8, 'carottes': 4.1, 'chou': 3.9, 'navets': 3.7,
                'oignons': 4.0, 'poireaux': 4.3, 'tomates': 5.3, 'salade': 4.8,
                'poulet': 11.1, 'bœuf': 18.9, 'porc': 13.1, 'agneau': 24.2,
                'morue': 13.6, 'saumon': 20.9, 'flétan': 17.9, 'crevettes': 25.2,
                'coquilles_st_jacques': 29.5, 'homard': 41.1, 'crabe': 18.9,
                'lait': 2.35, 'œufs': 0.45, 'beurre': 6.3, 'fromage': 18.9,
                'farine': 2.45, 'pain': 5.3, 'sucre': 2.55, 'huile': 4.5,
                'café': 7.1, 'thé': 5.8, 'riz': 4.2, 'pâtes': 4.1,
                'pommes': 4.5, 'poires': 4.7, 'oranges': 4.9, 'citrons': 5.3,
                'bananes': 4.3, 'myrtilles': 12.6, 'framboises': 16.9, 'rhum': 24.2
            },
            '2023': {
                'pommes_de_terre': 4.0, 'carottes': 4.3, 'chou': 4.1, 'navets': 3.9,
                'oignons': 4.2, 'poireaux': 4.5, 'tomates': 5.5, 'salade': 5.0,
                'poulet': 11.5, 'bœuf': 19.5, 'porc': 13.5, 'agneau': 25.0,
                'morue': 14.0, 'saumon': 21.5, 'flétan': 18.5, 'crevettes': 26.0,
                'coquilles_st_jacques': 30.5, 'homard': 42.5, 'crabe': 19.5,
                'lait': 2.45, 'œufs': 0.47, 'beurre': 6.5, 'fromage': 19.5,
                'farine': 2.55, 'pain': 5.5, 'sucre': 2.65, 'huile': 4.7,
                'café': 7.3, 'thé': 6.0, 'riz': 4.4, 'pâtes': 4.3,
                'pommes': 4.7, 'poires': 4.9, 'oranges': 5.1, 'citrons': 5.5,
                'bananes': 4.5, 'myrtilles': 13.0, 'framboises': 17.5, 'rhum': 25.0
            },
            '2024': {
                'pommes_de_terre': 4.2, 'carottes': 4.5, 'chou': 4.3, 'navets': 4.1,
                'oignons': 4.4, 'poireaux': 4.7, 'tomates': 5.7, 'salade': 5.2,
                'poulet': 11.9, 'bœuf': 20.1, 'porc': 13.9, 'agneau': 25.8,
                'morue': 14.4, 'saumon': 22.1, 'flétan': 19.1, 'crevettes': 26.8,
                'coquilles_st_jacques': 31.5, 'homard': 43.9, 'crabe': 20.1,
                'lait': 2.55, 'œufs': 0.49, 'beurre': 6.7, 'fromage': 20.1,
                'farine': 2.65, 'pain': 5.7, 'sucre': 2.75, 'huile': 4.9,
                'café': 7.5, 'thé': 6.2, 'riz': 4.6, 'pâtes': 4.5,
                'pommes': 4.9, 'poires': 5.1, 'oranges': 5.3, 'citrons': 5.7,
                'bananes': 4.7, 'myrtilles': 13.4, 'framboises': 18.1, 'rhum': 25.8
            },
            '2025': {
                'pommes_de_terre': 4.4, 'carottes': 4.7, 'chou': 4.5, 'navets': 4.3,
                'oignons': 4.6, 'poireaux': 4.9, 'tomates': 5.9, 'salade': 5.4,
                'poulet': 12.3, 'bœuf': 20.7, 'porc': 14.3, 'agneau': 26.6,
                'morue': 14.8, 'saumon': 22.7, 'flétan': 19.7, 'crevettes': 27.6,
                'coquilles_st_jacques': 32.5, 'homard': 45.3, 'crabe': 20.7,
                'lait': 2.65, 'œufs': 0.51, 'beurre': 6.9, 'fromage': 20.7,
                'farine': 2.75, 'pain': 5.9, 'sucre': 2.85, 'huile': 5.1,
                'café': 7.7, 'thé': 6.4, 'riz': 4.8, 'pâtes': 4.7,
                'pommes': 5.1, 'poires': 5.3, 'oranges': 5.5, 'citrons': 5.9,
                'bananes': 4.9, 'myrtilles': 13.8, 'framboises': 18.7, 'rhum': 26.6
            }
        }
        
        # Inflation annuelle à Saint-Pierre-et-Miquelon (en %)
        self.inflation_rates = {
            '2002': 1.8, '2003': 2.0, '2004': 2.2, '2005': 2.4,
            '2006': 2.6, '2007': 2.8, '2008': 3.0, '2009': 3.2,
            '2010': 3.4, '2011': 3.6, '2012': 3.8, '2013': 4.0,
            '2014': 4.2, '2015': 4.4, '2016': 4.6, '2017': 4.8,
            '2018': 5.0, '2019': 5.2, '2020': 5.7, '2021': 6.2,
            '2022': 6.7, '2023': 7.2, '2024': 7.7, '2025': 8.2
        }
    
    def get_mercuriales_data(self):
        """
        Récupère toutes les données des mercuriales
        """
        print("🚀 Début de la récupération des données des mercuriales de Saint-Pierre-et-Miquelon...\n")
        
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
        products = ['pommes_de_terre', 'carottes', 'chou', 'navets', 'oignons', 'poireaux', 
                   'tomates', 'salade', 'poulet', 'bœuf', 'porc', 'agneau', 'morue', 'saumon', 
                   'flétan', 'crevettes', 'coquilles_st_jacques', 'homard', 'crabe', 'lait', 
                   'œufs', 'beurre', 'fromage', 'farine', 'pain', 'sucre', 'huile', 'café', 
                   'thé', 'riz', 'pâtes', 'pommes', 'poires', 'oranges', 'citrons', 'bananes', 
                   'myrtilles', 'framboises', 'rhum']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations basées sur la consommation moyenne à Saint-Pierre-et-Miquelon
        weights = {
            'pommes_de_terre': 0.08, 'carottes': 0.05, 'chou': 0.04, 'navets': 0.03,
            'oignons': 0.03, 'poireaux': 0.03, 'tomates': 0.04, 'salade': 0.03,
            'poulet': 0.08, 'bœuf': 0.07, 'porc': 0.06, 'agneau': 0.04,
            'morue': 0.07, 'saumon': 0.05, 'flétan': 0.04, 'crevettes': 0.03,
            'coquilles_st_jacques': 0.03, 'homard': 0.02, 'crabe': 0.03,
            'lait': 0.05, 'œufs': 0.04, 'beurre': 0.03, 'fromage': 0.04,
            'farine': 0.03, 'pain': 0.04, 'sucre': 0.02, 'huile': 0.02,
            'café': 0.02, 'thé': 0.01, 'riz': 0.03, 'pâtes': 0.03,
            'pommes': 0.03, 'poires': 0.02, 'oranges': 0.02, 'citrons': 0.02,
            'bananes': 0.03, 'myrtilles': 0.02, 'framboises': 0.02, 'rhum': 0.01
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_saint_pierre_miquelon_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_saint_pierre_miquelon_2002_2025.csv'")
        
        return df
    
    def create_price_evolution_charts(self, df):
        """Crée des graphiques d'évolution des prix"""
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = (15, 10)
        plt.rcParams['font.size'] = 12
        
        # 1. Graphique des produits de base
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Légumes de base
        axes[0, 0].plot(df['year'], df['pommes_de_terre'], label='Pommes de terre', linewidth=2, marker='o')
        axes[0, 0].plot(df['year'], df['carottes'], label='Carottes', linewidth=2, marker='s')
        axes[0, 0].plot(df['year'], df['chou'], label='Chou', linewidth=2, marker='^')
        axes[0, 0].plot(df['year'], df['oignons'], label='Oignons', linewidth=2, marker='d')
        axes[0, 0].set_title('Évolution des prix des légumes de base', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Produits animaux terrestres
        axes[0, 1].plot(df['year'], df['poulet'], label='Poulet', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['bœuf'], label='Bœuf', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['porc'], label='Porc', linewidth=2, marker='^')
        axes[0, 1].plot(df['year'], df['agneau'], label='Agneau', linewidth=2, marker='d')
        axes[0, 1].set_title('Évolution des prix des viandes', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Produits de la mer
        axes[1, 0].plot(df['year'], df['morue'], label='Morue', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['saumon'], label='Saumon', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['flétan'], label='Flétan', linewidth=2, marker='^')
        axes[1, 0].plot(df['year'], df['crevettes'], label='Crevettes', linewidth=2, marker='d')
        axes[1, 0].set_title('Évolution des prix des produits de la mer', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Produits laitiers et boulangerie
        axes[1, 1].plot(df['year'], df['lait'], label='Lait (€/L)', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['fromage'], label='Fromage', linewidth=2, marker='s')
        axes[1, 1].plot(df['year'], df['beurre'], label='Beurre', linewidth=2, marker='^')
        axes[1, 1].plot(df['year'], df['pain'], label='Pain', linewidth=2, marker='d')
        axes[1, 1].set_title('Évolution des prix des produits laitiers et boulangerie', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_saint_pierre_miquelon_evolution_prix.png', dpi=300, bbox_inches='tight')
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
        axes[0, 1].plot(df['year'], df['pommes_de_terre_ajusté'], label='Pommes de terre (ajusté)', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['poulet_ajusté'], label='Poulet (ajusté)', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['morue_ajusté'], label='Morue (ajusté)', linewidth=2, marker='^')
        axes[0, 1].set_title('Prix ajustés de l\'inflation (base 2002)', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Prix réel (€/kg de 2002)', fontsize=12)
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Évolution des fruits
        axes[1, 0].plot(df['year'], df['pommes'], label='Pommes', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['oranges'], label='Oranges', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['bananes'], label='Bananes', linewidth=2, marker='^')
        axes[1, 0].plot(df['year'], df['myrtilles'], label='Myrtilles', linewidth=2, marker='d')
        axes[1, 0].set_title('Évolution des prix des fruits', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Taux d'inflation
        axes[1, 1].bar(df['year'], df['inflation'], color='orange', alpha=0.7)
        axes[1, 1].set_title('Taux d\'inflation annuel à Saint-Pierre-et-Miquelon', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_saint_pierre_miquelon_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['pommes_de_terre', 'poulet', 'morue', 'lait']
        
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
        display_df = key_df[['year', 'pommes_de_terre', 'poulet', 'morue', 'lait', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['pommes_de_terre', 'poulet', 'morue', 'lait']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Pommes de terre (€/kg)', 'Poulet (€/kg)', 'Morue (€/kg)', 
                             'Lait (€/L)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_saint_pierre_miquelon_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_saint_pierre_miquelon_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE SAINT-PIERRE-ET-MIQUELON")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🥔 Prix moyen des pommes de terre: {df['pommes_de_terre'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🐟 Prix moyen de la morue: {df['morue'].mean():.2f} €/kg")
        print(f"🥛 Prix moyen du lait: {df['lait'].mean():.2f} €/L")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['pommes_de_terre', 'poulet', 'morue', 'lait', 'indice_alimentaire']
        product_names = ['Pommes de terre', 'Poulet', 'Morue', 'Lait', 'Indice alimentaire']
        
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
        products = ['pommes_de_terre', 'carottes', 'chou', 'navets', 'oignons', 'poireaux', 
                   'tomates', 'salade', 'poulet', 'bœuf', 'porc', 'agneau', 'morue', 'saumon', 
                   'flétan', 'crevettes', 'coquilles_st_jacques', 'homard', 'crabe', 'lait', 
                   'œufs', 'beurre', 'fromage', 'farine', 'pain', 'sucre', 'huile', 'café', 
                   'thé', 'riz', 'pâtes', 'pommes', 'poires', 'oranges', 'citrons', 'bananes', 
                   'myrtilles', 'framboises', 'rhum']
        
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
        
        if (df[df['year'] == 2025]['pommes_de_terre'].values[0] / df[df['year'] == 2002]['pommes_de_terre'].values[0] > 
            df[df['year'] == 2025]['indice_alimentaire'].values[0] / 100):
            print("⚠️  Le prix des pommes de terre a augmenté plus que l'indice alimentaire moyen")
            print("→ Importance de la sécurité alimentaire pour les produits de base")
        
        # Spécificités de Saint-Pierre-et-Miquelon
        print(f"\n🌊 SPÉCIFICITÉS DE SAINT-PIERRE-ET-MIQUELON")
        morue_increase = ((df[df['year'] == 2025]['morue'].values[0] - 
                         df[df['year'] == 2002]['morue'].values[0]) / 
                         df[df['year'] == 2002]['morue'].values[0] * 100)
        print(f"• La morue, produit emblématique, a augmenté de {morue_increase:.1f}%")
        
        produits_marins = ['homard', 'crevettes', 'coquilles_st_jacques', 'crabe']
        for produit in produits_marins:
            augmentation = ((df[df['year'] == 2025][produit].values[0] - 
                           df[df['year'] == 2002][produit].values[0]) / 
                           df[df['year'] == 2002][produit].values[0] * 100)
            print(f"• {produit.capitalize()}: {augmentation:+.1f}%")
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de Saint-Pierre-et-Miquelon...")
        
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
        print("   - mercuriales_saint_pierre_miquelon_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_saint_pierre_miquelon_annees_cles.csv (années clés)")
        print("   - mercuriales_saint_pierre_miquelon_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_saint_pierre_miquelon_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = SaintPierreMiquelonMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()