import pandas as pd
file_path="/Users/jsin0034/dev/Pandasproj/Pandas.xlsx"
description_to_filter= "NAB NAB ATN"
df = pd.read_excel(file_path)
filtered_df = df[df.Description.eq(description_to_filter)]
print(filtered_df["Category"].to_string(index=False))
