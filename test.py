import streamlit as st
import pandas as pd
import mysql.connector as sql

# streamlit run D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\streamlit\test1\test.py
# https://streamlit.io/
# pipreqs --encoding utf-8 "D:\Dropbox\Empresa\Buydepa\COLOMBIA\DESARROLLO\streamlit\test1"
# https://share.streamlit.io/
# cuenta de github - agavirja

st.title('hellow world')
st.text('Este es un texto que lo pongo')
st.markdown('## Esto es un markdown')

db_connection  = sql.connect(user=st.secrets["user"], password=st.secrets["password"], host=st.secrets["host"], database=st.secrets["database"])
df      = pd.read_sql("SELECT id_inmueble FROM colombia.data_stock_inmuebles_caracteristicas" , con=db_connection)
st.write(df.describe())
db_connection.close()
