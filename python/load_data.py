import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

engine = create_engine(os.environ["DB_URL"])

trans = pd.read_csv("data/trans.csv", sep=";", low_memory=False)
trans["date"] = pd.to_datetime(trans["date"].astype(str), format="%y%m%d")
trans.to_sql("trans", engine, if_exists="replace", index=False, chunksize=50000)

for nume in ["account", "client", "disp", "loan", "card", "order", "district"]:
    df = pd.read_csv(DATA / f"{nume}.asc", sep=";")
    df.to_sql(nume, engine, if_exists="replace", index=False)