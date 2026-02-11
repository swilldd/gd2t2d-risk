import streamlit as st

# import requests

# url = 'http://localhost:9696/predict'

# response = requests.post(url, json=patient_history)

# t2dm_risk_prediction = response.json()

# print(t2dm_risk_prediction)

# if t2dm_risk_prediction['t2dm_risk']:
#     print('Patient at high risk of T2DM, inform primary care physician and Health Vistor.')
# else:
#     print('Patient at low risk of T2DM, no action required.')

# TODO: Create functions to generate app components



# TODO [X]: Create function for input form for predictions

def patient_history_form():
    """
    Function to generate form for collecting patient history to make predictions.

    Returns st.form container
    """
    with st.form("prediction-input"):
        st.write("Please enter your patient history below:")
        older_maternal_age = st.radio("Was the patient of advanced maternal age (≥35 years at delivery)?", ["Yes", "No"], horizontal=True).lower()
        prepregnancy_bmi = st.slider("What was the patients pre-pregnancy BMI?")
        if prepregnancy_bmi >= 25:
            high_pre_pregnancy_bmi_or_overweight = "yes"
        else:
            high_pre_pregnancy_bmi_or_overweight = "no"
        family_history_of_diabetes = st.radio("Does the patient have a family history of diabetes?", ["Yes", "No"], horizontal=True).lower()
        socioeconomic_factors_deprivation_quintile = st.selectbox("Which socioeconomic group does the patient fall into?", [1, 2, 3, 4, 5])
        presence_of_t2dm_associated_gene_variants = st.radio("Does the patient have any genes associated with type II diabetes?", ["Yes", "No"], horizontal=True).lower()
        ethnicity = st.selectbox("What is the ethnicity of your patient?", ["White", "Black", "Asian", "Mixed", "Other"])
        multiparity = st.radio("Does your patient have a history of multiparity (≥2 prior deliveries)?", ["Yes", "No"], horizontal=True).lower()
        insulin_treatment_during_pregnancy = st.radio("Did your patient have to receive an insulin treatment during their pregrnancy?", ["Yes", "No"], horizontal=True).lower()
        pregnancy_complications_hypertensive_disorders = st.radio("Did your patient suffer any hypertensive disorder complications during their pregnancy?", ["Yes", "No"], horizontal=True).lower()
        pregnancy_complications_preterm_delivery = st.radio("Did your patient have a preterm delivery?", ["Yes", "No"], horizontal=True).lower()
        pregnancy_complications_pph = st.radio("Did your patient suffer any PPH complications during birth?", ["Yes", "No"], horizontal=True).lower()
        gestational_weight_gain = st.radio("Did the patient have excessive gestational weight gain?", ["Yes", "No"], horizontal=True).lower()
        abnormal_ogtt_results = st.radio("What were the results of the patients ogtt?", ["Normal", "Abnormal"], horizontal=True)
        elevated_hba1c_during_pregnancy = st.radio("Did your patient have elevated hba1c during pregnancy?", ["Normal", "Abnormal"], horizontal=True)
        large_for_gestational_age = st.radio("Was the baby considered large for gestational age?", ["Yes", "No"], horizontal=True).lower()
        macrosomia_baby_birth_weightdelivered_a_baby_greater_than_3_5kg = st.radio("Did the newborn have macrosomia? (weight at birth above 3.5kg)", ["Yes", "No"], horizontal=True).lower()
        instrumental_delivery= st.radio("Were instruments required during birth?", ["Yes", "No"], horizontal=True).lower()
        nicu_admission = st.radio("Was the newborn admitted to the nicu?", ["Yes", "No"], horizontal=True).lower()
        obesity_or_unhealthy_postpartum_weight_gain = st.radio("Did your patient suffer with unhealthy weight gain post partum?", ["Yes", "No"], horizontal=True).lower()
        physical_inactivity = st.radio("Is your patient physically inactive?", ["Yes", "No"], horizontal=True).lower()
        unhealthy_diet = st.radio("Is your patient's diet considered unhealthy?", ["Yes", "No"], horizontal=True).lower()
        smoking = st.radio("Did your patient smoke during or after pregnancy?", ["Yes", "No"], horizontal=True).lower()
        alcohol_intake = st.radio("Did your patient drink alcohol during or after pregnancy?", ["Yes", "No"], horizontal=True).lower()
        does_not_undergo_postpartum_glucose_screening = st.radio("Has the patient failed to complete recommended postpartum glucose screening?", ["Yes", "No"], horizontal=True).lower()
        breastfeeding = st.radio("Does your patient breastfeed?", ["Yes", "No"], horizontal=True).lower()
        history_of_recurrence_of_gdm = st.radio("Does your patient have a history of recurring gestational diabetes?", ["Yes", "No"], horizontal=True).lower()

        # TODO [X]: Add rest of questions required to complete JSON request to be sent to API endpoint 
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            # TODO [X]: Add a way to convert responses into JSON request that can be sent to api endpoint.
            patient_history = {
                'older_maternal_age': older_maternal_age,
                'high_pre_pregnancy_bmi_or_overweight': high_pre_pregnancy_bmi_or_overweight,
                'family_history_of_diabetes': family_history_of_diabetes,
                'socioeconomic_factors_deprivation_quintile': socioeconomic_factors_deprivation_quintile, 
                'presence_of_t2dm_associated_gene_variants': presence_of_t2dm_associated_gene_variants,
                'ethnicity': ethnicity,
                'multiparity': multiparity,
                'insulin_treatment_during_pregnancy': insulin_treatment_during_pregnancy,
                'pregnancy_complications_hypertensive_disorders': pregnancy_complications_hypertensive_disorders,
                'pregnancy_complications_preterm_delivery': pregnancy_complications_preterm_delivery,
                'pregnancy_complications_pph': pregnancy_complications_pph,
                'gestational_weight_gain': gestational_weight_gain,
                'abnormal_ogtt_results': abnormal_ogtt_results,
                'elevated_hba1c_during_pregnancy': elevated_hba1c_during_pregnancy,
                'large_for_gestational_age': large_for_gestational_age,
                'macrosomia_baby_birth_weightdelivered_a_baby_greater_than_3_5kg': macrosomia_baby_birth_weightdelivered_a_baby_greater_than_3_5kg,
                'instrumental_delivery': instrumental_delivery,
                'nicu_admission': nicu_admission,
                'obesity_or_unhealthy_postpartum_weight_gain': obesity_or_unhealthy_postpartum_weight_gain,
                'physical_inactivity': physical_inactivity,
                'unhealthy_diet': unhealthy_diet,
                'smoking': smoking,
                'alcohol_intake': alcohol_intake,
                'does_not_undergo_postpartum_glucose_screening': does_not_undergo_postpartum_glucose_screening,
                'breastfeeding': breastfeeding,
                'history_of_recurrence_of_gdm': history_of_recurrence_of_gdm,
            }

            return patient_history






def main():
    st.title("GD2T2D Project", text_alignment="center")

    st.write("App summary. Outline what it does and what for")

    tab_1, tab_2, tab_3 = st.tabs(["Predictions", "Metrics", "About"])

    with tab_1:
        st.header("Make New Predictions", text_alignment="center")

        history = patient_history_form()

        with st.container():
            st.header("Explaining the results", text_alignment="center")
            st.write("This section is for explaining why the model made the prediction that it did.")
            st.write("There should be a graph or visual to appear to help explain")
            if history:
                st.write(history)


    with tab_2:
        st.header("Metrics", text_alignment="center")
        with st.container():
            st.write("Metrics on the data that we have to date.")

    with tab_3:
        st.header("About this App", text_alignment="center")
        st.markdown("""
        
        ### Why we built this app?

        This application was built to allow healthcare professionals to predict the risk of female patients developing type II Diabetes after suffering with gestational diabetes during pregnancy.
        
        ### How to use the app?

        Enter the required information about the patient and click submit to make a new risk prediction.

        ### What model powers these predictions?
        
        All predicitions are made by a random forest model. More to follow
        
        """)
            
    


if __name__ == "__main__":
    main()
