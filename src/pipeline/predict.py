#=============================#
#---------- Imports ----------#
#=============================#

import pickle
from src.logger import logging


#=============================#
#------- Load the model ------#
#=============================#

input_pipeline_path = './src/models/dv_rf_pipeline.bin'

logging.info(f"Loading model {input_pipeline_path}")

with open(input_pipeline_path, 'rb') as f_in:
    pipeline = pickle.load(f_in)


#=============================#
#--- Predict Diabetes Risk ---#
#=============================#

patient_example = {
    'older_maternal_age': 'yes',
    'high_pre_pregnancy_bmi_or_overweight': 'yes',
    'family_history_of_diabetes': 'yes',
    'socioeconomic_factors_deprivation_quintile': '2', 
    'presence_of_t2dm_associated_gene_variants': 'yes',
    'ethnicity': 'Asian',
    'multiparity': 'yes',
    'insulin_treatment_during_pregnancy': 'yes',
    'pregnancy_complications_hypertensive_disorders': 'no',
    'pregnancy_complications_preterm_delivery': 'no',
    'pregnancy_complications_pph': 'no',
    'gestational_weight_gain': 'yes',
    'abnormal_ogtt_results': 'Abnormal',
    'elevated_hba1c_during_pregnancy': 'Normal',
    'large_for_gestational_age': 'no',
    'macrosomia_baby_birth_weightdelivered_a_baby_greater_than_3_5kg': 'yes',
    'instrumental_delivery': 'no',
    'nicu_admission': 'no',
    'obesity_or_unhealthy_postpartum_weight_gain': 'yes',
    'physical_inactivity': 'yes',
    'unhealthy_diet': 'yes',
    'smoking': 'yes',
    'alcohol_intake': 'no',
    'does_not_undergo_postpartum_glucose_screening': 'no',
    'breastfeeding': 'no',
    'history_of_recurrence_of_gdm': 'yes',
}


logging.info(f"Patient factors: {patient_example}")

def predict_single(patient):
    result = pipeline.predict_proba(patient)[0, 1]
    return float(result)

y_pred = predict_single(patient_example)

print(f'Patient T2DM Probability: {y_pred:.3f}')

if y_pred >= 0.5:
    print('Patient at high risk of T2DM, inform primary care physician and Health Vistor.')
else:
    print('Patient at low risk of T2DM, no action required.')

logging.info(f"T2DM prediction probability: {y_pred}")