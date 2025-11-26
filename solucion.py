#importamos librerias
import pandas as pd
import sys

#definimos parametros
input='input/transactions_50k.jsonl'


#Realizamos la extracción
try:
    print('leemos el archivo{input}')
    df = pd.read_json(input, lines=True)
    pd.options.display.max_columns = None
except Exception as e:
    print(f"❌ Error inesperado: {e}")
    sys.exit(1)
print(df.head())

#### encuentro que la columna payment_method_type tiene una anidación de json, entonces normalizamos la columna payment_method_type
df_payment_method_type_expandida = pd.json_normalize(df['payment_method_type'])

# Unimos payment_method_type normalizado al df original
df = df.join(df_payment_method_type_expandida.add_prefix('pm_'))

print(df.head())

##agrupamos

#filtramos 
print('df')
print(df.head())
df_aprobadas = df[df["status"] == "APPROVED"]
print('df_aprobadas')
df_aprobadas.drop_duplicates(subset=["id"], inplace=True)
print(df_aprobadas)



#convertimos de datetime a time
df_aprobadas["updated_at"] = pd.to_datetime(df_aprobadas["updated_at"])
df_aprobadas["fecha"] = df_aprobadas["updated_at"].dt.date


df_group = (
    df_aprobadas
    .groupby(["pm_extra.bin", "fecha"])
    .agg(
        cantidad_transacciones=("id", "count"),
        monto_aprobado=("amount_in_cents", "sum")
    )
    .reset_index()
)

print('agrupada')
print(df_group)

# Guardamos en parquet
output_path = "output/agrupacion_bin_fecha.parquet"
df_group.to_parquet(output_path, index=False)

