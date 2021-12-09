from math import *

rhodeg = 180.0 / pi
rhogon = 200.0 / pi


class Winkel:
    @staticmethod
    def rad2gon(p_rad):
        return p_rad * rhogon

    @staticmethod
    def rad2deg(p_rad):
        return p_rad * rhodeg

    @staticmethod
    def deg2rad(p_deg):
        return p_deg / rhodeg

    @staticmethod
    def deg2gon(p_deg):
        return p_deg / rhodeg * rhogon

    @staticmethod
    def gon2rad(p_gon):
        return p_gon / rhogon

    @staticmethod
    def gon2deg(p_gon):
        return p_gon / rhogon * rhodeg
