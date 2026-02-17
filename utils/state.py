import streamlit as st
import pandas as pd
def init_state():
ss = st.session_state
# Charter
ss.setdefault("charter", {
"nombre": "Proyecto A3 (ejemplo)",
"problema": "El proceso actual genera retrabajo y no es
trazable.",
"objetivo": "Reducir tiempo de ciclo manteniendo control y
gobernanza.",
"alcance": "MVP en 6-8 semanas. Integración mínima con
sistemas existentes.",
"no_alcance": "Automatización total sin HITL en casos
críticos.",
"restricciones": "PII minimizada; auditoría obligatoria; SLO
latencia p95.",
"kpis": "Outcome: FCR | Efficiency: €/caso | Safety: fuga PII
/ alucinación",
})
# Stakeholders
ss.setdefault("stakeholders", pd.DataFrame([
{"Stakeholder": "Service Owner", "Interés": "Alto",
"Influencia": "Alta", "Necesidad": "Cumplir SLA y reducir retrabajo"},
{"Stakeholder": "CFO", "Interés": "Medio", "Influencia":
"Alta", "Necesidad": "Control de costes"},
{"Stakeholder": "Legal/DPO", "Interés": "Alto", "Influencia":
"Media", "Necesidad": "Cumplimiento y PII"},
{"Stakeholder": "Usuarios", "Interés": "Alto", "Influencia":
"Media", "Necesidad": "Respuestas rápidas y correctas"},
]))
# Backlog (para exportar a CSV/JSON)
ss.setdefault("backlog", pd.DataFrame([
{
"Epic": "Intake",
"User Story": "Como usuario, quiero un formulario guiado
para enviar casos completos.",
"Acceptance Criteria": "Campos obligatorios; validación;
confirmación.",
"Priority": "Must",
"Estimate": 5,
"Value": 8,
"Risk": 4,
},
{
"Epic": "Assistance",
"User Story": "Como agente, quiero sugerencias de
resolución basadas en KB (RAG).",
"Acceptance Criteria": "Cita fuentes; fallback; logging
sin PII.",
"Priority": "Should",
"Estimate": 8,
"Value": 9,
"Risk": 6,
},
]))
# Arquitectura (componentes y flujos)
ss.setdefault("components", pd.DataFrame([
{"Component": "UI (Portal)", "Type": "UI", "Responsibility":
"Captura de casos + feedback", "Owner": "PO", "Data": "Input
usuario"},
{"Component": "API Gateway", "Type": "Service",
"Responsibility": "Auth/RBAC + rate limit", "Owner": "SRE", "Data":
"Tokens, sesiones"},
{"Component": "RAG Service", "Type": "Service",
"Responsibility": "Recuperación KB + grounding", "Owner": "Eng",
"Data": "Docs KB"},
{"Component": "LLM Inference", "Type": "External",
"Responsibility": "Generación", "Owner": "Eng", "Data": "Prompts
(minimizados)"},
{"Component": "Audit Log", "Type": "DB", "Responsibility":
"Trazabilidad sin PII", "Owner": "SRE", "Data": "Eventos"},
]))
ss.setdefault("flows", pd.DataFrame([
{"From": "UI (Portal)", "To": "API Gateway", "Data": "Caso +
contexto", "Notes": "Validación en UI"},
{"From": "API Gateway", "To": "RAG Service", "Data": "Consulta
normalizada", "Notes": "PII minimizada"},
{"From": "RAG Service", "To": "LLM Inference", "Data":
"Contexto + prompt", "Notes": "Citas obligatorias"},
{"From": "API Gateway", "To": "Audit Log", "Data": "Eventos",
"Notes": "Sin PII"},
]))
# Gobernanza
ss.setdefault("raci", pd.DataFrame([
APP3 — DSI Project Integrator Studio (A3)
{"Actividad": "Operación y runbooks", "PO": "A", "SRE": "R",
"Legal": "C", "Data Steward": "C"},
{"Actividad": "Política de datos", "PO": "C", "SRE": "I",
"Legal": "A", "Data Steward": "R"},
{"Actividad": "Auditoría y logging", "PO": "A", "SRE": "R",
"Legal": "C", "Data Steward": "C"},
]))
ss.setdefault("raid", pd.DataFrame([
{"Tipo": "Risk", "Item": "PII en prompts/logs", "Mitigación":
"Minimización + filtros + auditoría", "Owner": "Data Steward",
"Estado": "Open"},
{"Tipo": "Assumption", "Item": "KB está actualizada",
"Mitigación": "Owner por dominio + revisión mensual", "Owner": "PO",
"Estado": "Open"},
{"Tipo": "Issue", "Item": "Latencia alta en picos",
"Mitigación": "Caching + rate limit + fallback", "Owner": "SRE",
"Estado": "Open"},
{"Tipo": "Dependency", "Item": "Acceso a KB/ITSM",
"Mitigación": "RBAC + contrato API", "Owner": "SRE", "Estado":
"Open"},
]))
ss.setdefault("data_policy", {
"contiene_pii": True,
"minimizacion": True,
"retention_days": 30,
"kill_switch": True,
"hitl_criticos": True,
})
# EEE-Gate + RAGA
ss.setdefault("eee_gate", {
"Evidence": {"kpis_definidos": False, "baseline": False,
"experimento": False},
"Ethics": {"pii_control": False, "auditoria": False,
"no_dark_patterns": True},
"Economics": {"cost_model": False, "tco": False,
"sensibilidad": False},
})
ss.setdefault("raga", {
"Risks": "PII, alucinación, latencia, dependencia de
sistemas.",
"Alternatives": "A) Más HITL vs B) Más automatización con
guardrails.",
"Governance": "Owners claros + controles mínimos +
auditoría.",
"Action": "Piloto controlado con métricas
valor/coste/riesgo.",
})
