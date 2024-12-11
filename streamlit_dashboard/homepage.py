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
body {
background-image: url("https://images.photowall.com/products/64251/green-trees-in-forest.jpg?h=699&q=85");
background-size: cover;
}
</style>
'''

    st.markdown(page_bg_img, unsafe_allow_html=True)
    with st.sidebar:
        st.write("")
        st.image("logo.png", width=300)
    with header_section:
        st.markdown(
            "<h1 style='text-align: center; color: green;'>Price Slashers Pipeline</h1>", unsafe_allow_html=True)


if __name__ == "__main__":
    home_page()
