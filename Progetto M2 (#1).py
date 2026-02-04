import pandas as pd
import numpy as np

dataset = {
    "Data": [
        "2023-01-01", "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04",
        "2023-01-05", "2023-01-05", "2023-01-06", "2023-01-07", "2023-01-08",
        "2023-01-09", "2023-01-10", None,          "2023-01-12", "2023-01-13",
        np.nan,    "2023-01-15", "2023-01-16", "2023-01-17", "2023-01-18"
    ],
    "Prodotto": [
        "A", "A", "B", "A", "C",
        "B", "B", "A", "C", "A",
        "B", "C", "A", "B", "A",
        "C", "B", "A", "C", "B"
    ],
    "Vendite": [
        10.0, 10.0, 15.0, 20.0, 5.0,
        12.0, 12.0, 18.0, 7.0, 22.0,
        14.0, 9.0, None, 16.0, 11.0,
        13.0, -5.0, 19.0, 8.0, 21.0
    ],
    "Prezzo": [
        100.0, 100.0, 150.0, 100.0, 200.0,
        150.0, 150.0, None,  200.0, 100.0,
        150.0, 200.0, 100.0, 150.0, 100.0,
        200.0, 150.0, 100.0, 200.0, 150.0
    ]
}

df = pd.DataFrame(dataset) #Creazione del dataset Pandas

print("Informazioni del Dataset") #stampa le informazioni
print(df.info())

print("Prime 5 righe del dataset") #head(5) stampa le prime 5 righe del dataset
print(df.head(5))

print("Statistiche descrittive") #.describe serve per analizzare le statistiche di base del dataset
print(df.describe())

print(f"Dataset prima delle modifiche\n")
print(df)

#-------------------------------------------------PULIZIA DEI DATI------------------------------------------------------------------------
#Elimina i valori Nan nella colonna ["Data"] e assicura che i valori delle vendite siano tutti positivi con abs()
df= df.dropna(subset=["Data"])
df["Vendite"] = df["Vendite"].abs()

df["Vendite"].fillna(df["Vendite"].mean(), inplace= True) #sostituisce i valori nulli con la media 
df["Prezzo"].fillna(df["Prezzo"].mean(), inplace= True)

#Rimozione dei dati duplicati
df["Data"] = pd.to_datetime(df["Data"], errors="coerce") #converte la data in datetime
df=df.dropna(subset=["Data"])
df = df.drop_duplicates()

print(df.info()) #Verifico che i dati siano nel formatto corretto

df["Vendite"] = df["Vendite"].round(0).astype("int32") #astype modifica il tipo di dato 
df["Prezzo"] = df["Prezzo"].astype("float16")

print(df)

print(df.info()) #informazioni del dataset per controllo pulizia ed ottimizzazione memoria

#--------------------------------------------ANALISI ESPLORATIVA--------------------------------------------------------------

vendite_totali = df.groupby("Prodotto")["Vendite"].sum().sort_values(ascending=False) #Vendite totali per prodotto 
print("Vendite totali per prodotto:")
print(vendite_totali)

più_venduto = vendite_totali.idxmax() #idmax() stampa l'indice del prodotto più venduto
meno_venduto = vendite_totali.idxmin()

print("--"*65)
print(f"\nProdotto più venduto:", più_venduto, "per", vendite_totali.max(), "unità")

print(f"\nProdotto meno venduto:", meno_venduto, "per", vendite_totali.min(), "unità")
print("--"*65)

print("Vendite per giorni") #Vendite per giorni
giornaliere = df.groupby("Data")["Vendite"].mean().sort_index() #Vendite per giorno
print(giornaliere)












