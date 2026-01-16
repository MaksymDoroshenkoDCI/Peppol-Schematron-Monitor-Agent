import streamlit as st
import os
import sys

# Ensure the root directory is in sys.path to allow importing agents
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.graph import run_graph

st.set_page_config(page_title="Peppol Schematron Monitor", layout="wide")

st.title("🧩 Peppol Schematron Monitor Agent")

st.sidebar.header("Controls")
if st.sidebar.button("🚀 Run Monitoring Pipeline"):
    with st.spinner("Agents are working..."):
        try:
            result = run_graph()
            st.session_state['result'] = result
            st.success("Pipeline finished successfully!")
        except Exception as e:
            st.error(f"Pipeline failed: {e}")

if 'result' in st.session_state:
    result = st.session_state['result']
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Schematron Changes")
        st.info(f"Versions: {result.get('previous_version')} -> {result.get('latest_version')}")
        
        diffs = result.get('diff_results', [])
        if diffs:
            st.warning(f"Found {len(diffs)} changes.")
            for d in diffs:
                st.write(f"**{d['type']}**: {d['details']}")
        else:
            st.success("No Schematron changes detected.")

    with col2:
        st.subheader("🎯 Mapping Impact")
        impacts = result.get('impact_analysis', [])
        if impacts:
            st.error(f"Found {len(impacts)} affected mappings.")
            for impact in impacts:
                st.write(f"**{impact.get('severity', 'INFO')}** in `{impact.get('mapping_file')}`")
                st.write(f"- Field: `{impact.get('affected_field')}`")
                st.write(f"- Reason: {impact.get('reason')}")
        else:
            st.success("No safe mappings affected.")

    st.subheader("📝 Report")
    report_content = result.get('report_summary', 'No report generated.')
    st.text_area("Report Content", report_content, height=300)
    
    st.download_button(
        label="Download Report",
        data=report_content,
        file_name="schematron_report.md",
        mime="text/markdown"
    )

st.sidebar.markdown("---")
st.sidebar.info("This is a PoC for the Agentic Peppol Monitor.")
