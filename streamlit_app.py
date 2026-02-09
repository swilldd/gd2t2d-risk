import streamlit as st

# import requests

# url = 'http://localhost:9696/predict'

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

# response = requests.post(url, json=patient_history)

# t2dm_risk_prediction = response.json()

# print(t2dm_risk_prediction)

# if t2dm_risk_prediction['t2dm_risk']:
#     print('Patient at high risk of T2DM, inform primary care physician and Health Vistor.')
# else:
#     print('Patient at low risk of T2DM, no action required.')

# TODO: Create functions to generate app components



# TODO: Create function for input form for predictions

def patient_history_form():
    """
    Function to generate form for collecting patient history to make predictions.

    Returns st.Form
    """
    with st.form("prediction-input"):
        st.write("Please enter your patient history below:")
        older_maternal_age = st.radio("Did the patient experience a geriatric pregnancy?", ["Yes", "No"], horizontal=True).lower()
        high_pre_pregnancy_bmi_or_overweight = st.slider("Pre-pregnancy BMI")
        family_history_of_diabetes = st.radio("Does the patient have a family history of diabetes?", ["Yes", "No"], horizontal=True).lower()
        socioeconomic_factors_deprivation_quintile = st.selectbox("Which socioeconomic group does the patient fall into?", [1, 2, 3, 4, 5])
        presence_of_t2dm_associated_gene_variants = st.radio("Does the patient have any genes associated with type II diabetes?", ["Yes", "No"], horizontal=True).lower()
        ethnicity = st.selectbox("What is the ethnicity of your patient?", ["White", "Black", "Asian", "Mixed", "Other"])
        multiparity = st.radio("Multiparity?", ["Yes", "No"], horizontal=True).lower()
        insulin_treatment_during_pregnancy = st.radio("Did your patient have to receive an insulin treatment during their pregrnancy?", ["Yes", "No"], horizontal=True).lower()
        pregnancy_complications_hypertensive_disorders = st.radio("Did your patient suffer any hypertensive disorder complications during their pregnancy?", ["Yes", "No"], horizontal=True).lower()
        pregnancy_complications_preterm_delivery = st.radio("pregnancy_complications_preterm_delivery?", ["Yes", "No"], horizontal=True).lower()
        # multiparity = st.radio("Multiparity?", ["Yes", "No"], horizontal=True).lower()
        # multiparity = st.radio("Multiparity?", ["Yes", "No"], horizontal=True).lower()
        # multiparity = st.radio("Multiparity?", ["Yes", "No"], horizontal=True).lower()
        # multiparity = st.radio("Multiparity?", ["Yes", "No"], horizontal=True).lower()
        # multiparity = st.radio("Multiparity?", ["Yes", "No"], horizontal=True).lower()
        # TODO: Add rest of questions required to complete JSON request to be sent to API endpoint
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            # TODO: Add a way to convert responses into JSON request that can be sent to api endpoint.
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

            st.write(patient_history)






def main():
    st.title("GD2T2D Project", text_alignment="center")

    st.write("App summary. Outline what it does and what for")

    tab_1, tab_2, tab_3 = st.tabs(["Predictions", "Metrics", "About"])

    with tab_1:
        st.header("Make New Predictions", text_alignment="center")

        patient_history_form()

        with st.container():
            st.header("Explaining the results", text_alignment="center")
            st.write("This section is for explaining why the model made the prediction that it did.")
            st.write("There should be a graph or visual to appear to help explain")


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
