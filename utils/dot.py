def arch_to_dot(components_df, flows_df) -> str:
"""
DOT para st.graphviz_chart (acepta string DOT).
"""
lines = [
"digraph G {",
"rankdir=LR;",
'node [shape=box, style="rounded"];'
]
comp_names = [str(x) for x in components_df["Component"].tolist()
if str(x).strip()]
comp_set = set(comp_names)
# nodos
for _, row in components_df.iterrows():
c = str(row.get("Component", "")).strip()
if not c:
continue
t = str(row.get("Type", "")).strip()
r = str(row.get("Responsibility", "")).strip()
label = f"{c}\\n[{t}]\\n{r}"
safe = label.replace('"', "'")
lines.append(f'"{c}" [label="{safe}"];')
# edges
for _, row in flows_df.iterrows():
a = str(row.get("From", "")).strip()
b = str(row.get("To", "")).strip()
if not a or not b or a not in comp_set or b not in comp_set:
continue
d = str(row.get("Data", "")).strip()
note = str(row.get("Notes", "")).strip()
elabel = f"{d}" + (f"\\n({note})" if note else "")
safe = elabel.replace('"', "'")
lines.append(f'"{a}" -> "{b}" [label="{safe}"];')
lines.append("}")
return "\n".join(lines)
