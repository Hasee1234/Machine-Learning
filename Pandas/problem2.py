import pandas as pd
s=pd.Series([100,200,"python",300.12,400])
s_new=pd.concat([s,pd.Series([100,"php"])],ignore_index=True)
print(s_new)