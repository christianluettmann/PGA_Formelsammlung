"""Klasse Punkt

"""


class Punkt:
    """Klasse Punkt

    :todo: Brauchen wir für den EPSG-Code auch einen Setter? Oder ist bei der Änderung zwangweise eine Transformation notwendig?

    """
    def __init__(self, p_y: float = 0.0, p_x: float = 0.0, p_nr: str = "", p_epsg: int = 0):
        """

        :param p_y: y- bzw. Rechtswert
        :type p_y: float
        :param p_x: x- bzw. Hochwert
        :type p_x:float
        :param p_nr: Punktnummer
        :type p_nr: str
        :param p_epsg: ESPG-Code
        :type p_epsg: int
        """
        self.__y: float = p_y
        self.__x: float = p_x
        self.__nr: str = p_nr
        self.__epsg: int = p_epsg

    def setze_y(self, p_y: float):
        """Setter für y

        :param p_y: y- bzw. Rechtswert
        :type p_y: float
        :return:
        """
        self.__y = p_y

    def setze_x(self, p_x: float):
        """Setter für x

        :param p_x: x- bzw. Hochwert
        :type p_x: float
        :return:
        """
        self.__x = p_x

    def setze_nr(self, p_nr: str):
        """Setter für nr

        :param p_nr: alphanumerische Punktnummer
        :type p_nr: str
        :return:
        """
        self.__nr = p_nr

    def hole_y(self) -> float:
        """Getter für y


        :return: y bzw. Rechtswert
        :rtype p_y: float
        """
        return self.__y

    def hole_x(self) -> float:
        """Getter für x

        :return: x bzw. Hochwert
        :rtype p_x: float
        """
        return self.__x

    def hole_nr(self) -> str:
        """Getter für nr

        :return: alphanumerische Punktnummer
        :rtype p_nr: str
        """
        return self.__nr

    def hole_epsg(self) -> int:
        """

        :return: EPSG-Code
        :type: int
        """
        return self.__epsg

    def __str__(self):
        zeichenkette: str = 'nr:' + self.__nr + ' y=' + str(self.__y) + ' x=' + str(self.__x) + ' EPSG:' + str(
            self.__epsg)
        return zeichenkette

    def hole_json(self):
        return self.__dict__

    def setze_json(self, p_dict):
        # Iteration über alle Elemente im Dictionary
        for schluessel, wert in p_dict.items():
            print(schluessel + ":" + str(wert))
            setattr(self, schluessel, wert)


if __name__ == "__main__":

    p1 = Punkt(42.6, 43.0, "P1", 25832)
    print(p1.hole_y())
    print(p1.hole_x())
    print(p1.hole_nr())
    print(p1)
