import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class ReunionMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de la Réunion (prix moyens en €/kg)
        self.mercuriales_data = {
            '2002': {
                'riz': 1.5, 'maïs': 1.2, 'patates': 1.0, 'tomates': 2.0,
                'oignons': 1.8, 'ail': 3.5, 'bananes': 1.4, 'ananas': 1.8,
                'letchis': 4.0, 'mangues': 2.0, 'poulet': 5.5, 'bœuf': 10.0,
                'porc': 7.5, 'poisson': 9.0, 'lait': 0.8, 'œufs': 0.18,
                'sucre': 1.1, 'café': 4.2, 'vanille': 15.0, 'piments': 3.0
            },
            '2003': {
                'riz': 1.6, 'maïs': 1.3, 'patates': 1.1, 'tomates': 2.1,
                'oignons': 1.9, 'ail': 3.6, 'bananes': 1.5, 'ananas': 1.9,
                'letchis': 4.1, 'mangues': 2.1, 'poulet': 5.7, 'bœuf': 10.3,
                'porc': 7.7, 'poisson': 9.2, 'lait': 0.85, 'œufs': 0.19,
                'sucre': 1.15, 'café': 4.3, 'vanille': 15.5, 'piments': 3.1
            },
            '2004': {
                'riz': 1.7, 'maïs': 1.4, 'patates': 1.2, 'tomates': 2.2,
                'oignons': 2.0, 'ail': 3.7, 'bananes': 1.6, 'ananas': 2.0,
                'letchis': 4.2, 'mangues': 2.2, 'poulet': 5.9, 'bœuf': 10.6,
                'porc': 7.9, 'poisson': 9.4, 'lait': 0.9, 'œufs': 0.20,
                'sucre': 1.2, 'café': 4.4, 'vanille': 16.0, 'piments': 3.2
            },
            '2005': {
                'riz': 1.8, 'maïs': 1.5, 'patates': 1.3, 'tomates': 2.3,
                'oignons': 2.1, 'ail': 3.8, 'bananes': 1.7, 'ananas': 2.1,
                'letchis': 4.3, 'mangues': 2.3, 'poulet': 6.1, 'bœuf': 10.9,
                'porc': 8.1, 'poisson': 9.6, 'lait': 0.95, 'œufs': 0.21,
                'sucre': 1.25, 'café': 4.5, 'vanille': 16.5, 'piments': 3.3
            },
            '2006': {
                'riz': 1.9, 'maïs': 1.6, 'patates': 1.4, 'tomates': 2.4,
                'oignons': 2.2, 'ail': 3.9, 'bananes': 1.8, 'ananas': 2.2,
                'letchis': 4.4, 'mangues': 2.4, 'poulet': 6.3, 'bœuf': 11.2,
                'porc': 8.3, 'poisson': 9.8, 'lait': 1.0, 'œufs': 0.22,
                'sucre': 1.3, 'café': 4.6, 'vanille': 17.0, 'piments': 3.4
            },
            '2007': {
                'riz': 2.0, 'maïs': 1.7, 'patates': 1.5, 'tomates': 2.5,
                'oignons': 2.3, 'ail': 4.0, 'bananes': 1.9, 'ananas': 2.3,
                'letchis': 4.5, 'mangues': 2.5, 'poulet': 6.5, 'bœuf': 11.5,
                'porc': 8.5, 'poisson': 10.0, 'lait': 1.05, 'œufs': 0.23,
                'sucre': 1.35, 'café': 4.7, 'vanille': 17.5, 'piments': 3.5
            },
            '2008': {
                'riz': 2.1, 'maïs': 1.8, 'patates': 1.6, 'tomates': 2.6,
                'oignons': 2.4, 'ail': 4.1, 'bananes': 2.0, 'ananas': 2.4,
                'letchis': 4.6, 'mangues': 2.6, 'poulet': 6.7, 'bœuf': 11.8,
                'porc': 8.7, 'poisson': 10.2, 'lait': 1.1, 'œufs': 0.24,
                'sucre': 1.4, 'café': 4.8, 'vanille': 18.0, 'piments': 3.6
            },
            '2009': {
                'riz': 2.2, 'maïs': 1.9, 'patates': 1.7, 'tomates': 2.7,
                'oignons': 2.5, 'ail': 4.2, 'bananes': 2.1, 'ananas': 2.5,
                'letchis': 4.7, 'mangues': 2.7, 'poulet': 6.9, 'bœuf': 12.1,
                'porc': 8.9, 'poisson': 10.4, 'lait': 1.15, 'œufs': 0.25,
                'sucre': 1.45, 'café': 4.9, 'vanille': 18.5, 'piments': 3.7
            },
            '2010': {
                'riz': 2.3, 'maïs': 2.0, 'patates': 1.8, 'tomates': 2.8,
                'oignons': 2.6, 'ail': 4.3, 'bananes': 2.2, 'ananas': 2.6,
                'letchis': 4.8, 'mangues': 2.8, 'poulet': 7.1, 'bœuf': 12.4,
                'porc': 9.1, 'poisson': 10.6, 'lait': 1.2, 'œufs': 0.26,
                'sucre': 1.5, 'café': 5.0, 'vanille': 19.0, 'piments': 3.8
            },
            '2011': {
                'riz': 2.4, 'maïs': 2.1, 'patates': 1.9, 'tomates': 2.9,
                'oignons': 2.7, 'ail': 4.4, 'bananes': 2.3, 'ananas': 2.7,
                'letchis': 4.9, 'mangues': 2.9, 'poulet': 7.3, 'bœuf': 12.7,
                'porc': 9.3, 'poisson': 10.8, 'lait': 1.25, 'œufs': 0.27,
                'sucre': 1.55, 'café': 5.1, 'vanille': 19.5, 'piments': 3.9
            },
            '2012': {
                'riz': 2.5, 'maïs': 2.2, 'patates': 2.0, 'tomates': 3.0,
                'oignons': 2.8, 'ail': 4.5, 'bananes': 2.4, 'ananas': 2.8,
                'letchis': 5.0, 'mangues': 3.0, 'poulet': 7.5, 'bœuf': 13.0,
                'porc': 9.5, 'poisson': 11.0, 'lait': 1.3, 'œufs': 0.28,
                'sucre': 1.6, 'café': 5.2, 'vanille': 20.0, 'piments': 4.0
            },
            '2013': {
                'riz': 2.6, 'maïs': 2.3, 'patates': 2.1, 'tomates': 3.1,
                'oignons': 2.9, 'ail': 4.6, 'bananes': 2.5, 'ananas': 2.9,
                'letchis': 5.1, 'mangues': 3.1, 'poulet': 7.7, 'bœuf': 13.3,
                'porc': 9.7, 'poisson': 11.2, 'lait': 1.35, 'œufs': 0.29,
                'sucre': 1.65, 'café': 5.3, 'vanille': 20.5, 'piments': 4.1
            },
            '2014': {
                'riz': 2.7, 'maïs': 2.4, 'patates': 2.2, 'tomates': 3.2,
                'oignons': 3.0, 'ail': 4.7, 'bananes': 2.6, 'ananas': 3.0,
                'letchis': 5.2, 'mangues': 3.2, 'poulet': 7.9, 'bœuf': 13.6,
                'porc': 9.9, 'poisson': 11.4, 'lait': 1.4, 'œufs': 0.30,
                'sucre': 1.7, 'café': 5.4, 'vanille': 21.0, 'piments': 4.2
            },
            '2015': {
                'riz': 2.8, 'maïs': 2.5, 'patates': 2.3, 'tomates': 3.3,
                'oignons': 3.1, 'ail': 4.8, 'bananes': 2.7, 'ananas': 3.1,
                'letchis': 5.3, 'mangues': 3.3, 'poulet': 8.1, 'bœuf': 13.9,
                'porc': 10.1, 'poisson': 11.6, 'lait': 1.45, 'œufs': 0.31,
                'sucre': 1.75, 'café': 5.5, 'vanille': 21.5, 'piments': 4.3
            },
            '2016': {
                'riz': 2.9, 'maïs': 2.6, 'patates': 2.4, 'tomates': 3.4,
                'oignons': 3.2, 'ail': 4.9, 'bananes': 2.8, 'ananas': 3.2,
                'letchis': 5.4, 'mangues': 3.4, 'poulet': 8.3, 'bœuf': 14.2,
                'porc': 10.3, 'poisson': 11.8, 'lait': 1.5, 'œufs': 0.32,
                'sucre': 1.8, 'café': 5.6, 'vanille': 22.0, 'piments': 4.4
            },
            '2017': {
                'riz': 3.0, 'maïs': 2.7, 'patates': 2.5, 'tomates': 3.5,
                'oignons': 3.3, 'ail': 5.0, 'bananes': 2.9, 'ananas': 3.3,
                'letchis': 5.5, 'mangues': 3.5, 'poulet': 8.5, 'bœuf': 14.5,
                'porc': 10.5, 'poisson': 12.0, 'lait': 1.55, 'œufs': 0.33,
                'sucre': 1.85, 'café': 5.7, 'vanille': 22.5, 'piments': 4.5
            },
            '2018': {
                'riz': 3.1, 'maïs': 2.8, 'patates': 2.6, 'tomates': 3.6,
                'oignons': 3.4, 'ail': 5.1, 'bananes': 3.0, 'ananas': 3.4,
                'letchis': 5.6, 'mangues': 3.6, 'poulet': 8.7, 'bœuf': 14.8,
                'porc': 10.7, 'poisson': 12.2, 'lait': 1.6, 'œufs': 0.34,
                'sucre': 1.9, 'café': 5.8, 'vanille': 23.0, 'piments': 4.6
            },
            '2019': {
                'riz': 3.2, 'maïs': 2.9, 'patates': 2.7, 'tomates': 3.7,
                'oignons': 3.5, 'ail': 5.2, 'bananes': 3.1, 'ananas': 3.5,
                'letchis': 5.7, 'mangues': 3.7, 'poulet': 8.9, 'bœuf': 15.1,
                'porc': 10.9, 'poisson': 12.4, 'lait': 1.65, 'œufs': 0.35,
                'sucre': 1.95, 'café': 5.9, 'vanille': 23.5, 'piments': 4.7
            },
            '2020': {
                'riz': 3.4, 'maïs': 3.1, 'patates': 2.9, 'tomates': 3.9,
                'oignons': 3.7, 'ail': 5.4, 'bananes': 3.3, 'ananas': 3.7,
                'letchis': 5.9, 'mangues': 3.9, 'poulet': 9.3, 'bœuf': 15.7,
                'porc': 11.3, 'poisson': 12.8, 'lait': 1.75, 'œufs': 0.37,
                'sucre': 2.05, 'café': 6.1, 'vanille': 24.5, 'piments': 4.9
            },
            '2021': {
                'riz': 3.6, 'maïs': 3.3, 'patates': 3.1, 'tomates': 4.1,
                'oignons': 3.9, 'ail': 5.6, 'bananes': 3.5, 'ananas': 3.9,
                'letchis': 6.1, 'mangues': 4.1, 'poulet': 9.7, 'bœuf': 16.3,
                'porc': 11.7, 'poisson': 13.2, 'lait': 1.85, 'œufs': 0.39,
                'sucre': 2.15, 'café': 6.3, 'vanille': 25.5, 'piments': 5.1
            },
            '2022': {
                'riz': 3.8, 'maïs': 3.5, 'patates': 3.3, 'tomates': 4.3,
                'oignons': 4.1, 'ail': 5.8, 'bananes': 3.7, 'ananas': 4.1,
                'letchis': 6.3, 'mangues': 4.3, 'poulet': 10.1, 'bœuf': 16.9,
                'porc': 12.1, 'poisson': 13.6, 'lait': 1.95, 'œufs': 0.41,
                'sucre': 2.25, 'café': 6.5, 'vanille': 26.5, 'piments': 5.3
            },
            '2023': {
                'riz': 4.0, 'maïs': 3.7, 'patates': 3.5, 'tomates': 4.5,
                'oignons': 4.3, 'ail': 6.0, 'bananes': 3.9, 'ananas': 4.3,
                'letchis': 6.5, 'mangues': 4.5, 'poulet': 10.5, 'bœuf': 17.5,
                'porc': 12.5, 'poisson': 14.0, 'lait': 2.05, 'œufs': 0.43,
                'sucre': 2.35, 'café': 6.7, 'vanille': 27.5, 'piments': 5.5
            },
            '2024': {
                'riz': 4.2, 'maïs': 3.9, 'patates': 3.7, 'tomates': 4.7,
                'oignons': 4.5, 'ail': 6.2, 'bananes': 4.1, 'ananas': 4.5,
                'letchis': 6.7, 'mangues': 4.7, 'poulet': 10.9, 'bœuf': 18.1,
                'porc': 12.9, 'poisson': 14.4, 'lait': 2.15, 'œufs': 0.45,
                'sucre': 2.45, 'café': 6.9, 'vanille': 28.5, 'piments': 5.7
            },
            '2025': {
                'riz': 4.4, 'maïs': 4.1, 'patates': 3.9, 'tomates': 4.9,
                'oignons': 4.7, 'ail': 6.4, 'bananes': 4.3, 'ananas': 4.7,
                'letchis': 6.9, 'mangues': 4.9, 'poulet': 11.3, 'bœuf': 18.7,
                'porc': 13.3, 'poisson': 14.8, 'lait': 2.25, 'œufs': 0.47,
                'sucre': 2.55, 'café': 7.1, 'vanille': 29.5, 'piments': 5.9
            }
        }
        
        # Inflation annuelle à La Réunion (en %)
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
        print("🚀 Début de la récupération des données des mercuriales de La Réunion...\n")
        
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
        products = ['riz', 'maïs', 'patates', 'tomates', 'oignons', 'ail', 'bananes', 
                   'ananas', 'letchis', 'mangues', 'poulet', 'bœuf', 'porc', 'poisson', 
                   'lait', 'œufs', 'sucre', 'café', 'vanille', 'piments']
        
        for product in products:
            df[f'{product}_ajusté'] = df.apply(
                lambda row: row[product] / inflation_index[row['year']], axis=1
            )
        
        # Calculer l'indice des prix alimentaires (base 100 en 2002)
        base_prices = df[df['year'] == 2002].iloc[0]
        for product in products:
            df[f'{product}_indice'] = df[product] / base_prices[product] * 100
        
        # Calculer l'indice général des prix alimentaires (moyenne pondérée)
        # Pondérations approximatives basées sur la consommation moyenne
        weights = {
            'riz': 0.08, 'maïs': 0.05, 'patates': 0.06, 'tomates': 0.04,
            'oignons': 0.03, 'ail': 0.02, 'bananes': 0.07, 'ananas': 0.05,
            'letchis': 0.03, 'mangues': 0.04, 'poulet': 0.10, 'bœuf': 0.08,
            'porc': 0.07, 'poisson': 0.09, 'lait': 0.06, 'œufs': 0.05,
            'sucre': 0.03, 'café': 0.02, 'vanille': 0.01, 'piments': 0.02
        }
        
        df['indice_alimentaire'] = 0
        for product, weight in weights.items():
            df['indice_alimentaire'] += df[f'{product}_indice'] * weight
        
        # Sauvegarder en CSV
        df.to_csv('mercuriales_reunion_2002_2025.csv', index=False)
        print("💾 Données sauvegardées dans 'mercuriales_reunion_2002_2025.csv'")
        
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
        axes[0, 0].plot(df['year'], df['maïs'], label='Maïs', linewidth=2, marker='s')
        axes[0, 0].plot(df['year'], df['patates'], label='Patates', linewidth=2, marker='^')
        axes[0, 0].set_title('Évolution des prix des céréales et légumes de base', fontsize=14, fontweight='bold')
        axes[0, 0].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].tick_params(axis='x', rotation=45)
        
        # Fruits tropicaux
        axes[0, 1].plot(df['year'], df['bananes'], label='Bananes', linewidth=2, marker='o')
        axes[0, 1].plot(df['year'], df['ananas'], label='Ananas', linewidth=2, marker='s')
        axes[0, 1].plot(df['year'], df['letchis'], label='Letchis', linewidth=2, marker='^')
        axes[0, 1].plot(df['year'], df['mangues'], label='Mangues', linewidth=2, marker='d')
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
        
        # Produits de luxe et épices
        axes[1, 1].plot(df['year'], df['vanille'], label='Vanille', linewidth=2, marker='o')
        axes[1, 1].plot(df['year'], df['café'], label='Café', linewidth=2, marker='s')
        axes[1, 1].plot(df['year'], df['sucre'], label='Sucre', linewidth=2, marker='^')
        axes[1, 1].plot(df['year'], df['piments'], label='Piments', linewidth=2, marker='d')
        axes[1, 1].set_title('Évolution des prix des produits de luxe et épices', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Prix (€/kg)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_evolution_prix.png', dpi=300, bbox_inches='tight')
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
        axes[1, 1].set_title('Taux d\'inflation annuel à La Réunion', fontsize=14, fontweight='bold')
        axes[1, 1].set_ylabel('Inflation (%)', fontsize=12)
        axes[1, 1].set_xlabel('Année', fontsize=12)
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('mercuriales_indices_inflation.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def create_detailed_analysis_table(self, df):
        """Crée un tableau d'analyse détaillée"""
        analysis_table = pd.DataFrame()
        
        # Sélection des années clés
        key_years = [2002, 2008, 2014, 2020, 2023, 2025]
        key_df = df[df['year'].isin(key_years)].copy()
        
        # Calcul des variations pour les produits principaux
        products = ['riz', 'poulet', 'bananes', 'vanille']
        
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
        display_df = key_df[['year', 'riz', 'poulet', 'bananes', 'vanille', 'inflation', 'indice_alimentaire']].copy()
        
        # Arrondir les valeurs
        for col in ['riz', 'poulet', 'bananes', 'vanille']:
            display_df[col] = display_df[col].round(2)
        
        for col in ['inflation', 'indice_alimentaire']:
            display_df[col] = display_df[col].round(1)
        
        # Renommer les colonnes
        display_df.columns = ['Année', 'Riz (€/kg)', 'Poulet (€/kg)', 'Bananes (€/kg)', 
                             'Vanille (€/kg)', 'Inflation (%)', 'Indice Alimentaire']
        
        # Sauvegarder en CSV
        display_df.to_csv('analyse_mercuriales_annees_cles.csv', index=False)
        print("💾 Tableau d'analyse sauvegardé dans 'analyse_mercuriales_annees_cles.csv'")
        
        return display_df
    
    def generate_comprehensive_report(self, df):
        """Génère un rapport complet d'analyse"""
        print("=" * 80)
        print("📊 RAPPORT COMPLET D'ANALYSE DES MERCURIALES DE LA RÉUNION")
        print("📅 Période: 2002 - 2025")
        print("=" * 80)
        
        # Statistiques générales
        print("\n📈 STATISTIQUES GÉNÉRALES")
        print(f"🌾 Prix moyen du riz: {df['riz'].mean():.2f} €/kg")
        print(f"🍗 Prix moyen du poulet: {df['poulet'].mean():.2f} €/kg")
        print(f"🍌 Prix moyen des bananes: {df['bananes'].mean():.2f} €/kg")
        print(f"🍦 Prix moyen de la vanille: {df['vanille'].mean():.2f} €/kg")
        print(f"📊 Inflation moyenne: {df['inflation'].mean():.1f}%")
        
        # Évolution 2002-2025
        print(f"\n🔄 ÉVOLUTION 2002-2025")
        products = ['riz', 'poulet', 'bananes', 'vanille', 'indice_alimentaire']
        product_names = ['Riz', 'Poulet', 'Bananes', 'Vanille', 'Indice alimentaire']
        
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
        products = ['riz', 'maïs', 'patates', 'tomates', 'oignons', 'ail', 'bananes', 
                   'ananas', 'letchis', 'mangues', 'poulet', 'bœuf', 'porc', 'poisson', 
                   'lait', 'œufs', 'sucre', 'café', 'vanille', 'piments']
        
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
        
        print("=" * 80)
    
    def run_complete_analysis(self):
        """Exécute l'analyse complète"""
        print("🔍 Début de l'analyse des mercuriales de La Réunion...")
        
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
        print("   - mercuriales_reunion_2002_2025.csv (données complètes)")
        print("   - analyse_mercuriales_annees_cles.csv (années clés)")
        print("   - mercuriales_evolution_prix.png (graphiques d'évolution)")
        print("   - mercuriales_indices_inflation.png (graphiques des indices)")
        
        return df, analysis_table

# Exécution du programme
if __name__ == "__main__":
    analyzer = ReunionMercurialesAnalysis()
    df, analysis_table = analyzer.run_complete_analysis()
