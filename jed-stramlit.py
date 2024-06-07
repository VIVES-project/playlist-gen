import streamlit as st
import streamlit_nested_layout
import qrcode



st.set_page_config(layout='wide')

col1, col2, col3 = st.columns((3,1,1))

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

with col1:
    with st.container(height = 600, border =True):
        st.image("pic.jpg", width = 1000)
    with st.container(height = 100, border = True):
        st.write("the quick brown fox jumps over the lazy dog                      ")
        
with col2:
    with st.container(height = 350, border = True):
        st.write("test test")
    with st.container(height = 350,border = True):


        def generate_qr(data):
            img = qrcode.make(data)
            img.save("qr_code.png")
            generate_qr("https://pypixel.com") 

with col3:
    with st.container(height = 700, border = True):
        st.title("Sunny Edge Vibe Playlist")
        with st.container(height = 700, border = True):
            st.write("Lil Nas X")


