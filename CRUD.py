import streamlit as st
from logic import flights
import plotly.express as px

fly = flights()

st.sidebar.title('Flights Analysis')

menu = st.sidebar.selectbox('Menu', ['Select One', 'Check Flights', 'Analysis'])

if menu == 'Select One':
    st.markdown('## WELCOME TO ANALYSIS ABOUT FLIGHTS.')
    st.markdown('### How can we help you?')
    st.divider()


elif menu == 'Check Flights':
    st.markdown('## CHECK FLIGHTS')
    st.divider()

    col1, col2 = st.columns(2)
    with col1:
        cities = fly.fetch_city_name()
        select1 = st.selectbox('Source', cities)

    with col2:
        cities2 = fly.fetch_city_name()
        select2 = st.selectbox('Destination', cities2)

    if st.button('Search'):

        if select1 == select2:
            st.markdown('#### No Flight exists')
        else:
            sou_des = fly.fetch_cities_data(select1, select2)
            st.dataframe(sou_des)

elif menu == 'Analysis':
    st.markdown('## ANALYSIS')
    st.divider()

    airline, frequeny = fly.fetch_count_flights()

    fig = px.pie(names=airline, values=frequeny, title='Flights')

    # Display the plot using Streamlit
    st.plotly_chart(fig)

    st.divider()


    source, number = fly.fetch_bussy_airport()

    fig2 = px.bar(x = source, y = number, title = 'Most busiest airport')
    st.plotly_chart(fig2)