import numpy as np
import pandas as pd

tabela = {'numeros': [3600, 3545, 3658, 3498, 3657, 3425, 3785, 3254, 3266, 3641,
                      3687, 3698, 3621, 3654, 3554, 3569, 3598, 3578, 3567, 3574]}
df = pd.DataFrame(tabela)
print(df)
print('Média: ', df['numeros'].mean())
print('Variancia: ', f"{df['numeros'].var(ddof=0):.2f}")
print('Desvio Padrão: ', f"{df['numeros'].std(ddof=0):.2f}")
