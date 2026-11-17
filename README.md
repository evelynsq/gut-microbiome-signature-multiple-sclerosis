# Gut Microbiome Molecular Signature Derivation for Detection of Multiple Sclerosis

```
.
├── EDA.ipynb
├── README.md
├── data
│   ├── original_datasets
│   └── preprocessed
├── environment.yml
└── make_DFs.ipynb
```

Notable files:

- `EDA.ipynb` contains initial exploratory data analysis of the two datasets.
- `make_DFs.ipynb` contains the preprocessing done to get our (Sample x Feature) dataframes found in `data/preprocessed`

Install dependencies:
```
conda env create -f environment.yml
```

Activate environment:
```
conda activate ms-gut-microbiota
```
