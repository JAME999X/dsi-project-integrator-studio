import streamlit as st
from utils.report import build_markdown, pdf_bytes, backlog_csv_bytes,
backlog_json_bytes
st.title("Exportar entregables")
md = build_markdown(st.session_state)
st.code(md, language="markdown")
c1, c2, c3, c4 = st.columns(4)
with c1:
st.download_button(" Reporte .md", md.encode("utf-8"),
"a3_reporte.md", "text/markdown", use_container_width=True)
with c2:
st.download_button(" Reporte .pdf", pdf_bytes(st.session_state),
"a3_reporte.pdf", "application/pdf", use_container_width=True)
with c3:
st.download_button(" Backlog .csv",
backlog_csv_bytes(st.session_state), "a3_backlog.csv", "text/csv",
use_container_width=True)
with c4:
st.download_button(" Backlog .json",
backlog_json_bytes(st.session_state), "a3_backlog.json",
"application/json", use_container_width=True)
