import streamlit as st
import pickle
import pandas as pd
import warnings
from css import get_css

warnings.filterwarnings('ignore')

# Constants
TOTAL_OVERS = 20
BALLS_PER_OVER = 6
TOTAL_WICKETS = 10
MAX_BALLS = TOTAL_OVERS * BALLS_PER_OVER

# Team lists
TEAMS = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Gujarat Titans',
    'Lucknow Super Giants',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals',
    'Punjab Kings'
]

CITIES = [
    'Hyderabad', 'Rajkot', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata',
    'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai', 'Cape Town',
    'Port Elizabeth', 'Durban', 'Centurion', 'East London',
    'Johannesburg', 'Kimberley', 'Bloemfontein', 'Ahmedabad',
    'Dharamsala', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
    'Cuttack', 'Visakhapatnam', 'Mohali', 'Bengaluru'
]

# Page configuration
st.set_page_config(
    page_title="IPL Win Predictor",
    page_icon="🏏",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Apply custom CSS
st.markdown(get_css(), unsafe_allow_html=True)

# Load the model
@st.cache_resource
def load_model():
    """Load the trained model from pickle file"""
    try:
        with open('pipe.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error("Model file 'pipe.pkl' not found. Please ensure it's in the same directory.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.stop()

pipe = load_model()

# Title
st.title('🏏 IPL WIN PREDICTOR')

# Team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the Batting Team', sorted(TEAMS))

with col2:
    bowling_team = st.selectbox('Select the Bowling Team', sorted(TEAMS))

# Validation: Same team cannot bat and bowl
if batting_team == bowling_team:
    st.warning("⚠️ Batting and Bowling teams cannot be the same!")

# City selection
selected_city = st.selectbox('Select Home City', sorted(CITIES))

# Target input
target = st.number_input('Target', value=0, min_value=0, step=1, format='%d')

# Match situation inputs
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score', value=0, min_value=0, step=1, format='%d')

with col4:
    overs = st.number_input('Overs Completed', value=0, min_value=0, max_value=19, step=1, format='%d')

with col5:
    wickets = st.number_input('Wickets Lost', value=0, min_value=0, max_value=9, step=1, format='%d')

# Predict button
if st.button('🎯 Predict Probability'):
    # Validation checks
    errors = []
    
    if batting_team == bowling_team:
        errors.append("Batting and Bowling teams must be different")
    
    if target <= 0:
        errors.append("Target must be greater than 0")
    
    if score > target:
        errors.append("Score cannot exceed the target")
    
    if overs == 0 and score > 0:
        errors.append("Overs completed cannot be 0 if score is greater than 0")
    
    balls_left = MAX_BALLS - (overs * BALLS_PER_OVER)
    runs_left = target - score
    
    if balls_left <= 0:
        errors.append("Match is already over (all overs completed)")
    
    if runs_left <= 0:
        errors.append("Target already achieved!")
    
    # Display errors if any
    if errors:
        for error in errors:
            st.error(f"❌ {error}")
    else:
        # Show loading spinner
        with st.spinner('Calculating win probabilities...'):
            try:
                # Calculate derived features
                wickets_left = TOTAL_WICKETS - wickets
                crr = score / overs if overs > 0 else 0
                rrr = (runs_left * BALLS_PER_OVER) / balls_left if balls_left > 0 else 0
                
                # Create input dataframe
                input_df = pd.DataFrame({
                    'batting_team': [batting_team],
                    'bowling_team': [bowling_team],
                    'city': [selected_city],
                    'runs_left': [runs_left],
                    'balls_left': [balls_left],
                    'wickets_left': [wickets_left],
                    'total_runs_x': [target],
                    'crr': [crr],
                    'rrr': [rrr]
                })
                
                # Make prediction
                result = pipe.predict_proba(input_df)
                
                loss = result[0][0]
                win = result[0][1]
                
                # Display results with animation
                st.markdown("---")
                st.subheader("📊 Win Probability")
                
                st.header(f"{batting_team} - {round(win * 100)}%")
                st.header(f"{bowling_team} - {round(loss * 100)}%")
                
                # Additional match context
                st.markdown("---")
                st.info(f"""
                **Match Situation:**
                - Runs Required: {runs_left} from {balls_left} balls
                - Current Run Rate: {crr:.2f}
                - Required Run Rate: {rrr:.2f}
                - Wickets Remaining: {wickets_left}
                """)
                
            except Exception as e:
                st.error(f"❌ Prediction failed: {str(e)}")
                st.info("Please check your input values and try again.")