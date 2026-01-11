# streamlit_app.py
import streamlit as st
import pandas as pd
import pickle

# Streamlit page config
st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎓",
    layout="wide"
)

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    /* Main App Background */
    .stApp {
        background: radial-gradient(circle at 10% 30%, #2c0a3a 10%, #1a0022 90%);
        background-attachment: fixed;
        color: #ffffff;
        min-height: 100vh;
    }
    
    /* Noise Texture Overlay */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
        opacity: 0.1;
        pointer-events: none;
        z-index: -1;
    }
    
    /* Main Content Container *
    
    /* Title Styling */
    .title {
        background: linear-gradient(45deg, #ff9d00, #ff6b00);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-size: 2.8rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -0.5px;
    }
    
    /* Subtitle Styling */
    .subtitle {
        color: #d0c4e4;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 300;
    }
    
    /* Column Styling */
    .st-emotion-cache-1v0mbdj, .st-emotion-cache-1p1nwyz {
        background: rgba(255, 255, 255, 0.03) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        margin: 0 10px !important;
        border: 1px solid rgba(255, 140, 0, 0.1) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2) !important;
        height: 100% !important;
    }
    
    /* Input Field Styling */
    .stTextInput input, .stNumberInput input, .stSelectbox select {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 140, 0, 0.3) !important;
        border-radius: 12px !important;
        color: white !important;
        padding: 12px 15px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput input:focus, .stNumberInput input:focus, .stSelectbox select:focus {
        border: 1px solid #ff8c00 !important;
        box-shadow: 0 0 0 2px rgba(255, 140, 0, 0.25) !important;
        background: rgba(255, 255, 255, 0.12) !important;
    }
    
    /* Input Label Styling */
    .stTextInput label, .stNumberInput label, .stSelectbox label, 
    .stSelectbox div[data-baseweb="select"] > div:first-child {
        color: #ffb26b !important;
        font-weight: 500 !important;
        font-size: 1.05rem !important;
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #ff8a00, #ff4d00) !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        padding: 12px 28px !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(255, 106, 0, 0.3) !important;
        transition: all 0.4s ease !important;
        display: block;
        margin: 2rem auto;
        width: auto !important;
        min-width: 300px !important;
        white-space: nowrap !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 106, 0, 0.5) !important;
        background: linear-gradient(135deg, #ff9500, #ff5a00) !important;
    }
    
    /* Success/Error Message Styling */
    .stSuccess {
        background: rgba(40, 167, 69, 0.2) !important;
        border: 1px solid rgba(40, 167, 69, 0.4) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        font-size: 1.3rem !important;
        text-align: center;
    }
    
    .stError {
        background: rgba(220, 53, 69, 0.2) !important;
        border: 1px solid rgba(220, 53, 69, 0.4) !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        font-size: 1.3rem !important;
        text-align: center;
    }
    
    /* Footer Styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #b8a1d9;
        font-size: 0.95rem;
        padding: 1rem;
        border-top: 1px solid rgba(255, 140, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content container
with st.container():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Banner
    st.markdown('<div class="banner"></div>', unsafe_allow_html=True)
    
    # Title and subtitle
    st.markdown('<div class="title">🎓 Placement Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Empower your decisions with data-driven insights</div>', unsafe_allow_html=True)

    # Load pipeline
    def load_pipeline(path="placement_pipeline.pkl"):
        with open(path, "rb") as f:
            return pickle.load(f)

    @st.cache_resource
    def get_pipeline():
        return load_pipeline()

    pipeline = get_pipeline()

    # Input form layout
    col1, col2, col3 = st.columns(3)
    
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        ssc_p = st.number_input("SSC Percentage (%)", 0.0, 100.0, step=0.1)
        hsc_p = st.number_input("HSC Percentage (%)", 0.0, 100.0, step=0.1)
        degree_p = st.number_input("Degree Percentage (%)", 0.0, 100.0, step=0.1)
        
    with col2:
        ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
        hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
        etest_p = st.number_input("E-Test Percentage (%)", 0.0, 100.0, step=0.1)  # Fixed typo
        mba_p = st.number_input("MBA Percentage (%)", 0.0, 100.0, step=0.1)
        
    with col3:
        hsc_s = st.selectbox("HSC Stream", ["Science", "Commerce", "Arts"])
        degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
        workex = st.selectbox("Work Experience", ["Yes", "No"])
        specialisation = st.selectbox("MBA Specialisation", ["Mkt&HR", "Mkt&Fin"])  # Fixed typo

    # Prediction section
    if st.button("Predict Placement"):
        input_df = pd.DataFrame([{
            'gender': gender,
            'ssc_p': ssc_p,
            'ssc_b': ssc_b,
            'hsc_p': hsc_p,
            'hsc_b': hsc_b,
            'hsc_s': hsc_s,
            'degree_p': degree_p,
            'degree_t': degree_t,
            'workex': workex,
            'etest_p': etest_p,
            'specialisation': specialisation,
            'mba_p': mba_p
        }])

        pred = pipeline.predict(input_df)[0]
        if pred == 1:
            st.success("✅ The student is likely to be **PLACED**.")
        else:
            st.error("❌ The student is likely to **NOT be placed**.")
            
    # Close main container
    st.markdown('</div>', unsafe_allow_html=True)

# Footer / credits
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)