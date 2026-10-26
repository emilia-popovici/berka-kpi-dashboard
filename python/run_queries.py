import os
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path
from sqlalchemy import create_engine, text

ROOT = Path(__file__).resolve().parent.parent
SQL_DIR = ROOT / "sql"
OUT_DIR = ROOT / "output"
OUT_DIR.mkdir(exist_ok=True)

load_dotenv(ROOT / ".env")
engine = create_engine(os.environ["DB_URL"])

for fisier in sorted(SQL_DIR.glob("*.sql")):
    sql = fisier.read_text()
    df = pd.read_sql(text(sql), engine)
    iesire = OUT_DIR / f"{fisier.stem}.csv"
    df.to_csv(iesire, index=False)
    print(f"{fisier.name}: {len(df)} randuri -> {iesire.name}", flush=True)