import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_model():
    data = pd.read_csv("dataset.csv")

    X = data.drop("risk", axis=1)
    y = data["risk"]

    model = DecisionTreeClassifier()
    model.fit(X, y)

    predictions = model.predict(X)
    acc = accuracy_score(y, predictions)

    return model, acc
