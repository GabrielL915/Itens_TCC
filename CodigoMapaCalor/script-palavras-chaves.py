import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

excelFile = pd.read_excel('', sheet_name='')

colunsExcel = excelFile.columns.tolist()

matrizCoOcorrencia = pd.DataFrame(columns=colunsExcel, index=colunsExcel)

for i in colunsExcel:
    for j in colunsExcel:
        matrizCoOcorrencia.loc[i, j] = (excelFile[i] & excelFile[j]).sum()

matrizCoOcorrencia = matrizCoOcorrencia.astype(int)

matrizCoOcorrencia.to_excel('matrizCoOcorrencia.xlsx', sheet_name='Planilha1')

plt.figure(figsize=(10, 8))

sns.heatmap(matrizCoOcorrencia, annot=True, fmt='d', cmap='Blues')

plt.title('Mapa de calor da matriz de co-ocorrência', fontsize=20)
plt.xlabel('CaracteristicasX', fontsize=13)
plt.ylabel('CaracteristicasY', fontsize=13)

plt.savefig('mapaCalor.png', dpi=300, bbox_inches='tight')

plt.close()