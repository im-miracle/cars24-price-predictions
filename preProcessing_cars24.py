import numpy as np
import pandas as pd
import os

def preprocessing(csvPath=None):
    if not csvPath:
        raise Exception("Data path missing")

    if not os.path.exists(csvPath):
        raise Exception("CSV File doesn't exist")

    print("-*-"*10)
    print("Loading the Data")
    print("-*-"*10)    
    df = pd.read_csv(csvPath)
    df["make"] = df["full_name"].apply(lambda x: x.split(" ")[0])
    df["model"] = df["full_name"].apply(lambda x: " ".join(x.split(" ")[1:]))
    df.drop(columns=["full_name"], inplace=True)
    df.columns = ['selling_price', 'make', 'model', 'year', 'seller_type', 'km_driven', 'fuel_type', 'transmission_type', 'mileage', 'engine', 'max_power', 'seats']

    print("-*-"*10)
    print("selling_price: Outlier Detection and Handling")
    print("-*-"*10)
    quantileThresholdValue = 0.99
    dfCutoffThreshold = df["selling_price"].quantile(quantileThresholdValue)
    percentDataRemoved = df.loc[df["selling_price"] > dfCutoffThreshold, "selling_price"].count()/df.shape[0]
    print("%0.2f percentile value: %f" % (quantileThresholdValue, dfCutoffThreshold))
    print("Outlier Data percent to trim: %f" % percentDataRemoved)
    df = df.loc[df["selling_price"] <= dfCutoffThreshold]


