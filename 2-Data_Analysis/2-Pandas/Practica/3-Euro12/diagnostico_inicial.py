import pandas as pd

def diagnostico_inicial(df: pd.DataFrame) -> None:
    """
    Ejecuta automáticamente las prácticas iniciales del 1 al 3:
      1. Exploración inicial
      2. Verificación de valores nulos
      3. Verificación de duplicados
    """

    separador = "=" * 55

    # ─────────────────────────────────────────
    # 1. EXPLORACIÓN INICIAL
    # ─────────────────────────────────────────
    print(separador)
    print("📊  EXPLORACIÓN INICIAL")
    print(separador)

    print(f"\n🔷 Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
    print(f"\n🔷 Columnas: {df.columns.tolist()}")
    print(f"\n🔷 Tipos de datos:\n{df.dtypes}")
    print(f"\n🔷 Primeras 5 filas: \n{df}")
    print(f"\n🔷 Estadísticas básicas:\n{df.describe(include='all')}")

    # ─────────────────────────────────────────
    # 2. VALORES NULOS
    # ─────────────────────────────────────────
    print(f"\n{separador}")
    print("🧹  VALORES NULOS")
    print(separador)

    nulos_total      = df.isnull().sum()
    nulos_porcentaje = (nulos_total / len(df)) * 100
    resumen_nulos    = pd.DataFrame({
        "Nulos"      : nulos_total,
        "Porcentaje" : nulos_porcentaje.map("{:.2f}%".format)
    })

    columnas_con_nulos = resumen_nulos[resumen_nulos["Nulos"] > 0]

    if columnas_con_nulos.empty:
        print("\n✅ No se encontraron valores nulos.")
    else:
        print(f"\n⚠️  Columnas con nulos:\n{columnas_con_nulos}")

    # ─────────────────────────────────────────
    # 3. DUPLICADOS
    # ─────────────────────────────────────────
    print(f"\n{separador}")
    print("🔁  DUPLICADOS")
    print(separador)

    total_duplicados = df.duplicated().sum()

    if total_duplicados == 0:
        print("\n✅ No se encontraron filas duplicadas.")
    else:
        print(f"\n⚠️  Filas duplicadas encontradas : {total_duplicados}")
        print(f"\n🔷 Filas duplicadas :\n{df[df.duplicated()]}")

    print(f"\n{separador}")
    print("✔️  Diagnóstico completado.")
    print(separador)


# ─────────────────────────────────────────
# USO
# ─────────────────────────────────────────
if __name__ == "__main__":
    df = pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv")
    diagnostico_inicial(df)