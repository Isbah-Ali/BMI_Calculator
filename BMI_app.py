import streamlit as st

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 20px !important;
        color: #FFFFFF !important;
        background-color: #000000 !important;
    }

    /* Button styling */
    .stButton>button {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        font-size: 20px !important;
        border-radius: 8px !important;
        border: none !important;
        font-weight: bold !important;
    }

    .stButton>button:hover {
        background-color: #009900 !important;
        color: white !important;
    }

    /* Input boxes, sliders, etc. */
    .stTextInput>div>div>input, textarea, .stSlider {
        background-color: #0D0D0D !important;
        color: #00FF7F !important;
        font-size: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("BMI Calculator")
st.sidebar.header("Isbah Ali")
st.sidebar.write("Hi I am Isbah, A Data Analyst. \nI Create interactive apps and dashboards using Streamlit. \n Contact Me: \nisbahali17@gmail.com ")
st.header("BMI Calculation: All for your health!" , divider = "blue")
st.write("Choose the units you are entering weight in:")

col1, col2 = st.columns(2)

with col1:
    weight_unit = st.selectbox("Select weight unit: ", ["Kg", "pound"])

with col2:
    height_unit = st.selectbox("Select height unit: ", ["Centimeters", "feet/inches"])


weight = st.number_input("Enter weight:", min_value=1.0)

col3, col4 = st.columns(2) 
if height_unit == "Centimeters":
    height = st.number_input("Enter height **(cm)**:", min_value=1.0, step=0.1)
 
else:
    with col3:
        feet = st.number_input("Enter **feet**:", min_value=0.0, step=1.0)
    with col4:
        inches = st.number_input("Enter **inches**:", min_value=0.0, step=1.0)

BMI = 0

if st.button("Submit"):
    if weight_unit == "pound":
        weight *= 0.453592
    if height_unit == "Centimeters":
        height /= 100
    if height_unit== "feet/inches":
        height = (feet+inches/12)*0.304

    BMI = round(weight / (height ** 2), 2)

    st.success(f"BMI calculated from above values is: {BMI}")

    if BMI < 18.5:
        st.info("Category: Under Weight", icon = ":material/sentiment_dissatisfied:")
    elif 18.5 <= BMI < 24.9:
        st.info("Category: Normal Weight", icon = ":material/sentiment_very_satisfied:")
    elif 25 <= BMI < 29.9:
        st.info("Category: Over Weight", icon = ":material/sentiment_neutral:")
    else:
        st.info("Category: Obese", icon = ":material/sentiment_dissatisfied:")

    
    
