import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_basis_heatmap(alice_bases, bob_bases, limit=40):
    """Генерира Heatmap за сравнение на базите (Изискване 2B)."""
    data = [alice_bases[:limit], bob_bases[:limit]]
    fig, ax = plt.subplots(figsize=(12, 3))
    sns.heatmap(data, annot=False, cmap="YlGnBu", cbar=False,
                yticklabels=["Alice Basis (+/x)", "Bob Basis (+/x)"], ax=ax)
    plt.title(f"Correlation Heatmap of Quantum Bases (First {limit} bits)")
    return fig

def plot_qber_gauge(qber):
    """Визуализира нивото на грешка спрямо критичния праг."""
    fig, ax = plt.subplots(figsize=(6, 4))
    color = 'red' if qber > 11 else 'green'
    ax.bar(['QBER (%)'], [qber], color=color, alpha=0.7)
    ax.axhline(y=11, color='black', linestyle='--', label='Security Threshold (11%)')
    ax.set_ylim(0, 50)
    ax.set_ylabel("Error Rate %")
    ax.legend()
    plt.title("Security Analysis")
    return fig