import os
import sys
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.pipeline.exception import CustomException
from src.pipeline.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    try:
        report = {}

        for model_name, model in models.items():
            logging.info(f"Training {model_name}...")

            # Get the parameters for this model
            params = param.get(model_name, {})

            if params:  # if parameters exist, do grid search
                gs = GridSearchCV(model, params, cv=3, n_jobs=-1, verbose=0)
                gs.fit(X_train, y_train)
                best_model = gs.best_estimator_
            else:  # if no params, fit directly
                model.fit(X_train, y_train)
                best_model = model

            # Evaluate
            y_train_pred = best_model.predict(X_train)
            y_test_pred = best_model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

            logging.info(
                f"{model_name}: Train R2={train_model_score:.3f}, Test R2={test_model_score:.3f}"
            )

        return report

    except Exception as e:
        raise CustomException(e, sys)
