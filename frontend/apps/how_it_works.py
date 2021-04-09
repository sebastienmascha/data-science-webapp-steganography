import os

import streamlit as st
import pandas as pd
import numpy as np

from .toc import Toc


PATH_RES_FOLDER = os.getcwd() + "/res/"


def toc_content(toc: Toc):
    st.image(PATH_RES_FOLDER + "img/HR-Analytics.jpg")
    toc.placeholder()

    # ----- HR Analytics: Job Change of Data Scientists -----
    toc.title("Abstract")
    st.markdown("A UC Berkeley research by [Sébastien Mascha](https://www.linkedin.com/in/sebastienmascha) and [Thomas Lecouedic](https://www.linkedin.com/in/thomas-lecouedic) advised by Professor Seema Saharan.")
    st.markdown("""
        A company which is active in Big Data and Data Science wants to hire data scientists among people who successfully pass some courses which conduct by the company. Many people signup for their training. Company wants to know which of these candidates are really wants to work for the company after training or looking for a new employment because it helps to reduce the cost and time as well as the quality of training or planning the courses and categorization of candidates. Information related to demographics, education, experience are in hands from candidates signup and enrollment.

        This dataset designed to understand the factors that lead a person to leave current job for HR researches too. By model(s) that uses the current credentials,demographics,experience data you will predict the probability of a candidate to look for a new job or will work for the company, as well as interpreting affected factors on employee decision.

        The whole data divided to train and test . Target isn't included in test but the test target values data file is in hands for related tasks. A sample submission correspond to enrollee_id of test set provided too with columns : enrollee _id , target

        **Dataset:**

        Link to the dataset: https://www.kaggle.com/arashnic/hr-analytics-job-change-of-data-scientists

        Data Source: Kaggle (https://www.kaggle.com)

        **Features:**

        - enrollee_id : Unique ID for candidate

        - city: City code

        - city_ development _index : Developement index of the city (scaled)

        - gender: Gender of candidate

        - relevent_experience: Relevant experience of candidate

        - enrolled_university: Type of University course enrolled if any

        - education_level: Education level of candidate

        - major_discipline :Education major discipline of candidate

        - experience: Candidate total experience in years

        - company_size: No of employees in current employer's company

        - company_type : Type of current employer

        - lastnewjob: Difference in years between previous job and current job

        - training_hours: training hours completed

        - target: 0 – Not looking for job change, 1 – Looking for a job change

        **Note:**

        - The dataset is imbalanced so it might affect our result if we dont handle it;
        - Most features are categorical (Nominal, Ordinal, Binary), some with high cardinality so encoding methods and techniques will help to boost models performance;
        - Missing imputation strategy might affect the results so it can be a part of your pipeline as well.
    """)
    toc.header("Research Questions")
    st.markdown("""
        **Target Prediction:**

        1. Does the number of training hours have an impact on the final decision?
        1. Are people with many years of experience and working in a large company more likely to stay in the company?
        1. Are young graduates more likely to stay in the company?
        1. Are people working in the field of data science but without experience willing to look for a new job?
        1. Are people in vocational retraining more willing than others to look for a new job?
        1. Are employees already working in the field of data Science more likely to refuse the job?
        1. Are people working in an Early Stage Startup more likely to stay in the company?
        1. Are undergraduate students not specialised in data science more likely to refuse the job?
        1. Are students enrolled in a part-time data science program more likely to decline the offer?
        1. To what extent is gender correlated with the target?
        1. Are people working in private companies more likely to stay in the company than people working in the public sector?
        1. Are people working in highly developed cities with many hours of training more likely to leave their jobs?
        1. Are small business employees ready to look for a new job, considering people who are not enrolled in any university?


        **Correlation between features:**
        
        14. Do people working in large companies have a high city development index?
        1. Do people who left their previous job more than two years ago generally take more hours of training? 
        1. Are large companies mostly located in developed cities?
        1. Do people with a Master's or PhD degree have fewer hours of training than others? 
        1. Are people coming from an underprivileged city and with a high education level looking for a new job?
        1. To what extent people without relevant experience will need more training hours?
        1. Do people who have taken a major discipline other than STEM take more hours of training?
    """)


    # ----- Data Science Pipeline -----
    toc.title("Data Science Pipeline")
    toc.header("Workspace: Dataiku & Colab")
    st.markdown("""
        To implement our Data Science life-cycle, we decided to use [Dataiku](https://www.dataiku.com) and [Google Colab](https://colab.research.google.com/).
        We installed Dataiku on a Ubuntu 18.04 machine using Docker and Traefik: [https://data.smascha.ai](https://data.smascha.ai)
        We used Google Colab thanks to Google Cloud Platform available at: [https://colab.research.google.com/](https://colab.research.google.com/)
        ### What is Dataiku?
        Dataiku is a cross-platform desktop application that includes a broad range of tools, such as notebooks (similar to Jupyter Notebook), workflow management (similar to Apache Airflow), and automated machine learning.
        We used Dataiku to quickly prepare our data and analyse categorical and numerical variables. Moreover, we wanted to quickly evaluate variety of algorithms before implementing them from scratch.
        With Dataiku you can train multiple models at the same time, while running Grid search to optimize parameters in the background.
        """)
    st.image(PATH_RES_FOLDER + "img/Dataiku-quick-modeling.png", use_column_width='auto')
    st.image(PATH_RES_FOLDER + "img/Dataiku-models-results.png")
    st.markdown("""
        Finally, we obtain great interpretation and visualization: feature importance, confusion matrix, ROC curve, density/decision/lift charts, detailed metrics.
        """)
    st.image(PATH_RES_FOLDER + "img/Dataiku-model-interpretation.png")
    st.markdown("""
        ### What is Google Colab?
        Colaboratory, or “Colab” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning and data analysis.
        Easy sharing, just like other Google services, you can share the results of your work with others just like you use Google Docs.
        Moreover, you have access to CPU, GPU and TPU (with limited usage of course, else you can pay for better performance).
        """)
    st.image(PATH_RES_FOLDER + "img/GColab-overview.png")

    toc.header("Algorithms & Results")
    toc.subheader("Note")
    st.markdown("""
    You can find the complete study on the notebook, [here](https://github.com/sebastienmascha/data-science-viz-streamlit-hr-analytics/blob/main/Python3_6_Notebook.ipynb). In particular, you will find more details on the methods used to develop our algorithms and optimize the hyperparameters. Finally, you will find the graphical analysis of the results as well as the interpretations.
    """)
    toc.subheader("Classification KNN")
    st.markdown("""
        **What is k-Nearest-Neighbors?**

        KNN is a non-parametric, lazy learning classification algorithm. 
        It is a simple algorithm that stores all available cases and classifies new cases by a majority vote of its k neighbors. The case being assigned to the class is most common amongst its K nearest neighbors measured by a distance function.

        KNN has three basic steps.

        * Calculate the distance.
        * Find the k nearest neighbours.
        * Vote for classes
        """)
    

    st.image("data:image/png;base64,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", width=400)
    st.markdown("""
        We believe k-Nearest-Neighbors is a great choice of algorithm for our dataset as we have a binary problem with a large set of labeled data.

        Indeed, our data points are separated into several classes and we cannot make any assumptions about our data.

        Furthermore, even if k-NN requires a lot of memory and RAM, our dataset is not too large (10000 values after preprocessing). Therefore, prediction stage will be fast enough.

        **Accuracy obtained**

        86%
        """)



    toc.subheader("Logistic Regression")
    st.markdown("""
        **What is Logistic Regression?**

        It’s a classification algorithm, that is used where the response variable is categorical. The idea of Logistic Regression is to find a relationship between features and probability of particular outcome.
        In our case we are dealing with a Binomial Logistic Regression because the response variable has two values 0 and 1 : "Looking for a new job" and "Not looking for a new job".

        You can observe below the difference between Linear Regression and Logistic Regression.
        """)
    st.image("data:image/png;base64,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", width=500)
    st.image("https://miro.medium.com/max/800/1*UgYbimgPXf6XXxMy2yqRLw.png")

    st.markdown("""
    **Accuracy obtained**
    73%
    """)


    toc.subheader("Naive Bayes")
    st.markdown("""

    **What is Naive Bayes' algorithm?**

    Naive Bayes algorithms are a set of supervised machine learning algorithms based on the Bayes probability theorem. Naive Bayes algorithms assume that there’s no correlation between features in a dataset used to train the model.
    
    **Naive**
    
    The word naive implies that every pair of features in the dataset is independent of each other. All naive Bayes classifiers work on the assumption that the value of a particular feature is independent from the value of any other feature for a given the class.
    
    **Bayes probability theorem**
    
    The Bayes theorem describes the probability of a feature, based on prior knowledge of situations related to that feature.
    """)
    st.image("https://miro.medium.com/max/6190/1*39U1Ln3tSdFqsfQy6ndxOA.png")
    st.markdown("""
    **Acuracy obtained**
    84%
    """)

    toc.subheader("Neural Networks")
    st.markdown("""
    We have used the MLP function from scikit learn to implement our neural network.
    
    **What is MLP?**
   
    For this algorithm, we are going to use the MLPClassifier model from sklearn.neural_network.
    
    MLP stands for Multi-layer Perceptron
    
    Multi-layer Perceptron is a supervised learning algorithm that learns a function by training on a dataset. Given a set of features and a target, it can learn a non-linear function approximator for either classification or regression. Here we will use classification because our problem suggests it to use it. It is different from logistic regression, in that between the input and the output layer, there can be one or more non-linear layers, called hidden layers. It will be a hyperparameter that we will adjust later.)
    """)
    st.image("https://miro.medium.com/max/3446/1*-IPQlOd46dlsutIbUq1Zcw.png")
    st.markdown("""
    **Accuarcy obtained**
    89%
    """)

    toc.subheader("SVM")
    st.markdown("""
    
    **What is SVM?**

    SVM stands for Support Vector Machine.
    
    In SVM, the line that is used to separate the classes is referred to as hyperplane. The data points on either side of the hyperplane that are closest to the hyperplane are called Support Vectors which is used to plot the boundary line.
    
    In SVM Classification, the data can be either linear or non-linear. There are different kernels that can be set in an SVM Classifier. For a linear dataset, we can set the kernel as 'linear'. On the other hand, for a non-linear dataset, there are two kernels, namely 'rbf' and 'polynomial'. In this, the data is mapped to a higher dimension which makes it easier to draw the hyperplane. Afterwards, it is brought down to the lower dimension. In this section we are going to use the SVC model from scikit learn and try diffenrent kernels to see which one is the best for our data)
    """)
    st.image("https://chrisalbon.com/machine_learning/support_vector_machines/svc_parameters_using_rbf_kernel/svc_parameters_using_rbf_kernel_17_0.png")
    st.markdown("""
    **Accuracy obtained**
    82%
    """)


    toc.subheader("K-Means")
    st.markdown("""

    **What is K-Means?**

    K-Means is a cluster analysis: cluster analysis or clustering is the task of grouping a set of objects in such a way that objects in the same group (called a cluster) are more similar to each other than to those in other groups (clusters). Clustering is unsupervised algorithm which means there is no label data points.

    K-means clustering aims to partition data into k clusters in a way that data points in the same cluster are similar and data points in the different clusters are farther apart.
    Similarity of two points is determined by the distance between them.
    There are many methods to measure the distance. Euclidean distance is one of most commonly used distance measurements.
    """)
    st.image("https://static.javatpoint.com/tutorial/machine-learning/images/k-means-clustering-algorithm-in-machine-learning.png")

    toc.subheader("Decision tree & Random forest")
    st.markdown("""

    **What are Decision Tree and Random forest?**

    Decision trees and random forests are supervised learning algorithms used for both classification and regression problems. In our case we are dealing with a binary classification problem. These two algorithms are best explained together because random forests are a bunch of decision trees combined.

    A decision tree is a supervised machine learning algorithm that can be used for both classification and regression problems. A decision tree is simply a series of sequential decisions made to reach a specific result.
    """)
    st.image("https://cdn.analyticsvidhya.com/wp-content/uploads/2020/05/rfc_vs_dt11.png")

    st.markdown("""
    Often, a single tree is not sufficient for producing effective results. This is where the Random Forest algorithm comes into the picture.

    Random Forest is a tree-based machine learning algorithm that leverages the power of multiple decision trees for making decisions. As the name suggests, it is a “forest” of trees!

    The Random Forest Algorithm combines the output of multiple (randomly created) Decision Trees to generate the final output.
    """)
    st.image("https://cdn.analyticsvidhya.com/wp-content/uploads/2020/02/rfc_vs_dt1.png")

    st.markdown("""
    **Accuracy obtained for both Decision Tree algorithm and Random Forest algorithm**
    Decision Tree: 87%
    
    Random Forest: 96%
    
    As planned the best accuracy is obtained with Random Forest algorithm
    """)

    
    # ----- Deployment in Production -----
    toc.title("Deployment in Production")
    toc.header("Docker: FastAPI + Streamlit")
    st.markdown("""
    - Frontend - Streamlit: [http://hr-analytics.smascha.ai](http://hr-analytics.smascha.ai)
    - API Documentation (Swagger OpenAPI Specification) - FastAPI: [http://hr-api.smascha.ai](http://hr-api.smascha.ai)
    
    FastAPI is a modern, fast (high-performance), web framework for building APIs with Python. FastAPI supports data validation via pydantic and automatic API documentation as well.
        Streamlit, meanwhile, is an application framework that makes it easy for data scientists and machine learning engineers to create powerful user interfaces that interact with machine learning models.
        """)
    toc.subheader("API Documentation with Sagger")
    st.image(PATH_RES_FOLDER + "img/FastAPI.png")
    toc.header("Load Balancer: Traefik")
    st.markdown("""
        - Reverse Proxy & Load Balancer - Traefik: [http://smascha.ai:8080](http://smascha.ai:8080)
        Traefik intercepts and routes every incoming request to the corresponding services.
        Documentation V.2.2: [https://doc.traefik.io/traefik/v2.2](https://doc.traefik.io/traefik/v2.2)
        """)
    st.image(PATH_RES_FOLDER + "img/Traefik.png")
    toc.header("Kubernetes")
    st.markdown("""
        Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.
        In fact, all our services (Frontend and Backend) are already containerized. They can be easily deployed to Kubernetes using Terraform.
        """)
    toc.header("Data Persistence - Microsoft SQL")
    st.markdown("""
        We decided to keep this website as stateless for privacy reason.\n\
        Nevertheless, we planned and tested the implementation of Microsoft SQL.

        We already deployed Microsoft SQL (version 2019) on smascha.ai thanks to the [official Docker image from Microsoft](https://hub.docker.com/_/microsoft-mssql-server).
        """)


def app():

    toc = Toc()
    st.sidebar.markdown("# Table of Contents")
    toc_content(toc)
    toc.generate()
