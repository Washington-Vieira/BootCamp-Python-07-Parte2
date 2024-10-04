import pandas as pd
import os
import glob

# Definindo a pasta onde os arquivos JSON estão armazenados
pasta = 'data'

def extrair_dados(path: str) -> pd.DataFrame:
    # Listando todos os arquivos JSON na pasta especificada
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    
    # Lendo cada arquivo JSON e armazenando em uma lista de DataFrames
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    
    # Concatenando todos os DataFrames em um único DataFrame
    df_total = pd.concat(df_list, ignore_index=True)
    
    return df_total

# Chamando a função e imprimindo o DataFrame consolidado
print(extrair_dados(path=pasta))
