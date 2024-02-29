import pickle  # Module used for serializing and deserializing Python objects
import streamlit as st  # Streamlit library for creating interactive web applications
from streamlit_option_menu import option_menu  # Custom option menu for navigation

# Setting up the page configuration for the Streamlit app
st.set_page_config(
    page_title="Multiple Disease Prediction",  # Title of the web application
    page_icon="🏥",  # Icon for the web application
    layout="wide"  # Setting the layout of the page
)

# Loading the saved machine learning models using pickle
diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))  # Loading the diabetes prediction model
parkinson_model = pickle.load(open('models/parkinson_model.sav', 'rb'))  # Loading the Parkinson's prediction model

# Sidebar for navigation using a custom option menu
selected = option_menu('Multiple Disease Prediction Dashboard',
                       ['Home', 'Diabetes Prediction', "Parkinson's Prediction"],  # List of menu options
                       icons=['house-fill', 'capsule-pill', 'heart-pulse-fill', 'people-fill'],  # Icons for each option
                       menu_icon='clipboard2-pulse',  # Icon for the main menu
                       orientation='horizontal')  # Orientation of the menu


# Home Page
if selected == 'Home':
    st.title('Multiple Disease Prediction using Machine Learning')  # Title of the Home page
    st.image('assets/main_banner.gif')  # Displaying an image on the Home page

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('💊Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input(
            'Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        # Determining the diagnosis based on the prediction result
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)  # Displaying the diagnosis result


# Parkinson's Prediction Page
if selected == "Parkinson's Prediction":

    # page title
    st.title("👨‍🦳Parkinson's Disease Prediction using ML")

# Input fields for features related to Parkinson's disease prediction...

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinson_diagnosis = ''

    # Button to trigger the Parkinson's disease prediction
    if st.button("Parkinson's Test Result"):
        parkinson_prediction = parkinson_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR,
              HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        # Determining the diagnosis based on the prediction result
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = "The person has Parkinson's disease"
        else:
            parkinson_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinson_diagnosis)  # Displaying the diagnosis result
