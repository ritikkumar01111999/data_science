import pickle
saved_model = pickle.dumps(classifier.fit(x_train_multilabel,multilabel_y_train ))
from_pickle = pickle.loads(saved_model)
from_pickle.predict(x_test_multilabel)
from sklearn.externals import joblib
joblib.dump(classifier.fit(x_train_multilabel,multilabel_y_train ), 'filename.pkl')
knn_from_joblib = joblib.load('filename.pkl')
knn_from_joblib.predict(x_test_multilabel)
testing = "need a 1 year experience person for handling the full stack developer job salary is 294$ per day"
