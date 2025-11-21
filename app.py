import os
import streamlit as st
import numpy as np

from power import get_stat_power, make_power_figure


def main():
    st.set_page_config(page_title="power explorer", layout="wide")

    st.title("График мощности биномиального критерия при H₁: $μ₁ > μ₀$")

    with st.sidebar:
        st.header("Параметры")

        p0 = st.slider("μ₀ (H₀)", 0.0, 1.0, 0.5, 0.01)
        p1 = st.slider("μ₁ (H₁)", 0.0, 1.0, 0.6, 0.01)
        alpha = st.slider("α (уровень значимости)", 0.001, 0.2, 0.05, 0.001)
        target_power = st.slider("Целевая мощность", 0.1, 0.99, 0.8, 0.01)
        n_max = st.number_input("Размер выборки N",  2, 20000, 500, step=30)
    n_grid = np.arange(0, n_max + 1, 10)
    power = get_stat_power(n_grid, p0, p1, alpha)

    fig, min_n = make_power_figure(n_grid, power, target_power)

    st.plotly_chart(fig, use_container_width=True)

    if min_n is not None:
        st.markdown(f"Минимальный $N$, при котором мощность >= {target_power:.2f}: **{min_n}**")
    else:
        st.markdown(f"При размере выборки $N$ = {n_max} целевая мощность >= {target_power:.2f} не достигается.")

    with st.container():
        st.divider()  
        st.markdown("### Контекст задачи \n (взята из открытой методички Академии Аналитиков Авито)")

        # для удобства вынес текст самой задачи в отдельный файл
        base_dir = os.path.dirname(os.path.abspath(__file__))
        md_path = os.path.join(base_dir, "content", "task.md")

        with open(md_path, "r", encoding="utf-8") as f:
            task_text = f.read()
        
        st.markdown(task_text)

if __name__ == "__main__":
    main()
