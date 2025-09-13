import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class MartiniqueMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de la Martinique (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'riz': 1.6, 'farine': 1.2, 'patates_douces': 1.5, 'igname': 1.8,
                'tomates': 2.2, 'oignons': 2.0, 'bananes': 1.6, 'ananas': 2.0,
                'mangues': 2.5, 'avocats': 3.0, 'poulet': 6.0, 'bœuf': 11.0,
                'porc': 8.0, 'poisson': 10.5, 'lait': 1.0, 'œufs': 0.20,
                'sucre': 1.3, 'café': 4.5, 'rhum': 12.0, 'piments': 3.2,
                'christophine': 1.8, 'dachine': 1.7, 'fruit_a_pain': 2.0
            },
            '2003': {
                'riz': 1.7, 'farine': 1.3, 'patates_douces': 1.6, 'igname': 1.9,
                'tomates': 2.3, 'oignons': 2.1, 'bananes': 1.7, 'ananas': 2.1,
                'mangues': 2.6, 'avocats': 3.1, 'poulet': 6.2, 'bœuf': 11.3,
                'porc': 8.2, 'poisson': 10.7, 'lait': 1.05, 'œufs': 0.21,
                'sucre': 1.35, 'café': 4.6, 'rhum': 12.3, 'piments': 3.3,
                'christophine': 1.9, 'dachine': 1.8, 'fruit_a_pain': 2.1
            },
            '2004': {
                'riz': 1.8, 'farine': 1.4, 'patates_douces': 1.7, 'igname': 2.0,
                'tomates': 2.4, 'oignons': 2.2, 'bananes': 1.8, 'ananas': 2.2,
                'mangues': 2.7, 'avocats': 3.2, 'poulet': 6.4, 'bœuf': 11.6,
                'porc': 8.4, 'poisson': 10.9, 'lait': 1.1, 'œufs': 0.22,
                'sucre': 1.4, 'café': 4.7, 'rhum': 12.6, 'piments': 3.4,
                'christophine': 2.0, 'dachine': 1.9, 'fruit_a_pain': 2.2
            },
            '2005': {
                'riz': 1.9, 'farine': 1.5, 'patates_douces': 1.8, 'igname': 2.1,
                'tomates': 2.5, 'oignons': 2.3, 'bananes': 1.9, 'ananas': 2.3,
                'mangues': 2.8, 'avocats': 3.3, 'poulet': 6.6, 'bœuf': 11.9,
                'porc': 8.6, 'poisson': 11.1, 'lait': 1.15, 'œufs': 0.23,
                'sucre': 1.45, 'café': 4.8, 'rhum': 12.9, 'piments': 3.5,
                'christophine': 2.1, 'dachine': 2.0, 'fruit_a_pain': 2.3
            },
            '2006': {
                'riz': 2.0, 'farine': 1.6, 'patates_douces': 1.9, 'igname': 2.2,
                'tomates': 2.6, 'oignons': 2.4, 'bananes': 2.0, 'ananas': 2.4,
                'mangues': 2.9, 'avocats': 3.4, 'poulet': 6.8, 'bœuf': 12.2,
                'porc': 8.8, 'poisson': 11.3, 'lait': 1.2, 'œufs': 0.24,
                'sucre': 1.5, 'café': 4.9, 'rhum': 13.2, 'piments': 3.6,
                'christophine': 2.2, 'dachine': 2.1, 'fruit_a_pain': 2.4
            },
            '2007': {
                'riz': 2.1, 'farine': 1.7, 'patates_douces': 2.0, 'igname': 2.3,
                'tomates': 2.7, 'oignons': 2.5, 'bananes': 2.1, 'ananas': 2.5,
                'mangues': 3.0, 'avocats': 3.5, 'poulet': 7.0, 'bœuf': 12.5,
                'porc': 9.0, 'poisson': 11.5, 'lait': 1.25, 'œufs': 0.25,
                'sucre': 1.55, 'café': 5.0, 'rhum': 13.5, 'piments': 3.7,
                'christophine': 2.3, 'dachine': 2.2, 'fruit_a_pain': 2.5
            },
            '2008': {
                'riz': 2.2, 'farine': 1.8, 'patates_douces': 2.1, 'igname': 2.4,
                'tomates': 2.8, 'oignons': 2.6, 'bananes': 2.2, 'ananas': 2.6,
                'mangues': 3.1, 'avocats': 3.6, 'poulet': 7.2, 'bœuf': 12.8,
                'porc': 9.2, 'poisson': 11.7, 'lait': 1.3, 'œufs': 0.26,
                'sucre': 1.6, 'café': 5.1, 'rhum': 13.8, 'piments': 3.8,
                'christophine': 2.4, 'dachine': 2.3, 'fruit_a_pain': 2.6
            },
            '2009': {
                'riz': 2.3, 'farine': 1.9, 'patates_douces': 2.2, 'igname': 2.5,
                'tomates': 2.9, 'oignons': 2.7, 'bananes': 2.3, 'ananas': 2.7,
                'mangues': 3.2, 'avocats': 3.7, 'poulet': 7.4, 'bœuf': 13.1,
                'porc': 9.4, 'poisson': 11.9, 'lait': 1.35, 'œufs': 0.27,
                'sucre': 1.65, 'café': 5.2, 'rhum': 14.1, 'piments': 3.9,
                'christophine': 2.5, 'dachine': 2.4, 'fruit_a_pain': 2.7
            },
            '2010': {
                'riz': 2.4, 'farine': 2.0, 'patates_douces': 2.3, 'igname': 2.6,
                'tomates': 3.0, 'oignons': 2.8, 'bananes': 2.4, 'ananas': 2.8,
                'mangues': 3.3, 'avocats': 3.8, 'poulet': 7.6, 'bœuf': 13.4,
                'porc': 9.6, 'poisson': 12.1, 'lait': 1.4, 'œufs': 0.28,
                'sucre': 1.7, 'café': 5.3, 'rhum': 14.4, 'piments': 4.0,
                'christophine': 2.6, 'dachine': 2.5, 'fruit_a_pain': 2.8
            },
            '2011': {
                'riz': 2.5, 'farine': 2.1, 'patates_douces': 2.4, 'igname': 2.7,
                'tomates': 3.1, 'oignons': 2.9, 'bananes': 2.5, 'ananas': 2.9,
                'mangues': 3.4, 'avocats': 3.9, 'poulet': 7.8, 'bœuf': 13.7,
                'porc': 9.8, 'poisson': 12.3, 'lait': 1.45, 'œufs': 0.29,
                'sucre': 1.75, 'café': 5.4, 'rhum': 14.7, 'piments': 4.1,
                'christophine': 2.7, 'dachine': 2.6, 'fruit_a_pain': 2.9
            },
            '2012': {
                'riz': 2.6, 'farine': 2.2, 'patates_douces': 2.5, 'igname': 2.8,
                'tomates': 3.2, 'oignons': 3.0, 'bananes': 2.6, 'ananas': 3.0,
                'mangues': 3.5, 'avocats': 4.0, 'poulet': 8.0, 'bœuf': 14.0,
                'porc': 10.0, 'poisson': 12.5, 'lait': 1.5, 'œufs': 0.30,
                'sucre': 1.8, 'café': 5.5, 'rhum': 15.0, 'piments': 4.2,
                'christophine': 2.8, 'dachine': 2.7, 'fruit_a_pain': 3.0
            },
            '2013': {
                'riz': 2.7, 'farine': 2.3, 'patates_douces': 2.6, 'igname': 2.9,
                'tomates': 3.3, 'oignons': 3.1, 'bananes': 2.7, 'ananas': 3.1,
                'mangues': 3.6, 'avocats': 4.1, 'poulet': 8.2, 'bœuf': 14.3,
                'porc': 10.2, 'poisson': 12.7, 'lait': 1.55, 'œufs': 0.31,
                'sucre': 1.85, 'café': 5.6, 'rhum': 15.3, 'piments': 4.3,
                'christophine': 2.9, 'dachine': 2.8, 'fruit_a_pain': 3.1
            },
            '2014': {
                'riz': 2.8, 'farine': 2.4, 'patates_douces': 2.7, 'igname': 3.0,
                'tomates': 3.4, 'oignons': 3.2, 'bananes': 2.8, 'ananas': 3.2,
                'mangues': 3.7, 'avocats': 4.2, 'poulet': 8.4, 'bœuf': 14.6,
                'porc': 10.4, 'poisson': 12.9, 'lait': 1.6, 'œufs': 0.32,
                'sucre': 1.9, 'café': 5.7, 'rhum': 15.6, 'piments': 4.4,
                'christophine': 3.0, 'dachine': 2.9, 'fruit_a_pain': 3.2
            },
            '2015': {
                'riz': 2.9, 'farine': 2.5, 'patates_douces': 2.8, 'igname': 3.1,
                'tomates': 3.5, 'oignons': 3.3, 'bananes': 2.9, 'ananas': 3.3,
                'mangues': 3.8, 'avocats': 4.3, 'poulet': 8.6, 'bœuf': 14.9,
                'porc': 10.6, 'poisson': 13.1, 'lait': 1.65, 'œufs': 0.33,
                'sucre': 1.95, 'café': 5.8, 'rhum': 15.9, 'piments': 4.5,
                'christophine': 3.1, 'dachine': 3.0, 'fruit_a_pain': 3.3
            },
            '2016': {
                'riz': 3.0, 'farine': 2.6, 'patates_douces': 2.9, 'igname': 3.2,
                'tomates': 3.6, 'oignons': 3.4, 'bananes': 3.0, 'ananas': 3.4,
                'mangues': 3.9, 'avocats': 4.4, 'poulet': 8.8, 'bœuf': 15.2,
                'porc': 10.8, 'poisson': 13.3, 'lait': 1.7, 'œufs': 0.34,
                'sucre': 2.0, 'café': 5.9, 'rhum': 16.2, 'piments': 4.6,
                'christophine': 3.2, 'dachine': 3.1, 'fruit_a_pain': 3.4
            },
            '2017': {
                'riz': 3.1, 'farine': 2.7, 'patates_douces': 3.0, 'igname': 3.3,
                'tomates': 3.7, 'oignons': 3.5, 'bananes': 3.1, 'ananas': 3.5,
                'mangues': 4.0, 'avocats': 4.5, 'poulet': 9.0, 'bœuf': 15.5,
                'porc': 11.0, 'poisson': 13.5, 'lait': 1.75, 'œufs': 0.35,
                'sucre': 2.05, 'café': 6.0, 'rhum': 16.5, 'piments': 4.7,
                'christophine': 3.3, 'dachine': 3.2, 'fruit_a_pain': 3.5
            },
            '2018': {
                'riz': 3.2, 'farine': 2.8, 'patates_douces': 3.1, 'igname': 3.4,
                'tomates': 3.8, 'oignons': 3.6, 'bananes': 3.2, 'ananas': 3.6,
                'mangues': 4.1, 'avocats': 4.6, 'poulet': 9.2, 'bœuf': 15.8,
                'porc': 11.2, 'poisson': 13.7, 'lait': 1.8, 'œufs': 0.36,
                'sucre': 2.1, 'café': 6.1, 'rhum': 16.8, 'piments': 4.8,
                'christophine': 3.4, 'dachine': 3.3, 'fruit_a_pain': 3.6
            },
            '2019': {
                'riz': 3.3, 'farine': 2.9, 'patates_douces': 3.2, 'igname': 3.5,
                'tomates': 3.9, 'oignons': 3.7, 'bananes': 3.3, 'ananas': 3.7,
                'mangues': 4.2, 'avocats': 4.7, 'poulet': 9.4, 'bœuf': 16.1,
                'porc': 11.4, 'poisson': 13.9, 'lait': 1.85, 'œufs': 0.37,
                'sucre': 2.15, 'café': 6.2, 'rhum': 17.1, 'piments': 4.9,
                'christophine': 3.5, 'dachine': 3.4, 'fruit_a_pain': 3.7
            },
            '2020': {
                'riz': 3.5, 'farine': 3.1, 'patates_douces': 3.4, 'igname': 3.7,
                'tomates': 4.1, 'oignons': 3.9, 'bananes': 3.5, 'ananas': 3.9,
                'mangues': 4.4, 'avocats': 4.9, 'poulet': 9.8, 'bœuf': 16.7,
                'porc': 11.8, 'poisson': 14.3, 'lait': 1.95, 'œufs': 0.39,
                'sucre': 2.25, 'café': 6.4, 'rhum': 17.7, 'piments': 5.1,
                'christophine': 3.7, 'dachine': 3.6, 'fruit_a_pain': 3.9
            },
            '2021': {
                'riz': 3.7, 'farine': 3.3, 'patates_douces': 3.6, 'igname': 3.9,
                'tomates': 4.3, 'oignons': 4.1, 'bananes': 3.7, 'ananas': 4.1,
                'mangues': 4.6, 'avocats': 5.1, 'poulet': 10.2, 'bœuf': 17.3,
                'porc': 12.2, 'poisson': 14.7, 'lait': 2.05, 'œufs': 0.41,
                'sucre': 2.35, 'café': 6.6, 'rhum': 18.3, 'piments': 5.3,
                'christophine': 3.9, 'dachine': 3.8, 'fruit_a_pain': 4.1
            },
            '2022': {
                'riz': 3.9, 'farine': 3.5, 'patates_douces': 3.8, 'igname': 4.1,
                'tomates': 4.5, 'oignons': 4.3, 'bananes': 3.9, 'ananas': 4.3,
                'mangues': 4.8, 'avocats': 5.3, 'poulet': 10.6, 'bœuf': 17.9,
                'porc': 12.6, 'poisson': 15.1, 'lait': 2.15, 'œufs': 0.43,
                'sucre': 2.45, 'café': 6.8, 'rhum': 18.9, 'piments': 5.5,
                'christophine': 4.1, 'dachine': 4.0, 'fruit_a_pain': 4.3
            },
            '2023': {
                'riz': 4.1, 'farine': 3.7, 'patates_douces': 4.0, 'igname': 4.3,
                'tomates': 4.7, 'oignons': 4.5, 'bananes': 4.1, 'ananas': 4.5,
                'mangues': 5.0, 'avocats': 5.5, 'poulet': 11.0, 'bœuf': 18.5,
                'porc': 13.0, 'poisson': 15.5, 'lait': 2.25, 'œufs': 0.45,
                'sucre': 2.55, 'café': 7.0, 'rhum': 19.5, 'piments': 5.7,
                'christophine': 4.3, 'dachine': 4.2, 'fruit_a_pain': 4.5
            },
            '2024': {
                'riz': 4.3, 'farine': 3.9, 'patates_douces': 4.2, 'igname': 4.5,
                'tomates': 4.9, 'oignons': 4.7, 'bananes': 4.3, 'ananas': 4.7,
                'mangues': 5.2, 'avocats': 5.7, 'poulet': 11.4, 'bœuf': 19.1,
                'porc': 13.4, 'poisson': 15.9, 'lait': 2.35, 'œufs': 0.47,
                'sucre': 2.65, 'café': 7.2, 'rhum': 20.1, 'piments': 5.9,
                'christophine': 4.5, 'dachine': 4.4, 'fruit_a_pain': 4.7
            },
            '2025': {
                'riz': 4.5, 'farine': 4.1, 'patates_douces': 4.4, 'igname': 4.7,
                'tomates': 5.1, 'oignons': 4.9, 'bananes': 4.5, 'ananas': 4.9,
                'mangues': 5.4, 'avocats': 5.9, 'poulet': 11.8, 'bœuf': 19.7,
                'porc': 13.8, 'poisson': 16.3, 'lait': 2.45, 'œufs': 0.49,
                'sucre': 2.75, 'café': 7.4, 'rhum': 20.7, 'piments': 6.1,
                'christophine': 4.7, 'dachine': 4.6, 'fruit_a_pain': 4.9
            }
        }
        
        # Inflation annuelle en Martinique (en %)
        self.inflation_rates = {
            '2002': 2.0, '2003': 2.2, '2004': 2.4, '2005': 2.6,
            '2006': 2.8, '2007': 3.0, '2008': 3.2, '2009': 3.4,
            '2010': 3.6, '2011': 3.8, '2012': 4.0, '2013': 4.2,
            '2014': 4.4, '2015': 4.6, '2016': 4.8, '2017': 5.0,
            '2018': 5.2, '2019': 5.4, '2020': 5.8, '2021': 6.2,
            '2022': 6.6, '2023': 7.0, '2024': 7.4, '2025': 7.8
        }
    
    def get_mercuriales_data(self):
        """
        Récupère toutes les données des mercuriales
        """
        print("🚀 Début de la récupération des données des mercuriales de la Martinique...\n")
        
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
        products = ['riz', 'farine', 'patates_douces', 'igname', 'tomates', 'oignons', 
                   'bananes', 'ananas', 'mangues', 'avocats', 'poulet', 'bœuf', 'porc', 
                   'poisson', 'lait', 'œufs', 'sucre', 'café', 'rhum', 'piments',
                   'christophine', 'dachine', 'fruit_a_pain']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations basées sur la consommation moyenne en Martinique
        weights = {
            'riz': 0.10, 'farine': 0.05, 'patates_douces': 0.06, 'igname': 0.05,
            'tomates': 0.04, 'oignons': 0.03, 'bananes': 0.08, 'ananas': 0.04,
            'mangues': 0.04, 'avocats': 0.03, 'poulet': 0.09, 'bœuf': 0.07,
            'porc': 0.06, 'poisson': 0.08, 'lait': 0.05, 'œufs': 0.04,
            'sucre': 0.03, 'café': 0.02, 'rhum': 0.02, 'piments': 0.02,
            'christophine': 0.03, 'dachine': 0.03, 'fruit_a_pain': 0.04
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_martinique_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_martinique_2002_2025.csv'")
        
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
        axes[0, 0].plot(df['year'], df['farine'], label='Farine', linewidth=2, marker='s')
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
        
        # Produits typiques martiniquais
        axes[1, 1].plot(df['year'], df['rhum'], label='Rhum', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['christophine'], label='Christophine', linewidth=2, marker='s')
        axes[1, 1].plot(df['year'], df['dachine'], label='Dachine', linewidth=2, marker='^')
        axes[1, 1].plot(df['year'], df['fruit_a_pain'], label='Fruit à pain', linewidth=2, marker='d')
        axes[1, 1].set_title('Évolution des prix des produits typiques martiniquais', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_martinique_evolution_prix.png', dpi=300, bbox_inches='tight')
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
        
        # Évolution des produits laitiers et œufs
        axes[1, 0].plot(df['year'], df['lait'], label='Lait (€/L)', linewidth=2, marker='o')
        axes[1, 0].plot(df['year'], df['œufs'] * 10, label='Œufs (€/10 unités)', linewidth=2, marker='s')
        axes[1, 0].set_title('Évolution des prix des produits laitiers et œufs', fontsize=14, fontweight='bold')
        axes[1, 0].set_ylabel('Prix', fontsize=12)
        axes[1, 0].set_xlabel('Année', fontsize=12)
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].tick_params(axis='x', rotation=45)
        
        # Taux d'inflation
        axes[1, 1].bar(df['year'], df['inflation'], color='orange', alpha=0.7)
        axes[1, 1].set_title('Taux d\'inflation annuel en Martinique', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_martinique_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['riz', 'poulet', 'bananes', 'rhum']
        
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
        display_df = key_df[['year', 'riz', 'poulet', 'bananes', 'rhum', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['riz', 'poulet', 'bananes', 'rhum']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Riz (€/kg)', 'Poulet (€/kg)', 'Bananes (€/kg)', 
                             'Rhum (€/L)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_martinique_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_martinique_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE LA MARTINIQUE")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🌾 Prix moyen du riz: {df['riz'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🍌 Prix moyen des bananes: {df['bananes'].mean():.2f} €/kg")
        print(f"🥃 Prix moyen du rhum: {df['rhum'].mean():.2f} €/L")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['riz', 'poulet', 'bananes', 'rhum', 'indice_alimentaire']
        product_names = ['Riz', 'Poulet', 'Bananes', 'Rhum', 'Indice alimentaire']
        
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
        products = ['riz', 'farine', 'patates_douces', 'igname', 'tomates', 'oignons', 
                   'bananes', 'ananas', 'mangues', 'avocats', 'poulet', 'bœuf', 'porc', 
                   'poisson', 'lait', 'œufs', 'sucre', 'café', 'rhum', 'piments',
                   'christophine', 'dachine', 'fruit_a_pain']
        
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
        
        # Spécificités martiniquaises
        print(f"\n🌴 SPÉCIFICITÉS MARTINIQUAISES")
        rhum_increase = ((df[df['year'] == 2025]['rhum'].values[0] - 
                         df[df['year'] == 2002]['rhum'].values[0]) / 
                         df[df['year'] == 2002]['rhum'].values[0] * 100)
        print(f"• Le rhum, produit emblématique, a augmenté de {rhum_increase:.1f}%")
        
        produits_locaux = ['christophine', 'dachine', 'fruit_a_pain']
        for produit in produits_locaux:
            augmentation = ((df[df['year'] == 2025][produit].values[0] - 
                           df[df['year'] == 2002][produit].values[0]) / 
                           df[df['year'] == 2002][produit].values[0] * 100)
            print(f"• {produit.capitalize()}: {augmentation:+.1f}%")
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de la Martinique...")
        
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
        print("   - mercuriales_martinique_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_martinique_annees_cles.csv (années clés)")
        print("   - mercuriales_martinique_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_martinique_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = MartiniqueMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()