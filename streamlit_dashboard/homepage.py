"""

Creating a home page to greet customers for our dashboard. 

"""
import streamlit as st

st.set_page_config(layout="wide")
header_section = st.container(border=True, height=500)


def home_page() -> None:
    """ Function that runs the whole home page. """

    page_bg_img = '''
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://windybot.com/img/6k9ecnQIon74X6sFLeQc.jpg");
    background-size: cover;
    }

    [data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
    }

    [data-testid="stVerticalBorderWrapper"] {
    background-image: url("https://cdn.corporatefinanceinstitute.com/assets/cash-ratio.jpg");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    with st.sidebar:
        st.write("")
        st.image("logo.png", use_container_width=True, clamp=True)
    with header_section:
        container_img = '''
        <style>
        [data-testid="stVerticalBorderWrapper"] {
        background-image: url("https://cdn.corporatefinanceinstitute.com/assets/cash-ratio.jpg");
        background-size: cover;
        }
        </style>
        '''
        st.markdown(container_img, unsafe_allow_html=True)
        st.markdown(
            "<h1 style='text-align: center; color: #ebffe1;'>Price Slashers Pipeline</h1>", unsafe_allow_html=True)


if __name__ == "__main__":
    home_page()
