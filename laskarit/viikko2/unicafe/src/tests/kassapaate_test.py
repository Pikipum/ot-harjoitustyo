import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_rahamaara_ja_myydyt_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)


    def test_kateisosto_toimii_edullisilla(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.edulliset, 1)


    def test_kateisosto_toimii_maukkailla(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.maukkaat, 1)


    def test_rahat_annetaan_takaisin_jos_ei_riita_edulliset(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(210), 210)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_rahat_annetaan_takaisin_jos_ei_riita_maukkaat(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(210), 210)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_toimii_edullisilla_jos_rahaa(self):
        maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(maksukortti.saldo, 260)

    def test_korttiosto_ei_onnistu_edullisilla_jos__ei_rahaa(self):
        maksukortti = Maksukortti(50)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(maksukortti), False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksukortti.saldo, 50)

    def test_korttiosto_toimii_maukkailla_jos_rahaa(self):
        maksukortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(maksukortti.saldo, 100)

    def test_korttiosto_ei_onnistu_maukkailla_jos__ei_rahaa(self):
        maksukortti = Maksukortti(50)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(maksukortti), False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo, 50)


    def test_kortin_lataus_toimii(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(maksukortti.saldo, 100)

    def test_kassan_saldo_ei_muutu_ostettaessa_kortilla(self):
        maksukortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -100)
        self.assertEqual(maksukortti.saldo, 0)