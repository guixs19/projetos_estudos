import pandas as pd
df=pd.read_excel("Produtos_Desafio.xlsx")
#fiz um dataframe

#alterar o valores da coluna para casa decimal
df["Imposto (%)"]= df["Imposto (%)"]/100

#criar uma coluna preço com Imposto  e com a multiplicação preços com Imposto * 1+ preço unitario

df["Preço Com Imposto"]= df["Preço Unitário"] * (1+ df["Imposto (%)"])
#salva como novo arquivo xlxs
df.to_excel("Produtos_Imposto.xlsx",index=False)
