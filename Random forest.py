from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
n_estimator=[int(x) for x in np.linspace(start=10,stop=80,num=10)]
max_features=['auto','sqrt']
max_depth = [2,4]
min_samples_split = [2, 5]
min_samples_leaf = [1,2]
bootstrap = [True, False]
random_grid = {'n_estimator': n_estimator,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
#print(random_grid)
rf = RandomForestClassifier()
rf_grind=GridSearchCV(estimator = rf, param_grid = random_grid,  cv = 3, verbose=2, n_jobs = 4)
rf=rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
#rf.best_params_

y_pred
# view accuracy 
accuracy_score(y_test,y_pred)
print_score(y_pred, rf)
accu=cross_val_score(rf,X_train,y_train)
np.mean(accu)
