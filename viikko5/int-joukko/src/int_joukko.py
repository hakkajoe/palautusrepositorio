class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or self.OLETUSKASVATUS
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def _varmista_kapasiteetti(self):
        if self.alkioiden_lkm % len(self.ljono) == 0:
            uusi_koko = self.alkioiden_lkm + self.kasvatuskoko
            uusi_lista = self._luo_lista(uusi_koko)
            self._kopioi_lista(self.ljono, uusi_lista)
            self.ljono = uusi_lista

    def _kopioi_lista(self, lahde, kohde):
        for i in range(len(lahde)):
            kohde[i] = lahde[i]

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1
            self._varmista_kapasiteetti()
            return True
        return False

    def poista(self, n):
        if n in self.ljono[:self.alkioiden_lkm]:
            indeksi = self.ljono.index(n)
            self.ljono[indeksi] = 0
            self._siirra_vasemmalle(indeksi)
            self.alkioiden_lkm -= 1
            return True
        return False

    def _siirra_vasemmalle(self, indeksi):
        for i in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[i] = self.ljono[i + 1]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def _yhdiste_eroitus_leikkaus(a, b, operaatio):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            if operaatio(i in b_taulu):
                tulos.lisaa(i)

        return tulos

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in a_taulu:
            tulos.lisaa(i)

        for j in b_taulu:
            tulos.lisaa(j)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        return IntJoukko._yhdiste_eroitus_leikkaus(a, b, lambda x: x)

    @staticmethod
    def erotus(a, b):
        return IntJoukko._yhdiste_eroitus_leikkaus(a, b, lambda x: not x)

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
