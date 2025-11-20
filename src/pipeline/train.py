#============================#
#---------- Imports ---------#
#============================#

import pandas as pd
import sklearn

from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline

import pickle
from datetime import datetime
from src.logger import logging

#============================#
#----- Data Preparation -----#
#============================#

def load_and_preprocess_data(path: str) -> pd.DataFrame: 
    """Function to load data as dataframe and preprocess for model training.
    Params:
        path (str): path to file. Could be string or url
    Returns:
        df: pd.DataFrame
    """
    logging.info("Loading data...")
    df = pd.read_csv(path)
    df.columns = df.columns.str.lower().str.replace(' ', '_')

    logging.info(f"df shape: {df.shape}")

    return df


#============================#
#------ Model Training ------#
#============================#

def train_model(df:pd.DataFrame) -> sklearn.pipeline.Pipeline:
    """Function to train DictVectoriser and RandomForest model instance and save to pipeline.
    Params:
        df (pd.Dataframe): preprocessed dataframe to be used to train the model
    Returns:
        pipeline: sklearn.pipeline.Pipeline
    """
    logging.info("Beginning training model on data...")

    features = [
        'older_maternal_age', 'high_pre_pregnancy_bmi_or_overweight',
       'family_history_of_diabetes',
       'socioeconomic_factors_deprivation_quintile',
       'presence_of_t2dm_associated_gene_variants', 'ethnicity', 'multiparity',
       'insulin_treatment_during_pregnancy',
       'pregnancy_complications_hypertensive_disorders',
       'pregnancy_complications_preterm_delivery',
       'pregnancy_complications_pph', 'gestational_weight_gain',
       'abnormal_ogtt_results', 'elevated_hba1c_during_pregnancy',
       'large_for_gestational_age',
       'macrosomia_baby_birth_weightdelivered_a_baby_greater_than_3_5kg',
       'instrumental_delivery', 'nicu_admission',
       'obesity_or_unhealthy_postpartum_weight_gain', 'physical_inactivity',
       'unhealthy_diet', 'smoking', 'alcohol_intake',
       'does_not_undergo_postpartum_glucose_screening', 'breastfeeding',
       'history_of_recurrence_of_gdm',
    ]

    y_train = df.t2dm_risk

    train_dict = df[features].to_dict(orient='records')

    pipeline = make_pipeline(
        DictVectorizer(), 
        RandomForestClassifier(
            n_estimators=10, 
            max_depth=5, 
            min_samples_leaf=3,
            random_state=42)
        )
    
    pipeline.fit(train_dict, y_train)

    logging.info(f"Training complete.")

    return pipeline


#============================#
#----- Pipeline Storage -----#
#============================#

def save_model(pipeline: sklearn.pipeline.Pipeline):
    """
    Function to save model pipeline to bin file.
    Params:
        pipeline (sklearn.pipeline.Pipeline): Pipeline object containing DictVectoriser(), and LogisticRegression()
    """
    logging.info(f"Saving Model...")

    output_file_name = f'./src/models/dv_rf_pipeline.bin'

    with open(output_file_name, 'wb') as f_out:
        pickle.dump(pipeline, f_out)

    logging.info(f"Model saved to: ./../models/{output_file_name}")


#============================#
#----- Main Script Logic ----#
#============================#

def main():
    logging.info("Loading data...")
    data_path = "./data/processed/decoded_data.csv"
    df = load_and_preprocess_data(data_path)
    pipeline = train_model(df)
    save_model(pipeline)
    logging.info("Training Complete.")

if __name__ == "__main__":
    main()