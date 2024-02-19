import streamlit as st
import langchain_helper as lh

st.title("Restaurant Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine", ("American", "French", "Indian", "Japanese", "Thai"))


if cuisine:
    response = lh.generate_restaurant_name_and_menu(cuisine)
    st.header(response['restaurant_name'].strip())
    st.subheader(response['cuisine'].strip())
    st.write('**Menu**')
    menu_items = response['menu_items'].split(',')
    for item in menu_items:
        st.write(f'{item.strip()}')
