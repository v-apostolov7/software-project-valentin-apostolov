# software-project-valentin-apostolov
# 🔐 BB84 Quantum Key Distribution Simulator

An interactive, modular Python-based simulator of the **BB84 Quantum Key Distribution (QKD)** protocol. Developed as a semester project for the **Technical University of Sofia**.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://software-project-valentin-apostolov.streamlit.app/)

## 🚀 Live Demo
You can access the live simulation here: 
👉 **[software-project-valentin-apostolov.streamlit.app](https://software-project-valentin-apostolov.streamlit.app/)**

---

## 📋 Project Overview
This software simulates the fundamental principles of quantum cryptography. It allows users to visualize how quantum mechanics (specifically the Heisenberg Uncertainty Principle) ensures secure communication between two parties (**Alice** and **Bob**) and detects any potential eavesdropping by a third party (**Eve**).

### Key Features:
* **Modular Architecture:** Object-Oriented Programming (OOP) design for scalability and clarity.
* **Interactive Simulation:** Adjust the number of photons and toggle eavesdropping in real-time.
* **Statistical Analysis:** * **Basis Correlation Heatmap:** Visualizes the overlap between preparation and measurement bases.
    * **QBER Analysis:** Calculates the Quantum Bit Error Rate to determine channel security.
* **Automatic Detection:** Secure key generation is only successful if QBER remains below the **11%** threshold.

---

## 🛠️ Technological Framework
* **Language:** Python 3.9+
* **Frontend:** [Streamlit](https://streamlit.io/)
* **Logic & Math:** NumPy, Pandas
* **Visualization:** Matplotlib, Seaborn

---

## 📂 Project Structure
* `app.py` - Main entry point and Streamlit UI configuration.
* `actors.py` - Logic for Alice, Bob, and Eve (Measure-and-Resend strategy).
* `quantum_core.py` - Simulation of qubit preparation and measurement.
* `protocol.py` - BB84 specific logic: Sifting and Error estimation.
* `visualization.py` - Functions for generating heatmaps and QBER charts.
* `requirements.txt` - Dependency list for deployment.

---

## 📥 Installation & Local Run
To run this project on your local machine:

1. **Clone the repository:**
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
2. **Install dependencies:**
   pip install -r requirements.txt
3. **Launch the app:**
   streamlit run app.py
