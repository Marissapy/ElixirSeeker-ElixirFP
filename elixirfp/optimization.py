from sklearn.model_selection import KFold, RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold
import numpy as np
from .fingerprints import generate_fingerprints
import xgboost as xgb  
from scipy.stats import randint as sp_randint
from scipy.stats import uniform

def optimize_fingerprint(df, fp_type, n_bits_range):
    best_score = float('inf')
    best_n_bits = 0
    best_params = None
    best_importances = None

    for n_bits in range(n_bits_range[0], n_bits_range[1] + 1, 8):
        fingerprints = [generate_fingerprints(smiles, fp_type, n_bits) for smiles in df['SMILES']]
        X = np.array(fingerprints)
        y = df['Value'].values
        
        model = xgb.XGBRegressor()  # Correct usage of xgboost after import
        param_grid = {
        'classifier__learning_rate': uniform(0.01, 0.19),
        'classifier__max_depth': sp_randint(3, 13),
        'classifier__n_estimators': sp_randint(50, 501),
        'classifier__min_child_weight': sp_randint(1, 6),
        'classifier__gamma': uniform(0, 0.2)
        }
        kf = KFold(n_splits=2, shuffle=True, random_state=42)
        search = RandomizedSearchCV(model, param_grid, cv=kf, n_iter=10, scoring='neg_mean_squared_error', random_state=42)
        search.fit(X, y)

        mean_score = -search.best_score_
        if mean_score < best_score:
            best_score = mean_score
            best_n_bits = n_bits
            best_params = search.best_params_
            best_importances = search.best_estimator_.feature_importances_

    return best_n_bits, best_params, best_score, best_importances
