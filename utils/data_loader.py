import pandas as pd
import os

def load_and_process_france_data(raw_dir="data/raw/France") -> pd.DataFrame:
    # --- Load Debt from World Bank ---
    debt_path = os.path.join(raw_dir, "138151a4-6fe8-4339-9bb7-028bdb79d3b3_Data.csv")
    df_wb = pd.read_csv(debt_path)
    df_wb = df_wb.dropna(subset=["Series Code"])
    df_wb = df_wb[(df_wb["Country Name"] == "France") & (df_wb["Series Code"] == "GC.DOD.TOTL.GD.ZS")]

    df_long = df_wb.melt(
        id_vars=["Country Name", "Series Name", "Series Code"],
        var_name="Year",
        value_name="DebtPctGDP"
    )
    df_long["Year"] = df_long["Year"].str.extract(r"(\d{4})")
    df_long = df_long.dropna(subset=["Year"])
    df_long["Year"] = df_long["Year"].astype(int)
    df_long["DebtPctGDP"] = pd.to_numeric(df_long["DebtPctGDP"], errors="coerce")
    df_debt = df_long[["Year", "DebtPctGDP"]].dropna()

    # --- Load Deficit Data ---
    deficit_path = os.path.join(raw_dir, "France_deficit.csv")
    df_deficit = pd.read_csv(deficit_path)

    # --- Load and Process ECB Rate ---
    ecb_path = os.path.join(raw_dir, "ECB Data Portal_20250609175119.csv")
    
    df_ecb = pd.read_csv(ecb_path)
    df_ecb.columns = ["Date", "TimePeriod", "ECBRate"]
    df_ecb["Date"] = pd.to_datetime(df_ecb["Date"], errors="coerce")
    df_ecb["ECBRate"] = pd.to_numeric(df_ecb["ECBRate"], errors="coerce")
    df_ecb = df_ecb.dropna(subset=["ECBRate"])
    df_ecb = df_ecb.sort_values("Date")

    # Create a full daily time series
    date_range = pd.date_range(start=df_ecb["Date"].min(), end=df_ecb["Date"].max(), freq="D")
    df_full = pd.DataFrame({"Date": date_range})
    df_full = df_full.merge(df_ecb[["Date", "ECBRate"]], on="Date", how="left")

    # Forward-fill to get the effective rate at each date
    df_full["ECBRate"] = df_full["ECBRate"].ffill()

    # Compute annual average ECB rate
    df_full["Year"] = df_full["Date"].dt.year
    df_ecb_annual = df_full.groupby("Year")["ECBRate"].mean().reset_index()


    # --- Merge All ---
    df = df_debt.merge(df_deficit, on="Year", how="inner")
    df = df.merge(df_ecb_annual, on="Year", how="left")
    df = df.dropna(subset=["DebtPctGDP", "DeficitPctGDP", "ECBRate"])
    df = df.sort_values("Year").reset_index(drop=True)

    return df

