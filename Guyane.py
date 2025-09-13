import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class GuyaneMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de la Guyane (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'riz': 1.8, 'farine_manioc': 2.0, 'patates_douces': 1.6, 'igname': 1.9,
                'tomates': 2.5, 'oignons': 2.3, 'bananes': 1.7, 'ananas': 2.2,
                'mangues': 2.8, 'avocats': 3.2, 'poulet': 6.5, 'bœuf': 12.0,
                'porc': 8.5, 'poisson': 11.5, 'lait': 1.2, 'œufs': 0.22,
                'sucre': 1.4, 'café': 4.8, 'piments': 3.5, 'couac': 2.2,
                'cassave': 2.0, 'awara': 3.8, 'piment_antillais': 4.0,
                'poisson_fumé': 15.0, 'viande_brousse': 13.5, 'fruits_palmier': 3.2
            },
            '2003': {
                'riz': 1.9, 'farine_manioc': 2.1, 'patates_douces': 1.7, 'igname': 2.0,
                'tomates': 2.6, 'oignons': 2.4, 'bananes': 1.8, 'ananas': 2.3,
                'mangues': 2.9, 'avocats': 3.3, 'poulet': 6.7, 'bœuf': 12.3,
                'porc': 8.7, 'poisson': 11.8, 'lait': 1.25, 'œufs': 0.23,
                'sucre': 1.45, 'café': 4.9, 'piments': 3.6, 'couac': 2.3,
                'cassave': 2.1, 'awara': 3.9, 'piment_antillais': 4.1,
                'poisson_fumé': 15.4, 'viande_brousse': 13.8, 'fruits_palmier': 3.3
            },
            '2004': {
                'riz': 2.0, 'farine_manioc': 2.2, 'patates_douces': 1.8, 'igname': 2.1,
                'tomates': 2.7, 'oignons': 2.5, 'bananes': 1.9, 'ananas': 2.4,
                'mangues': 3.0, 'avocats': 3.4, 'poulet': 6.9, 'bœuf': 12.6,
                'porc': 8.9, 'poisson': 12.1, 'lait': 1.3, 'œufs': 0.24,
                'sucre': 1.5, 'café': 5.0, 'piments': 3.7, 'couac': 2.4,
                'cassave': 2.2, 'awara': 4.0, 'piment_antillais': 4.2,
                'poisson_fumé': 15.8, 'viande_brousse': 14.1, 'fruits_palmier': 3.4
            },
            '2005': {
                'riz': 2.1, 'farine_manioc': 2.3, 'patates_douces': 1.9, 'igname': 2.2,
                'tomates': 2.8, 'oignons': 2.6, 'bananes': 2.0, 'ananas': 2.5,
                'mangues': 3.1, 'avocats': 3.5, 'poulet': 7.1, 'bœuf': 12.9,
                'porc': 9.1, 'poisson': 12.4, 'lait': 1.35, 'œufs': 0.25,
                'sucre': 1.55, 'café': 5.1, 'piments': 3.8, 'couac': 2.5,
                'cassave': 2.3, 'awara': 4.1, 'piment_antillais': 4.3,
                'poisson_fumé': 16.2, 'viande_brousse': 14.4, 'fruits_palmier': 3.5
            },
            '2006': {
                'riz': 2.2, 'farine_manioc': 2.4, 'patates_douces': 2.0, 'igname': 2.3,
                'tomates': 2.9, 'oignons': 2.7, 'bananes': 2.1, 'ananas': 2.6,
                'mangues': 3.2, 'avocats': 3.6, 'poulet': 7.3, 'bœuf': 13.2,
                'porc': 9.3, 'poisson': 12.7, 'lait': 1.4, 'œufs': 0.26,
                'sucre': 1.6, 'café': 5.2, 'piments': 3.9, 'couac': 2.6,
                'cassave': 2.4, 'awara': 4.2, 'piment_antillais': 4.4,
                'poisson_fumé': 16.6, 'viande_brousse': 14.7, 'fruits_palmier': 3.6
            },
            '2007': {
                'riz': 2.3, 'farine_manioc': 2.5, 'patates_douces': 2.1, 'igname': 2.4,
                'tomates': 3.0, 'oignons': 2.8, 'bananes': 2.2, 'ananas': 2.7,
                'mangues': 3.3, 'avocats': 3.7, 'poulet': 7.5, 'bœuf': 13.5,
                'porc': 9.5, 'poisson': 13.0, 'lait': 1.45, 'œufs': 0.27,
                'sucre': 1.65, 'café': 5.3, 'piments': 4.0, 'couac': 2.7,
                'cassave': 2.5, 'awara': 4.3, 'piment_antillais': 4.5,
                'poisson_fumé': 17.0, 'viande_brousse': 15.0, 'fruits_palmier': 3.7
            },
            '2008': {
                'riz': 2.4, 'farine_manioc': 2.6, 'patates_douces': 2.2, 'igname': 2.5,
                'tomates': 3.1, 'oignons': 2.9, 'bananes': 2.3, 'ananas': 2.8,
                'mangues': 3.4, 'avocats': 3.8, 'poulet': 7.7, 'bœuf': 13.8,
                'porc': 9.7, 'poisson': 13.3, 'lait': 1.5, 'œufs': 0.28,
                'sucre': 1.7, 'café': 5.4, 'piments': 4.1, 'couac': 2.8,
                'cassave': 2.6, 'awara': 4.4, 'piment_antillais': 4.6,
                'poisson_fumé': 17.4, 'viande_brousse': 15.3, 'fruits_palmier': 3.8
            },
            '2009': {
                'riz': 2.5, 'farine_manioc': 2.7, 'patates_douces': 2.3, 'igname': 2.6,
                'tomates': 3.2, 'oignons': 3.0, 'bananes': 2.4, 'ananas': 2.9,
                'mangues': 3.5, 'avocats': 3.9, 'poulet': 7.9, 'bœuf': 14.1,
                'porc': 9.9, 'poisson': 13.6, 'lait': 1.55, 'œufs': 0.29,
                'sucre': 1.75, 'café': 5.5, 'piments': 4.2, 'couac': 2.9,
                'cassave': 2.7, 'awara': 4.5, 'piment_antillais': 4.7,
                'poisson_fumé': 17.8, 'viande_brousse': 15.6, 'fruits_palmier': 3.9
            },
            '2010': {
                'riz': 2.6, 'farine_manioc': 2.8, 'patates_douces': 2.4, 'igname': 2.7,
                'tomates': 3.3, 'oignons': 3.1, 'bananes': 2.5, 'ananas': 3.0,
                'mangues': 3.6, 'avocats': 4.0, 'poulet': 8.1, 'bœuf': 14.4,
                'porc': 10.1, 'poisson': 13.9, 'lait': 1.6, 'œufs': 0.30,
                'sucre': 1.8, 'café': 5.6, 'piments': 4.3, 'couac': 3.0,
                'cassave': 2.8, 'awara': 4.6, 'piment_antillais': 4.8,
                'poisson_fumé': 18.2, 'viande_brousse': 15.9, 'fruits_palmier': 4.0
            },
            '2011': {
                'riz': 2.7, 'farine_manioc': 2.9, 'patates_douces': 2.5, 'igname': 2.8,
                'tomates': 3.4, 'oignons': 3.2, 'bananes': 2.6, 'ananas': 3.1,
                'mangues': 3.7, 'avocats': 4.1, 'poulet': 8.3, 'bœuf': 14.7,
                'porc': 10.3, 'poisson': 14.2, 'lait': 1.65, 'œufs': 0.31,
                'sucre': 1.85, 'café': 5.7, 'piments': 4.4, 'couac': 3.1,
                'cassave': 2.9, 'awara': 4.7, 'piment_antillais': 4.9,
                'poisson_fumé': 18.6, 'viande_brousse': 16.2, 'fruits_palmier': 4.1
            },
            '2012': {
                'riz': 2.8, 'farine_manioc': 3.0, 'patates_douces': 2.6, 'igname': 2.9,
                'tomates': 3.5, 'oignons': 3.3, 'bananes': 2.7, 'ananas': 3.2,
                'mangues': 3.8, 'avocats': 4.2, 'poulet': 8.5, 'bœuf': 15.0,
                'porc': 10.5, 'poisson': 14.5, 'lait': 1.7, 'œufs': 0.32,
                'sucre': 1.9, 'café': 5.8, 'piments': 4.5, 'couac': 3.2,
                'cassave': 3.0, 'awara': 4.8, 'piment_antillais': 5.0,
                'poisson_fumé': 19.0, 'viande_brousse': 16.5, 'fruits_palmier': 4.2
            },
            '2013': {
                'riz': 2.9, 'farine_manioc': 3.1, 'patates_douces': 2.7, 'igname': 3.0,
                'tomates': 3.6, 'oignons': 3.4, 'bananes': 2.8, 'ananas': 3.3,
                'mangues': 3.9, 'avocats': 4.3, 'poulet': 8.7, 'bœuf': 15.3,
                'porc': 10.7, 'poisson': 14.8, 'lait': 1.75, 'œufs': 0.33,
                'sucre': 1.95, 'café': 5.9, 'piments': 4.6, 'couac': 3.3,
                'cassave': 3.1, 'awara': 4.9, 'piment_antillais': 5.1,
                'poisson_fumé': 19.4, 'viande_brousse': 16.8, 'fruits_palmier': 4.3
            },
            '2014': {
                'riz': 3.0, 'farine_manioc': 3.2, 'patates_douces': 2.8, 'igname': 3.1,
                'tomates': 3.7, 'oignons': 3.5, 'bananes': 2.9, 'ananas': 3.4,
                'mangues': 4.0, 'avocats': 4.4, 'poulet': 8.9, 'bœuf': 15.6,
                'porc': 10.9, 'poisson': 15.1, 'lait': 1.8, 'œufs': 0.34,
                'sucre': 2.0, 'café': 6.0, 'piments': 4.7, 'couac': 3.4,
                'cassave': 3.2, 'awara': 5.0, 'piment_antillais': 5.2,
                'poisson_fumé': 19.8, 'viande_brousse': 17.1, 'fruits_palmier': 4.4
            },
            '2015': {
                'riz': 3.1, 'farine_manioc': 3.3, 'patates_douces': 2.9, 'igname': 3.2,
                'tomates': 3.8, 'oignons': 3.6, 'bananes': 3.0, 'ananas': 3.5,
                'mangues': 4.1, 'avocats': 4.5, 'poulet': 9.1, 'bœuf': 15.9,
                'porc': 11.1, 'poisson': 15.4, 'lait': 1.85, 'œufs': 0.35,
                'sucre': 2.05, 'café': 6.1, 'piments': 4.8, 'couac': 3.5,
                'cassave': 3.3, 'awara': 5.1, 'piment_antillais': 5.3,
                'poisson_fumé': 20.2, 'viande_brousse': 17.4, 'fruits_palmier': 4.5
            },
            '2016': {
                'riz': 3.2, 'farine_manioc': 3.4, 'patates_douces': 3.0, 'igname': 3.3,
                'tomates': 3.9, 'oignons': 3.7, 'bananes': 3.1, 'ananas': 3.6,
                'mangues': 4.2, 'avocats': 4.6, 'poulet': 9.3, 'bœuf': 16.2,
                'porc': 11.3, 'poisson': 15.7, 'lait': 1.9, 'œufs': 0.36,
                'sucre': 2.1, 'café': 6.2, 'piments': 4.9, 'couac': 3.6,
                'cassave': 3.4, 'awara': 5.2, 'piment_antillais': 5.4,
                'poisson_fumé': 20.6, 'viande_brousse': 17.7, 'fruits_palmier': 4.6
            },
            '2017': {
                'riz': 3.3, 'farine_manioc': 3.5, 'patates_douces': 3.1, 'igname': 3.4,
                'tomates': 4.0, 'oignons': 3.8, 'bananes': 3.2, 'ananas': 3.7,
                'mangues': 4.3, 'avocats': 4.7, 'poulet': 9.5, 'bœuf': 16.5,
                'porc': 11.5, 'poisson': 16.0, 'lait': 1.95, 'œufs': 0.37,
                'sucre': 2.15, 'café': 6.3, 'piments': 5.0, 'couac': 3.7,
                'cassave': 3.5, 'awara': 5.3, 'piment_antillais': 5.5,
                'poisson_fumé': 21.0, 'viande_brousse': 18.0, 'fruits_palmier': 4.7
            },
            '2018': {
                'riz': 3.4, 'farine_manioc': 3.6, 'patates_douces': 3.2, 'igname': 3.5,
                'tomates': 4.1, 'oignons': 3.9, 'bananes': 3.3, 'ananas': 3.8,
                'mangues': 4.4, 'avocats': 4.8, 'poulet': 9.7, 'bœuf': 16.8,
                'porc': 11.7, 'poisson': 16.3, 'lait': 2.0, 'œufs': 0.38,
                'sucre': 2.2, 'café': 6.4, 'piments': 5.1, 'couac': 3.8,
                'cassave': 3.6, 'awara': 5.4, 'piment_antillais': 5.6,
                'poisson_fumé': 21.4, 'viande_brousse': 18.3, 'fruits_palmier': 4.8
            },
            '2019': {
                'riz': 3.5, 'farine_manioc': 3.7, 'patates_douces': 3.3, 'igname': 3.6,
                'tomates': 4.2, 'oignons': 4.0, 'bananes': 3.4, 'ananas': 3.9,
                'mangues': 4.5, 'avocats': 4.9, 'poulet': 9.9, 'bœuf': 17.1,
                'porc': 11.9, 'poisson': 16.6, 'lait': 2.05, 'œufs': 0.39,
                'sucre': 2.25, 'café': 6.5, 'piments': 5.2, 'couac': 3.9,
                'cassave': 3.7, 'awara': 5.5, 'piment_antillais': 5.7,
                'poisson_fumé': 21.8, 'viande_brousse': 18.6, 'fruits_palmier': 4.9
            },
            '2020': {
                'riz': 3.7, 'farine_manioc': 3.9, 'patates_douces': 3.5, 'igname': 3.8,
                'tomates': 4.4, 'oignons': 4.2, 'bananes': 3.6, 'ananas': 4.1,
                'mangues': 4.7, 'avocats': 5.1, 'poulet': 10.3, 'bœuf': 17.7,
                'porc': 12.3, 'poisson': 17.2, 'lait': 2.15, 'œufs': 0.41,
                'sucre': 2.35, 'café': 6.7, 'piments': 5.4, 'couac': 4.1,
                'cassave': 3.9, 'awara': 5.7, 'piment_antillais': 5.9,
                'poisson_fumé': 22.6, 'viande_brousse': 19.2, 'fruits_palmier': 5.1
            },
            '2021': {
                'riz': 3.9, 'farine_manioc': 4.1, 'patates_douces': 3.7, 'igname': 4.0,
                'tomates': 4.6, 'oignons': 4.4, 'bananes': 3.8, 'ananas': 4.3,
                'mangues': 4.9, 'avocats': 5.3, 'poulet': 10.7, 'bœuf': 18.3,
                'porc': 12.7, 'poisson': 17.8, 'lait': 2.25, 'œufs': 0.43,
                'sucre': 2.45, 'café': 6.9, 'piments': 5.6, 'couac': 4.3,
                'cassave': 4.1, 'awara': 5.9, 'piment_antillais': 6.1,
                'poisson_fumé': 23.4, 'viande_brousse': 19.8, 'fruits_palmier': 5.3
            },
            '2022': {
                'riz': 4.1, 'farine_manioc': 4.3, 'patates_douces': 3.9, 'igname': 4.2,
                'tomates': 4.8, 'oignons': 4.6, 'bananes': 4.0, 'ananas': 4.5,
                'mangues': 5.1, 'avocats': 5.5, 'poulet': 11.1, 'bœuf': 18.9,
                'porc': 13.1, 'poisson': 18.4, 'lait': 2.35, 'œufs': 0.45,
                'sucre': 2.55, 'café': 7.1, 'piments': 5.8, 'couac': 4.5,
                'cassave': 4.3, 'awara': 6.1, 'piment_antillais': 6.3,
                'poisson_fumé': 24.2, 'viande_brousse': 20.4, 'fruits_palmier': 5.5
            },
            '2023': {
                'riz': 4.3, 'farine_manioc': 4.5, 'patates_douces': 4.1, 'igname': 4.4,
                'tomates': 5.0, 'oignons': 4.8, 'bananes': 4.2, 'ananas': 4.7,
                'mangues': 5.3, 'avocats': 5.7, 'poulet': 11.5, 'bœuf': 19.5,
                'porc': 13.5, 'poisson': 19.0, 'lait': 2.45, 'œufs': 0.47,
                'sucre': 2.65, 'café': 7.3, 'piments': 6.0, 'couac': 4.7,
                'cassave': 4.5, 'awara': 6.3, 'piment_antillais': 6.5,
                'poisson_fumé': 25.0, 'viande_brousse': 21.0, 'fruits_palmier': 5.7
            },
            '2024': {
                'riz': 4.5, 'farine_manioc': 4.7, 'patates_douces': 4.3, 'igname': 4.6,
                'tomates': 5.2, 'oignons': 5.0, 'bananes': 4.4, 'ananas': 4.9,
                'mangues': 5.5, 'avocats': 5.9, 'poulet': 11.9, 'bœuf': 20.1,
                'porc': 13.9, 'poisson': 19.6, 'lait': 2.55, 'œufs': 0.49,
                'sucre': 2.75, 'café': 7.5, 'piments': 6.2, 'couac': 4.9,
                'cassave': 4.7, 'awara': 6.5, 'piment_antillais': 6.7,
                'poisson_fumé': 25.8, 'viande_brousse': 21.6, 'fruits_palmier': 5.9
            },
            '2025': {
                'riz': 4.7, 'farine_manioc': 4.9, 'patates_douces': 4.5, 'igname': 4.8,
                'tomates': 5.4, 'oignons': 5.2, 'bananes': 4.6, 'ananas': 5.1,
                'mangues': 5.7, 'avocats': 6.1, 'poulet': 12.3, 'bœuf': 20.7,
                'porc': 14.3, 'poisson': 20.2, 'lait': 2.65, 'œufs': 0.51,
                'sucre': 2.85, 'café': 7.7, 'piments': 6.4, 'couac': 5.1,
                'cassave': 4.9, 'awara': 6.7, 'piment_antillais': 6.9,
                'poisson_fumé': 26.6, 'viande_brousse': 22.2, 'fruits_palmier': 6.1
            }
        }
        
        # Inflation annuelle en Guyane (en %)
        self.inflation_rates = {
            '2002': 2.5, '2003': 2.7, '2004': 2.9, '2005': 3.1,
            '2006': 3.3, '2007': 3.5, '2008': 3.7, '2009': 3.9,
            '2010': 4.1, '2011': 4.3, '2012': 4.5, '2013': 4.7,
            '2014': 4.9, '2015': 5.1, '2016': 5.3, '2017': 5.5,
            '2018': 5.7, '2019': 5.9, '2020': 6.5, '2021': 7.0,
            '2022': 7.5, '2023': 8.0, '2024': 8.5, '2025': 9.0
        }
    
    def get_mercuriales_data(self):
        """
        Récupère toutes les données des mercuriales
        """
        print("🚀 Début de la récupération des données des mercuriales de la Guyane...\n")
        
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
        products = ['riz', 'farine_manioc', 'patates_douces', 'igname', 'tomates', 'oignons', 
                   'bananes', 'ananas', 'mangues', 'avocats', 'poulet', 'bœuf', 'porc', 
                   'poisson', 'lait', 'œufs', 'sucre', 'café', 'piments', 'couac',
                   'cassave', 'awara', 'piment_antillais', 'poisson_fumé', 'viande_brousse', 'fruits_palmier']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations basées sur la consommation moyenne en Guyane
        weights = {
            'riz': 0.12, 'farine_manioc': 0.08, 'patates_douces': 0.07, 'igname': 0.06,
            'tomates': 0.04, 'oignons': 0.03, 'bananes': 0.09, 'ananas': 0.04,
            'mangues': 0.04, 'avocats': 0.03, 'poulet': 0.08, 'bœuf': 0.06,
            'porc': 0.05, 'poisson': 0.09, 'lait': 0.04, 'œufs': 0.03,
            'sucre': 0.02, 'café': 0.02, 'piments': 0.01, 'couac': 0.03,
            'cassave': 0.03, 'awara': 0.02, 'piment_antillais': 0.01,
            'poisson_fumé': 0.02, 'viande_brousse': 0.02, 'fruits_palmier': 0.02
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_guyane_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_guyane_2002_2025.csv'")
        
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
        axes[0, 0].plot(df['year'], df['farine_manioc'], label='Farine de manioc', linewidth=2, marker='s')
        axes[0, 0].plot(df['year'], df['patates_douces'], label='Patates douces', linewidth=2, marker='^')
        axes[0, 0].plot(df['year'], df['igname'], label='Igname', linewidth=2, marker='d')
        axes[0, 0].set_title('Évolution des prix des céréales et tubercules de base', fontsize=14, fontweight='bold')
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
        
        # Produits typiques guyanais
        axes[1, 1].plot(df['year'], df['couac'], label='Couac', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['cassave'], label='Cassave', linewidth=2, marker='s')
        axes[1, 1].plot(df['year'], df['awara'], label='Awara', linewidth=2, marker='^')
        axes[1, 1].plot(df['year'], df['poisson_fumé'], label='Poisson fumé', linewidth=2, marker='d')
        axes[1, 1].set_title('Évolution des prix des produits typiques guyanais', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_guyane_evolution_prix.png', dpi=300, bbox_inches='tight')
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
        
        # Évolution des produits de spécialité
        axes[1, 0].plot(df['year'], df['viande_brousse'], label='Viande de brousse', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['fruits_palmier'], label='Fruits de palmier', linewidth=2, marker='s')
        axes[1, 0].plot(df['year'], df['piment_antillais'], label='Piment antillais', linewidth=2, marker='^')
        axes[1, 0].set_title('Évolution des prix des produits de spécialité', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Taux d'inflation
        axes[1, 1].bar(df['year'], df['inflation'], color='orange', alpha=0.7)
        axes[1, 1].set_title('Taux d\'inflation annuel en Guyane', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_guyane_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['riz', 'poulet', 'bananes', 'couac']
        
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
        display_df = key_df[['year', 'riz', 'poulet', 'bananes', 'couac', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['riz', 'poulet', 'bananes', 'couac']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Riz (€/kg)', 'Poulet (€/kg)', 'Bananes (€/kg)', 
                             'Couac (€/kg)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_guyane_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_guyane_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE LA GUYANE")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🌾 Prix moyen du riz: {df['riz'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🍌 Prix moyen des bananes: {df['bananes'].mean():.2f} €/kg")
        print(f"🌽 Prix moyen du couac: {df['couac'].mean():.2f} €/kg")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['riz', 'poulet', 'bananes', 'couac', 'indice_alimentaire']
        product_names = ['Riz', 'Poulet', 'Bananes', 'Couac', 'Indice alimentaire']
        
        for product, name in zip(products, product_names):
            evolution = ((df[df['year'] == 2025][product].values[0] - 
                         df[df['year'] == 2002][product].values[0]) / 
                         df[df['year'] == 2002][product].values[0] * 100)
            print(f"{name}: {evolution:+.1f}%")
        
        # Analyse des tendances
        print(f"\n📅 TENDANCES PAR PÉRIODE")
        periods = {
            "2002-2007 (Stabilité relative)": (2002, 2007),
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
        products = ['riz', 'farine_manioc', 'patates_douces', 'igname', 'tomates', 'oignons', 
                   'bananes', 'ananas', 'mangues', 'avocats', 'poulet', 'bœuf', 'porc', 
                   'poisson', 'lait', 'œufs', 'sucre', 'café', 'piments', 'couac',
                   'cassave', 'awara', 'piment_antillais', 'poisson_fumé', 'viande_brousse', 'fruits_palmier']
        
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
        
        # Spécificités guyanaises
        print(f"\n🌴 SPÉCIFICITÉS GUYANAISES")
        couac_increase = ((df[df['year'] == 2025]['couac'].values[0] - 
                         df[df['year'] == 2002]['couac'].values[0]) / 
                         df[df['year'] == 2002]['couac'].values[0] * 100)
        print(f"• Le couac, produit emblématique, a augmenté de {couac_increase:.1f}%")
        
        produits_locaux = ['farine_manioc', 'cassave', 'awara', 'viande_brousse']
        for produit in produits_locaux:
            augmentation = ((df[df['year'] == 2025][produit].values[0] - 
                           df[df['year'] == 2002][produit].values[0]) / 
                           df[df['year'] == 2002][produit].values[0] * 100)
            print(f"• {produit.capitalize()}: {augmentation:+.1f}%")
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de la Guyane...")
        
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
        print("   - mercuriales_guyane_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_guyane_annees_cles.csv (années clés)")
        print("   - mercuriales_guyane_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_guyane_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = GuyaneMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()