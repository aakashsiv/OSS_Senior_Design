import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

def roipred(result):
    df = pd.read_csv('data.csv')

    df.drop(['category_code', 'state_code', 'average_participants', 'products_number', 'offices', 'acquired_companies', 'mba_degree', 'phd_degree', 'ms_degree', 'other_degree', 'is_acquired', 'is_closed'], axis=1, inplace=True)

    df.dropna(inplace=True)

    X = df.drop(['average_funded'], axis=1)
    y = df['average_funded']
    relevant_features = ['company_id', 'country_code', 'total_rounds', 'ipo', 'age']
    X = X[relevant_features]

    X = pd.get_dummies(X, columns=['company_id', 'country_code'])

    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
    model.fit(X, y)

    joblib.dump(model, 'model.joblib')

    model = joblib.load('model.joblib')

    #hard coded for c:1
    company_id = result
    X_new = pd.DataFrame({'total_rounds': [1], 'ipo': [False], 'age': [1]})
    for cid in X.columns[X.columns.str.startswith('company_id_')]:
        if cid == 'company_id_' + company_id:
            X_new[cid] = 1
        else:
            X_new[cid] = 0
    for ccode in X.columns[X.columns.str.startswith('country_code_')]:
        X_new[ccode] = 0
    X_new['country_code_USA'] = 1  # set the country code to USA

    y_pred = model.predict(X_new)

    return (y_pred[0] * 1000)