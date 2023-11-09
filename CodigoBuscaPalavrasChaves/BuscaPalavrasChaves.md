# Analisador de PDF

Este projeto permite que você pesquise palavras-chave em arquivos PDF dentro de uma pasta específica e mova (ou copie) os arquivos que contêm essas palavras-chave para uma nova pasta.

## Como usar

1. Clone este repositório para o seu computador.
2. Navegue até o diretório do projeto.
3. Execute o script `script-busca.py`.
 ```bash
  py script-busca.py

 ```
## Configuração

### Adicionar Rota da Pasta

Para especificar a pasta de onde os PDFs serão lidos, modifique a seguinte linha no script:
 ```python
  directory = "ROTA_DA_PASTA_AQUI"

 ```
### Especificar Pasta de Destino

Para especificar a pasta para onde os PDFs correspondentes serão movidos, modifique a seguinte linha:
 ```python
  target_directory = "ROTA_DA_PASTA_DESTINO_AQUI"

 ```
