from fastapi import FastAPI

import pandas as pd

from tqdm import tqdm
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split

from xgboost import XGBClassifier


def extract_domain(url):
    try:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        if domain.startswith('www.'):
            domain = domain[4:]
        return domain
    except:
        pass


def parse_url_features(urls):
    results = []
    for url in tqdm(urls):
        parsed_url = urlparse(url)
        features = {}

        features['length'] = len(url)
        features['num_subdomains'] = url.count('.')
        features['num_dots'] = url.count('.')
        features['is_https'] = 1 if parsed_url.scheme == 'https' else 0
        features['path_length'] = len(parsed_url.path)
        features['special_chars'] = 1 if any(char in url for char in ['#', '%', '&']) else 0
        results.append(features)

    return pd.DataFrame(results)


def parse_url_features_one(url: str):
    parsed_url = urlparse(url)
    features = {}

    features['length'] = len(url)
    features['num_subdomains'] = url.count('.')
    features['num_dots'] = url.count('.')
    features['is_https'] = 1 if parsed_url.scheme == 'https' else 0
    features['path_length'] = len(parsed_url.path)
    features['special_chars'] = 1 if any(char in url for char in ['#', '%', '&']) else 0
    results = [features]

    return pd.DataFrame(results)


def predict():
    train = pd.read_csv("./train.csv")
    train['domain'] = train['url'].apply(extract_domain)

    X = train["url"]
    y = train["result"]

    features_dataframe = parse_url_features(X.to_list())

    X_train, X_test, y_train, y_test = train_test_split(
        features_dataframe.to_numpy(),
        y,
        random_state=47,
        test_size=0.1,
        shuffle=True
    )

    model = XGBClassifier(learning_rate=0.2, max_depth=7, objective='binary:logistic', n_estimators=100)
    model.fit(X_train, y_train)

    model.predict(X_test)
    return model


model = predict()
app = FastAPI()


@app.post("/predict")
async def read_item(url: str):
    df = parse_url_features_one(url)
    result = model.predict(df.values)
    print(url)
    print(result[0] == 1)
    if result[0] == 1:
        return True
    return False
