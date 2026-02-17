import streamlit as st
from utils.state import init_state
st.set_page_config(page_title="DSI Project Integrator Studio",
page_icon=" ", layout="wide")
init_state()
pages = {
"A3 Studio": [
st.Page("pages/1_home_charter.py", title="Charter",
icon=" "),
st.Page("pages/2_backlog.py", title="Backlog", icon=" "),
st.Page("pages/3_arquitectura.py", title="Arquitectura",
icon=" "),
st.Page("pages/4_gobernanza.py", title="Gobernanza",
icon=" "),
st.Page("pages/5_eee_raga.py", title="EEE-Gate + RAGA",
icon=" "),
st.Page("pages/6_exportar.py", title="Exportar", icon=" "),
]
}
pg = st.navigation(pages, position="sidebar", expanded=True)
pg.run()
