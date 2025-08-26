import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

datos = pd.read_csv("U4_01_housing.csv")

datos.head()
datos["ocean_proximity"].value_counts()
datos.info()
datos.describe()
datos.hist(figsize=(15, 8), bins=30, edgecolor="black")
plt.tight_layout()
plt.show()

sb.scatterplot(
    x="latitude",
    y="longitude",
    data=datos,
    hue="median_house_value",
    palette="coolwarm",
    size="population",
    sizes=(10, 200),
    alpha=0.6,
    linewidth=0,
    legend="brief",
)
plt.tight_layout()
plt.show()

datos_na = datos.dropna().copy()

dummies = pd.get_dummies(datos_na["ocean_proximity"], dtype=int, prefix="ocean")
datos_na = datos_na.join(dummies).drop(columns=["ocean_proximity"])
corr_all = datos_na.corr()
sb.set(rc={'figure.figsize': (15, 8)})
sb.heatmap(corr_all, annot=True, cmap="YlGnBu")
plt.tight_layout()
plt.show()

corr_target = corr_all["median_house_value"].sort_values(ascending=False)
print("Correlación con 'median_house_value':\n", corr_target)
sb.scatterplot(x=datos_na["median_house_value"], y=datos_na["median_income"])
plt.tight_layout()
plt.show()

datos_na["bedroom_ratio"] = datos_na["total_bedrooms"] / datos_na["total_rooms"]
corr_all = datos_na.corr()
sb.set(rc={'figure.figsize': (15, 8)})
sb.heatmap(corr_all, annot=True, cmap="YlGnBu")
plt.tight_layout()
plt.show()

X = datos_na.drop(columns=["median_house_value"])  
y = datos_na["median_house_value"]                

from sklearn.model_selection import train_test_split
X_ent, X_pru, y_ent, y_pru = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LinearRegression
modelo=LinearRegression()
modelo.fit(X_ent, y_ent)
y_pred = modelo.predict(X_pru)
tabla = pd.DataFrame(
    {"Prediccion": y_pred, "Valor Real": y_pru},
    index=y_pru.index
)

tabla["Prediccion"] = tabla["Prediccion"].round(6)
tabla["Valor Real"] = tabla["Valor Real"].round(1)


muestra = tabla.sample(5, random_state=0).sort_index()

print(muestra.to_string())
print(modelo.score(X_ent, y_ent))
print(modelo.score(X_pru, y_pru))

from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_pru, y_pred)
print(mse)
rmse = np.sqrt(mse)
print(rmse)
