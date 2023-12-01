class Otel:
    def __init__(self, otelID, adi, yildiz):
        self.otelID = otelID
        self.adi = adi
        self.yildiz = yildiz
        self.odalar = []
        self.calisanlar = []

    def otel_bilgisi_al(self):
        return f"{self.adi} Otel (ID: {self.otelID}) - {self.yildiz} Yıldızlı"

    def oda_ekle(self, oda):
        self.odalar.append(oda)

    def calisan_ekle(self, calisan):
        self.calisanlar.append(calisan)

class LuxuryOtel(Otel):
    def __init__(self, otelID, adi, yildiz, ozel_hizmet):
        super().__init__(otelID, adi, yildiz)
        self.ozel_hizmet = ozel_hizmet

    def ozel_hizmet_sagla(self):
        print(f"{self.adi} Otel, özel hizmet sunuyor: {self.ozel_hizmet}")

class Oda:
    def __init__(self, odaID, tip, kapasite, fiyat):
        self.odaID = odaID
        self.tip = tip
        self.kapasite = kapasite
        self.fiyat = fiyat
        self.musteri = None

    def oda_bilgisi_al(self):
        return f"{self.tip} Tipi Oda (ID: {self.odaID}) - Fiyat: {self.fiyat} TL"

    def musteri_rezerve_et(self, musteri):
        self.musteri = musteri

    def musteri_cikis_yap(self):
        self.musteri = None

class Calisan:
    def __init__(self, calisanID, isim, pozisyon, maas):
        self.calisanID = calisanID
        self.isim = isim
        self.pozisyon = pozisyon
        self.maas = maas

    def maas_artir(self, miktar):
        self.maas += miktar

class Musteri:
    def __init__(self, musteriID, adi, soyadi, telefon):
        self.musteriID = musteriID
        self.adi = adi
        self.soyadi = soyadi
        self.telefon = telefon

# Kullanım örneği
otel = LuxuryOtel(1, "Lüks Otel", 5, "Özel Spa Hizmeti")

calisan1 = Calisan(1001, "Ahmet", "Resepsiyonist", 3000)
calisan2 = Calisan(1002, "Ayşe", "Temizlik Görevlisi", 2500)

oda1 = Oda(201, "Standart", 2, 200)
oda2 = Oda(202, "Suit", 4, 400)

musteri1 = Musteri(3001, "Ali", "Veli", "555-1234")
musteri2 = Musteri(3002, "Mehmet", "Can", "555-5678")

oda1.musteri_rezerve_et(musteri1)
oda2.musteri_rezerve_et(musteri2)

otel.calisan_ekle(calisan1)
otel.calisan_ekle(calisan2)
otel.oda_ekle(oda1)
otel.oda_ekle(oda2)

# Bilgileri görüntüle
print(otel.otel_bilgisi_al())
for oda in otel.odalar:
    print(f" - {oda.oda_bilgisi_al()}")
    if oda.musteri:
        print(f"   * Rezerve Edilen Müşteri: {oda.musteri.adi} {oda.musteri.soyadi}")
    else:
        print("   * Oda Boş")

print("\nÇalışanlar:")
for calisan in otel.calisanlar:
    print(f" - {calisan.isim} ({calisan.pozisyon})")

# Lüks otel özel hizmeti
otel.ozel_hizmet_sagla()
