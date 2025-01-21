from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from data_ml_assignment.models.base_model import BaseModel


class SVCModel(BaseModel):
    def __init__(self, **kwargs):
        super().__init__(
            model=Pipeline(
                [("countv", CountVectorizer()),("svc", SVC(**kwargs))]
                )
            )
