import streamlit as st
import time

st.set_page_config(page_title="Sigma AI Reviewer", layout="wide")

# Стилі Sigma
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .report-card { background: white; padding: 20px; border-radius: 12px; border: 1px solid #d1d5db; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
    .sigma-badge { background: #0052cc; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; margin-right: 5px; }
    </style>
    """, unsafe_allow_html=True)

# Сценарії (Моки)
SCENARIOS = {
    "PR #124: Update Login (Python)": "def login(user, pwd):\n    query = f\"SELECT * FROM users WHERE u='{user}' AND p='{pwd}'\"\n    return db.execute(query)",
    "PR #125: Dashboard (React)": "useEffect(() => {\n    fetchData();\n}, [Math.random()])",
    "PR #126: Database Fix (SQL)": "SELECT * FROM large_table JOIN other_table ON true"
}

# Сайдбар
st.sidebar.image("https://sigma.software/wp-content/themes/sigma/assets/img/logo.svg", width=150)
st.sidebar.title("Configuration")
selected_pr = st.sidebar.selectbox("Select Pull Request", list(SCENARIOS.keys()), key="pr_selector")
persona = st.sidebar.radio("Review Persona", ["🔍 Auditor", "🎓 Mentor", "👊 Blunt Lead"])

st.title("🤖 Sigma Multi-Flavor AI Reviewer")

# Основна зона
code_to_review = st.text_area("Code for analysis", value=SCENARIOS[selected_pr], height=200)

if st.button("🚀 Run Adaptive Review", use_container_width=True):
    with st.status("Sigma AI Engine active...") as status:
        st.write("🔍 **Phase 1:** Scanning code structure...")
        time.sleep(1.2) # Робимо паузу довшою
        
        st.write("📂 **Phase 2:** Detecting tech stack & context...")
        time.sleep(1.5)
        
        st.write(f"⚙️ **Phase 3:** Injecting {persona} persona rules...")
        time.sleep(1.2)
        
        st.write("🧠 **Phase 4:** Running heuristic security analysis...")
        time.sleep(1.8)
        
        status.update(label="✅ Analysis Complete. Generating Report...", state="complete")

    # Логіка виводу
    if "def" in code_to_review or "SELECT" in code_to_review:
        score, color = (4, "red") if "Auditor" in persona else (5, "orange")
        if "Auditor" in persona:
            res = "### 🛡 RISK SCORE CARD\n| Risk | Level |\n| :--- | :--- |\n| SQL Injection | HIGH |\n| Data Leak | MED |\n\n**Estimated fix time:** 45 mins"
        elif "Mentor" in persona:
            res = "### 🔍 Observation\nPotential SQL Injection.\n### 💡 Why it matters\nAttackers can bypass auth.\n### 🔄 Before-After\n`db.execute(q, params)`"
        else:
            res = "### 🔴 DO NOT MERGE\nSeriously? String interpolation in SQL? My grandma codes more secure than this. Fix it."
    else:
        score, color = (9, "green"), "### ✅ Looks Good\nCode is clean and follows standards."

    st.markdown(f"""
    <div class="report-card">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <h2>{persona} Review</h2>
            <div style="background: {color}; color: white; padding: 10px 20px; border-radius: 8px; font-size: 24px;">{score}/10</div>
        </div>
        <div style="margin-top: 10px;">
            <span class="sigma-badge">Security</span><span class="sigma-badge">Sigma Standard</span>
        </div>
        <hr>
        {res}
    </div>
    """, unsafe_allow_html=True)

st.sidebar.write("---")
st.sidebar.info("Team: Kachan' 🥬")