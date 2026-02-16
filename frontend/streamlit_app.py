import streamlit as st
import requests
import os


# Get API URL from environment variable, fallback to localhost for development
API_URL = os.getenv('API_URL', 'http://localhost:9696')


# TODO [X]: Create function for input form for predictions

def patient_history_form():
    """
    Function to generate form for collecting patient history to make predictions.

    Return:
        - patient_history (dict) if form submitted
        - None if no form submitted
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
        socioeconomic_factors_deprivation_quintile = st.selectbox("Which socioeconomic group does the patient fall into?", ["1", "2", "3", "4", "5"])
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

        return None


# TODO [X]: Create function to make predictions

def make_predicition(patient_history):

    """
    Send patient history to API and get prediction
    
    Args:
        patient_history: Dictionary containing patient information
        
    Returns:
        Dictionary with prediction results or None if error
    """
    try:
        with st.spinner('🔄 Connecting to prediction service...'):
            response = requests.post(
                f'{API_URL}/predict',
                json=patient_history,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
    except requests.exceptions.ConnectionError:
        st.error(f"Cannot connect to API at {API_URL}. Please ensure the API service is running.")
        return None
    except requests.exceptions.Timeout:
        st.error("Request timed out. Please try again.")
        return None
    except requests.exceptions.HTTPError as e:
        st.error(f"API Error: {e.response.status_code} - {e.response.text}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
        return None
    

def display_prediction_results(prediction):
    """
    Display the prediction results in a user-friendly format
    
    Args:
        prediction: Dictionary containing t2dm_probability and t2dm_risk
    """
    st.success("Prediction Complete!")
    
    # Display metrics in columns
    col1, col2 = st.columns(2)
    
    with col1:
        probability_pct = prediction['t2dm_probability'] * 100
        st.metric(
            label="Type 2 Diabetes Probability",
            value=f"{probability_pct:.1f}%"
        )
    
    with col2:
        if prediction['t2dm_risk']:
            st.metric(
                label="Risk Assessment",
                value="HIGH RISK",
                delta="⚠️ Action Required",
                delta_color="inverse"
            )
        else:
            st.metric(
                label="Risk Assessment",
                value="LOW RISK",
                delta="✓ No immediate action",
                delta_color="normal"
            )
    
    st.divider()
    
    # Clinical recommendations
    st.subheader("Clinical Recommendations")
    
    if prediction['t2dm_risk']:
        st.warning("""
        **HIGH RISK PATIENT** - Please consider the following actions:
        
        - Inform primary care physician and Health Visitor
        - Schedule regular glucose monitoring
        - Recommend lifestyle modifications (diet and exercise)
        - Consider early intervention programs
        - Monitor for symptoms of Type 2 Diabetes
        """)
    else:
        st.info("""
        **LOW RISK PATIENT** - Standard follow-up recommended:
        
        - Continue routine postpartum care
        - Annual glucose screening recommended
        - Encourage healthy lifestyle habits
        - Provide educational materials on diabetes prevention
        """)



# TODO: Create function to check api health


def main():
    st.title("GD2T2D Risk Prediction System", text_alignment="center")

    st.write("""A clinical decision support tool that predicts the risk of developing Type 2 Diabetes 
in women with a history of Gestational Diabetes. This application uses 
machine learning to analyze patient history and provide healthcare professionals with 
evidence-based risk assessments to support early intervention and personalized care planning.""")

    
    st.info("""
    **How to use this tool:**
    1. Complete the patient history form below
    2. Click 'Submit' to make a new prediction
    3. Review the risk assessment
    4. Follow clinical recommendations
    """)

    tab_1, tab_2, tab_3 = st.tabs(["Predictions", "Metrics", "About"])

    with tab_1:
        st.header("Make New Predictions", text_alignment="center")

        history = patient_history_form()
        if history:

            with st.container():
                st.header("Results", text_alignment="center")
                if history:
                    risk_prediction = make_predicition(history)
                    display_prediction_results(risk_prediction)
                # TODO: Add plot for shap values for prediction
                # Show the input data in an expander
                with st.expander("📋 View Submitted Patient Data"):
                    st.json(history)
        

            


    with tab_2:
        st.header("Metrics", text_alignment="center")
        with st.container():
            st.write("Metrics on the data that we have to date.")

    with tab_3:
        st.header("About this App", text_alignment="center")

        st.markdown("""
        ### Purpose
        
        This test application was built to help healthcare professionals predict the risk of 
        female patients developing Type II Diabetes (T2DM) after suffering with gestational 
        diabetes mellitus (GDM) during pregnancy.
        
        ### How to Use
        
        1. Navigate to the **Predictions** tab
        2. Complete the patient history form with accurate information
        3. Click the **Submit** button to make a new prediction
        4. Review the prediction results and risk assessment
        5. Follow the clinical recommendations provided
        
        ### Model Information
        
        - **Model Type:** Random Forest Classifier
        - **Input Features:** 26 clinical and demographic features
        - **Output:** T2DM probability and binary risk classification (threshold: 0.5)
        
        ### Important Notes
        
        - This tool is designed to assist clinical decision-making, not replace it
        - Always use clinical judgment when interpreting results
        - Predictions should be combined with other clinical assessments
        - Regular monitoring and follow-up remain essential
        
        ### Privacy & Data
        
        - Patient data is processed in real-time and not stored
        - All predictions are stateless

        """)



if __name__ == "__main__":
    main()
