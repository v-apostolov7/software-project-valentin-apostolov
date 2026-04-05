import numpy as np
from quantum_core import QuantumChannel


class Alice:
    def __init__(self, n_bits):
        self.n_bits = n_bits
        self.bits = np.random.randint(2, size=n_bits)
        self.bases = np.random.randint(2, size=n_bits)

    def generate_photons(self):
        return [QuantumChannel.prepare_qubit(b, s) for b, s in zip(self.bits, self.bases)]


class Bob:
    def __init__(self, n_bits):
        self.bases = np.random.randint(2, size=n_bits)

    def measure(self, photons):
        return np.array([QuantumChannel.measure_qubit(p, b) for p, b in zip(photons, self.bases)])


class Eve:
    """Подслушвач, който прилага стратегия 'Measure-and-Resend'."""

    def __init__(self, n_bits):
        self.bases = np.random.randint(2, size=n_bits)

    def intercept(self, photons):
        intercepted_photons = []
        for p, b in zip(photons, self.bases):
            # Ева измерва фотона в случайна база
            measured_bit = QuantumChannel.measure_qubit(p, b)
            # Изпраща нов фотон към Боб в същата база, в която е мерила
            intercepted_photons.append(QuantumChannel.prepare_qubit(measured_bit, b))
        return intercepted_photons