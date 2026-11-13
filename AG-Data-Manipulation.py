import pandas as pd

df1_samples = pd.read_excel("data/Table_S1_Participant_and_samples.xlsx", sheet_name = "Sample phenotype")
df2_species = pd.read_excel("data/Table_S5_Metagenomics_data.xlsx", sheet_name = "species")

df2_species = df2_species.set_index("Taxa")

#flip axis on df2 
df2_species = df2_species.T
df2_species.index.name = "iMSMS_ID" 
df2_species = df2_species.reset_index()

merged_samples_species = df1_samples.merge(df2_species, on = "iMSMS_ID", how = "inner")

print("df1", df1_samples.shape)
print("df2", df2_species.shape)
print("merged", merged_samples_species.shape)

print("number of columns:", len(merged_samples_species.columns)) #1737 columns 
print("number of rows:", len(merged_samples_species.index)) #1152 rows 
#print("names of columns:", merged_samples_species.columns.tolist()) #Uncomment for names to print 
merged_samples_species = merged_samples_species.set_index("iMSMS_ID")
#print("names of rows", merged_samples_species.index.tolist()) #Uncomment for names to print

cohort_pos = merged_samples_species.columns.get_loc("Cohort")
taxa_cols = merged_samples_species.columns[cohort_pos + 1:]
print("number of species features:", len(taxa_cols)) #1677 features 

#removing features not needed - not species features
data = merged_samples_species.iloc[:, merged_samples_species.columns.get_loc("Cohort") + 1:]
#print("Just Species Features Named:", data.columns.tolist()) #Uncomment for just species features apart of excess column cleaned data to print 

#############################################################################################################################

df1_samples_02 = pd.read_excel("data/mmc3.xlsx", sheet_name = "Microbiome particpants")
df2_species_02 = pd.read_excel("data/mmc4.xlsx", sheet_name = "Species")

id_col = df2_species_02.columns[0]
df2_species_02[id_col] = df2_species_02[id_col].astype(str).str.split("_").str[-1].str.strip()
df2_species_02 = df2_species_02.rename(columns = {id_col:"FD" })

merged_samples_species_02 = df1_samples_02.merge(df2_species_02, on = "FD", how = "inner")

print("df1", df1_samples_02.shape)
print("df2", df2_species_02.shape)
print("merged", merged_samples_species_02.shape)

print("number of columns:", len(merged_samples_species_02.columns)) #707 columns
print("number of row:", len(merged_samples_species_02.index)) #187 rows
#print("names of columns:", merged_samples_species_02.columns.tolist()) #Uncomment for names to print
merged_samples_species_02 = merged_samples_species_02.set_index("FD") #Uncomment for names to print 
#print("names of rows", merged_samples_species_02.index.tolist())

pt_pos = merged_samples_species_02.columns.get_loc("Previous treatments")
taxa_cols_02 = merged_samples_species_02.columns[pt_pos + 1:]
print("number of species features:", len(taxa_cols_02)) #1677 features 

#removing features not needed - not species features
data_2 = merged_samples_species_02.iloc[:, merged_samples_species_02.columns.get_loc("Previous treatments") + 1:]
#print("Just Species Features Named:", data_2.columns.tolist()) #Uncomment for just species features apart of excess column cleaned data to print 

###############################################################################################################################

#### More Parsing Through DataSet 1 ####

print(merged_samples_species['treatment_status'].value_counts().reindex(['Treated', 'Untreated', 'Control']))

#Treated: 367 -- Testing Data -- 

#Untreated: 209 -- Training Data -- 

#Control: 576 

print(merged_samples_species['site'].value_counts().reindex(['San Francisco', 'Boston', 'New York', 'Edinburgh', 'Buenos Aires', 'San Sebastian', 'Pittsburgh']))

#All subjects fine for now because models will be healthy vs MS 

#San Francisco: 328 subjects

#Boston: 84 subjects  

#New York: 118 subjects 

#Edinburgh: 262 subjects 

#Buenos Aires: 258 subjects 

#San Sebastian: 78 subjects

#Pittsburgh: 24 subjects


# M vs. F 

print(merged_samples_species['sex'].value_counts().reindex(['M', 'F']))

#Total F: 601
#Total M: 551 

print(pd.crosstab(merged_samples_species['treatment_status'], merged_samples_species['sex']))

#Total Untreated F: 145
#Total Treated F: 255
#Total Control F: 201

#Total Untreated M: 64 
#Total Treated M: 112
#Total Control M: 375

##################################################################################################################
#print(merged_samples_species.columns.tolist())
#print(merged_samples_species_02.columns.tolist())

##Species names are different##
##Can also be seen looking at data and data_2##

##Standardizing data_2 features to be condensed to just species##

import re 

def standardize_species(names):

    standardized_names = [] 

    for name in names:

        match = re.search(r's__([^|]+)', name) #help here from AI with regex match -- better standardizing will be needed -- some species names have trailing letter symbols

        if match:
            species = match.group(1)
        else:
            species = name #no s__ pattern 

        species = species.replace('_', ' ')

        species = species.strip() #remove extra white space

        standardized_names.append(species)

    return standardized_names
    
results = standardize_species(data_2.columns.tolist())

#print(sorted(results))

#print(sorted(data.columns)) 

##Matching lower-case standardized data_2 features to lower-case data features##

##data_2 was standardized to match data## 

lowercase_standardized_data_2_features = {result.lower() for result in results}
lowercase_data_features = {col.lower().strip() for col in data.columns} 

matches = sorted(lowercase_standardized_data_2_features.intersection(lowercase_data_features))

print(matches)

print(len(matches))





