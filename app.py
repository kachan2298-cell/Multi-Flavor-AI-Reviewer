import streamlit as st
import time

# Налаштування сторінки в стилі Sigma
st.set_page_config(page_title="Sigma Multi-Flavor AI Reviewer", layout="wide")

# CSS для брендингу
st.markdown("""
    <style>
    .stApp { background-color: #f4f7f9; }
    .report-card { 
        background: white; 
        padding: 25px; 
        border-radius: 15px; 
        border-left: 8px solid #0052cc; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }
    .sigma-logo { font-size: 24px; font-weight: bold; color: #0052cc; margin-bottom: 20px; }
    .risk-table { font-family: monospace; background: #2d2d2d; color: #61afef; padding: 15px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Сценарії Pull Request (Приклади коду)
SCENARIOS = {
    "PR #124: Auth Security (Python)": """@pytest.fixture
def ecp_settings(settings):
    settings.ECP_AUTH = {
        'CERT_VALIDATION_ENABLED': False,
        'AUTO_CREATE_USER': True,
    }""",
    "PR #125: UI Logic (React)": "useEffect(() => { fetchData(); }, [Math.random()])",
    "PR #126: Data Query (SQL)": "query = f'SELECT * FROM users WHERE id = {user_id}'"
}

# --- SIDEBAR ---
st.sidebar.markdown("<div class='sigma-logo'>Sigma AI Engine</div>", unsafe_allow_html=True)
st.sidebar.write("---")

selected_pr = st.sidebar.selectbox("📂 Select Pull Request", list(SCENARIOS.keys()), key="pr_selector_unique")
persona = st.sidebar.radio("👤 Review Persona", ["🔍 Auditor", "🎓 Mentor", "🔴 Blunt Lead"])

st.sidebar.write("---")
st.sidebar.info("Team: **Kachan** 🥬 | Ideathon 2026")

# --- MAIN UI ---
st.title("🤖 Sigma Multi-Flavor AI Reviewer")
st.write("Adaptive code review for Enterprise standards.")

code_input = st.text_area("Code to analyze:", value=SCENARIOS[selected_pr], height=200)

if st.button("🚀 Run Adaptive Review", use_container_width=True):
    # Симуляція "розумної" роботи
    with st.status("Analyzing code complexity...") as status:
        st.write("🔍 Detecting tech stack (Python/Django detected)...")
        time.sleep(1.2)
        st.write(f"⚙️ Applying **{persona}** persona rules...")
        time.sleep(1.5)
        st.write("🧠 Running security & performance heuristics...")
        time.sleep(1.8)
        status.update(label="Analysis Complete!", state="complete")

    # Вставка контенту на основі рев'ю Насті
    if "Auditor" in persona:
        res_content = """
### 🛡 RISK SCORE CARD
<div class='risk-table'>
┌────────────────────────────────────────────────────────┐<br>
│ Overall Risk Score:   4.5 / 10  (10 = Critical)        │<br>
├───────────────────────┬────────────────────────────────┤<br>
│ Security:       5     │ Performance:   3               │<br>
│ Architecture:   6     │ Scalability:   2               │<br>
├───────────────────────┴────────────────────────────────┤<br>
│ Critical findings:  1 │ Warnings:     5                │<br>
│ Info findings:      4 │ <b>Estimated fix time: 2h 30m</b>     │<br>
└────────────────────────────────────────────────────────┘
</div>

**CRITICAL:** `CERT_VALIDATION_ENABLED: False` detected. This bypasses SSL/TLS verification and opens the system to MITM attacks.
**Standard:** OWASP A02:2021 / CWE-295
**Fix:** Isolate the dangerous flag: `assert os.getenv('DJANGO_ENV') != 'production'`
"""
    elif "Mentor" in persona:
        res_content = """
### 🎓 Mentor Observation
**DRY Violation (90% Duplication):** Identical fixture bodies for different algorithms.
### 💡 Why this matters
Duplicated code increases maintenance cost and risk of bugs when logic changes.
### 🔄 Before vs After
**Before:** Two separate functions for DSTU4145 and RSA.
**After:** `_make_ecp_settings(settings, algorithm)` — one factory to rule them all.
**Naming:** Rename `User()` to `user_model` as per PEP 8 standards.
"""
    else: # Blunt Lead
        res_content = """
### 🔴 DO NOT MERGE
**Seriously? Hardcoded 'False' for security?** My grandma codes more secure than this. 
Fix the certificate validation and DRY your tears (and your code) before even thinking about a PR. 
**Verdict:** BLOCK MERGE.
"""

    # Відображення картки рев'ю
    st.markdown(f"""
    <div class='report-card'>
        <div style='display: flex; justify-content: space-between;'>
            <h2 style='margin:0;'>{persona} Report</h2>
            <span style='background:#0052cc; color:white; padding:5px 15px; border-radius:10px;'>Sigma Certified</span>
        </div>
        <hr>
        {res_content}
    </div>
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.caption("Built for Sigma Software Ideathon. Context-aware AI code review prototype.")