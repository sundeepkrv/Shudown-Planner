import streamlit as st

def render_header(title,subtitle=None):
	st.markdown(f"""<h3>{title}</h3>""",unsafe_allow_html=True,text_alignment="center")
	if subtitle:
		st.caption(subtitle,text_alignment="center")
	st.markdown("<hr style='margin: 1px 0px;'/>",unsafe_allow_html=True,text_alignment="center")