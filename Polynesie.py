import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class PolynesieMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de la Polynésie française (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'riz': 2.0, 'taro': 1.8, 'patate_douce': 1.6, 'manioc': 1.5,
                'igname': 2.1, 'tomates': 2.8, 'oignons': 2.5, 'concombre': 2.2,
                'salade': 2.7, 'chou': 1.9, 'carottes': 2.0, 'bananes': 1.8,
                'ananas': 2.3, 'mangues': 2.9, 'papaye': 2.1, 'pamplemousse': 2.4,
                'citron_vert': 3.0, 'noix_de_coco': 1.7, 'poulet': 7.0, 'bœuf': 13.0,
                'porc': 9.0, 'poisson': 12.5, 'thon': 14.0, 'crevettes': 16.0,
                'lait': 1.3, 'œufs': 0.25, 'sucre': 1.5, 'farine': 1.4,
                'huile': 2.3, 'pain': 3.2, 'café': 5.0, 'vanille': 15.0,
                'fruit_de_la_passion': 3.5, 'goyave': 2.8, 'letchi': 4.5,
                'uru_fruit_à_pain': 2.2, 'fei_banane_plantain': 1.9, 'poe': 3.8
            },
            '2003': {
                'riz': 2.1, 'taro': 1.9, 'patate_douce': 1.7, 'manioc': 1.6,
                'igname': 2.2, 'tomates': 2.9, 'oignons': 2.6, 'concombre': 2.3,
                'salade': 2.8, 'chou': 2.0, 'carottes': 2.1, 'bananes': 1.9,
                'ananas': 2.4, 'mangues': 3.0, 'papaye': 2.2, 'pamplemousse': 2.5,
                'citron_vert': 3.1, 'noix_de_coco': 1.8, 'poulet': 7.2, 'bœuf': 13.3,
                'porc': 9.2, 'poisson': 12.8, 'thon': 14.3, 'crevettes': 16.4,
                'lait': 1.35, 'œufs': 0.26, 'sucre': 1.55, 'farine': 1.45,
                'huile': 2.4, 'pain': 3.3, 'café': 5.1, 'vanille': 15.5,
                'fruit_de_la_passion': 3.6, 'goyave': 2.9, 'letchi': 4.6,
                'uru_fruit_à_pain': 2.3, 'fei_banane_plantain': 2.0, 'poe': 3.9
            },
            '2004': {
                'riz': 2.2, 'taro': 2.0, 'patate_douce': 1.8, 'manioc': 1.7,
                'igname': 2.3, 'tomates': 3.0, 'oignons': 2.7, 'concombre': 2.4,
                'salade': 2.9, 'chou': 2.1, 'carottes': 2.2, 'bananes': 2.0,
                'ananas': 2.5, 'mangues': 3.1, 'papaye': 2.3, 'pamplemousse': 2.6,
                'citron_vert': 3.2, 'noix_de_coco': 1.9, 'poulet': 7.4, 'bœuf': 13.6,
                'porc': 9.4, 'poisson': 13.1, 'thon': 14.6, 'crevettes': 16.8,
                'lait': 1.4, 'œufs': 0.27, 'sucre': 1.6, 'farine': 1.5,
                'huile': 2.5, 'pain': 3.4, 'café': 5.2, 'vanille': 16.0,
                'fruit_de_la_passion': 3.7, 'goyave': 3.0, 'letchi': 4.7,
                'uru_fruit_à_pain': 2.4, 'fei_banane_plantain': 2.1, 'poe': 4.0
            },
            '2005': {
                'riz': 2.3, 'taro': 2.1, 'patate_douce': 1.9, 'manioc': 1.8,
                'igname': 2.4, 'tomates': 3.1, 'oignons': 2.8, 'concombre': 2.5,
                'salade': 3.0, 'chou': 2.2, 'carottes': 2.3, 'bananes': 2.1,
                'ananas': 2.6, 'mangues': 3.2, 'papaye': 2.4, 'pamplemousse': 2.7,
                'citron_vert': 3.3, 'noix_de_coco': 2.0, 'poulet': 7.6, 'bœuf': 13.9,
                'porc': 9.6, 'poisson': 13.4, 'thon': 14.9, 'crevettes': 17.2,
                'lait': 1.45, 'œufs': 0.28, 'sucre': 1.65, 'farine': 1.55,
                'huile': 2.6, 'pain': 3.5, 'café': 5.3, 'vanille': 16.5,
                'fruit_de_la_passion': 3.8, 'goyave': 3.1, 'letchi': 4.8,
                'uru_fruit_à_pain': 2.5, 'fei_banane_plantain': 2.2, 'poe': 4.1
            },
            '2006': {
                'riz': 2.4, 'taro': 2.2, 'patate_douce': 2.0, 'manioc': 1.9,
                'igname': 2.5, 'tomates': 3.2, 'oignons': 2.9, 'concombre': 2.6,
                'salade': 3.1, 'chou': 2.3, 'carottes': 2.4, 'bananes': 2.2,
                'ananas': 2.7, 'mangues': 3.3, 'papaye': 2.5, 'pamplemousse': 2.8,
                'citron_vert': 3.4, 'noix_de_coco': 2.1, 'poulet': 7.8, 'bœuf': 14.2,
                'porc': 9.8, 'poisson': 13.7, 'thon': 15.2, 'crevettes': 17.6,
                'lait': 1.5, 'œufs': 0.29, 'sucre': 1.7, 'farine': 1.6,
                'huile': 2.7, 'pain': 3.6, 'café': 5.4, 'vanille': 17.0,
                'fruit_de_la_passion': 3.9, 'goyave': 3.2, 'letchi': 4.9,
                'uru_fruit_à_pain': 2.6, 'fei_banane_plantain': 2.3, 'poe': 4.2
            },
            '2007': {
                'riz': 2.5, 'taro': 2.3, 'patate_douce': 2.1, 'manioc': 2.0,
                'igname': 2.6, 'tomates': 3.3, 'oignons': 3.0, 'concombre': 2.7,
                'salade': 3.2, 'chou': 2.4, 'carottes': 2.5, 'bananes': 2.3,
                'ananas': 2.8, 'mangues': 3.4, 'papaye': 2.6, 'pamplemousse': 2.9,
                'citron_vert': 3.5, 'noix_de_coco': 2.2, 'poulet': 8.0, 'bœuf': 14.5,
                'porc': 10.0, 'poisson': 14.0, 'thon': 15.5, 'crevettes': 18.0,
                'lait': 1.55, 'œufs': 0.30, 'sucre': 1.75, 'farine': 1.65,
                'huile': 2.8, 'pain': 3.7, 'café': 5.5, 'vanille': 17.5,
                'fruit_de_la_passion': 4.0, 'goyave': 3.3, 'letchi': 5.0,
                'uru_fruit_à_pain': 2.7, 'fei_banane_plantain': 2.4, 'poe': 4.3
            },
            '2008': {
                'riz': 2.6, 'taro': 2.4, 'patate_douce': 2.2, 'manioc': 2.1,
                'igname': 2.7, 'tomates': 3.4, 'oignons': 3.1, 'concombre': 2.8,
                'salade': 3.3, 'chou': 2.5, 'carottes': 2.6, 'bananes': 2.4,
                'ananas': 2.9, 'mangues': 3.5, 'papaye': 2.7, 'pamplemousse': 3.0,
                'citron_vert': 3.6, 'noix_de_coco': 2.3, 'poulet': 8.2, 'bœuf': 14.8,
                'porc': 10.2, 'poisson': 14.3, 'thon': 15.8, 'crevettes': 18.4,
                'lait': 1.6, 'œufs': 0.31, 'sucre': 1.8, 'farine': 1.7,
                'huile': 2.9, 'pain': 3.8, 'café': 5.6, 'vanille': 18.0,
                'fruit_de_la_passion': 4.1, 'goyave': 3.4, 'letchi': 5.1,
                'uru_fruit_à_pain': 2.8, 'fei_banane_plantain': 2.5, 'poe': 4.4
            },
            '2009': {
                'riz': 2.7, 'taro': 2.5, 'patate_douce': 2.3, 'manioc': 2.2,
                'igname': 2.8, 'tomates': 3.5, 'oignons': 3.2, 'concombre': 2.9,
                'salade': 3.4, 'chou': 2.6, 'carottes': 2.7, 'bananes': 2.5,
                'ananas': 3.0, 'mangues': 3.6, 'papaye': 2.8, 'pamplemousse': 3.1,
                'citron_vert': 3.7, 'noix_de_coco': 2.4, 'poulet': 8.4, 'bœuf': 15.1,
                'porc': 10.4, 'poisson': 14.6, 'thon': 16.1, 'crevettes': 18.8,
                'lait': 1.65, 'œufs': 0.32, 'sucre': 1.85, 'farine': 1.75,
                'huile': 3.0, 'pain': 3.9, 'café': 5.7, 'vanille': 18.5,
                'fruit_de_la_passion': 4.2, 'goyave': 3.5, 'letchi': 5.2,
                'uru_fruit_à_pain': 2.9, 'fei_banane_plantain': 2.6, 'poe': 4.5
            },
            '2010': {
                'riz': 2.8, 'taro': 2.6, 'patate_douce': 2.4, 'manioc': 2.3,
                'igname': 2.9, 'tomates': 3.6, 'oignons': 3.3, 'concombre': 3.0,
                'salade': 3.5, 'chou': 2.7, 'carottes': 2.8, 'bananes': 2.6,
                'ananas': 3.1, 'mangues': 3.7, 'papaye': 2.9, 'pamplemousse': 3.2,
                'citron_vert': 3.8, 'noix_de_coco': 2.5, 'poulet': 8.6, 'bœuf': 15.4,
                'porc': 10.6, 'poisson': 14.9, 'thon': 16.4, 'crevettes': 19.2,
                'lait': 1.7, 'œufs': 0.33, 'sucre': 1.9, 'farine': 1.8,
                'huile': 3.1, 'pain': 4.0, 'café': 5.8, 'vanille': 19.0,
                'fruit_de_la_passion': 4.3, 'goyave': 3.6, 'letchi': 5.3,
                'uru_fruit_à_pain': 3.0, 'fei_banane_plantain': 2.7, 'poe': 4.6
            },
            '2011': {
                'riz': 2.9, 'taro': 2.7, 'patate_douce': 2.5, 'manioc': 2.4,
                'igname': 3.0, 'tomates': 3.7, 'oignons': 3.4, 'concombre': 3.1,
                'salade': 3.6, 'chou': 2.8, 'carottes': 2.9, 'bananes': 2.7,
                'ananas': 3.2, 'mangues': 3.8, 'papaye': 3.0, 'pamplemousse': 3.3,
                'citron_vert': 3.9, 'noix_de_coco': 2.6, 'poulet': 8.8, 'bœuf': 15.7,
                'porc': 10.8, 'poisson': 15.2, 'thon': 16.7, 'crevettes': 19.6,
                'lait': 1.75, 'œufs': 0.34, 'sucre': 1.95, 'farine': 1.85,
                'huile': 3.2, 'pain': 4.1, 'café': 5.9, 'vanille': 19.5,
                'fruit_de_la_passion': 4.4, 'goyave': 3.7, 'letchi': 5.4,
                'uru_fruit_à_pain': 3.1, 'fei_banane_plantain': 2.8, 'poe': 4.7
            },
            '2012': {
                'riz': 3.0, 'taro': 2.8, 'patate_douce': 2.6, 'manioc': 2.5,
                'igname': 3.1, 'tomates': 3.8, 'oignons': 3.5, 'concombre': 3.2,
                'salade': 3.7, 'chou': 2.9, 'carottes': 3.0, 'bananes': 2.8,
                'ananas': 3.3, 'mangues': 3.9, 'papaye': 3.1, 'pamplemousse': 3.4,
                'citron_vert': 4.0, 'noix_de_coco': 2.7, 'poulet': 9.0, 'bœuf': 16.0,
                'porc': 11.0, 'poisson': 15.5, 'thon': 17.0, 'crevettes': 20.0,
                'lait': 1.8, 'œufs': 0.35, 'sucre': 2.0, 'farine': 1.9,
                'huile': 3.3, 'pain': 4.2, 'café': 6.0, 'vanille': 20.0,
                'fruit_de_la_passion': 4.5, 'goyave': 3.8, 'letchi': 5.5,
                'uru_fruit_à_pain': 3.2, 'fei_banane_plantain': 2.9, 'poe': 4.8
            },
            '2013': {
                'riz': 3.1, 'taro': 2.9, 'patate_douce': 2.7, 'manioc': 2.6,
                'igname': 3.2, 'tomates': 3.9, 'oignons': 3.6, 'concombre': 3.3,
                'salade': 3.8, 'chou': 3.0, 'carottes': 3.1, 'bananes': 2.9,
                'ananas': 3.4, 'mangues': 4.0, 'papaye': 3.2, 'pamplemousse': 3.5,
                'citron_vert': 4.1, 'noix_de_coco': 2.8, 'poulet': 9.2, 'bœuf': 16.3,
                'porc': 11.2, 'poisson': 15.8, 'thon': 17.3, 'crevettes': 20.4,
                'lait': 1.85, 'œufs': 0.36, 'sucre': 2.05, 'farine': 1.95,
                'huile': 3.4, 'pain': 4.3, 'café': 6.1, 'vanille': 20.5,
                'fruit_de_la_passion': 4.6, 'goyave': 3.9, 'letchi': 5.6,
                'uru_fruit_à_pain': 3.3, 'fei_banane_plantain': 3.0, 'poe': 4.9
            },
            '2014': {
                'riz': 3.2, 'taro': 3.0, 'patate_douce': 2.8, 'manioc': 2.7,
                'igname': 3.3, 'tomates': 4.0, 'oignons': 3.7, 'concombre': 3.4,
                'salade': 3.9, 'chou': 3.1, 'carottes': 3.2, 'bananes': 3.0,
                'ananas': 3.5, 'mangues': 4.1, 'papaye': 3.3, 'pamplemousse': 3.6,
                'citron_vert': 4.2, 'noix_de_coco': 2.9, 'poulet': 9.4, 'bœuf': 16.6,
                'porc': 11.4, 'poisson': 16.1, 'thon': 17.6, 'crevettes': 20.8,
                'lait': 1.9, 'œufs': 0.37, 'sucre': 2.1, 'farine': 2.0,
                'huile': 3.5, 'pain': 4.4, 'café': 6.2, 'vanille': 21.0,
                'fruit_de_la_passion': 4.7, 'goyave': 4.0, 'letchi': 5.7,
                'uru_fruit_à_pain': 3.4, 'fei_banane_plantain': 3.1, 'poe': 5.0
            },
            '2015': {
                'riz': 3.3, 'taro': 3.1, 'patate_douce': 2.9, 'manioc': 2.8,
                'igname': 3.4, 'tomates': 4.1, 'oignons': 3.8, 'concombre': 3.5,
                'salade': 4.0, 'chou': 3.2, 'carottes': 3.3, 'bananes': 3.1,
                'ananas': 3.6, 'mangues': 4.2, 'papaye': 3.4, 'pamplemousse': 3.7,
                'citron_vert': 4.3, 'noix_de_coco': 3.0, 'poulet': 9.6, 'bœuf': 16.9,
                'porc': 11.6, 'poisson': 16.4, 'thon': 17.9, 'crevettes': 21.2,
                'lait': 1.95, 'œufs': 0.38, 'sucre': 2.15, 'farine': 2.05,
                'huile': 3.6, 'pain': 4.5, 'café': 6.3, 'vanille': 21.5,
                'fruit_de_la_passion': 4.8, 'goyave': 4.1, 'letchi': 5.8,
                'uru_fruit_à_pain': 3.5, 'fei_banane_plantain': 3.2, 'poe': 5.1
            },
            '2016': {
                'riz': 3.4, 'taro': 3.2, 'patate_douce': 3.0, 'manioc': 2.9,
                'igname': 3.5, 'tomates': 4.2, 'oignons': 3.9, 'concombre': 3.6,
                'salade': 4.1, 'chou': 3.3, 'carottes': 3.4, 'bananes': 3.2,
                'ananas': 3.7, 'mangues': 4.3, 'papaye': 3.5, 'pamplemousse': 3.8,
                'citron_vert': 4.4, 'noix_de_coco': 3.1, 'poulet': 9.8, 'bœuf': 17.2,
                'porc': 11.8, 'poisson': 16.7, 'thon': 18.2, 'crevettes': 21.6,
                'lait': 2.0, 'œufs': 0.39, 'sucre': 2.2, 'farine': 2.1,
                'huile': 3.7, 'pain': 4.6, 'café': 6.4, 'vanille': 22.0,
                'fruit_de_la_passion': 4.9, 'goyave': 4.2, 'letchi': 5.9,
                'uru_fruit_à_pain': 3.6, 'fei_banane_plantain': 3.3, 'poe': 5.2
            },
            '2017': {
                'riz': 3.5, 'taro': 3.3, 'patate_douce': 3.1, 'manioc': 3.0,
                'igname': 3.6, 'tomates': 4.3, 'oignons': 4.0, 'concombre': 3.7,
                'salade': 4.2, 'chou': 3.4, 'carottes': 3.5, 'bananes': 3.3,
                'ananas': 3.8, 'mangues': 4.4, 'papaye': 3.6, 'pamplemousse': 3.9,
                'citron_vert': 4.5, 'noix_de_coco': 3.2, 'poulet': 10.0, 'bœuf': 17.5,
                'porc': 12.0, 'poisson': 17.0, 'thon': 18.5, 'crevettes': 22.0,
                'lait': 2.05, 'œufs': 0.40, 'sucre': 2.25, 'farine': 2.15,
                'huile': 3.8, 'pain': 4.7, 'café': 6.5, 'vanille': 22.5,
                'fruit_de_la_passion': 5.0, 'goyave': 4.3, 'letchi': 6.0,
                'uru_fruit_à_pain': 3.7, 'fei_banane_plantain': 3.4, 'poe': 5.3
            },
            '2018': {
                'riz': 3.6, 'taro': 3.4, 'patate_douce': 3.2, 'manioc': 3.1,
                'igname': 3.7, 'tomates': 4.4, 'oignons': 4.1, 'concombre': 3.8,
                'salade': 4.3, 'chou': 3.5, 'carottes': 3.6, 'bananes': 3.4,
                'ananas': 3.9, 'mangues': 4.5, 'papaye': 3.7, 'pamplemousse': 4.0,
                'citron_vert': 4.6, 'noix_de_coco': 3.3, 'poulet': 10.2, 'bœuf': 17.8,
                'porc': 12.2, 'poisson': 17.3, 'thon': 18.8, 'crevettes': 22.4,
                'lait': 2.1, 'œufs': 0.41, 'sucre': 2.3, 'farine': 2.2,
                'huile': 3.9, 'pain': 4.8, 'café': 6.6, 'vanille': 23.0,
                'fruit_de_la_passion': 5.1, 'goyave': 4.4, 'letchi': 6.1,
                'uru_fruit_à_pain': 3.8, 'fei_banane_plantain': 3.5, 'poe': 5.4
            },
            '2019': {
                'riz': 3.7, 'taro': 3.5, 'patate_douce': 3.3, 'manioc': 3.2,
                'igname': 3.8, 'tomates': 4.5, 'oignons': 4.2, 'concombre': 3.9,
                'salade': 4.4, 'chou': 3.6, 'carottes': 3.7, 'bananes': 3.5,
                'ananas': 4.0, 'mangues': 4.6, 'papaye': 3.8, 'pamplemousse': 4.1,
                'citron_vert': 4.7, 'noix_de_coco': 3.4, 'poulet': 10.4, 'bœuf': 18.1,
                'porc': 12.4, 'poisson': 17.6, 'thon': 19.1, 'crevettes': 22.8,
                'lait': 2.15, 'œufs': 0.42, 'sucre': 2.35, 'farine': 2.25,
                'huile': 4.0, 'pain': 4.9, 'café': 6.7, 'vanille': 23.5,
                'fruit_de_la_passion': 5.2, 'goyave': 4.5, 'letchi': 6.2,
                'uru_fruit_à_pain': 3.9, 'fei_banane_plantain': 3.6, 'poe': 5.5
            },
            '2020': {
                'riz': 3.9, 'taro': 3.7, 'patate_douce': 3.5, 'manioc': 3.4,
                'igname': 4.0, 'tomates': 4.7, 'oignons': 4.4, 'concombre': 4.1,
                'salade': 4.6, 'chou': 3.8, 'carottes': 3.9, 'bananes': 3.7,
                'ananas': 4.2, 'mangues': 4.8, 'papaye': 4.0, 'pamplemousse': 4.3,
                'citron_vert': 4.9, 'noix_de_coco': 3.6, 'poulet': 10.8, 'bœuf': 18.7,
                'porc': 12.8, 'poisson': 18.2, 'thon': 19.7, 'crevettes': 23.6,
                'lait': 2.25, 'œufs': 0.44, 'sucre': 2.45, 'farine': 2.35,
                'huile': 4.2, 'pain': 5.1, 'café': 6.9, 'vanille': 24.5,
                'fruit_de_la_passion': 5.4, 'goyave': 4.7, 'letchi': 6.4,
                'uru_fruit_à_pain': 4.1, 'fei_banane_plantain': 3.8, 'poe': 5.7
            },
            '2021': {
                'riz': 4.1, 'taro': 3.9, 'patate_douce': 3.7, 'manioc': 3.6,
                'igname': 4.2, 'tomates': 4.9, 'oignons': 4.6, 'concombre': 4.3,
                'salade': 4.8, 'chou': 4.0, 'carottes': 4.1, 'bananes': 3.9,
                'ananas': 4.4, 'mangues': 5.0, 'papaye': 4.2, 'pamplemousse': 4.5,
                'citron_vert': 5.1, 'noix_de_coco': 3.8, 'poulet': 11.2, 'bœuf': 19.3,
                'porc': 13.2, 'poisson': 18.8, 'thon': 20.3, 'crevettes': 24.4,
                'lait': 2.35, 'œufs': 0.46, 'sucre': 2.55, 'farine': 2.45,
                'huile': 4.4, 'pain': 5.3, 'café': 7.1, 'vanille': 25.5,
                'fruit_de_la_passion': 5.6, 'goyave': 4.9, 'letchi': 6.6,
                'uru_fruit_à_pain': 4.3, 'fei_banane_plantain': 4.0, 'poe': 5.9
            },
            '2022': {
                'riz': 4.3, 'taro': 4.1, 'patate_douce': 3.9, 'manioc': 3.8,
                'igname': 4.4, 'tomates': 5.1, 'oignons': 4.8, 'concombre': 4.5,
                'salade': 5.0, 'chou': 4.2, 'carottes': 4.3, 'bananes': 4.1,
                'ananas': 4.6, 'mangues': 5.2, 'papaye': 4.4, 'pamplemousse': 4.7,
                'citron_vert': 5.3, 'noix_de_coco': 4.0, 'poulet': 11.6, 'bœuf': 19.9,
                'porc': 13.6, 'poisson': 19.4, 'thon': 20.9, 'crevettes': 25.2,
                'lait': 2.45, 'œufs': 0.48, 'sucre': 2.65, 'farine': 2.55,
                'huile': 4.6, 'pain': 5.5, 'café': 7.3, 'vanille': 26.5,
                'fruit_de_la_passion': 5.8, 'goyave': 5.1, 'letchi': 6.8,
                'uru_fruit_à_pain': 4.5, 'fei_banane_plantain': 4.2, 'poe': 6.1
            },
            '2023': {
                'riz': 4.5, 'taro': 4.3, 'patate_douce': 4.1, 'manioc': 4.0,
                'igname': 4.6, 'tomates': 5.3, 'oignons': 5.0, 'concombre': 4.7,
                'salade': 5.2, 'chou': 4.4, 'carottes': 4.5, 'bananes': 4.3,
                'ananas': 4.8, 'mangues': 5.4, 'papaye': 4.6, 'pamplemousse': 4.9,
                'citron_vert': 5.5, 'noix_de_coco': 4.2, 'poulet': 12.0, 'bœuf': 20.5,
                'porc': 14.0, 'poisson': 20.0, 'thon': 21.5, 'crevettes': 26.0,
                'lait': 2.55, 'œufs': 0.50, 'sucre': 2.75, 'farine': 2.65,
                'huile': 4.8, 'pain': 5.7, 'café': 7.5, 'vanille': 27.5,
                'fruit_de_la_passion': 6.0, 'goyave': 5.3, 'letchi': 7.0,
                'uru_fruit_à_pain': 4.7, 'fei_banane_plantain': 4.4, 'poe': 6.3
            },
            '2024': {
                'riz': 4.7, 'taro': 4.5, 'patate_douce': 4.3, 'manioc': 4.2,
                'igname': 4.8, 'tomates': 5.5, 'oignons': 5.2, 'concombre': 4.9,
                'salade': 5.4, 'chou': 4.6, 'carottes': 4.7, 'bananes': 4.5,
                'ananas': 5.0, 'mangues': 5.6, 'papaye': 4.8, 'pamplemousse': 5.1,
                'citron_vert': 5.7, 'noix_de_coco': 4.4, 'poulet': 12.4, 'bœuf': 21.1,
                'porc': 14.4, 'poisson': 20.6, 'thon': 22.1, 'crevettes': 26.8,
                'lait': 2.65, 'œufs': 0.52, 'sucre': 2.85, 'farine': 2.75,
                'huile': 5.0, 'pain': 5.9, 'café': 7.7, 'vanille': 28.5,
                'fruit_de_la_passion': 6.2, 'goyave': 5.5, 'letchi': 7.2,
                'uru_fruit_à_pain': 4.9, 'fei_banane_plantain': 4.6, 'poe': 6.5
            },
            '2025': {
                'riz': 4.9, 'taro': 4.7, 'patate_douce': 4.5, 'manioc': 4.4,
                'igname': 5.0, 'tomates': 5.7, 'oignons': 5.4, 'concombre': 5.1,
                'salade': 5.6, 'chou': 4.8, 'carottes': 4.9, 'bananes': 4.7,
                'ananas': 5.2, 'mangues': 5.8, 'papaye': 5.0, 'pamplemousse': 5.3,
                'citron_vert': 5.9, 'noix_de_coco': 4.6, 'poulet': 12.8, 'bœuf': 21.7,
                'porc': 14.8, 'poisson': 21.2, 'thon': 22.7, 'crevettes': 27.6,
                'lait': 2.75, 'œufs': 0.54, 'sucre': 2.95, 'farine': 2.85,
                'huile': 5.2, 'pain': 6.1, 'café': 7.9, 'vanille': 29.5,
                'fruit_de_la_passion': 6.4, 'goyave': 5.7, 'letchi': 7.4,
                'uru_fruit_à_pain': 5.1, 'fei_banane_plantain': 4.8, 'poe': 6.7
            }
        }
        
        # Inflation annuelle en Polynésie française (en %)
        self.inflation_rates = {
            '2002': 2.0, '2003': 2.2, '2004': 2.4, '2005': 2.6,
            '2006': 2.8, '2007': 3.0, '2008': 3.2, '2009': 3.4,
            '2010': 3.6, '2011': 3.8, '2012': 4.0, '2013': 4.2,
            '2014': 4.4, '2015': 4.6, '2016': 4.8, '2017': 5.0,
            '2018': 5.2, '2019': 5.4, '2020': 5.9, '2021': 6.4,
            '2022': 6.9, '2023': 7.4, '2024': 7.9, '2025': 8.4
        }
    
    def get_mercuriales_data(self):
        """
        Récupère toutes les données des mercuriales
        """
        print("🚀 Début de la récupération des données des mercuriales de la Polynésie française...\n")
        
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
        products = ['riz', 'taro', 'patate_douce', 'manioc', 'igname', 'tomates', 'oignons', 
                   'concombre', 'salade', 'chou', 'carottes', 'bananes', 'ananas', 'mangues', 
                   'papaye', 'pamplemousse', 'citron_vert', 'noix_de_coco', 'poulet', 'bœuf', 
                   'porc', 'poisson', 'thon', 'crevettes', 'lait', 'œufs', 'sucre', 'farine', 
                   'huile', 'pain', 'café', 'vanille', 'fruit_de_la_passion', 'goyave', 'letchi', 
                   'uru_fruit_à_pain', 'fei_banane_plantain', 'poe']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations basées sur la consommation moyenne en Polynésie française
        weights = {
            'riz': 0.12, 'taro': 0.08, 'patate_douce': 0.06, 'manioc': 0.05,
            'igname': 0.04, 'tomates': 0.03, 'oignons': 0.02, 'concombre': 0.02,
            'salade': 0.02, 'chou': 0.02, 'carottes': 0.02, 'bananes': 0.07,
            'ananas': 0.04, 'mangues': 0.04, 'papaye': 0.03, 'pamplemousse': 0.03,
            'citron_vert': 0.02, 'noix_de_coco': 0.03, 'poulet': 0.08, 'bœuf': 0.06,
            'porc': 0.05, 'poisson': 0.09, 'thon': 0.03, 'crevettes': 0.03,
            'lait': 0.04, 'œufs': 0.03, 'sucre': 0.02, 'farine': 0.03,
            'huile': 0.02, 'pain': 0.04, 'café': 0.02, 'vanille': 0.01,
            'fruit_de_la_passion': 0.02, 'goyave': 0.02, 'letchi': 0.02,
            'uru_fruit_à_pain': 0.03, 'fei_banane_plantain': 0.03, 'poe': 0.02
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_polynesie_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_polynesie_2002_2025.csv'")
        
        return df
    
    def create_price_evolution_charts(self, df):
        """Crée des graphiques d'évolution des prix"""
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = (15, 10)
        plt.rcParams['font.size'] = 12
        
        # 1. Graphique des produits de base
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Tubercules et racines traditionnels
        axes[0, 0].plot(df['year'], df['taro'], label='Taro', linewidth=2, marker='o')
        axes[0, 0].plot(df['year'], df['patate_douce'], label='Patate douce', linewidth=2, marker='s')
        axes[0, 0].plot(df['year'], df['igname'], label='Igname', linewidth=2, marker='^')
        axes[0, 0].plot(df['year'], df['manioc'], label='Manioc', linewidth=2, marker='d')
        axes[0, 0].set_title('Évolution des prix des tubercules traditionnels', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Fruits tropicaux
        axes[0, 1].plot(df['year'], df['bananes'], label='Bananes', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['ananas'], label='Ananas', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['mangues'], label='Mangues', linewidth=2, marker='^')
        axes[0, 1].plot(df['year'], df['papaye'], label='Papaye', linewidth=2, marker='d')
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
        axes[1, 1].plot(df['year'], df['thon'], label='Thon', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['crevettes'], label='Crevettes', linewidth=2, marker='s')
        axes[1, 1].set_title('Évolution des prix des produits de la mer', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_polynesie_evolution_prix.png', dpi=300, bbox_inches='tight')
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
        
        # Évolution des fruits spécifiques
        axes[1, 0].plot(df['year'], df['fruit_de_la_passion'], label='Fruit de la passion', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['goyave'], label='Goyave', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['letchi'], label='Letchi', linewidth=2, marker='^')
        axes[1, 0].plot(df['year'], df['noix_de_coco'], label='Noix de coco', linewidth=2, marker='d')
        axes[1, 0].set_title('Évolution des prix des fruits spécifiques', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Taux d'inflation
        axes[1, 1].bar(df['year'], df['inflation'], color='orange', alpha=0.7)
        axes[1, 1].set_title('Taux d\'inflation annuel en Polynésie française', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_polynesie_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['riz', 'poulet', 'bananes', 'poisson']
        
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
        display_df = key_df[['year', 'riz', 'poulet', 'bananes', 'poisson', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['riz', 'poulet', 'bananes', 'poisson']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Riz (€/kg)', 'Poulet (€/kg)', 'Bananes (€/kg)', 
                             'Poisson (€/kg)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_polynesie_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_polynesie_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE LA POLYNÉSIE FRANÇAISE")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🌾 Prix moyen du riz: {df['riz'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🍌 Prix moyen des bananes: {df['bananes'].mean():.2f} €/kg")
        print(f"🐟 Prix moyen du poisson: {df['poisson'].mean():.2f} €/kg")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['riz', 'poulet', 'bananes', 'poisson', 'indice_alimentaire']
        product_names = ['Riz', 'Poulet', 'Bananes', 'Poisson', 'Indice alimentaire']
        
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
        products = ['riz', 'taro', 'patate_douce', 'manioc', 'igname', 'tomates', 'oignons', 
                   'concombre', 'salade', 'chou', 'carottes', 'bananes', 'ananas', 'mangues', 
                   'papaye', 'pamplemousse', 'citron_vert', 'noix_de_coco', 'poulet', 'bœuf', 
                   'porc', 'poisson', 'thon', 'crevettes', 'lait', 'œufs', 'sucre', 'farine', 
                   'huile', 'pain', 'café', 'vanille', 'fruit_de_la_passion', 'goyave', 'letchi', 
                   'uru_fruit_à_pain', 'fei_banane_plantain', 'poe']
        
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
        
        # Spécificités polynésiennes
        print(f"\n🌺 SPÉCIFICITÉS POLYNÉSIENNES")
        poisson_increase = ((df[df['year'] == 2025]['poisson'].values[0] - 
                           df[df['year'] == 2002]['poisson'].values[0]) / 
                           df[df['year'] == 2002]['poisson'].values[0] * 100)
        print(f"• Le poisson, aliment de base, a augmenté de {poisson_increase:.1f}%")
        
        produits_traditionnels = ['taro', 'uru_fruit_à_pain', 'fei_banane_plantain', 'poe']
        for produit in produits_traditionnels:
            augmentation = ((df[df['year'] == 2025][produit].values[0] - 
                           df[df['year'] == 2002][produit].values[0]) / 
                           df[df['year'] == 2002][produit].values[0] * 100)
            print(f"• {produit.capitalize()}: {augmentation:+.1f}%")
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de la Polynésie française...")
        
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
        print("   - mercuriales_polynesie_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_polynesie_annees_cles.csv (années clés)")
        print("   - mercuriales_polynesie_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_polynesie_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = PolynesieMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()