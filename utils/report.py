import io
import json
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer,
Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
def _df_to_table(df):
data = [list(df.columns)] + df.astype(str).values.tolist()
t = Table(data, repeatRows=1)
t.setStyle(TableStyle([
("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
("GRID", (0,0), (-1,-1), 0.5, colors.grey),
("VALIGN", (0,0), (-1,-1), "TOP"),
("FONTSIZE", (0,0), (-1,-1), 8),
]))
return t
def build_markdown(ss) -> str:
ch = ss["charter"]
dp = ss["data_policy"]
eee = ss["eee_gate"]
raga = ss["raga"]
md = []
md.append("# DSI Project Integrator Studio — Reporte\n")
md.append(f"- Fecha: **{date.today().isoformat()}**\n")
md.append("## 1) Project Charter\n")
md.append(f"- Nombre: **{ch['nombre']}**\n")
md.append(f"- Problema: {ch['problema']}\n")
md.append(f"- Objetivo: {ch['objetivo']}\n")
md.append(f"- Alcance: {ch['alcance']}\n")
md.append(f"- No-alcance: {ch['no_alcance']}\n")
md.append(f"- Restricciones: {ch['restricciones']}\n")
md.append(f"- KPIs: {ch['kpis']}\n")
md.append("\n## 2) Stakeholders\n")
md.append(ss["stakeholders"].to_markdown(index=False))
md.append("\n\n## 3) Backlog\n")
md.append(ss["backlog"].to_markdown(index=False))
md.append("\n\n## 4) Arquitectura (componentes)\n")
md.append(ss["components"].to_markdown(index=False))
md.append("\n\n## 5) Arquitectura (flujos)\n")
md.append(ss["flows"].to_markdown(index=False))
md.append("\n\n## 6) Gobernanza — RACI\n")
md.append(ss["raci"].to_markdown(index=False))
md.append("\n\n## 7) Gobernanza — RAID\n")
md.append(ss["raid"].to_markdown(index=False))
md.append("\n\n## 8) Política de datos (mínimos)\n")
md.append(f"- Contiene PII: **{dp['contiene_pii']}**\n")
md.append(f"- Minimización: **{dp['minimizacion']}**\n")
md.append(f"- Retención (días): **{dp['retention_days']}**\n")
md.append(f"- Kill switch: **{dp['kill_switch']}**\n")
md.append(f"- HITL en críticos: **{dp['hitl_criticos']}**\n")
md.append("\n## 9) EEE-Gate\n")
for pillar, checks in eee.items():
md.append(f"### {pillar}\n")
for k, v in checks.items():
box = "x" if v else " "
md.append(f"- [{box}] {k}\n")
md.append("\n## 10) RAGA\n")
md.append(f"- **Risks:** {raga['Risks']}\n")
md.append(f"- **Alternatives:** {raga['Alternatives']}\n")
md.append(f"- **Governance:** {raga['Governance']}\n")
md.append(f"- **Action:** {raga['Action']}\n")
return "\n".join(md)
def pdf_bytes(ss) -> bytes:
styles = getSampleStyleSheet()
buf = io.BytesIO()
doc = SimpleDocTemplate(
buf, pagesize=A4,
leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm,
bottomMargin=2*cm
)
story = []
ch = ss["charter"]
story.append(Paragraph("DSI Project Integrator Studio — Reporte",
styles["Title"]))
story.append(Spacer(1, 8))
story.append(Paragraph(f"Proyecto: <b>{ch['nombre']}</b>",
styles["BodyText"]))
story.append(Paragraph(f"Objetivo: {ch['objetivo']}",
styles["BodyText"]))
story.append(Spacer(1, 10))
story.append(Paragraph("Stakeholders", styles["Heading2"]))
story.append(_df_to_table(ss["stakeholders"]))
story.append(Spacer(1, 10))
story.append(Paragraph("Backlog", styles["Heading2"]))
story.append(_df_to_table(ss["backlog"]))
story.append(Spacer(1, 10))
story.append(Paragraph("Arquitectura — Componentes",
styles["Heading2"]))
story.append(_df_to_table(ss["components"]))
story.append(Spacer(1, 10))
story.append(Paragraph("Arquitectura — Flujos",
styles["Heading2"]))
story.append(_df_to_table(ss["flows"]))
story.append(Spacer(1, 10))
story.append(Paragraph("RACI", styles["Heading2"]))
story.append(_df_to_table(ss["raci"]))
story.append(Spacer(1, 10))
story.append(Paragraph("RAID", styles["Heading2"]))
story.append(_df_to_table(ss["raid"]))
doc.build(story)
return buf.getvalue()
def backlog_csv_bytes(ss) -> bytes:
return ss["backlog"].to_csv(index=False).encode("utf-8")
def backlog_json_bytes(ss) -> bytes:
items = ss["backlog"].to_dict(orient="records")
return json.dumps(items, ensure_ascii=False,
indent=2).encode("utf-8")
