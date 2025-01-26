import xgboost as xgb
from sklearn.feature_extraction.text import CountVectorizer
from data_ml_assignment.models.base_model import BaseModel


class XGBCModel(BaseModel):
    def __init__(self, **kwargs):
        self.vectorizer = CountVectorizer()
        self.classifier = xgb.XGBClassifier(**kwargs)
        super().__init__(None)

    def fit(self, x_train, y_train):
        x_train_vec = self.vectorizer.fit_transform(x_train)
        self.classifier.fit(x_train_vec, y_train)
        return self

    def predict(self, x_test):
        x_test_vec = self.vectorizer.transform(x_test)
        return self.classifier.predict(x_test_vec)

    def save(self, path):
        import joblib
        model_data = {
            'vectorizer': self.vectorizer,
            'classifier': self.classifier
        }
        joblib.dump(model_data, path)

    def load(self, path):
        import joblib
        model_data = joblib.load(path)
        self.vectorizer = model_data['vectorizer']
        self.classifier = model_data['classifier']
