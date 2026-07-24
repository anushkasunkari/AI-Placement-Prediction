import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Career & Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("placement_model.pkl", "rb"))

# ---------------- TITLE ----------------
st.title("🎓 AI Career & Placement Prediction")
st.write("Fill in the student details to predict placement.")

st.markdown("---")

# ---------------- INPUTS ----------------

col1, col2 = st.columns(2)

with col1:
    student_id = st.number_input("Student ID", min_value=1, step=1)

    gender = st.selectbox(
        "Gender (Encoded)",
        [0, 1],
        help="Use the encoded value from your dataset."
    )

    age = st.number_input("Age", 15, 40, 20)

    branch = st.selectbox(
        "Branch (Encoded)",
        [0, 1, 2],
        help="Use the encoded branch value from your dataset."
    )

    cgpa = st.number_input("CGPA", 0.0, 10.0, 7.5)

    tenth = st.number_input("10th Percentage", 0.0, 100.0, 75.0)

    twelfth = st.number_input("12th Percentage", 0.0, 100.0, 75.0)

    python = st.slider("Python Skill", 0, 10, 5)

    java = st.slider("Java Skill", 0, 10, 5)

    sql = st.slider("SQL Skill", 0, 10, 5)

    excel = st.slider("Excel Skill", 0, 10, 5)

    powerbi = st.slider("Power BI Skill", 0, 10, 5)


with col2:

    tableau = st.slider("Tableau Skill", 0, 10, 5)

    ml = st.slider("Machine Learning Skill", 0, 10, 5)

    communication = st.slider("Communication Skill", 0, 10, 5)

    aptitude = st.slider("Aptitude Score", 0, 100, 50)

    projects = st.number_input("Projects", 0, 20, 2)

    internship = st.number_input("Internships", 0, 10, 1)

    certifications = st.number_input("Certifications", 0, 20, 2)

    leetcode = st.number_input("LeetCode Problems", 0, 1000, 100)

    hackathons = st.number_input("Hackathons", 0, 20, 1)

    resume = st.slider("Resume Score", 0, 100, 70)

    readiness = st.slider("Placement Readiness", 0, 100, 70)

    salary = st.number_input(
        "Expected Salary (LPA)",
        1.0,
        50.0,
        5.0
    )

st.markdown("---")

# ---------------- PREDICTION ----------------

if st.button("Predict Placement"):

    input_df = pd.DataFrame([[
        student_id,
        gender,
        age,
        branch,
        cgpa,
        tenth,
        twelfth,
        python,
        java,
        sql,
        excel,
        powerbi,
        tableau,
        ml,
        communication,
        aptitude,
        projects,
        internship,
        certifications,
        leetcode,
        hackathons,
        resume,
        readiness,
        salary
    ]], columns=[
        "Student_ID",
        "Gender",
        "Age",
        "Branch",
        "CGPA",
        "Tenth_Percentage",
        "Twelfth_Percentage",
        "Python",
        "Java",
        "SQL",
        "Excel",
        "PowerBI",
        "Tableau",
        "Machine_Learning",
        "Communication_Skill",
        "Aptitude_Score",
        "Projects",
        "Internship",
        "Certifications",
        "LeetCode_Problems",
        "Hackathons",
        "Resume_Score",
        "Placement_Readiness",
        "Expected_Salary_LPA"
    ])

    prediction = model.predict(input_df)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("🎉 Congratulations! The student is likely to be PLACED.")
        st.balloons()
    else:
        st.error("❌ The student is less likely to be placed.")
        st.info("Try improving CGPA, aptitude, communication, projects, certifications, and technical skills.")
