import pytest
from Parametrizados import fatorial

@pytest.mark.parametrize("n, esperado", [
	(0, 1),
	(1, 1),
	(2, 2),
	(3, 6),
	(5, 120),
])
def test_fatorial_valores(n, esperado):
	assert fatorial(n) == esperado

@pytest.mark.parametrize("n", [-1, -2, -10])
def test_fatorial_negativo(n):
	with pytest.raises(RecursionError):
		fatorial(n)