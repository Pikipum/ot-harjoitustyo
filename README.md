# PyChat

Tämän sovelluksen avulla voit liittyä chat-huoneeseen ja viestitellä muiden henkilöiden kanssa. Sovellus tukee useita käyttäjiä, joilla kaikilla on oma käyttäjänimi ja salasana. Käyttjät voivat lähettää viestejä chathuoneeseen, johon ne tallentuvat muiden käyttäjien luettavaksi.

## Python versio

Sovellus on testattu toimivaksi Python 3.8 ja 3.10 -versiolla.

## Dokumentaatio

[vaatimusmaarittely.md](https://github.com/Pikipum/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[arkkitehtuuri.md](https://github.com/Pikipum/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[tyokirjanpito.md](https://github.com/Pikipum/ot-harjoitustyo/blob/master/dokumentaatio/tyokirjanpito.md)

[changelog.md](https://github.com/Pikipum/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

Voit asentaa sovelluksen vaatimat moduulit poetryllä seuraavasti:

1. Asenna tarvittavat moduulit (kuten pylint) kirjoittamalla terminaaliin:

```bash
poetry install
```

2. Siirry halutessasi virtuaaliympäristöön:

```bash
poetry shell
```

3. Sovelluksen voi suorittaa invoken avulla (ei toimi WSL):

```bash
poetry run invoke start
```

Sovellukselle on myös määritelty invoken avulla testejä. 

Testikattavuus:

```bash
poetry run invoke coverage-report
```
Koodin laatu Pylintin avulla:

```bash
poetry run invoke lint
```

