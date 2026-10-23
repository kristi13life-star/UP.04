import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Электронный журнал - Аналитика", layout="wide")
st.title("📚 Электронный журнал - Панель завуча")

with st.sidebar:
    st.header("⚙️ Фильтры")
    days = st.selectbox("Период (дней)", [7, 30, 90, 365], index=1)

try:
    # KPI
    kpi = requests.get(f"{API_URL}/api/reports/kpi/", params={"days": days}).json()
    c1, c2, c3 = st.columns(3)
    c1.metric("📊 Средний балл", kpi.get("avg_grade", 0))
    c2.metric("📝 Всего оценок", kpi.get("total_grades", 0))
    c3.metric("👨‍🎓 Студентов", kpi.get("students_count", 0))

    # Топ студентов
    st.header("🏆 Топ-5 студентов")
    top = requests.get(f"{API_URL}/api/reports/top-students/").json()
    if top:
        st.table(top)

    # Статистика по предметам
    st.header("📈 Успеваемость по предметам")
    stats = requests.get(f"{API_URL}/api/reports/subject-stats/").json()
    if stats:
        st.table(stats)

except Exception as e:
    st.error(f"Ошибка подключения к API: {e}")
    st.info("Убедитесь, что Django-сервер запущен: python manage.py runserver")