import streamlit as st
from streamlit_calendar import (calendar)
from components.header import (render_header)
from services.calendar_service import (CalendarService)

def show():
	render_header("🗓️ Shutdown Calendar","Calendar View of Shutdown Events")
	st.html("""<style>iframe[title="streamlit_calendar.calendar"] {height:500px!important;}</style>""")
	calendar_css = """.fc{height:500px!important;font-size:12px!important;}.fc-scroller{overflow:none;}"""
	events = (CalendarService.get_calendar_events())
	calendar(events=events,options={"initialView":"dayGridMonth","handleWindowResize":True},custom_css=calendar_css,key="max_height_calendar")