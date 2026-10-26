import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
load_dotenv(ROOT / ".env")

engine = create_engine(os.environ["DB_URL"])

trans = pd.read_csv("data/trans.csv", sep=";", low_memory=False)
trans["date"] = pd.to_datetime(trans["date"].astype(str), format="%y%m%d")
trans.to_sql("trans", engine, if_exists="replace", index=False, chunksize=50000)

DATE_COLS = {
    "account": ["date"],
    "loan": ["date"],
    "card": ["issued"],
}

for nume in ["account", "client", "disp", "loan", "card", "order", "district"]:
    df = pd.read_csv(DATA / f"{nume}.csv", sep=";")
    for col in DATE_COLS.get(nume, []):
        df[col] = pd.to_datetime(df[col].astype(str).str[:6], format="%y%m%d")
    df.to_sql(nume, engine, if_exists="replace", index=False)