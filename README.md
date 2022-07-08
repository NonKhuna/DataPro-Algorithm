# DataPro algorithm

The task is learning the common structure of data. The DataPro algorithm is the algorithm that finds statistically significant patterns in a set of token sequences.
This repository is Implemented from the paper "Learning the Common Structure of Data" by Kristina Lerman and Steven Minton.

## Installation

```
pip install datapro-learning
```

## Get started

How to use model with this lib:

```python
from datapro import DataPro
import pandas as pd

# Read data file
df = pd.read_excel("street_road.xlsx")
df = df.dropna()

# Choose a column, type list or pandas series.
data_sample = df["หน่วยรับผิดชอบ"]


# Create datapro object.
datapro = DataPro(alpha=0.05, k_percentage=10)

# Train with data
datapro.fit(data_sample)

# show result
print(datapro.evaluate_score())
```

# Customize 
## Load new type's tree.
This algorithm uses a type's tree to assign types to tokens and can be configured by using JSON file with a structure like the below.
> **_NOTE:_**  Every time there is a new significant token, it's will be a child of these nodes as a specific node.
```json
  {
    "TOKEN": {
      "regex": ".*",
      "children": [
        "PUNCT",
        "ALPHANUM"
      ],
      "parent": ""
    },
    "PUNCT": {
      "regex": "^[\\.\\?!,:'()\"]$",
      "children": [],
      "parent": "TOKEN"
    },
    "ALPHANUM": {
      "regex": "[\\da-zA-Z]+",
      "children": [
        "ALPHA",
        "NUMBER"
      ],
      "parent": "TOKEN"
    },
    "ALPHA": {
      "regex": "^[a-zA-Z]+$",
      "children": [
        "CAPS",
        "LOWER",
        "ALLCAPS"
      ],
      "parent": "ALPHANUM"
    },
  }
```
By default, these are all general token on type's tree.
```
                  TOKEN
                /        \
           PUNCT        ALPHANUM  
                     /           \
                ALPHA            NUMBER  
             /    |    \         |        \
       ALLCAPS   CAPS   LOWER   DECIMAL   INT
                                           |
                                         DIGIT
```
### Load new file 
Using method `load_tree_type`
```python
  datapro.load_tree_type("<name>.json")
```

# Reference

https://www.aaai.org/Papers/AAAI/2000/AAAI00-093.pdf
