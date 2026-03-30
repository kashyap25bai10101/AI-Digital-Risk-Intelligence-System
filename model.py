import pandas as pd
from sklearn.tree import DecisionTreeClassifier

def train_model():
    data = pd.read_csv("dataset.csv")

    X = data.drop("risk", axis=1)
    y = data["risk"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    return model
