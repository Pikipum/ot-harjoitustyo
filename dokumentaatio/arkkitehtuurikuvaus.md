# Arkkitehtuurikuvaus



## Rakenne

Ohjelman päätoimintojen rakenne on hajautettu neljään alueeseen:

### Käyttöliittymä ja päätoiminnot

Käyttöliittymä vastaa graafisesta käyttöliittymästä, sekä sovelluksen ohjaamisesta. Samalla se pyörittää sovelluksen looppia, jonka aikana pelaaja voi tehdä komentoja ja ohjata peliä.

### Shakkinappulat

Tämä osio vastaa shakkinappuloiden identiteetistä, kuvien lataamisesta, kuvan mitoista, sekä omasta sijainnistaan.

Kuvat ladataan nimen perusteella, ja ne sijaitsevat images/ kansiossa. 

### Liikkeiden tarkistus

Tämä luokka vastaa liikkeiden tarkistuksesta, eli siitä, onko pelaajan tekemä siirto sallitty. Jos on, luokka palauttaa True. Jos näin ei ole, luokka palauttaa False.

### Laudan alustaminen

Tähän luokkaan on talletettu tavallinen pelin aloitustilanne, joka luo uusia nappula-olioita oikeille paikoilleen, ja palauttaa listaolion, joka sisältää 8 listaa, joissa jokaisessa on 8 listaa. Tämä on pelin ruudukko, eli 8x8 jossa on 64 ruutua.

## Sovelluslogiikka

Sovellus toimii loopissa, kunnes peli suljetaan. Loopin aikana sovellus tarkkailee käyttäjän hiirellä tekemiä komentoja. Se katsoo missä kohtaa hiiri on, ja kun hiiren nappi painetaan pohjaan, käyttöliittymä tarkastaa, onko siinä kohdassa jokin siirrettävä nappula. Jos näin on, nappulan voi vetää haluttuun kohtaan. Tämän jälkeen ohjelma tarkastaa, onko siirto sallittu. Jos näin on, siirto tapahtuu, ja vuoro siirtyy toiselle osapuolelle. Valkoinen saa tehdä ensimmäisen siirron.

## Tiedostot

Peli sisältää images-kansion, jossa on kustomoidut ikonit jokaiselle pelinappulalle, sekä käyttöliittymän napeille.

## Heikkoudet

Kaikki säännöt eivät ole ohjelmoitu. Normaalisti shakkipeli loppuu siihen, kun kuninkaalla ei ole enää siirtoja. Tässä pelissä peli kuitenkin jatkuu ikuisesti.
