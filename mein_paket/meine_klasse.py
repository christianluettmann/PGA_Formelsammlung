class MeineKlasse:

    def __init__(self):

        # public: innerhalb der Klasse und von außen les- und schreibbar
        self.instanz_attribut = 42
        pass

    def set_attribut(self, p_attribut):
        """Setter
        Setzt in der Regel ein privates Attribut.
        :param p_attribut:
        :return:
        """
        self.instanz_attribut = p_attribut

    def get_attribut(self):
        """Getter
        Holt in der Regel ein privates Attribut.
        :return:
        """
        return self.instanz_attribut

    @staticmethod
    def statische_methode(p_wert):
        """

        :param p_wert:
        :return:
        """
        return p_wert*2



if __name__ == "__main__":

    mk = MeineKlasse()
    print(mk.instanz_attribut)

    print(MeineKlasse.statische_methode(67))
