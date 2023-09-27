""" Quantum Mechanics 2020
"""
from scipy import constants as const
import math
import unittest


def collide(wi, theta):
	wc=const.h/(const.m_e*const.c)
	return wi+wc*(1-math.cos(theta))

def Lorentz(v):
	if const.c<v:
		return 0
	return 1/math.sqrt(1-v*v/(const.c*const.c))


class TestCompton(unittest.TestCase):

	def test_collide(self):
		wi=200e-12
		res = collide(wi, math.pi)
		wc=const.h/(const.m_e*const.c)
		ans = wi+2*wc
		self.assertEqual(ans, res)

	def test_Lorentz(self):
		res = gamma(0)
		self.assertEqual(1, res)


	def test_brogliewave(self):
		wi=200e-12
		wc=const.h/(const.m_e*const.c)
		print(f"{wc=}")
		wf=wi+2*wc
		print(f"{wf=}")
		dp=const.h*(1/wi+1/wf) # delta p (momentum)
		v=dp/const.m_e
		print(f"{v=}")
		v=v*const.c/math.sqrt(v*v+const.c*const.c)
		print(f"{v=}")
		v=const.h/const.m_e/100e-12
		#v=const.h/const.m_e*(1/200e-12+1/202.4e-12)
		print(f"{v=}")
		print()

		wi=wc
		wf=wi+2*wc
		print(f"{wf=}")
		dp=const.h*(1/wi+1/wf)
		print(f"{dp=}")
		v=dp/const.m_e
		print(f"{v=}")
		vc=v/const.c
		print(f"{vc=}")
		print()

		ev=1.602e-19
		e=const.e
		print(f"{e=}")
		print(f"{ev=}")
		print()
		we=const.h/math.sqrt(2*const.m_e*const.e)
		print(f"{we=}")
		wea=we/1e-10
		print(f"{wea=}")
		print()


		a0=(4*math.pi*const.epsilon_0*const.hbar*const.hbar)/(const.m_e*const.e*const.e)
		a0=a0/1e-12
		print(f"{a0=}")

		wcbar=const.hbar/(const.m_e*const.c)
		print(f"{wcbar=}")
		wcbar*=1e15
		print(f"{wcbar=} fm")
		r0=wcbar/137
		print(f"{r0=}")
		ev=1.602e-19
		r0=(ev/const.c)*(ev/const.c)/const.m_e
		r0=(ev*ev)/(const.c*const.c*const.m_e)
		print(f"{r0=}")
		r0*=1e15
		print(f"{r0=} fm")
		print()

		wc=const.h/(const.m_e*const.c)
		print(f"{wc=}")
		wc*=1e12
		print(f"{wc=}")
		print()

		ev=1.602e-19
		energy=1000e9*ev
		print(f"{energy=}")
		wcollider=const.h/math.sqrt(2*const.m_e*energy)
		print(f"{wcollider=}")
		wcollider*=1e15
		print(f"{wcollider=}")
		energy=7e12*ev
		wcollider=const.h/math.sqrt(2*const.m_e*energy)
		print(f"{wcollider=}")
		wcollider*=1e15
		print(f"{wcollider=}")
		print()

		delta=12.264259661581491
		w=delta/math.sqrt(1e12)*1e-10
		w*=1e15
		print(f"{w=}")

		ev=1.602e-19
		energy=1000e9*ev
		# print(f"{energy=}")
		# v=math.sqrt(2*energy/const.m_e)
		# print(f"{v=}")
		# beta=v/const.c
		# print(f"{beta=}")
		# gamma=1/math.sqrt(1-beta*beta)
		# print(f"{gamma=}")
		# wcollider=const.h/math.sqrt(2*const.m_e*energy)
		# wcollider/=gamma
		# print(f"{wcollider=}")
		# wcollider*=1e15
		# print(f"{wcollider=}")
		print()

		W=const.h*const.c/energy
		print(f"{w=} m")
		w=const.h*const.c/math.sqrt(energy*energy+2*energy*const.m_e*const.c*const.c)
		print(f"{w=} m")


if __name__ == '__main__':
	unittest.main(argv=['first-arg-is-ignored'], exit=False)
