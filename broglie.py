"""Calculate Broglie wave length.

Usage: broglie.py [--test|-t] [--help|-h]

Options:
    -h, --help  show this help message and exit
    -t, --test  perform unit test
"""
from scipy import constants as const

import math
import unittest
from docopt import docopt


def broglie(p):
	""" take p in kg*m/s and return de Broglie wavelength in m.
	"""
	# h = 6.63e-34
	w = const.h / p
	print(f"{w=} m")
	print(f"{w*1e9=} nm")
	print(f"{w*1e15=} fm")
	return w


def inV(ev):
	evj = 1.602176634e-19
	J_per_eV = const.physical_constants['electron volt-joule relationship']
	eV_per_J = const.physical_constants['joule-electron volt relationship']
	return ev*J_per_ev[0]


class TestBroglie(unittest.TestCase):

	def test_compton(self):
		p = 9.109e-31 * 6.0e6
		w = broglie(p)

		p = 2000 * 22.4  # kg*m/s
		w = broglie(p)

		p = 10e-3 * .1
		w = broglie(p)

		t = 300
		kb = 1.38e-23
		ke = 3 / 2 * kb * t
		m = 1e-18  # kg
		v = math.sqrt(2 * ke / m)
		p = m * v
		p = math.sqrt(2 * ke * m)
		w = broglie(p)

		t = 100e-6
		kb = 1.38e-23
		ke = 3 / 2 * kb * t
		m = 87 * 1.660e-27  # kg
		m = 87 / const.Avogadro * 1e-3
		v = math.sqrt(2 * ke / m)
		p = m * v
		p = math.sqrt(2 * ke * m)
		w = broglie(p)

		ej = const.h * const.c / 400e-9
		f = const.c / 400e-9
		print(f"{ej=}")
		print(f"{f=}")
		evj = 1.602176634e-19
		J_per_eV = const.physical_constants['electron volt-joule relationship']
		eV_per_J = const.physical_constants['joule-electron volt relationship']
		ev = ej * eV_per_J[0]
		unit = eV_per_J[1]
		print(f"{unit=}")
		print(f"{ev=}")
		ev = 193 * 2 * math.pi / 400
		print(f"{ev=}")
		print()

		ej = const.h * const.c / 700e-9
		f = const.c / 700e-9
		print(f"{f=}")
		# evj=1.602176634e-19
		ev = ej / evj
		print(f"{ev=}")

		print()
		n = 300 / (const.h * 2.5e9)
		print(f"{n=}")

		deltaE = 4.2 * 10 * 200
		t = deltaE / 300
		print(f"{t=}")
		totalN = n * t
		print(f"{totalN=}")


if __name__ == '__main__':
	args = docopt(__doc__, argv='--help')
	if args["--test"] or args["-t"]:
 		unittest.main(argv=['first-arg-is-ignored'], exit=False)
