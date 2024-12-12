"""

Creating a home page to greet customers for our dashboard. 

"""
import streamlit as st
import requests
import streamlit.components.v1 as components


def home_page() -> None:
    """ Function that runs the whole home page. """
    st.logo("logo.png", size='large')

    initial_banner()
    st.container(height=2, border=False)
    information_section()


def meet_us_button():
    with st.popover(label="Meet Us!"):
        st.markdown("Ahahaha")


def information_section():
    """Adding size to buttons"""
    st.markdown("""
    <style>
                
    .stButton>button {
    color: #30693e;
    border-radius: 10%;
    height: 5em;
    width: 10em;
                
    }
    </style>""", unsafe_allow_html=True)
    c = st.columns(7)
    with c[1]:
        st.button("Meet Us")
    with c[3]:
        st.button("Get Started!")
    with c[5]:
        st.button("Help Us!")

    components.iframe("https://store.steampowered.com/")


def initial_banner() -> None:
    """ Top Banner """
    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://static.vecteezy.com/system/resources/previews/002/323/313/non_2x/banknotes-rain-money-falling-vector.jpg");
    background-size: cover;
    }

    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }

    [data-testid="stVerticalBorderWrapper"] {
    background-image: url("https://cdn.corporatefinanceinstitute.com/assets/cash-ratio.jpg");
    background-size: cover;
    }

    .border-class {
        border: 2px solid #555
    }

    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
                <head>
                <img src='https://i.imgur.com/VJL4LVo.png' class="border-class">
                </head>
                """,
                unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(page_title="Price Slashers - Sales Tracker",
                       page_icon="💸", layout="wide")
    home_page()
