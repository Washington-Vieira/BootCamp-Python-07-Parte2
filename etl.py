import pandas as pd
import os
import glob
# uma funcao de extract que le e consolida json

#glob listar qualquer biblioteca sempre quando quiser colocar qualquer nome coloca *
pasta = 'data'
def extrair_dados(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    #Concatenar dataframe
    df_total = pd.concat(df_list, ignore_index=True)
    return(df_total)

print(extrair_dados(path=pasta))
    #print(df_total)
# uma funcao que transforma

# uma funcao que le load em csv ou parquet


