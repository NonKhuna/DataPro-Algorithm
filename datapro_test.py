from datapro import DataPro
import pandas as pd

# Read data file
df = pd.read_excel("street_road.xlsx")
df = df.dropna()

# Choose a column.
data_sample = df["รหัสสายทาง"]


# Create datapro object.
s = DataPro(alpha=0.05, k_percentage=1)


# Train with data
s.fit(data_sample)

# show result
print(s.evaluate_score())
