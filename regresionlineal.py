from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

try:
    import seaborn as sb
except ImportError:
    sb = None

from sklearn.linear_model import LinearRegression

# === Cargar CSV (mismo directorio del script) ===
BASE = Path(__file__).resolve().parent
csv_path = BASE / "altura.csv"
df = pd.read_csv(csv_path)

# === Normalizar nombres de columnas (quita espacios y pone minúsculas) ===
df.columns = df.columns.str.strip().str.lower()

# DEBUG: verifica nombres reales de columnas
print("Columnas:", repr(list(df.columns)))  # p.ej. ['altura', 'peso']

# Asegúrate de que existan
required = {"altura", "peso"}
if not required.issubset(df.columns):
    raise ValueError(f"El CSV debe tener columnas {required}, pero tiene {df.columns.tolist()}")

print(df.info())
print(df.head())

# === Gráfico ===
plt.figure()
if sb is not None:
    sb.scatterplot(data=df, x="altura", y="peso")
else:
    plt.scatter(df["altura"], df["peso"])
plt.xlabel("Altura (m)")
plt.ylabel("Peso (kg)")
plt.title("Altura vs. Peso")
plt.tight_layout()
plt.show()


X = df[["altura"]]   
y = df["peso"]      

modelo = LinearRegression()
modelo.fit(X, y)

altura = 1.75
pred = modelo.predict([[altura]])[0]
print(f"Para altura {altura:.2f} m, peso predicho = {pred:.2f} kg")

r2 = modelo.score(X, y)
print(f"R²: {r2:.3f}")
