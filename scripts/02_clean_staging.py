import pandas as pd

RAW_PATH = "../data_lake/raw/"
STAGING_PATH = "../data_lake/staging/"

# Aggregated dataset
raw_agg = RAW_PATH + "dvf_statistics_aggregated.csv"
out_agg = STAGING_PATH + "dvf_statistics_aggregated_staging.csv"

df_agg = pd.read_csv(raw_agg)

# Remove duplicates
df_agg = df_agg.drop_duplicates()

# Standardize column names
df_agg.columns = df_agg.columns.str.lower().str.strip()

# Standardize text columns
for col in ["code_geo", "libelle_geo", "code_parent", "echelle_geo"]:
    df_agg[col] = df_agg[col].astype(str).str.strip().str.upper()

# Fill missing numeric values with 0
num_cols = df_agg.select_dtypes(include="float64").columns
df_agg[num_cols] = df_agg[num_cols].fillna(0)

# Keep useful columns
keep_agg = [
    "code_geo",
    "libelle_geo",
    "code_parent",
    "echelle_geo",
    "nb_ventes_whole_appartement",
    "moy_prix_m2_whole_appartement",
    "med_prix_m2_whole_appartement",
    "nb_ventes_whole_maison",
    "moy_prix_m2_whole_maison",
    "med_prix_m2_whole_maison",
    "nb_ventes_whole_apt_maison",
    "moy_prix_m2_whole_apt_maison",
    "med_prix_m2_whole_apt_maison",
    "nb_ventes_whole_local",
    "moy_prix_m2_whole_local",
    "med_prix_m2_whole_local"
]

df_agg = df_agg[keep_agg]

df_agg.to_csv(out_agg, index=False)
print("Aggregated dataset saved to STAGING")

# Monthly dataset
raw_monthly = RAW_PATH + "dvf_statistics_monthly.csv"
out_monthly = STAGING_PATH + "dvf_statistics_monthly_staging.csv"

df_monthly = pd.read_csv(raw_monthly)

# Remove duplicates
df_monthly = df_monthly.drop_duplicates()

# Standardize column names
df_monthly.columns = df_monthly.columns.str.lower().str.strip()

# Standardize text columns
for col in ["code_geo", "libelle_geo", "code_parent", "echelle_geo"]:
    df_monthly[col] = df_monthly[col].astype(str).str.strip().str.upper()

# Time preparation
df_monthly["annee_mois"] = pd.to_datetime(
    df_monthly["annee_mois"], format="%Y-%m", errors="coerce"
)

df_monthly["year"] = df_monthly["annee_mois"].dt.year
df_monthly["month"] = df_monthly["annee_mois"].dt.month

# Fill missing numeric values with 0
num_cols = df_monthly.select_dtypes(include=["float64", "int64"]).columns
df_monthly[num_cols] = df_monthly[num_cols].fillna(0)

# Keep useful columns
keep_monthly = [
    "code_geo",
    "libelle_geo",
    "code_parent",
    "echelle_geo",
    "annee_mois",
    "year",
    "month",
    "nb_ventes_maison",
    "moy_prix_m2_maison",
    "med_prix_m2_maison",
    "nb_ventes_appartement",
    "moy_prix_m2_appartement",
    "med_prix_m2_appartement",
    "nb_ventes_local",
    "moy_prix_m2_local",
    "med_prix_m2_local",
    "nb_ventes_apt_maison",
    "moy_prix_m2_apt_maison",
    "med_prix_m2_apt_maison"
]

df_monthly = df_monthly[keep_monthly]

df_monthly.to_csv(out_monthly, index=False)
print("Monthly dataset saved to STAGING")
