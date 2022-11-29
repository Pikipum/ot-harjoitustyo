# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat lähettää viestejä chat-huoneeseen, jossa viestit säilyvät luettavissa.

## Käyttäjät

Alkuvaiheessa sovelluksella on ainoastaan tavallisia chattikäyttäjiä, jotka voivat kirjoittaa viestejä. Myöhemmin sovellukseen saatetaan myös lisätä esimerkiksi moderaattorikäyttäjiä, jotka voivat myös poistaa viestejä.

## Käyttöliittymäluonnos

Sovellus koostuu aluksi kahdesta eri näkymästä.

Ensimmäinen näkymä on kirjautumisruutu, jossa käyttäjä voi kirjautua sisään tililleen käyttämällä tunnusta ja salasanaa.

Jos kirjautuminen onnistuu, käyttäjä pääsee chat-ikkunaan, jossa voi lukea vanhoja viestejä ja lähettää uusia.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

Kaksi kenttää ja kaksi nappia:

Kentät: Tunnus ja salasana
Napit: Kirjaudu ja Luo tunnus

Luo tunnus:
- Käyttäjätunnuksen luominen ja salasanan valitseminen

tai

- Käyttäjä voi kirjautua järjestelmään
    - Jos tunnus ja salasana löytyy tietokannasta, käyttäjä pääsee chat-näkymään.

### Kirjautumisen jälkeen

- Käyttäjä voi lukea vanhoja viestejä joita on lähetetty.
- Ruudun alaosassa tyhjä kenttä, johon kirjottamalla ja painamalla enteriä viesti lähtee muille nähtäväksi.

## Jatkokehitysideoita

Perusversion jälkeen järjestelmää täydennetään ajan salliessa esim. seuraavilla toiminnallisuuksilla:

- Erilaiset kanavat, esim. aiheittain
- Käyttäjäoikeudet (viestien poisto, käyttäjien potkiminen)
- Multimediaviestit, esimerkiksi kuvien lähettäminen
- Sovelluksen kytkeminen verkkoon