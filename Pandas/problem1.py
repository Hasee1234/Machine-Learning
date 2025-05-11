import pandas as pd
series=pd.Series([100,200,"python",300.12,400])
print(series.dtypes)
series2=pd.to_numeric(series, errors='coerce')
print(series2.dtypes)
# import pandas as pd
# series=pd.DataFrame([100,200,"python",300.12,400])
# print(series.dtypes)
# series2=pd.to_numeric(series[0], errors='coerce')
# print(series2.dtypes)
