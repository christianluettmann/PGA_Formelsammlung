"""Klasse Punkt"""


class Punkt:
    """Klasse Punkt

    TODO: Brauchen wir für den EPSG-Code auch einen Setter? (zwangsweise Transformation notwendig?)
    """
    def __init__(self, p_y: float = 0.0, p_x: float = 0.0, p_nr: str = "", p_epsg: int = 0):
        """

        :param p_y: y-Wert bzw. Rechtswert
        :type p_y: float
        :param p_x: x-Wert bzw. Hochwert
        :type p_x: float
        :param p_nr: Punktnummer (Text zulässig)
        :type p_nr: str
        :param p_epsg: EPSG-Code
        :type p_epsg: int
        """
        self.__y: float = p_y
        self.__x: float = p_x
        self.__nr: str = p_nr
        self.__epsg: int = p_epsg

    def setze_y(self, p_y: float):
        """Setter für y-Koordinate

        :param p_y: y-Wert bzw. Rechtswert
        :type p_y: float
        """
        self.__y = p_y

    def setze_x(self, p_x: float):
        """Setter für x-Koordinate

        :param p_x: x-Wert bzw. Hochwert
        :type p_x: float
        """
        self.__x = p_x

    def setze_nr(self, p_nr: str):
        """Setter für Punktnummer

        :param p_nr: alphanumerische Punktnummer
        :type p_nr: str
        """
        self.__nr = p_nr

    def hole_y(self) -> float:
        """Getter für y-Koordinate

        :return: y-Wert bzw. Rechtswert
        :rtype: float
        """
        return self.__y

    def hole_x(self) -> float:
        """Getter für x-Koordinate

        :return: x-Wert bzw. Hochwert
        :rtype: float
        """
        return self.__x

    def hole_nr(self) -> str:
        """Getter für Punktnummer

        :return: alphanumerische Punktnummer
        :rtype: str
        """
        return self.__nr

    def hole_epsg(self) -> int:
        """Getter für EPSG-Code

        :return: EPSG-Code
        :rtype: int
        """
        return self.__epsg

    def __str__(self) -> str:
        return f"nr:{self.__nr} y={self.__y} x={self.__x} EPSG: {self.__epsg}"

    def hole_json(self):
        return self.__dict__

    def setze_json(self, p_dict):
        for schluessel, wert in p_dict.items():
            setattr(self, schluessel, wert)



if __name__ == "__main__":
    p1 = Punkt(42.6, 43.0, "P1", 25832)
    print(p1)
