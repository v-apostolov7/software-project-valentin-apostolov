import numpy as np

class BB84Logic:
    @staticmethod
    def perform_sifting(alice_bases, bob_bases, alice_bits, bob_results):
        """Сравнява базите и запазва само битовете, където те съвпадат."""
        matches = (alice_bases == bob_bases)
        alice_key = alice_bits[matches]
        bob_key = bob_results[matches]
        return alice_key, bob_key, matches

    @staticmethod
    def calculate_qber(alice_key, bob_key):
        """Изчислява процента на грешните битове (Quantum Bit Error Rate)."""
        if len(alice_key) == 0:
            return 0.0
        errors = np.sum(alice_key != bob_key)
        return (errors / len(alice_key)) * 100