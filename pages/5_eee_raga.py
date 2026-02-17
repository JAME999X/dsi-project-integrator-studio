import streamlit as st
st.title("EEE-Gate + RAGA")
st.subheader("EEE-Gate (Evidence / Ethics / Economics)")
eee = st.session_state["eee_gate"]
for pillar in ["Evidence", "Ethics", "Economics"]:
st.markdown(f"### {pillar}")
for k in list(eee[pillar].keys()):
eee[pillar][k] = st.checkbox(f"{pillar}: {k}",
value=eee[pillar][k], key=f"{pillar}_{k}")
st.session_state["eee_gate"] = eee
st.divider()
st.subheader("RAGA (texto defendible)")
raga = st.session_state["raga"]
raga["Risks"] = st.text_area("Risks", value=raga["Risks"], height=80)
raga["Alternatives"] = st.text_area("Alternatives",
value=raga["Alternatives"], height=80)
raga["Governance"] = st.text_area("Governance",
value=raga["Governance"], height=80)
raga["Action"] = st.text_area("Action", value=raga["Action"],
height=80)
st.session_state["raga"] = raga
# Señal didáctica: gate incompleto
missing = []
for pillar, checks in eee.items():
for k, v in checks.items():
if not v and not (pillar == "Ethics" and k ==
"no_dark_patterns"):
missing.append(f"{pillar}:{k}")
if missing:
st.warning("EEE-Gate incompleto: " + ", ".join(missing))
else:
st.success("EEE-Gate completo (según checks).")
