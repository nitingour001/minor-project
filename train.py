import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import pickle
from features import extract_features

def make_xy(df: pd.DataFrame):
    X = [extract_features(u) for u in df['url'].tolist()]
    y = df['label'].astype(int).tolist()
    return X, y

def main():
    df = pd.read_csv('sample_data.csv')
    X, y = make_xy(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    clf = LogisticRegression(max_iter=200, n_jobs=None)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    with open('model.pkl','wb') as f:
        pickle.dump(clf, f)
    print('Saved model to model.pkl')

if __name__ == '__main__':
    main()
