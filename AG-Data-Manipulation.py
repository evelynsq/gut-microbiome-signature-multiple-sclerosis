import pandas as pd

df1_samples = pd.read_excel("data/Table_S1_Participant_and_samples.xlsx", sheet_name = "Sample phenotype")

df2_species = pd.read_excel("data/Table_S5_Metagenomics_data.xlsx", sheet_name = "species")

#flip axis on df2 

df2_species = df2_species.T

df2_species.index.name = "iMSMS_ID"

df2_species = df2_species.reset_index()

merged_samples_species = df1_samples.merge(df2_species, on = "iMSMS_ID", how = "inner")

print("df1", df1_samples.shape)
print("df2", df2_species.shape)
print("merged", merged_samples_species.shape)

df1_samples_02 = pd.read_excel("data/mmc3.xlsx", sheet_name = "Microbiome particpants")

df2_species_02 = pd.read_excel("data/mmc4.xlsx", sheet_name = "Species")

id_col = df2_species_02.columns[0]
df2_species_02[id_col] = df2_species_02[id_col].astype(str).str.split("_").str[-1].str.strip()
df2_species_02 = df2_species_02.rename(columns = {id_col:"FD" })

merged_samples_species_02 = df1_samples_02.merge(df2_species_02, on = "FD", how = "inner")

print("df1", df1_samples_02.shape)
print("df2", df2_species_02.shape)
print("merged", merged_samples_species_02.shape)