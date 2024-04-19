import pandas as pd
from pyproj import Transformer

def replace_comma(df, columns):
    for col in columns:
        df[col] = df[col].apply(lambda x: str(x).replace(',', '.')).astype(float)

def transform_coords(x_84, y_84):
    x_92, y_92 = transformer.transform(y_84, x_84)
    return x_92, y_92

print('''
Oczekiwany format danych wejściowych:
- Plik z rozszerzeniem xlsx. 
- Dane do konwersji znajdują się w pierwszym arkuszu. 
- Współrzędne do konwersji znajdują się w kolumnach o nagłówkach X_84, Y_84 (wielkość liter ma znaczenie)
    ''')
filename = input('\nPodaj nazwę pliku xlsx (bez rozszerzenia): ')
df = pd.read_excel(f'{filename}.xlsx', sheet_name=0)

transformer = Transformer.from_crs("epsg:4326", "epsg:2180")

columns_to_convert = ['X_84', 'Y_84']

replace_comma(df, columns_to_convert)

df[['X_92', 'Y_92']] = df.apply(lambda row: transform_coords(row['X_84'], row['Y_84']), axis=1, result_type='expand')

df.to_excel(f'{filename}_92.xlsx', index=False)
print(f'\nZapisano plik wynikowy: {filename}_92.xlsx')


