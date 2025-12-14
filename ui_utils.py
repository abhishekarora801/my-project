import streamlit as st

@st.cache_data
def load_css():
  """Load and cache CSS styles"""
  try:
    with open("resources/styles.css") as f:
      return f.read()
  except Exception as e:
    print(f"[ERROR] Failed to load CSS: {e}")
    return ""

def setup_ui():
  """Configure the UI components"""
  # Configure page with minimal settings
  st.set_page_config(
    page_title="Banking Assistant",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"  # Collapse sidebar for faster loading
  )

  # Apply cached CSS
  st.markdown(f"<style>{load_css()}</style>", unsafe_allow_html=True)

  # Header section
  st.markdown("<h1 class='header-title'>🏦 Banking Assistant</h1>", unsafe_allow_html=True)
  st.markdown("<p class='header-subtitle'>Ask questions about accounts, cards, loans, insurance, or investments. Also support exchange rate queries.</p>", unsafe_allow_html=True)
  
  # Add toggle button for prompt template selection - positioned at the bottom near the input bar
  # We'll add this to the display_chat_history function instead to position it near the input

def display_chat_history():
  """Display the chat message history"""
  for message in st.session_state.messages:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])

  # Add toggle button for prompt template selection aligned with chat messages
  # Create a container for the toggle button
  toggle_container = st.container()
  
  # Create the toggle button using radio buttons with horizontal layout
  # We'll place this directly in the main flow, aligned with messages
  selected_template = st.radio(
    "Response Style:",
    ["Detailed", "Brief"],
    horizontal=True,
    index=0 if st.session_state.prompt_template_type == 'detailed' else 1,
    key="template_toggle",
    help="Toggle between detailed or brief response styles"
  )
  
  # Update session state based on selection
  if selected_template == "Detailed":
    st.session_state.prompt_template_type = 'detailed'
  else:
    st.session_state.prompt_template_type = 'brief'

  # Add space at bottom for fixed input
  st.markdown("<br><br><br><br>", unsafe_allow_html=True)
