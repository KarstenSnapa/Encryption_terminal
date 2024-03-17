# Encryption_terminal
Hva er alle filene?

Encrypt.py er min hovedfil, det er her jeg har prøvd å lage en kode som kan enkrypte meldinger som bruker en private key til å gjøre alle individuelle bokstaver til unike tall du ikke vil kunne vite hva er uten å ha private keyen.

Problemet med dette er at hvis du gir ut private keyen og meldingen til brukeren er det ganske lett å knekke koden, men hvis noen som ikke har koden prøver å lese meldingen vil de aldri forstå den.


Decrypt.py er skriptet som skal la brukeren dekryptere koden, grunnen til at jeg har valgt å bruke to forskjellige filer til dette er for at det er lettere å vise at enkrypteringen og dekrypteringen faktisk funker og at ikke jeg jukser ved å lagre meldingen som en variabel og bare printe den ut senere.

problemet med Decrypt.py er at skriptet ikke lar meg lagre bokstaver som "æøå" og tegn som ",.-@" dette er et veldig stort problem siden enkrypsjonen var planlagt å bli brukt for eposter og passord.


test og test-decrypt var meg som testet for å se om et Caesar cipher hadde funket, et Caeser cipher er når du flytter alle bokstaver til siden, disse hadde akkuratt samme problemer som de første programmene men hadde også vært lettere å løse for vanlige folk.


Hva var planen?

Planen min var å lage 2 nettsider som lot deg sende meldinger mellom disse to sidene, med en database som lagrer alle meldinger.


Hva klarte jeg?

Nettsidene var ikke funksjonelle, knappen funker men resultatet kommer utenfor selve skjermen og jeg kom ikke til delen der jeg skulle sette opp databasen engang


problemløsning:

Mens jeg lagde enkrypsjonen har alle problemene mine vært med delen der jeg gjør bokstavene til tall, det første problemet var at jeg glemte lister startet med 0 og jeg måtte legge til + 1.

etter det fikk jeg mye problemer med å dekryptere siden en melding ville bare blitt en lang liste med tall og dekrypt programmet visste ikke når en bokstav sluttet og den andre startet. derfor måtte jeg legge til bokstavene "a" og "S" for at programmet kunne lese setningene ordentlig.




