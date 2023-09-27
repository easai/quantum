"""Calculate Compton wave length.

Usage: compton.py [--test|-t] [--help|-h]

Options:
    -h, --help  show this help message and exit
    -t, --test  perform unit test
"""
from scipy import constants as const
import unittest
from docopt import docopt


def compton(m):
	''' return Compton wavelength in m.
		argument m in in kg.

	lambda*nu=c
	e=mc*c
	e=h*nu=h*c/lambda
	'''
	return const.h / (m * const.c)


def compton_MeV(energy):
	'''return Compton wavelength in m.
		argument m is in MeV.

	energy=h*nu=h*c/lambda
	lambda=h*c/e=2*pi*(hbar*c)/energy
	'''
	p = const.physical_constants['reduced Planck constant times c in MeV fm']
	wavelength = 2 * const.pi * p[0] / energy
	wavelength /= 1e15
	return wavelength


class TestCompton(unittest.TestCase):

	def test_compton(self):
		print(f"{const.m_e=}")
		wavelength_e = compton(const.m_e)
		print(f"{wavelength_e=}")
		mev = const.physical_constants['electron mass energy equivalent in MeV']
		wavelength_e = compton_MeV(mev[0])
		print(f"{wavelength_e=}")
		print()
		# self.assertEqual()
		print(f"{const.m_p=}")
		wavelength_p = compton(const.m_p)
		print(f"{wavelength_p=}")
		wavelength_p = compton_MeV(937)
		print(f"{wavelength_p=}")
		print()

		lp = .8e-15
		print(f"{lp=}")
		ratio = wavelength_p / lp
		print(f"{ratio=}")


if __name__ == '__main__':
	args = docopt(__doc__, argv='--help')
	if args["--test"] or args["-t"]:
 		unittest.main(argv=['first-arg-is-ignored'], exit=False)
