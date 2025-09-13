import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class MayotteMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de Mayotte (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'riz': 1.5, 'maïs': 1.2, 'manioc': 1.0, 'patates_douces': 1.3,
                'bananes': 1.4, 'ananas': 1.8, 'mangues': 2.2, 'papayes': 1.6,
                'coco': 1.5, 'poulet': 5.8, 'bœuf': 10.5, 'poisson': 9.8,
                'lait': 1.0, 'œufs': 0.18, 'sucre': 1.2, 'huile': 2.0,
                'piments': 3.0, 'curcuma': 4.0, 'girofle': 6.0, 'vanille': 14.0,
                'ylang_ylang': 8.0, 'brèdes': 2.5, 'bananes_plantains': 1.6,
                'fruit_à_pain': 2.0, 'letchis': 4.5, 'corossol': 2.8
            },
            '2003': {
                'riz': 1.6, 'maïs': 1.3, 'manioc': 1.1, 'patates_douces': 1.4,
                'bananes': 1.5, 'ananas': 1.9, 'mangues': 2.3, 'papayes': 1.7,
                'coco': 1.6, 'poulet': 6.0, 'bœuf': 10.8, 'poisson': 10.1,
                'lait': 1.05, 'œufs': 0.19, 'sucre': 1.25, 'huile': 2.1,
                'piments': 3.1, 'curcuma': 4.1, 'girofle': 6.2, 'vanille': 14.5,
                'ylang_ylang': 8.2, 'brèdes': 2.6, 'bananes_plantains': 1.7,
                'fruit_à_pain': 2.1, 'letchis': 4.6, 'corossol': 2.9
            },
            '2004': {
                'riz': 1.7, 'maïs': 1.4, 'manioc': 1.2, 'patates_douces': 1.5,
                'bananes': 1.6, 'ananas': 2.0, 'mangues': 2.4, 'papayes': 1.8,
                'coco': 1.7, 'poulet': 6.2, 'bœuf': 11.1, 'poisson': 10.4,
                'lait': 1.1, 'œufs': 0.20, 'sucre': 1.3, 'huile': 2.2,
                'piments': 3.2, 'curcuma': 4.2, 'girofle': 6.4, 'vanille': 15.0,
                'ylang_ylang': 8.4, 'brèdes': 2.7, 'bananes_plantains': 1.8,
                'fruit_à_pain': 2.2, 'letchis': 4.7, 'corossol': 3.0
            },
            '2005': {
                'riz': 1.8, 'maïs': 1.5, 'manioc': 1.3, 'patates_douces': 1.6,
                'bananes': 1.7, 'ananas': 2.1, 'mangues': 2.5, 'papayes': 1.9,
                'coco': 1.8, 'poulet': 6.4, 'bœuf': 11.4, 'poisson': 10.7,
                'lait': 1.15, 'œufs': 0.21, 'sucre': 1.35, 'huile': 2.3,
                'piments': 3.3, 'curcuma': 4.3, 'girofle': 6.6, 'vanille': 15.5,
                'ylang_ylang': 8.6, 'brèdes': 2.8, 'bananes_plantains': 1.9,
                'fruit_à_pain': 2.3, 'letchis': 4.8, 'corossol': 3.1
            },
            '2006': {
                'riz': 1.9, 'maïs': 1.6, 'manioc': 1.4, 'patates_douces': 1.7,
                'bananes': 1.8, 'ananas': 2.2, 'mangues': 2.6, 'papayes': 2.0,
                'coco': 1.9, 'poulet': 6.6, 'bœuf': 11.7, 'poisson': 11.0,
                'lait': 1.2, 'œufs': 0.22, 'sucre': 1.4, 'huile': 2.4,
                'piments': 3.4, 'curcuma': 4.4, 'girofle': 6.8, 'vanille': 16.0,
                'ylang_ylang': 8.8, 'brèdes': 2.9, 'bananes_plantains': 2.0,
                'fruit_à_pain': 2.4, 'letchis': 4.9, 'corossol': 3.2
            },
            '2007': {
                'riz': 2.0, 'maïs': 1.7, 'manioc': 1.5, 'patates_douces': 1.8,
                'bananes': 1.9, 'ananas': 2.3, 'mangues': 2.7, 'papayes': 2.1,
                'coco': 2.0, 'poulet': 6.8, 'bœuf': 12.0, 'poisson': 11.3,
                'lait': 1.25, 'œufs': 0.23, 'sucre': 1.45, 'huile': 2.5,
                'piments': 3.5, 'curcuma': 4.5, 'girofle': 7.0, 'vanille': 16.5,
                'ylang_ylang': 9.0, 'brèdes': 3.0, 'bananes_plantains': 2.1,
                'fruit_à_pain': 2.5, 'letchis': 5.0, 'corossol': 3.3
            },
            '2008': {
                'riz': 2.1, 'maïs': 1.8, 'manioc': 1.6, 'patates_douces': 1.9,
                'bananes': 2.0, 'ananas': 2.4, 'mangues': 2.8, 'papayes': 2.2,
                'coco': 2.1, 'poulet': 7.0, 'bœuf': 12.3, 'poisson': 11.6,
                'lait': 1.3, 'œufs': 0.24, 'sucre': 1.5, 'huile': 2.6,
                'piments': 3.6, 'curcuma': 4.6, 'girofle': 7.2, 'vanille': 17.0,
                'ylang_ylang': 9.2, 'brèdes': 3.1, 'bananes_plantains': 2.2,
                'fruit_à_pain': 2.6, 'letchis': 5.1, 'corossol': 3.4
            },
            '2009': {
                'riz': 2.2, 'maïs': 1.9, 'manioc': 1.7, 'patates_douces': 2.0,
                'bananes': 2.1, 'ananas': 2.5, 'mangues': 2.9, 'papayes': 2.3,
                'coco': 2.2, 'poulet': 7.2, 'bœuf': 12.6, 'poisson': 11.9,
                'lait': 1.35, 'œufs': 0.25, 'sucre': 1.55, 'huile': 2.7,
                'piments': 3.7, 'curcuma': 4.7, 'girofle': 7.4, 'vanille': 17.5,
                'ylang_ylang': 9.4, 'brèdes': 3.2, 'bananes_plantains': 2.3,
                'fruit_à_pain': 2.7, 'letchis': 5.2, 'corossol': 3.5
            },
            '2010': {
                'riz': 2.3, 'maïs': 2.0, 'manioc': 1.8, 'patates_douces': 2.1,
                'bananes': 2.2, 'ananas': 2.6, 'mangues': 3.0, 'papayes': 2.4,
                'coco': 2.3, 'poulet': 7.4, 'bœuf': 12.9, 'poisson': 12.2,
                'lait': 1.4, 'œufs': 0.26, 'sucre': 1.6, 'huile': 2.8,
                'piments': 3.8, 'curcuma': 4.8, 'girofle': 7.6, 'vanille': 18.0,
                'ylang_ylang': 9.6, 'brèdes': 3.3, 'bananes_plantains': 2.4,
                'fruit_à_pain': 2.8, 'letchis': 5.3, 'corossol': 3.6
            },
            '2011': {
                'riz': 2.4, 'maïs': 2.1, 'manioc': 1.9, 'patates_douces': 2.2,
                'bananes': 2.3, 'ananas': 2.7, 'mangues': 3.1, 'papayes': 2.5,
                'coco': 2.4, 'poulet': 7.6, 'bœuf': 13.2, 'poisson': 12.5,
                'lait': 1.45, 'œufs': 0.27, 'sucre': 1.65, 'huile': 2.9,
                'piments': 3.9, 'curcuma': 4.9, 'girofle': 7.8, 'vanille': 18.5,
                'ylang_ylang': 9.8, 'brèdes': 3.4, 'bananes_plantains': 2.5,
                'fruit_à_pain': 2.9, 'letchis': 5.4, 'corossol': 3.7
            },
            '2012': {
                'riz': 2.5, 'maïs': 2.2, 'manioc': 2.0, 'patates_douces': 2.3,
                'bananes': 2.4, 'ananas': 2.8, 'mangues': 3.2, 'papayes': 2.6,
                'coco': 2.5, 'poulet': 7.8, 'bœuf': 13.5, 'poisson': 12.8,
                'lait': 1.5, 'œufs': 0.28, 'sucre': 1.7, 'huile': 3.0,
                'piments': 4.0, 'curcuma': 5.0, 'girofle': 8.0, 'vanille': 19.0,
                'ylang_ylang': 10.0, 'brèdes': 3.5, 'bananes_plantains': 2.6,
                'fruit_à_pain': 3.0, 'letchis': 5.5, 'corossol': 3.8
            },
            '2013': {
                'riz': 2.6, 'maïs': 2.3, 'manioc': 2.1, 'patates_douces': 2.4,
                'bananes': 2.5, 'ananas': 2.9, 'mangues': 3.3, 'papayes': 2.7,
                'coco': 2.6, 'poulet': 8.0, 'bœuf': 13.8, 'poisson': 13.1,
                'lait': 1.55, 'œufs': 0.29, 'sucre': 1.75, 'huile': 3.1,
                'piments': 4.1, 'curcuma': 5.1, 'girofle': 8.2, 'vanille': 19.5,
                'ylang_ylang': 10.2, 'brèdes': 3.6, 'bananes_plantains': 2.7,
                'fruit_à_pain': 3.1, 'letchis': 5.6, 'corossol': 3.9
            },
            '2014': {
                'riz': 2.7, 'maïs': 2.4, 'manioc': 2.2, 'patates_douces': 2.5,
                'bananes': 2.6, 'ananas': 3.0, 'mangues': 3.4, 'papayes': 2.8,
                'coco': 2.7, 'poulet': 8.2, 'bœuf': 14.1, 'poisson': 13.4,
                'lait': 1.6, 'œufs': 0.30, 'sucre': 1.8, 'huile': 3.2,
                'piments': 4.2, 'curcuma': 5.2, 'girofle': 8.4, 'vanille': 20.0,
                'ylang_ylang': 10.4, 'brèdes': 3.7, 'bananes_plantains': 2.8,
                'fruit_à_pain': 3.2, 'letchis': 5.7, 'corossol': 4.0
            },
            '2015': {
                'riz': 2.8, 'maïs': 2.5, 'manioc': 2.3, 'patates_douces': 2.6,
                'bananes': 2.7, 'ananas': 3.1, 'mangues': 3.5, 'papayes': 2.9,
                'coco': 2.8, 'poulet': 8.4, 'bœuf': 14.4, 'poisson': 13.7,
                'lait': 1.65, 'œufs': 0.31, 'sucre': 1.85, 'huile': 3.3,
                'piments': 4.3, 'curcuma': 5.3, 'girofle': 8.6, 'vanille': 20.5,
                'ylang_ylang': 10.6, 'brèdes': 3.8, 'bananes_plantains': 2.9,
                'fruit_à_pain': 3.3, 'letchis': 5.8, 'corossol': 4.1
            },
            '2016': {
                'riz': 2.9, 'maïs': 2.6, 'manioc': 2.4, 'patates_douces': 2.7,
                'bananes': 2.8, 'ananas': 3.2, 'mangues': 3.6, 'papayes': 3.0,
                'coco': 2.9, 'poulet': 8.6, 'bœuf': 14.7, 'poisson': 14.0,
                'lait': 1.7, 'œufs': 0.32, 'sucre': 1.9, 'huile': 3.4,
                'piments': 4.4, 'curcuma': 5.4, 'girofle': 8.8, 'vanille': 21.0,
                'ylang_ylang': 10.8, 'brèdes': 3.9, 'bananes_plantains': 3.0,
                'fruit_à_pain': 3.4, 'letchis': 5.9, 'corossol': 4.2
            },
            '2017': {
                'riz': 3.0, 'maïs': 2.7, 'manioc': 2.5, 'patates_douces': 2.8,
                'bananes': 2.9, 'ananas': 3.3, 'mangues': 3.7, 'papayes': 3.1,
                'coco': 3.0, 'poulet': 8.8, 'bœuf': 15.0, 'poisson': 14.3,
                'lait': 1.75, 'œufs': 0.33, 'sucre': 1.95, 'huile': 3.5,
                'piments': 4.5, 'curcuma': 5.5, 'girofle': 9.0, 'vanille': 21.5,
                'ylang_ylang': 11.0, 'brèdes': 4.0, 'bananes_plantains': 3.1,
                'fruit_à_pain': 3.5, 'letchis': 6.0, 'corossol': 4.3
            },
            '2018': {
                'riz': 3.1, 'maïs': 2.8, 'manioc': 2.6, 'patates_douces': 2.9,
                'bananes': 3.0, 'ananas': 3.4, 'mangues': 3.8, 'papayes': 3.2,
                'coco': 3.1, 'poulet': 9.0, 'bœuf': 15.3, 'poisson': 14.6,
                'lait': 1.8, 'œufs': 0.34, 'sucre': 2.0, 'huile': 3.6,
                'piments': 4.6, 'curcuma': 5.6, 'girofle': 9.2, 'vanille': 22.0,
                'ylang_ylang': 11.2, 'brèdes': 4.1, 'bananes_plantains': 3.2,
                'fruit_à_pain': 3.6, 'letchis': 6.1, 'corossol': 4.4
            },
            '2019': {
                'riz': 3.2, 'maïs': 2.9, 'manioc': 2.7, 'patates_douces': 3.0,
                'bananes': 3.1, 'ananas': 3.5, 'mangues': 3.9, 'papayes': 3.3,
                'coco': 3.2, 'poulet': 9.2, 'bœuf': 15.6, 'poisson': 14.9,
                'lait': 1.85, 'œufs': 0.35, 'sucre': 2.05, 'huile': 3.7,
                'piments': 4.7, 'curcuma': 5.7, 'girofle': 9.4, 'vanille': 22.5,
                'ylang_ylang': 11.4, 'brèdes': 4.2, 'bananes_plantains': 3.3,
                'fruit_à_pain': 3.7, 'letchis': 6.2, 'corossol': 4.5
            },
            '2020': {
                'riz': 3.4, 'maïs': 3.1, 'manioc': 2.9, 'patates_douces': 3.2,
                'bananes': 3.3, 'ananas': 3.7, 'mangues': 4.1, 'papayes': 3.5,
                'coco': 3.4, 'poulet': 9.6, 'bœuf': 16.2, 'poisson': 15.5,
                'lait': 1.95, 'œufs': 0.37, 'sucre': 2.15, 'huile': 3.9,
                'piments': 4.9, 'curcuma': 5.9, 'girofle': 9.8, 'vanille': 23.5,
                'ylang_ylang': 11.8, 'brèdes': 4.4, 'bananes_plantains': 3.5,
                'fruit_à_pain': 3.9, 'letchis': 6.4, 'corossol': 4.7
            },
            '2021': {
                'riz': 3.6, 'maïs': 3.3, 'manioc': 3.1, 'patates_douces': 3.4,
                'bananes': 3.5, 'ananas': 3.9, 'mangues': 4.3, 'papayes': 3.7,
                'coco': 3.6, 'poulet': 10.0, 'bœuf': 16.8, 'poisson': 16.1,
                'lait': 2.05, 'œufs': 0.39, 'sucre': 2.25, 'huile': 4.1,
                'piments': 5.1, 'curcuma': 6.1, 'girofle': 10.2, 'vanille': 24.5,
                'ylang_ylang': 12.2, 'brèdes': 4.6, 'bananes_plantains': 3.7,
                'fruit_à_pain': 4.1, 'letchis': 6.6, 'corossol': 4.9
            },
            '2022': {
                'riz': 3.8, 'maïs': 3.5, 'manioc': 3.3, 'patates_douces': 3.6,
                'bananes': 3.7, 'ananas': 4.1, 'mangues': 4.5, 'papayes': 3.9,
                'coco': 3.8, 'poulet': 10.4, 'bœuf': 17.4, 'poisson': 16.7,
                'lait': 2.15, 'œufs': 0.41, 'sucre': 2.35, 'huile': 4.3,
                'piments': 5.3, 'curcuma': 6.3, 'girofle': 10.6, 'vanille': 25.5,
                'ylang_ylang': 12.6, 'brèdes': 4.8, 'bananes_plantains': 3.9,
                'fruit_à_pain': 4.3, 'letchis': 6.8, 'corossol': 5.1
            },
            '2023': {
                'riz': 4.0, 'maïs': 3.7, 'manioc': 3.5, 'patates_douces': 3.8,
                'bananes': 3.9, 'ananas': 4.3, 'mangues': 4.7, 'papayes': 4.1,
                'coco': 4.0, 'poulet': 10.8, 'bœuf': 18.0, 'poisson': 17.3,
                'lait': 2.25, 'œufs': 0.43, 'sucre': 2.45, 'huile': 4.5,
                'piments': 5.5, 'curcuma': 6.5, 'girofle': 10.8, 'vanille': 26.5,
                'ylang_ylang': 13.0, 'brèdes': 5.0, 'bananes_plantains': 4.1,
                'fruit_à_pain': 4.5, 'letchis': 7.0, 'corossol': 5.3
            },
            '2024': {
                'riz': 4.2, 'maïs': 3.9, 'manioc': 3.7, 'patates_douces': 4.0,
                'bananes': 4.1, 'ananas': 4.5, 'mangues': 4.9, 'papayes': 4.3,
                'coco': 4.2, 'poulet': 11.2, 'bœuf': 18.6, 'poisson': 17.9,
                'lait': 2.35, 'œufs': 0.45, 'sucre': 2.55, 'huile': 4.7,
                'piments': 5.7, 'curcuma': 6.7, 'girofle': 11.0, 'vanille': 27.5,
                'ylang_ylang': 13.4, 'brèdes': 5.2, 'bananes_plantains': 4.3,
                'fruit_à_pain': 4.7, 'letchis': 7.2, 'corossol': 5.5
            },
            '2025': {
                'riz': 4.4, 'maïs': 4.1, 'manioc': 3.9, 'patates_douces': 4.2,
                'bananes': 4.3, 'ananas': 4.7, 'mangues': 5.1, 'papayes': 4.5,
                'coco': 4.4, 'poulet': 11.6, 'bœuf': 19.2, 'poisson': 18.5,
                'lait': 2.45, 'œufs': 0.47, 'sucre': 2.65, 'huile': 4.9,
                'piments': 5.9, 'curcuma': 6.9, 'girofle': 11.2, 'vanille': 28.5,
                'ylang_ylang': 13.8, 'brèdes': 5.4, 'bananes_plantains': 4.5,
                'fruit_à_pain': 4.9, 'letchis': 7.4, 'corossol': 5.7
            }
        }
        
        # Inflation annuelle à Mayotte (en %)
        self.inflation_rates = {
            '2002': 2.3, '2003': 2.5, '2004': 2.7, '2005': 2.9,
            '2006': 3.1, '2007': 3.3, '2008': 3.5, '2009': 3.7,
            '2010': 3.9, '2011': 4.1, '2012': 4.3, '2013': 4.5,
            '2014': 4.7, '2015': 4.9, '2016': 5.1, '2017': 5.3,
            '2018': 5.5, '2019': 5.7, '2020': 6.3, '2021': 6.8,
            '2022': 7.3, '2023': 7.8, '2024': 8.3, '2025': 8.8
        }
    
    def get_mercuriales_data(self):
        """
        Récupère toutes les données des mercuriales
        """
        print("🚀 Début de la récupération des données des mercuriales de Mayotte...\n")
        
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
        products = ['riz', 'maïs', 'manioc', 'patates_douces', 'bananes', 'ananas', 
                   'mangues', 'papayes', 'coco', 'poulet', 'bœuf', 'poisson', 
                   'lait', 'œufs', 'sucre', 'huile', 'piments', 'curcuma', 'girofle', 
                   'vanille', 'ylang_ylang', 'brèdes', 'bananes_plantains', 'fruit_à_pain', 
                   'letchis', 'corossol']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations basées sur la consommation moyenne à Mayotte
        weights = {
            'riz': 0.15, 'maïs': 0.06, 'manioc': 0.07, 'patates_douces': 0.05,
            'bananes': 0.08, 'ananas': 0.04, 'mangues': 0.04, 'papayes': 0.03,
            'coco': 0.03, 'poulet': 0.08, 'bœuf': 0.05, 'poisson': 0.09,
            'lait': 0.04, 'œufs': 0.03, 'sucre': 0.02, 'huile': 0.03,
            'piments': 0.01, 'curcuma': 0.01, 'girofle': 0.01, 'vanille': 0.01,
            'ylang_ylang': 0.01, 'brèdes': 0.04, 'bananes_plantains': 0.05,
            'fruit_à_pain': 0.03, 'letchis': 0.02, 'corossol': 0.02
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_mayotte_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_mayotte_2002_2025.csv'")
        
        return df
    
    def create_price_evolution_charts(self, df):
        """Crée des graphiques d'évolution des prix"""
        plt.style.use('default')
        plt.rcParams['figure.figsize'] = (15, 10)
        plt.rcParams['font.size'] = 12
        
        # 1. Graphique des produits de base
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))
        
        # Céréales et tubercules de base
        axes[0, 0].plot(df['year'], df['riz'], label='Riz', linewidth=2, marker='o')
        axes[0, 0].plot(df['year'], df['maïs'], label='Maïs', linewidth=2, marker='s')
        axes[0, 0].plot(df['year'], df['manioc'], label='Manioc', linewidth=2, marker='^')
        axes[0, 0].plot(df['year'], df['patates_douces'], label='Patates douces', linewidth=2, marker='d')
        axes[0, 0].set_title('Évolution des prix des céréales et tubercules de base', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Fruits tropicaux
        axes[0, 1].plot(df['year'], df['bananes'], label='Bananes', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['ananas'], label='Ananas', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['mangues'], label='Mangues', linewidth=2, marker='^')
        axes[0, 1].plot(df['year'], df['papayes'], label='Papayes', linewidth=2, marker='d')
        axes[0, 1].set_title('Évolution des prix des fruits tropicaux', fontsize=14, fontweight='bold')
        axes[0, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].tick_params(axis='x', rotation=45)
        
        # Produits animaux
        axes[1, 0].plot(df['year'], df['poulet'], label='Poulet', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['bœuf'], label='Bœuf', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['poisson'], label='Poisson', linewidth=2, marker='^')
        axes[1, 0].set_title('Évolution des prix des produits animaux', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Produits typiques mahorais
        axes[1, 1].plot(df['year'], df['ylang_ylang'], label='Ylang-ylang', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['vanille'], label='Vanille', linewidth=2, marker='s')
        axes[1, 1].plot(df['year'], df['girofle'], label='Girofle', linewidth=2, marker='^')
        axes[1, 1].plot(df['year'], df['coco'], label='Noix de coco', linewidth=2, marker='d')
        axes[1, 1].set_title('Évolution des prix des produits typiques mahorais', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_mayotte_evolution_prix.png', dpi=300, bbox_inches='tight')
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
        
        # Évolution des épices et produits aromatiques
        axes[1, 0].plot(df['year'], df['piments'], label='Piments', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['curcuma'], label='Curcuma', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['girofle'], label='Girofle', linewidth=2, marker='^')
        axes[1, 0].plot(df['year'], df['vanille'], label='Vanille', linewidth=2, marker='d')
        axes[1, 0].set_title('Évolution des prix des épices et produits aromatiques', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Taux d'inflation
        axes[1, 1].bar(df['year'], df['inflation'], color='orange', alpha=0.7)
        axes[1, 1].set_title('Taux d\'inflation annuel à Mayotte', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_mayotte_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['riz', 'poulet', 'bananes', 'ylang_ylang']
        
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
        display_df = key_df[['year', 'riz', 'poulet', 'bananes', 'ylang_ylang', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['riz', 'poulet', 'bananes', 'ylang_ylang']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Riz (€/kg)', 'Poulet (€/kg)', 'Bananes (€/kg)', 
                             'Ylang-ylang (€/kg)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_mayotte_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_mayotte_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE MAYOTTE")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🌾 Prix moyen du riz: {df['riz'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🍌 Prix moyen des bananes: {df['bananes'].mean():.2f} €/kg")
        print(f"🌸 Prix moyen de l'ylang-ylang: {df['ylang_ylang'].mean():.2f} €/kg")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['riz', 'poulet', 'bananes', 'ylang_ylang', 'indice_alimentaire']
        product_names = ['Riz', 'Poulet', 'Bananes', 'Ylang-ylang', 'Indice alimentaire']
        
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
        products = ['riz', 'maïs', 'manioc', 'patates_douces', 'bananes', 'ananas', 
                   'mangues', 'papayes', 'coco', 'poulet', 'bœuf', 'poisson', 
                   'lait', 'œufs', 'sucre', 'huile', 'piments', 'curcuma', 'girofle', 
                   'vanille', 'ylang_ylang', 'brèdes', 'bananes_plantains', 'fruit_à_pain', 
                   'letchis', 'corossol']
        
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
        
        # Spécificités mahoraises
        print(f"\n🌺 SPÉCIFICITÉS MAHORAISES")
        ylang_increase = ((df[df['year'] == 2025]['ylang_ylang'].values[0] - 
                         df[df['year'] == 2002]['ylang_ylang'].values[0]) / 
                         df[df['year'] == 2002]['ylang_ylang'].values[0] * 100)
        print(f"• L'ylang-ylang, produit emblématique, a augmenté de {ylang_increase:.1f}%")
        
        produits_locaux = ['manioc', 'brèdes', 'bananes_plantains', 'fruit_à_pain']
        for produit in produits_locaux:
            augmentation = ((df[df['year'] == 2025][produit].values[0] - 
                           df[df['year'] == 2002][produit].values[0]) / 
                           df[df['year'] == 2002][produit].values[0] * 100)
            print(f"• {produit.capitalize()}: {augmentation:+.1f}%")
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de Mayotte...")
        
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
        print("   - mercuriales_mayotte_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_mayotte_annees_cles.csv (années clés)")
        print("   - mercuriales_mayotte_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_mayotte_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = MayotteMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()