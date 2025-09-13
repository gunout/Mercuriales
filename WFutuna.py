import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class WallisFutunaMercurialesAnalysis:
    def __init__(self):
        # Données historiques des mercuriales de Wallis et Futuna (prix moyens en XPF/kg)
        # Conversion approximative: 1€ ≈ 120 XPF
        self.mercuriales_data = {
            '2002': {
                'riz': 180, 'taro': 120, 'igname': 150, 'patates_douces': 100,
                'bananes': 150, 'papaye': 120, 'noix_de_coco': 80, 'manioc': 90,
                'fruits_a_pain': 110, 'poulet': 700, 'porc': 900, 'poisson': 1100,
                'crabe': 800, 'langouste': 1500, 'lait': 100, 'œufs': 25,
                'sucre': 130, 'farine': 140, 'huile': 300, 'conserves_poisson': 450
            },
            '2003': {
                'riz': 185, 'taro': 125, 'igname': 155, 'patates_douces': 105,
                'bananes': 155, 'papaye': 125, 'noix_de_coco': 85, 'manioc': 95,
                'fruits_a_pain': 115, 'poulet': 720, 'porc': 930, 'poisson': 1130,
                'crabe': 830, 'langouste': 1550, 'lait': 105, 'œufs': 26,
                'sucre': 135, 'farine': 145, 'huile': 310, 'conserves_poisson': 465
            },
            '2004': {
                'riz': 190, 'taro': 130, 'igname': 160, 'patates_douces': 110,
                'bananes': 160, 'papaye': 130, 'noix_de_coco': 90, 'manioc': 100,
                'fruits_a_pain': 120, 'poulet': 740, 'porc': 960, 'poisson': 1160,
                'crabe': 860, 'langouste': 1600, 'lait': 110, 'œufs': 27,
                'sucre': 140, 'farine': 150, 'huile': 320, 'conserves_poisson': 480
            },
            '2005': {
                'riz': 195, 'taro': 135, 'igname': 165, 'patates_douces': 115,
                'bananes': 165, 'papaye': 135, 'noix_de_coco': 95, 'manioc': 105,
                'fruits_a_pain': 125, 'poulet': 760, 'porc': 990, 'poisson': 1190,
                'crabe': 890, 'langouste': 1650, 'lait': 115, 'œufs': 28,
                'sucre': 145, 'farine': 155, 'huile': 330, 'conserves_poisson': 495
            },
            '2006': {
                'riz': 200, 'taro': 140, 'igname': 170, 'patates_douces': 120,
                'bananes': 170, 'papaye': 140, 'noix_de_coco': 100, 'manioc': 110,
                'fruits_a_pain': 130, 'poulet': 780, 'porc': 1020, 'poisson': 1220,
                'crabe': 920, 'langouste': 1700, 'lait': 120, 'œufs': 29,
                'sucre': 150, 'farine': 160, 'huile': 340, 'conserves_poisson': 510
            },
            '2007': {
                'riz': 210, 'taro': 145, 'igname': 175, 'patates_douces': 125,
                'bananes': 175, 'papaye': 145, 'noix_de_coco': 105, 'manioc': 115,
                'fruits_a_pain': 135, 'poulet': 800, 'porc': 1050, 'poisson': 1250,
                'crabe': 950, 'langouste': 1750, 'lait': 125, 'œufs': 30,
                'sucre': 155, 'farine': 165, 'huile': 350, 'conserves_poisson': 525
            },
            '2008': {
                'riz': 220, 'taro': 150, 'igname': 180, 'patates_douces': 130,
                'bananes': 180, 'papaye': 150, 'noix_de_coco': 110, 'manioc': 120,
                'fruits_a_pain': 140, 'poulet': 820, 'porc': 1080, 'poisson': 1280,
                'crabe': 980, 'langouste': 1800, 'lait': 130, 'œufs': 31,
                'sucre': 160, 'farine': 170, 'huile': 360, 'conserves_poisson': 540
            },
            '2009': {
                'riz': 230, 'taro': 155, 'igname': 185, 'patates_douces': 135,
                'bananes': 185, 'papaye': 155, 'noix_de_coco': 115, 'manioc': 125,
                'fruits_a_pain': 145, 'poulet': 840, 'porc': 1110, 'poisson': 1310,
                'crabe': 1010, 'langouste': 1850, 'lait': 135, 'œufs': 32,
                'sucre': 165, 'farine': 175, 'huile': 370, 'conserves_poisson': 555
            },
            '2010': {
                'riz': 240, 'taro': 160, 'igname': 190, 'patates_douces': 140,
                'bananes': 190, 'papaye': 160, 'noix_de_coco': 120, 'manioc': 130,
                'fruits_a_pain': 150, 'poulet': 860, 'porc': 1140, 'poisson': 1340,
                'crabe': 1040, 'langouste': 1900, 'lait': 140, 'œufs': 33,
                'sucre': 170, 'farine': 180, 'huile': 380, 'conserves_poisson': 570
            },
            '2011': {
                'riz': 250, 'taro': 165, 'igname': 195, 'patates_douces': 145,
                'bananes': 195, 'papaye': 165, 'noix_de_coco': 125, 'manioc': 135,
                'fruits_a_pain': 155, 'poulet': 880, 'porc': 1170, 'poisson': 1370,
                'crabe': 1070, 'langouste': 1950, 'lait': 145, 'œufs': 34,
                'sucre': 175, 'farine': 185, 'huile': 390, 'conserves_poisson': 585
            },
            '2012': {
                'riz': 260, 'taro': 170, 'igname': 200, 'patates_douces': 150,
                'bananes': 200, 'papaye': 170, 'noix_de_coco': 130, 'manioc': 140,
                'fruits_a_pain': 160, 'poulet': 900, 'porc': 1200, 'poisson': 1400,
                'crabe': 1100, 'langouste': 2000, 'lait': 150, 'œufs': 35,
                'sucre': 180, 'farine': 190, 'huile': 400, 'conserves_poisson': 600
            },
            '2013': {
                'riz': 270, 'taro': 175, 'igname': 205, 'patates_douces': 155,
                'bananes': 205, 'papaye': 175, 'noix_de_coco': 135, 'manioc': 145,
                'fruits_a_pain': 165, 'poulet': 920, 'porc': 1230, 'poisson': 1430,
                'crabe': 1130, 'langouste': 2050, 'lait': 155, 'œufs': 36,
                'sucre': 185, 'farine': 195, 'huile': 410, 'conserves_poisson': 615
            },
            '2014': {
                'riz': 280, 'taro': 180, 'igname': 210, 'patates_douces': 160,
                'bananes': 210, 'papaye': 180, 'noix_de_coco': 140, 'manioc': 150,
                'fruits_a_pain': 170, 'poulet': 940, 'porc': 1260, 'poisson': 1460,
                'crabe': 1160, 'langouste': 2100, 'lait': 160, 'œufs': 37,
                'sucre': 190, 'farine': 200, 'huile': 420, 'conserves_poisson': 630
            },
            '2015': {
                'riz': 290, 'taro': 185, 'igname': 215, 'patates_douces': 165,
                'bananes': 215, 'papaye': 185, 'noix_de_coco': 145, 'manioc': 155,
                'fruits_a_pain': 175, 'poulet': 960, 'porc': 1290, 'poisson': 1490,
                'crabe': 1190, 'langouste': 2150, 'lait': 165, 'œufs': 38,
                'sucre': 195, 'farine': 205, 'huile': 430, 'conserves_poisson': 645
            },
            '2016': {
                'riz': 300, 'taro': 190, 'igname': 220, 'patates_douces': 170,
                'bananes': 220, 'papaye': 190, 'noix_de_coco': 150, 'manioc': 160,
                'fruits_a_pain': 180, 'poulet': 980, 'porc': 1320, 'poisson': 1520,
                'crabe': 1220, 'langouste': 2200, 'lait': 170, 'œufs': 39,
                'sucre': 200, 'farine': 210, 'huile': 440, 'conserves_poisson': 660
            },
            '2017': {
                'riz': 310, 'taro': 195, 'igname': 225, 'patates_douces': 175,
                'bananes': 225, 'papaye': 195, 'noix_de_coco': 155, 'manioc': 165,
                'fruits_a_pain': 185, 'poulet': 1000, 'porc': 1350, 'poisson': 1550,
                'crabe': 1250, 'langouste': 2250, 'lait': 175, 'œufs': 40,
                'sucre': 205, 'farine': 215, 'huile': 450, 'conserves_poisson': 675
            },
            '2018': {
                'riz': 320, 'taro': 200, 'igname': 230, 'patates_douces': 180,
                'bananes': 230, 'papaye': 200, 'noix_de_coco': 160, 'manioc': 170,
                'fruits_a_pain': 190, 'poulet': 1020, 'porc': 1380, 'poisson': 1580,
                'crabe': 1280, 'langouste': 2300, 'lait': 180, 'œufs': 41,
                'sucre': 210, 'farine': 220, 'huile': 460, 'conserves_poisson': 690
            },
            '2019': {
                'riz': 330, 'taro': 205, 'igname': 235, 'patates_douces': 185,
                'bananes': 235, 'papaye': 205, 'noix_de_coco': 165, 'manioc': 175,
                'fruits_a_pain': 195, 'poulet': 1040, 'porc': 1410, 'poisson': 1610,
                'crabe': 1310, 'langouste': 2350, 'lait': 185, 'œufs': 42,
                'sucre': 215, 'farine': 225, 'huile': 470, 'conserves_poisson': 705
            },
            '2020': {
                'riz': 350, 'taro': 215, 'igname': 245, 'patates_douces': 195,
                'bananes': 245, 'papaye': 215, 'noix_de_coco': 175, 'manioc': 185,
                'fruits_a_pain': 205, 'poulet': 1080, 'porc': 1450, 'poisson': 1650,
                'crabe': 1350, 'langouste': 2450, 'lait': 195, 'œufs': 44,
                'sucre': 225, 'farine': 235, 'huile': 490, 'conserves_poisson': 735
            },
            '2021': {
                'riz': 370, 'taro': 225, 'igname': 255, 'patates_douces': 205,
                'bananes': 255, 'papaye': 225, 'noix_de_coco': 185, 'manioc': 195,
                'fruits_a_pain': 215, 'poulet': 1120, 'porc': 1490, 'poisson': 1690,
                'crabe': 1390, 'langouste': 2550, 'lait': 205, 'œufs': 46,
                'sucre': 235, 'farine': 245, 'huile': 510, 'conserves_poisson': 765
            },
            '2022': {
                'riz': 390, 'taro': 235, 'igname': 265, 'patates_douces': 215,
                'bananes': 265, 'papaye': 235, 'noix_de_coco': 195, 'manioc': 205,
                'fruits_a_pain': 225, 'poulet': 1160, 'porc': 1530, 'poisson': 1730,
                'crabe': 1430, 'langouste': 2650, 'lait': 215, 'œufs': 48,
                'sucre': 245, 'farine': 255, 'huile': 530, 'conserves_poisson': 795
            },
            '2023': {
                'riz': 410, 'taro': 245, 'igname': 275, 'patates_douces': 225,
                'bananes': 275, 'papaye': 245, 'noix_de_coco': 205, 'manioc': 215,
                'fruits_a_pain': 235, 'poulet': 1200, 'porc': 1570, 'poisson': 1770,
                'crabe': 1470, 'langouste': 2750, 'lait': 225, 'œufs': 50,
                'sucre': 255, 'farine': 265, 'huile': 550, 'conserves_poisson': 825
            },
            '2024': {
                'riz': 430, 'taro': 255, 'igname': 285, 'patates_douces': 235,
                'bananes': 285, 'papaye': 255, 'noix_de_coco': 215, 'manioc': 225,
                'fruits_a_pain': 245, 'poulet': 1240, 'porc': 1610, 'poisson': 1810,
                'crabe': 1510, 'langouste': 2850, 'lait': 235, 'œufs': 52,
                'sucre': 265, 'farine': 275, 'huile': 570, 'conserves_poisson': 855
            },
            '2025': {
                'riz': 450, 'taro': 265, 'igname': 295, 'patates_douces': 245,
                'bananes': 295, 'papaye': 265, 'noix_de_coco': 225, 'manioc': 235,
                'fruits_a_pain': 255, 'poulet': 1280, 'porc': 1650, 'poisson': 1850,
                'crabe': 1550, 'langouste': 2950, 'lait': 245, 'œufs': 54,
                'sucre': 275, 'farine': 285, 'huile': 590, 'conserves_poisson': 885
            }
        }
        
        # Catégories de produits
        self.categories = {
            'produits_de_base': ['riz', 'sucre', 'farine', 'huile', 'lait'],
            'tubercules': ['taro', 'igname', 'patates_douces', 'manioc'],
            'fruits': ['bananes', 'papaye', 'noix_de_coco', 'fruits_a_pain'],
            'viandes': ['poulet', 'porc'],
            'produits_de_la_mer': ['poisson', 'crabe', 'langouste', 'conserves_poisson'],
            'autres': ['œufs']
        }
        
        # Création du DataFrame
        self.df = pd.DataFrame(self.mercuriales_data).T
        self.years = list(self.mercuriales_data.keys())
        
    def calculate_inflation(self):
        """Calcule l'inflation annuelle pour chaque produit"""
        inflation_df = self.df.pct_change() * 100
        return inflation_df
    
    def calculate_category_prices(self):
        """Calcule le prix moyen par catégorie de produits"""
        category_prices = {}
        for category, products in self.categories.items():
            category_prices[category] = self.df[products].mean(axis=1)
        return pd.DataFrame(category_prices)
    
    def calculate_overall_inflation(self):
        """Calcule l'inflation globale moyenne par année"""
        inflation_df = self.calculate_inflation()
        return inflation_df.mean(axis=1)
    
    def plot_price_evolution(self, products=None):
        """Affiche l'évolution des prix pour certains produits"""
        if products is None:
            products = ['riz', 'taro', 'poisson', 'poulet']
        
        plt.figure(figsize=(12, 6))
        for product in products:
            if product in self.df.columns:
                plt.plot(self.years, self.df[product], marker='o', label=product)
        
        plt.title('Évolution des prix des produits alimentaires à Wallis et Futuna')
        plt.xlabel('Année')
        plt.ylabel('Prix moyen (XPF/kg)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def plot_category_evolution(self):
        """Affiche l'évolution des prix par catégorie"""
        category_prices = self.calculate_category_prices()
        
        plt.figure(figsize=(12, 6))
        for category in category_prices.columns:
            plt.plot(self.years, category_prices[category], marker='o', label=category)
        
        plt.title('Évolution des prix par catégorie de produits à Wallis et Futuna')
        plt.xlabel('Année')
        plt.ylabel('Prix moyen (XPF/kg)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def plot_inflation_rates(self):
        """Affiche les taux d'inflation par année"""
        inflation_df = self.calculate_inflation()
        overall_inflation = self.calculate_overall_inflation()
        
        plt.figure(figsize=(12, 6))
        plt.bar(self.years[1:], overall_inflation[1:], color='skyblue')
        plt.title('Taux d\'inflation annuel moyen à Wallis et Futuna')
        plt.xlabel('Année')
        plt.ylabel('Taux d\'inflation (%)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    
    def compare_products_inflation(self):
        """Compare l'inflation cumulée pour différents produits"""
        start_year = '2002'
        end_year = '2025'
        
        inflation_cumulative = (self.df.loc[end_year] / self.df.loc[start_year] - 1) * 100
        
        # Sélectionner les 10 produits avec la plus forte inflation
        top_10 = inflation_cumulative.nlargest(10)
        
        plt.figure(figsize=(12, 6))
        plt.barh(top_10.index, top_10.values, color='salmon')
        plt.title(f'Inflation cumulée des produits alimentaires à Wallis et Futuna ({start_year}-{end_year})')
        plt.xlabel('Inflation cumulée (%)')
        plt.tight_layout()
        plt.show()
    
    def generate_report(self):
        """Génère un rapport complet sur les mercuriales"""
        print("=" * 60)
        print("ANALYSE DES MERCURIALES DE WALLIS ET FUTUNA")
        print("=" * 60)
        
        # Inflation globale
        overall_inflation = self.calculate_overall_inflation()
        print(f"\nInflation moyenne annuelle: {overall_inflation.mean():.2f}%")
        
        # Produits avec la plus forte inflation
        inflation_cumulative = (self.df.loc['2025'] / self.df.loc['2002'] - 1) * 100
        top_5_inflation = inflation_cumulative.nlargest(5)
        print("\nTop 5 des produits avec la plus forte inflation (2002-2025):")
        for product, inflation in top_5_inflation.items():
            print(f"  - {product}: {inflation:.1f}%")
        
        # Produits avec la plus faible inflation
        bottom_5_inflation = inflation_cumulative.nsmallest(5)
        print("\nTop 5 des produits avec la plus faible inflation (2002-2025):")
        for product, inflation in bottom_5_inflation.items():
            print(f"  - {product}: {inflation:.1f}%")
        
        # Prix moyens par catégorie en 2025
        category_prices = self.calculate_category_prices()
        print(f"\nPrix moyens par catégorie en 2025 (XPF/kg):")
        for category in category_prices.columns:
            price = category_prices.loc['2025', category]
            print(f"  - {category}: {price:.0f} XPF/kg")
        
        print("\n" + "=" * 60)

# Exécution de l'analyse
if __name__ == "__main__":
    analysis = WallisFutunaMercurialesAnalysis()
    
    # Génération du rapport
    analysis.generate_report()
    
    # Visualisations
    analysis.plot_price_evolution()
    analysis.plot_category_evolution()
    analysis.plot_inflation_rates()
    analysis.compare_products_inflation()