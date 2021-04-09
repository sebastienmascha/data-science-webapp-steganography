from typing import List
import json

import streamlit as st
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


API_URL = "https://hr-api.smascha.ai"
# API_URL = "http://localhost:8080"


def create_custom_selectbox(title: str, options: List, index: int = 0):
    custom_selectbox = st.selectbox(
        title,
        options,
        index,
    )
    st.markdown('You selected:' + custom_selectbox)
    return custom_selectbox


def handle_map_dictionary(value, dictionary):
    try: value = dictionary[value]
    except Exception: 
        pass
    return value


def app():
    st.title("HR Analytics")
    st.info("Enter your profile and receive feedback on your carreer! 🚀 We don't store your data 🔐")
    st.markdown("## What is your profil?")

    st.markdown("#### User Details")
    # Gender
    selected_gender = st.radio("Gender:", options=['Woman', 'Man', 'Other'])
    selected_gender = handle_map_dictionary(selected_gender, {'Woman':'Female', 'Man':'Male'})
    # city_development_index
    selected_city_development_index = str(st.slider("What is your city development index?", min_value=0., max_value=1., value=0.62, step=0.01))
    # city
    selected_city = create_custom_selectbox(title="What is your city Postal code?", options=['1',  '2',  '7',  '8',  '9',  '10',  '11',  '12',  '13',  '14',  '16',  '18',  '19',  '20',  '21',  '23',  '24',  '25',  '26',  '27',  '28',  '30',  '31',  '33',  '36',  '37',  '39',  '40',  '41',  '42',  '43',  '44',  '45',  '46',  '48',  '50',  '53',  '54',  '55',  '57',  '59',  '61',  '62',  '64',  '65',  '67',  '69',  '70',  '71',  '72',  '73',  '74',  '75',  '76',  '77',  '78',  '79',  '80',  '81',  '82',  '83',  '84',  '89',  '90',  '91',  '93',  '94',  '97',  '98',  '99',  '100',  '101',  '102',  '103',  '104',  '105',  '106',  '107',  '109',  '111',  '114',  '115',  '116',  '117',  '118',  '120',  '121',  '123',  '126',  '127',  '128',  '129',  '131',  '133',  '134',  '136',  '138',  '139',  '140',  '141',  '142',  '143',  '144',  '145',  '146',  '149',  '150',  '152',  '155',  '157',  '158',  '159',  '160',  '162',  '165',  '166',  '167',  '171',  '173',  '175',  '176',  '179',  '180'], index=16)

    st.markdown("#### Education")
    # Enrolled University
    selected_enrolled_university = create_custom_selectbox(title="Are you currently enroled in a university?", options=['Full-Time', 'Part-Time', 'No Enrollmennt'], index=1)
    selected_enrolled_university = handle_map_dictionary(selected_enrolled_university, {'Full-Time':'Full time course', 'Part-Time':'Part time course', 'No Enrollmennt':'no_enrollment'})
    # Education Level
    selected_education_level = create_custom_selectbox(title="What is your education level?", options=['Primary School', 'High School', 'Masters', 'Graduate', 'Phd'], index=3)
    # Major Discipline
    selected_major_discipline = create_custom_selectbox(title="What is your major discipline?", options=['STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major', 'Other'])

    st.markdown("#### Experience")
    # Relevent Experience
    selected_relevent_experience = str(st.checkbox("Do you have a relevant experience?", value=True))
    selected_relevent_experience = handle_map_dictionary(selected_relevent_experience, {'True':'Has relevent experience', 'False':'No relevent experience'})
    # Experience
    selected_experience = str(st.slider("How many years of experience do you have?", min_value=0, max_value=28, value=14, step=1))
    # Type of current employer
    selected_company_type = create_custom_selectbox(title="What kind of company are you working for?", options=['NGO', 'Public Sector', 'Early Stage Startup', 'Funded Startup', 'Pvt Ltd', 'Other'], index=4)
    # company_size
    selected_company_size = create_custom_selectbox(title="How many employees are you in your current company?", options=['1-9', '10-49', '50-99', '100-500', '500-999', '1000-4999', '5000-9999', '10000-20000'], index=4)
    # last_new_job
    selected_last_new_job = str(st.slider("Difference in years between previous job and current job:", min_value=0, max_value=9, value=1, step=1))
    # training_hours
    selected_training_hours = str(st.slider("How many training hours are you taking?", min_value=0, max_value=200, value=150, step=1))


    st.markdown("## Are you looking for a job change?")
    selected_model = st.radio("Select the AI model you wish to use:", options=['Random Forest (accuracy: 96%)', 'Decision Tree (accuracy: 87%)', 'Neural Networks (accuracy: 89%)'])
    selected_model = handle_map_dictionary(selected_model, {'Random Forest (accuracy: 96%)':'rf_pipe', 'Decision Tree (accuracy: 87%)':'dt_pipe', 'K-Nearest-Neighbour (accuracy: 85%)':'knn_gscv', 'Neural Networks (accuracy: 89%)':'mlp_final', 'Support Vector Machine (accuracy: 82%)':'svclassifier'})
    st.markdown("""
        Soon available: 
        - K-Nearest-Neighbour (accuracy: 85%)
        - Support Vector Machine (accuracy: 82%)
        """)

    if st.button("Start the Prediction"):
        print("\n----- Handle Prediction -----")
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        user_input_json = {
            "gender": selected_gender,
            "relevent_experience": selected_relevent_experience,
            "enrolled_university": selected_enrolled_university,
            "education_level": selected_education_level,
            "major_discipline": selected_major_discipline,
            "experience": selected_experience,
            "company_size": selected_company_size,
            "company_type": selected_company_type,
            "last_new_job": selected_last_new_job,
            "training_hours": selected_training_hours,
            "city_development_index": selected_city_development_index,
            "city": selected_city,
            }
        response = requests.post(API_URL + '/' + selected_model, headers=headers, json=user_input_json)
        print(response.text)
        response_json = json.loads(response.text)
        if response_json['prediction_class'] == 1:
            st.success("Looking for a job change! 🤝🚀")
        else:
            st.error('Not looking for job change! ⚠️')
        if abs(response_json['prediction_proba_1'] - response_json['prediction_proba_0']) > 0.3:
            st.info("🎉 The probability that you're looking for a job is: " + str(response_json['prediction_proba_1']))
        else:
            st.warning("⚠️ The probability that you're looking for a job is: " + str(response_json['prediction_proba_1']))
        st.info("Our random forest model took {:.2f} second to process! ⚡".format(response_json['time']))


        st.markdown("## Should you continue your job or take more training hours?")

        # Education level
        fig, axes = plt.subplots()
        list_proba = []
        LIST_EDUCATION_LEVEL = ['Primary School', 'High School', 'Masters', 'Graduate', 'Phd']
        with st.spinner('Wait for it... Processing in progress! ⚙️🕐'):
            for education_level in LIST_EDUCATION_LEVEL:
                new_education_level = education_level
                user_input_json = {
                    "gender": selected_gender,
                    "relevent_experience": selected_relevent_experience,
                    "enrolled_university": selected_enrolled_university,
                    "education_level": new_education_level,
                    "major_discipline": selected_major_discipline,
                    "experience": selected_experience,
                    "company_size": selected_company_size,
                    "company_type": selected_company_type,
                    "last_new_job": selected_last_new_job,
                    "training_hours": selected_training_hours,
                    "city_development_index": selected_city_development_index,
                    "city": selected_city,
                    }
                response = requests.post(API_URL + '/' + selected_model, headers=headers, json=user_input_json)
                response_json = json.loads(response.text)
                list_proba.append(response_json['prediction_proba_1'])
            d = {'Education Level': LIST_EDUCATION_LEVEL, 'Probaility: looking for a job': list_proba}
            df = pd.DataFrame(data=d)
            sns.lineplot(data=df, x="Education Level", y="Probaility: looking for a job")
            st.pyplot(fig)
        st.info("This analysis is only to compare your self to other candidates. Everyone is unique.")

        # last_new_job and experience
        fig, axes = plt.subplots()
        list_proba = []
        YEAR_IN_COMPANY_MAX = 30
        YEAR_IN_COMPANY_STEP = 1
        with st.spinner('Wait for it... Processing in progress! ⚙️🕐'):
            for i in range(0, YEAR_IN_COMPANY_MAX, YEAR_IN_COMPANY_STEP):
                year_in_company = i
                new_last_new_job = selected_last_new_job + str(year_in_company)
                new_experience = selected_experience + str(year_in_company)
                user_input_json = {
                    "gender": selected_gender,
                    "relevent_experience": selected_relevent_experience,
                    "enrolled_university": selected_enrolled_university,
                    "education_level": selected_education_level,
                    "major_discipline": selected_major_discipline,
                    "experience": new_experience,
                    "company_size": selected_company_size,
                    "company_type": selected_company_type,
                    "last_new_job": new_last_new_job,
                    "training_hours": selected_training_hours,
                    "city_development_index": selected_city_development_index,
                    "city": selected_city,
                    }
                response = requests.post(API_URL + '/' + selected_model, headers=headers, json=user_input_json)
                response_json = json.loads(response.text)
                list_proba.append(response_json['prediction_proba_1'])
            d = {'Year to stay in current company': [*range(0, YEAR_IN_COMPANY_MAX, YEAR_IN_COMPANY_STEP)], 'Probaility: looking for a job': list_proba}
            df = pd.DataFrame(data=d)
            sns.lineplot(data=df, x="Year to stay in current company", y="Probaility: looking for a job")
            st.pyplot(fig)
        max_proba_years = max(list_proba)
        list_best_years_no = [i for i, j in enumerate(list_proba) if j == max_proba_years]
        if len(list_best_years_no) < 6:
            st.markdown("You should stay **" + str(list_best_years_no) + "** year(s) in your current company.")
        else: 
            st.info("Look like your current company will not change your profile. Feel free to stay as long as you want and learn as much as you can.")

        # Training Hours
        fig, axes = plt.subplots()
        list_proba_for_training_hours = []
        TRAINING_HOURS_MAX = 200
        TRAINING_HOURS_STEP = 10
        with st.spinner('Wait for it... Processing in progress! ⚙️🕐'):
            for i in range(0, TRAINING_HOURS_MAX, TRAINING_HOURS_STEP):
                new_training_hours = i
                user_input_json = {
                    "gender": selected_gender,
                    "relevent_experience": selected_relevent_experience,
                    "enrolled_university": selected_enrolled_university,
                    "education_level": selected_education_level,
                    "major_discipline": selected_major_discipline,
                    "experience": selected_experience,
                    "company_size": selected_company_size,
                    "company_type": selected_company_type,
                    "last_new_job": selected_last_new_job,
                    "training_hours": new_training_hours,
                    "city_development_index": selected_city_development_index,
                    "city": selected_city,
                    }
                response = requests.post(API_URL + '/' + selected_model, headers=headers, json=user_input_json)
                response_json = json.loads(response.text)
                list_proba_for_training_hours.append(response_json['prediction_proba_1'])
            d_training_hours = {'No of training hours': [*range(0, TRAINING_HOURS_MAX, TRAINING_HOURS_STEP)], 'Probaility: looking for a job': list_proba_for_training_hours}
            df_training_hours = pd.DataFrame(data=d_training_hours)
            sns.lineplot(data=df_training_hours, x="No of training hours", y="Probaility: looking for a job")
            st.pyplot(fig)
        max_proba_for_training_hours = max(list_proba_for_training_hours)
        list_best_training_hours_no = [i for i, j in enumerate(list_proba_for_training_hours) if j == max_proba_for_training_hours]
        st.info("You should take **" + str(list_best_training_hours_no) + "** training hours.")
        if list_best_training_hours_no[0] < 50:
            st.success("Sounds like you already have a great profil. You don't need much more training hours.")
        else:
            st.warning("You have a very interresting profile but you lack of knowledge in Data Science field. \nYou should take more training hours.")
 