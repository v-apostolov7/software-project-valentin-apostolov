import numpy as np


class QuantumChannel:
    """Симулира предаването на квантова информация през канал."""

    @staticmethod
    def prepare_qubit(bit, basis):
        """Превръща бит и база в квантово състояние (репрезентирано като речник)."""
        # Basis 0: Rectilinear (+), Basis 1: Diagonal (x)
        return {"bit": bit, "basis": basis}

    @staticmethod
    def measure_qubit(qubit, measure_basis):
        """Симулира измерване на кубит. Ако базите не съвпадат, се въвежда неопределеност."""
        if qubit["basis"] == measure_basis:
            return qubit["bit"]
        else:
            # Принцип на Хайзенберг: измерване в грешна база дава случаен резултат
            return np.random.randint(2)