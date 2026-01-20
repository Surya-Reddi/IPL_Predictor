"""
CSS styling for IPL Win Predictor
Dark vibrant design with high contrast and complementary colors
"""

def get_css():
    return """
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    
    /* Main background with dark vibrant gradient */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main container styling */
    .main {
        background: rgba(26, 26, 46, 0.85);
        border-radius: 25px;
        padding: 2.5rem;
        box-shadow: 0 25px 70px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 107, 107, 0.2);
    }
    
    /* Title styling - Bright and vibrant */
    h1 {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 50%, #48dbfb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        text-align: center;
        font-size: 3.5rem !important;
        margin-bottom: 2.5rem;
        filter: drop-shadow(0 0 20px rgba(255, 107, 107, 0.5));
        letter-spacing: 2px;
    }
    
    /* Headers (result headers) - High contrast */
    h2 {
        color: #ffffff;
        padding: 2rem;
        border-radius: 18px;
        text-align: center;
        font-weight: 700;
        font-size: 2rem !important;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    h2:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
    }
    
    /* First result (winning team) - Complementary green */
    h2:first-of-type {
        background: linear-gradient(135deg, #0be881 0%, #05c46b 100%);
        box-shadow: 0 10px 30px rgba(11, 232, 129, 0.4);
    }
    
    /* Second result (losing team) - Complementary red */
    h2:nth-of-type(2) {
        background: linear-gradient(135deg, #ff3838 0%, #ff6348 100%);
        box-shadow: 0 10px 30px rgba(255, 56, 56, 0.4);
    }
    
    /* Labels - HIGH VISIBILITY with bright contrasting colors */
    label {
        color: #feca57 !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        margin-bottom: 0.8rem !important;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        text-shadow: 0 2px 10px rgba(254, 202, 87, 0.3);
        display: block !important;
    }
    
    /* Select boxes - Bright contrasting colors */
    .stSelectbox {
        margin-bottom: 1.5rem;
    }
    
    .stSelectbox > div > div {
        background: linear-gradient(135deg, #2d3561 0%, #1e2749 100%);
        border-radius: 12px;
        border: 3px solid #ff6b6b;
        font-weight: 700;
        color: #ffffff;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(255, 107, 107, 0.3);
    }
    
    .stSelectbox > div > div:hover {
        border-color: #feca57;
        box-shadow: 0 8px 25px rgba(254, 202, 87, 0.5);
        transform: translateY(-2px);
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #48dbfb;
        box-shadow: 0 0 0 3px rgba(72, 219, 251, 0.3);
    }
    
    /* Dropdown options */
    .stSelectbox option {
        background: #1e2749;
        color: #ffffff;
        font-weight: 600;
    }
    
    /* Number inputs - Vibrant with high contrast */
    .stNumberInput > div > div > input {
        background: linear-gradient(135deg, #2d3561 0%, #1e2749 100%);
        border-radius: 12px;
        border: 3px solid #48dbfb;
        font-weight: 700;
        color: #ffffff;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 5px 20px rgba(72, 219, 251, 0.3);
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #0be881;
        box-shadow: 0 0 0 3px rgba(11, 232, 129, 0.3);
        transform: translateY(-2px);
    }
    
    .stNumberInput > div > div > input:hover {
        border-color: #feca57;
        box-shadow: 0 8px 25px rgba(254, 202, 87, 0.4);
    }
    
    /* Number input buttons */
    .stNumberInput button {
        background: #ff6b6b !important;
        color: white !important;
        border: none !important;
        font-weight: bold;
    }
    
    .stNumberInput button:hover {
        background: #ff3838 !important;
    }
    
    /* Predict button - Eye-catching with animation */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b 0%, #ff3838 100%);
        color: white;
        font-weight: 800;
        font-size: 1.5rem;
        padding: 1rem 3rem;
        border-radius: 60px;
        border: 3px solid #feca57;
        width: 100%;
        margin-top: 2.5rem;
        box-shadow: 0 15px 35px rgba(255, 107, 107, 0.5);
        transition: all 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 2px;
        position: relative;
        overflow: hidden;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: left 0.5s;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 20px 45px rgba(255, 107, 107, 0.7);
        background: linear-gradient(135deg, #ff3838 0%, #ff6b6b 100%);
        border-color: #48dbfb;
    }
    
    .stButton > button:active {
        transform: translateY(-2px) scale(0.98);
    }
    
    /* Columns */
    [data-testid="column"] {
        padding: 0.8rem;
    }
    
    /* Info/Warning messages - High contrast */
    .stAlert {
        border-radius: 15px;
        font-weight: 600;
        font-size: 1.05rem;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }
    
    /* Warning */
    [data-baseweb="notification"] {
        background: linear-gradient(135deg, #feca57 0%, #ff9ff3 100%);
        border-left: 6px solid #ff6b6b;
        color: #1a1a2e;
        font-weight: 700;
    }
    
    /* Error messages */
    .stAlert[data-testid="stAlert"] {
        background: linear-gradient(135deg, #ff3838 0%, #ff6348 100%);
        color: white;
        border: none;
        font-weight: 700;
    }
    
    /* Info messages */
    div[data-testid="stMarkdownContainer"] > div > div {
        color: #e9ecef;
        font-weight: 500;
    }
    
    /* Markdown text in info box */
    .stInfo {
        background: linear-gradient(135deg, #2d3561 0%, #1e2749 100%);
        border-left: 6px solid #48dbfb;
        color: #ffffff;
        border-radius: 12px;
        font-weight: 600;
    }
    
    /* Subheaders */
    h3 {
        color: #48dbfb !important;
        font-weight: 700 !important;
        font-size: 1.8rem !important;
        text-align: center;
        text-shadow: 0 2px 15px rgba(72, 219, 251, 0.4);
    }
    
    /* Horizontal rule */
    hr {
        border-color: rgba(254, 202, 87, 0.3) !important;
        margin: 2rem 0 !important;
    }
    
    /* Success message */
    .element-container div[data-testid="stMarkdownContainer"] {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Spinner - Matching theme */
    .stSpinner > div {
        border-top-color: #ff6b6b !important;
        border-right-color: #feca57 !important;
        border-bottom-color: #48dbfb !important;
    }
    
    /* Scrollbar - Styled to match dark theme */
    ::-webkit-scrollbar {
        width: 12px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1a1a2e;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #ff6b6b 0%, #feca57 50%, #48dbfb 100%);
        border-radius: 10px;
        border: 2px solid #1a1a2e;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #48dbfb 0%, #feca57 50%, #ff6b6b 100%);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        h1 {
            font-size: 2.2rem !important;
        }
        
        h2 {
            font-size: 1.5rem !important;
            padding: 1.2rem;
        }
        
        label {
            font-size: 1rem !important;
        }
        
        .stButton > button {
            font-size: 1.2rem;
            padding: 0.8rem 2rem;
        }
        
        .main {
            padding: 1.5rem;
        }
    }
    
    /* Additional contrast improvements */
    p {
        color: #e9ecef !important;
        font-weight: 500;
    }
    
    /* Input placeholder text */
    input::placeholder {
        color: rgba(255, 255, 255, 0.5) !important;
        font-weight: 600;
    }
    
    /* Glow effect for interactive elements */
    .stSelectbox > div > div:focus-within,
    .stNumberInput > div > div > input:focus {
        filter: drop-shadow(0 0 15px currentColor);
    }
    </style>
    """