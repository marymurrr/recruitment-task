# Virtual Column – Pandas Safe Computation

Add computed columns to your pandas DataFrame safely and efficiently. Designed for recruitment tasks with robust validation and no unsafe code.

## Features
- ✅ Supports basic operations: `+`, `-`, `*`
- ✅ Validates column names before computation
- ✅ Returns empty DataFrame on invalid input
- ✅ Fully safe: no `eval`, no security risks
- ✅ Easy integration into existing projects

## Quick Example
```python
import pandas as pd
from virtual_column import add_virtual_column

df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df = add_virtual_column(df, 'c', 'a + b')
print(df)
#    a  b  c
# 0  1  3  4
# 1  2  4  6
