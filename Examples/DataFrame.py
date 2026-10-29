import pandas as pd
df = pd.DataFrame(
    data={
        "Femme": [40, 60],
        "Homme": [60, 40]

    },
    index=["Marié", "Célibataire"]
)
New=pd.Series([20,80], index=["Marié", "Célibataire"],)
df["Nonbinaire"]=New
print(df)
print(df.dtypes)
print(df.set_index("Femme"))
print(df.columns)
new_names ={
    "Nonbinaire": "Non déterminé",
}
print(df.rename(columns=new_names))
print(df['Femme']>50)

