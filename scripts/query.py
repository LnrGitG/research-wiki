#!/usr/bin/env python3
"""
Query interface for research-wiki data layer.
Combines SQL (DuckDB) + Vector search (LanceDB).
"""
import duckdb
import pandas as pd
from pathlib import Path
import sys

ROOT = Path(__file__).parent.parent
PROCESSED = ROOT / "data/processed"

# DuckDB connection with httpfs for remote Parquet
con = duckdb.connect()
con.execute("INSTALL httpfs; LOAD httpfs;")

# Auto-register all processed Parquet files as views
def register_tables():
    for p in PROCESSED.glob("*.parquet"):
        table_name = p.stem
        # Skip metadata files
        if not table_name.endswith('.meta'):
            try:
                con.execute(f"CREATE OR REPLACE VIEW {table_name} AS SELECT * FROM read_parquet('{p}')")
            except Exception as e:
                print(f"Warning: could not register {table_name}: {e}", file=sys.stderr)

register_tables()

def sql(query: str) -> pd.DataFrame:
    """Execute SQL query on processed data."""
    return con.execute(query).fetchdf()

def list_tables() -> list:
    """List available tables."""
    return [row[0] for row in con.execute("SHOW TABLES").fetchall()]

def describe_table(table: str) -> pd.DataFrame:
    """Show table schema."""
    return con.execute(f"DESCRIBE {table}").fetchdf()

def preview(table: str, n: int = 5) -> pd.DataFrame:
    """Preview first N rows."""
    return con.execute(f"SELECT * FROM {table} LIMIT {n}").fetchdf()

def query_natural(question: str) -> dict:
    """
    Natural language query dispatcher.
    Returns dict with 'sql' results and/or 'vector' results.
    """
    q = question.lower()
    
    results = {'sql': None, 'vector': None, 'tables': list_tables()}
    
    # Detect if SQL is needed
    sql_keywords = [
        'сколько', 'динамик', 'тренд', 'сравни', 'корреляц', 'регресс', 
        'вбп', 'показател', 'таблиц', 'данн', 'числ', 'статистик',
        'график', 'plot', 'chart', 'correlation', 'regression', 'trend'
    ]
    needs_sql = any(k in q for k in sql_keywords)
    
    if needs_sql:
        # Try to auto-generate a useful query
        tables = list_tables()
        results['sql'] = {
            'available_tables': tables,
            'sample_queries': {
                'mortgage_by_region': """
                    SELECT region, period, value 
                    FROM cbr_mortgage_new_loans 
                    WHERE metric = 'volume_mln_rub' AND currency = 'TOTAL'
                    ORDER BY period DESC LIMIT 20
                """,
                'usd_rate': """
                    SELECT date, vunit_rate 
                    FROM cbr_usd_rate 
                    ORDER BY date DESC LIMIT 20
                """,
                'correlation_mortgage_usd': """
                    SELECT 
                        date_trunc('month', m.period) as month,
                        m.value as mortgage_mln_rub,
                        u.vunit_rate as usd_rate
                    FROM cbr_mortgage_new_loans m
                    JOIN cbr_usd_rate u 
                      ON date_trunc('month', m.period) = date_trunc('month', u.date)
                    WHERE m.metric = 'volume_mln_rub' AND m.currency = 'TOTAL'
                    ORDER BY month DESC LIMIT 24
                """,
            }
        }
    
    return results

def run_sql(query: str) -> pd.DataFrame:
    """Execute arbitrary SQL and return DataFrame."""
    return con.execute(query).fetchdf()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python query.py <SQL query or natural question>")
        print("Tables:", list_tables())
        sys.exit(1)
    
    arg = ' '.join(sys.argv[1:])
    
    # If it looks like SQL, execute it
    if arg.strip().upper().startswith(('SELECT', 'WITH', 'DESCRIBE', 'SHOW')):
        df = run_sql(arg)
        print(df.to_string())
    else:
        # Natural language
        import json
        result = query_natural(arg)
        print(json.dumps(result, ensure_ascii=False, indent=2, default=str))