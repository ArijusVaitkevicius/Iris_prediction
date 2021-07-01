from dataclasses import dataclass
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


def model():
    iris = sns.load_dataset('iris')
    cols = iris.columns.tolist()
    x = iris[cols[:-1]]
    y = iris['species']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    new_model = LogisticRegression().fit(x_train, y_train)

    with open('iris_predictor.pickle', 'wb') as f:
        pickle.dump(new_model, f)


@dataclass
class Flower:
    """Klasė kuri priima gėlės duomenis..."""
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    model = None

    def prediction(self):
        pickled_model = open('iris_predictor.pickle', 'rb')
        loaded_model = pickle.load(pickled_model)

        prediction = loaded_model.predict([[self.sepal_length, self.sepal_width, self.petal_length, self.petal_width]])
        return prediction[0]
