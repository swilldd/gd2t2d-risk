"""Pydantic models for FastAPI GDM/T2DM risk prediction service"""

from typing import Literal
from pydantic import BaseModel, Field

class Patient(BaseModel):
    """Define model for Request - Patient"""
    older_maternal_age: Literal["yes", "no"]
    high_pre_pregnancy_bmi_or_overweight: Literal["yes", "no"]
    family_history_of_diabetes: Literal["yes", "no"]
    socioeconomic_factors_deprivation_quintile: Literal["1", "2", "3", "4", "5"]
    presence_of_t2dm_associated_gene_variants: Literal["yes", "no"]
    ethnicity: Literal["Other", "Mixed", "Black", "Asian", "White"]
    multiparity: Literal["yes", "no"]
    insulin_treatment_during_pregnancy: Literal["yes", "no"]
    pregnancy_complications_hypertensive_disorders: Literal["yes", "no"]
    pregnancy_complications_preterm_delivery: Literal["yes", "no"]
    pregnancy_complications_pph: Literal["yes", "no"]
    gestational_weight_gain: Literal["yes", "no"]
    abnormal_ogtt_results: Literal["Normal", "Abnormal"]
    elevated_hba1c_during_pregnancy: Literal["Normal", "Elevated"]
    large_for_gestational_age: Literal["yes", "no"]
    macrosomia_baby_birth_weightdelivered_a_baby_greater_than_3_5kg: Literal["yes", "no"]
    instrumental_delivery: Literal["yes", "no"]
    nicu_admission: Literal["yes", "no"]
    obesity_or_unhealthy_postpartum_weight_gain: Literal["yes", "no"]
    physical_inactivity: Literal["yes", "no"]
    unhealthy_diet: Literal["yes", "no"]
    smoking: Literal["yes", "no"]
    alcohol_intake: Literal["yes", "no"]
    does_not_undergo_postpartum_glucose_screening: Literal["yes", "no"]
    breastfeeding: Literal["yes", "no"]
    history_of_recurrence_of_gdm: Literal["yes", "no"]


class PredictResponse(BaseModel):
    """Define model for Response - T2DM Risk Prediction"""
    t2dm_probability: float
    t2dm_risk: bool