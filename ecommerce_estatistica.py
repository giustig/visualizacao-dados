import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

plt.hist(df['Nota'], bins=100, color='red', alpha=0.8)
plt.title('Média de notas dos produtos - Frequência')
plt.xlabel('Nota')
plt.ylabel('Quantidade')
plt.show()

plt.hexbin(df['Desconto'], df['Qtd_Vendidos_Cod'], gridsize=20, cmap='Blues')
plt.colorbar(label='Quantidade de produtos')
plt.xlabel('Desconto (em %)')
plt.ylabel('Vendas totais')
plt.title('Dispersão de Desconto e Vendas totais')
plt.show()

corr = df[['Nota', 'Preço', 'Desconto', 'Qtd_Vendidos_Cod']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f")
plt.title('Mapa de calor da correlação entre variáveis')
plt.show()

plt.figure(figsize=(10, 6))
df['Temporada'].value_counts().plot(kind='bar', color='#90ee70')
plt.title('Produtos vendidos por temporada')
plt.xlabel('Temporada')
plt.ylabel('Quantidade')
plt.xticks(rotation=75)
plt.show()

x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=64)
plt.title('Distribuição de quantidade de unidades vendidas')
plt.show()

plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color='#863e9c')
plt.title('Densidade de Notas de produtos')
plt.xlabel('Notas')
plt.show()

sns.regplot(x='Desconto', y='Qtd_Vendidos_Cod', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Unidades vendidas por desconto')
plt.xlabel('Desconto (em %)')
plt.ylabel('Unidades vendidas')
plt.show()