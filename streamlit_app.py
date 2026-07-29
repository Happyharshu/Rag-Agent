"""
streamlit_app.py
────────────────
Root-level entry point for Streamlit Community Cloud.
Streamlit Cloud expects the app file at the repository root by default.
This simply re-exports the app defined in app/main.py.
"""
# Re-run the main Streamlit app
import runpy
runpy.run_module("app.main", run_name="__main__", alter_sys=True)
