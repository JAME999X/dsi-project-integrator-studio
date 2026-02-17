import streamlit as st
st.title("Gobernanza (RACI + RAID + Política de datos)")
st.subheader("RACI")
raci = st.session_state["raci"]
st.session_state["raci"] = st.data_editor(raci, num_rows="dynamic",
width="stretch", hide_index=True)
st.subheader("RAID")
raid = st.session_state["raid"]
st.session_state["raid"] = st.data_editor(raid, num_rows="dynamic",
width="stretch", hide_index=True)
st.subheader("Política de datos (mínimos)")
dp = st.session_state["data_policy"]
dp["contiene_pii"] = st.checkbox("Contiene PII",
value=dp["contiene_pii"])
dp["minimizacion"] = st.checkbox("Minimización activa (no logs con
PII)", value=dp["minimizacion"])
dp["retention_days"] = st.number_input("Retención (días)",
min_value=1, value=int(dp["retention_days"]), step=5)
dp["kill_switch"] = st.checkbox("Kill switch definido",
value=dp["kill_switch"])
dp["hitl_criticos"] = st.checkbox("HITL para casos críticos",
value=dp["hitl_criticos"])
st.session_state["data_policy"] = dp
