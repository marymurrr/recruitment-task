import pandas as pd
import re
from typing import Callable, Dict

VALID_LABEL = re.compile(r"^[A-Za-z_]+$")
ALLOWED_OPERATORS: Dict[str, Callable[[pd.Series, pd.Series], pd.Series]] = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
}

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # --- Validate new column name ---
    if not VALID_LABEL.fullmatch(new_column):
        return pd.DataFrame()

    # --- Validate existing column names ---
    if not all(VALID_LABEL.fullmatch(col) for col in df.columns):
        return pd.DataFrame()

    if not role or not isinstance(role, str):
        return pd.DataFrame()

    role = role.strip()

    # --- Parse expression ---
    match = re.fullmatch(r"\s*([A-Za-z_]+)\s*([\+\-\*])\s*([A-Za-z_]+)\s*", role)
    if not match:
        return pd.DataFrame()

    col1, operator, col2 = match.groups()

    # --- Validate columns existence ---
    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame()

    operation = ALLOWED_OPERATORS.get(operator)
    if not operation:
        return pd.DataFrame()

    try:
        result_df = df.copy()
        result_df[new_column] = operation(result_df[col1], result_df[col2])
        return result_df
    except Exception:
        return pd.DataFrame()
