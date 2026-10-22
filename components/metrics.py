import streamlit as st

def render_metrics(metrics):
	"""
	metrics: [("Total",100),("Pending",20)]
	"""
	columns = st.columns(len(metrics))
	for idx, metric in enumerate(metrics):
		label = metric[0]
		value = metric[1]
		columns[idx].metric(label=label,value=value)