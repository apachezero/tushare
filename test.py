import tushare as ts
import pandas as pd
# 导入后加入以下列，再显示时显示完全。
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)


pro = ts.pro_api("3d62f91594b6320fbc9f0d5f3e94d0e94fdd1c12f8460147ed5fee54")

df = pro.daily(ts_code="600760.sh", start_date='20210801', end_date='20210806')
print(df)
