
from __future__ import annotations

import streamlit as st

from lib.config import APP_TITLE, APP_ICON

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🎭 Monkey Baa Impact Analytics")
st.caption("KPI + OKR + Theory of Change dashboard prototype built on your workbook.")

left, right = st.columns([1.3, 1])

with left:
    st.markdown(
        """
        ### What this app is designed to show
        - **Dashboard:** headline KPIs, show-level comparisons, child and parent signals
        - **Theory of Change & OKRs:** progress against impact objectives, not just outputs
        - **AI Insights:** prompt-style natural language summaries
        - **Data Quality:** evidence that the analysis is grounded in real cleaned tables

        ### Why this structure works for Monkey Baa
        Monkey Baa already tracks indicators through its outcomes framework, so this app separates:
        - **KPI reporting** = what happened
        - **OKR tracking** = what change the organisation is trying to create
        - **Theory of Change** = why those indicators matter
        """
    )

with right:
    st.info(
        """
        **Suggested page order for demo**
        1. Dashboard  
        2. Theory of Change & OKRs  
        3. AI Insights  
        4. Data Quality
        """
    )
    st.success("Use the sidebar to open each page.")
