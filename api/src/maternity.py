"""
This file represents the front end of our application that would be used by a midwife to input pateint history, and receive predictions of t2dm risk.
    We will use this to test our endpoint.
"""

import requests

url = 'http://localhost:9696/predict'

patient_history = {
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

response = requests.post(url, json=patient_history)

t2dm_risk_prediction = response.json()

print(t2dm_risk_prediction)

if t2dm_risk_prediction['t2dm_risk']:
    print('Patient at high risk of T2DM, inform primary care physician and Health Vistor.')
else:
    print('Patient at low risk of T2DM, no action required.')