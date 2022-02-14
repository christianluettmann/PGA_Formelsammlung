from math import pi

rhodeg: float = 180.0 / pi
rhogon: float = 200.0 / pi


class Winkel:
    @staticmethod
    def rad2gon(p_rad: float) -> float:
        """Wandelt einen Winkel in Radiant in einen Winkel in Gon um.

        :param p_rad: Winkel in Radiant
        :type p_rad: float
        :return: Winkel in Gon
        :rtype: float
        """
        return p_rad * rhogon

    @staticmethod
    def rad2deg(p_rad: float) -> float:
        """Wandelt einen Winkel in Radiant in einen Winkel in Grad um.

        :param p_rad: Winkel in Radiant
        :type p_rad: float
        :return: Winkel in Grad
        :rtype: float
        """
        return p_rad * rhodeg

    @staticmethod
    def deg2rad(p_deg: float) -> float:
        """Wandelt einen Winkel in Grad in einen Winkel in Radiant um.

        :param p_deg: Winkel in Grad
        :type p_deg: float
        :return: Winkel in Radiant
        :rtype: float
        """
        return p_deg / rhodeg

    @staticmethod
    def deg2gon(p_deg: float) -> float:
        """Wandelt einen Winkel in Grad in einen Winkel in Gon um.

        :param p_deg: Winkel in Grad
        :type p_deg: float
        :return: Winkel in Gon
        :rtype: float
        """
        return p_deg / rhodeg * rhogon

    @staticmethod
    def gon2rad(p_gon: float) -> float:
        """Wandelt einen Winkel in Gon in einen Winkel in Radiant um.

        :param p_gon: Winkel in Gon
        :type p_gon: float
        :return: Winkel in Radiant
        :rtype: float
        """
        return p_gon / rhogon

    @staticmethod
    def gon2deg(p_gon: float) -> float:
        """Wandelt einen Winkel in Gon in einen Winkel in Grad um.

        :param p_gon: Winkel in Gon
        :type p_gon: float
        :return: Winkel in Grad
        :rtype: float
        """
        return p_gon / rhogon * rhodeg
