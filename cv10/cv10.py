

class Zvire(object):

    def __init__(self,jmeno = "",druh = "",hmotnost =0):
        self._jmeno = jmeno
        self._druh = druh
        self._hmotnost = hmotnost

    @property
    def jmeno(self):
        return self._jmeno

    @jmeno.setter
    def jmeno(self,ajmeno):
        self._jmeno = ajmeno

    @property
    def druh(self):
        return self._druh

    @druh.setter
    def druh(self,adruh):
        self._druh = adruh

    @property
    def hmotnost(self):
        return self._hmotnost

    @hmotnost.setter
    def hmotnost(self,ahm):
        self._hmotnost = ahm

    def __str__(self):
        return "Zvire {} druhu {} a hmotnosti {} kg".format(
            self.jmeno,self.druh,self.hmotnost
        )


k = Zvire()
k.jmeno = "Mikeš"
k.druh = "kočka"
k.hmotnost = 3

l = Zvire(jmeno = "Alík", hmotnost=5)

print(k)
print(type(k))

print(l)
print(type(l))
