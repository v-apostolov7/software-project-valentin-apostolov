import streamlit as st
import pandas as pd
from actors import Alice, Bob, Eve
from protocol import BB84Logic
import visualization as vis

# Настройка на страницата
st.set_page_config(page_title="Quantum BB84 Simulator", layout="wide", page_icon="🔐")

# Стилизиране
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔐 BB84 Quantum Key Distribution Simulator")
st.markdown("---")

# Sidebar за контрол
st.sidebar.header("🛠️ Simulation Control")
n_bits = st.sidebar.slider("Number of Photons", 20, 1000, 200)
eavesdrop = st.sidebar.checkbox("Activate Eavesdropper (Eve)")
run_sim = st.sidebar.button("Execute BB84 Protocol")

if run_sim:
    # Инициализация на участниците
    alice = Alice(n_bits)
    bob = Bob(n_bits)

    # 1. Генериране на фотони
    photons = alice.generate_photons()

    # 2. Интервенция на Ева (ако е активна)
    if eavesdrop:
        eve = Eve(n_bits)
        photons = eve.intercept(photons)

    # 3. Боб измерва
    bob_results = bob.measure(photons)

    # 4. Пресяване (Sifting)
    alice_key, bob_key, matches = BB84Logic.perform_sifting(
        alice.bases, bob.bases, alice.bits, bob_results
    )

    # 5. Анализ
    qber = BB84Logic.calculate_qber(alice_key, bob_key)
    is_secure = qber < 11.0

    # Визуализация на резултатите в Dashboard
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Photons Sent", n_bits)
    c2.metric("Sifted Key Length", len(alice_key))
    c3.metric("QBER", f"{qber:.1f}%")
    c4.metric("Security", "PASS" if is_secure else "FAIL", delta_color="inverse")

    st.markdown("### 📊 Statistical Analysis")
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.pyplot(vis.plot_basis_heatmap(alice.bases, bob.bases))
        st.caption("Heatmap showing overlap between Alice's preparation bases and Bob's measurement bases.")

    with col_right:
        st.pyplot(vis.plot_qber_gauge(qber))

    if not is_secure:
        st.error("🚨 SECURITY ALERT: Eavesdropping detected! QBER is above 11%. Key discarded.")
    else:
        st.success("✅ Secure key exchange successful. No significant noise or interception detected.")

    # Детайлна таблица с данни (т. 2A)
    with st.expander("🔍 View Raw Protocol Data"):
        raw_df = pd.DataFrame({
            "Alice Bits": alice.bits[:20],
            "Alice Bases": alice.bases[:20],
            "Bob Bases": bob.bases[:20],
            "Bob Results": bob_results[:20],
            "Match": matches[:20]
        })
        st.table(raw_df)
        st.info("Note: Basis 0 = Rectilinear (+), Basis 1 = Diagonal (x)")

else:
    st.info("Adjust the settings in the sidebar and click 'Execute' to start the quantum simulation.")