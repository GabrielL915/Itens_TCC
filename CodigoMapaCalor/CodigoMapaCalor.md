# Código de Mapa de Calor de uma Matriz de Coocorrência

Este script Python realiza uma análise de coocorrência utilizando uma planilha Excel como entrada. O código lê uma planilha, calcula a matriz de co-ocorrência para as colunas fornecidas e, em seguida, gera um mapa de calor usando `seaborn` e `matplotlib`.

## Como Usar
1. Clone este repositório para o seu computador.
2. Navegue até o diretório do projeto.
3. Execute o script `script-palavras-chaves.py`.
 ```bash
  py script-busca.py

 ```

## Configuração
Para executar este script, você precisará ter um ambiente Python configurado com as bibliotecas `pandas`, `seaborn` e `matplotlib` instaladas. 

1. Instale as bibliotecas necessárias, se ainda não estiverem instaladas:

```bash
pip install pandas seaborn matplotlib

 ```

### Adicionar Rota da Planilha

2. Para especificar a pasta de onde os PDFs serão lidos, modifique a seguinte linha no script:

 ```python
 excelFile = pd.read_excel('ROTA DA PLANILHA AQUI', sheet_name='NOME DA ABA')
 
 ```
