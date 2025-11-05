# Encryptie
Dit is een applicatie met een CLI waarmee gebruikers eenvoudig teksten kunnen versleutelen en ontsleutelen met een symmetrische encryptie.  
Het doel is om gevoelige informatie veilig opteslaan en overtedragen op basis van een wachtwoord.


## Functionaliteit
Het werkt zo je voert een tekst en een wachtwoord in en de applicatie maakt daar een versleutelde tekst van die veilig opgeslagen of gedeeld kan worden. Later kan je deze versleutelde tekst weer terug omzetten naar de originele tekst zolang je de zelfde wachtwoord gebruikt. 

De applicatie heeft vier belangrijke punten: 

Als eerste versleutelen.
 De tekst die de gebruiker invoert wordt omgezet in een beveiligde code dus ciphertext met AES-256. De output is een base64-string die makkelijk kan worden opgeslagen of gedeeld. 

Als tweede ontsleutelen. 
 Als je de versleutelde tekst en het juiste wachtwoord invoert dan kan de applicatie de originele tekst weer herstellen. 

Als derde key-derivatie.
 Het ingevoerde wachtwoord wordt niet direct als sleutel gebruikt. In plaats daarvan gebruikt de applicatie PBKDF2-HMAC-SHA256 met een random salt van 16 bytes en 300.000 iteraties om een sterke sleutel te maken. Dit maakt het veel moeilijker voor een hacker om het wachtwoord te raden. 

Als vierde integriteit. 
 De applicatie gebruikt Fernet wat naast encryptie ook controleert of de tekst niet is aangepast via HMAC. Dit betekent dat je zeker kan weten dat de versleutelde tekst niet is veranderd. 


## Cryptografie en keuzes 

De applicatie maakt gebruik van symmetrische encryptie dit betekent dat dezelfde sleutel wordt gebruikt om de tekst te versleutelen en te ontsleutelen. Een voordeel hiervan is dat het snel en efficiënt werkt. Een nadeel is dat het lastig kan zijn om de sleutel veilig te delen als er meerdere gebruikers zijn. 

Voor de encryptie heb ik gekozen voor: 

AES-256 via Fernet want dit is modern, veilig en gebruikt authenticated encryption. Dus het beschermt niet alleen tegen het lezen van de tekst maar ook tegen het wijzigen daarvan. 

PBKDF2-HMAC-SHA256 voor key derivatie hiermee wordt het wachtwoord omgezet in een sterke sleutel en daardoor worden brute-force aanvallen moeilijker gemaakt.  

En een salt van 16 bytes dit voorkomt dat aanvallers makkelijk gebruik kunnen maken van rainbow tables. 


## Sleutelbeheer 

Deze applicatie slaat geen sleutels op. De gebruiker voert alleen een wachtwoord in en daaruit wordt dynamisch een sleutel gemaakt met PBKDF2 en een random salt.  

Het voordeel hiervan is dat er geen bestand met een sleutel op de computer staat die gestolen kan worden. Het nadeel is dat de gebruiker zijn wachtwoord goed moet onthouden want zonder het juiste wachtwoord kan de tekst niet meer ontsleuteld worden. 


## Kerckhoffs's Principe 

Het Kerckhoffs principe zegt dat een encryptiesysteem veilig moet blijven zelfs als alles over het systeem bekend is behalve de sleutel.  

In deze applicatie kan de code kan openbaar zijn want de veiligheid hangt alleen af van het wachtwoord. 

Door het gebruik van PBKDF2 met salt  is de applicatie beschermt tegen brute-force en rainbow-table aanvallen. 

AES-256 en Fernet zijn algemeen bekend en getest. 

Dus dit betekent dat mijn applicatie voldoet aan het Kerckhoffs principe want de beveiliging hiervan hangt volledig af op de geheimhouding van het wachtwoord en niet op de geheimhouding van de code of het algoritme. 


## Gebruik
**Run encryptie.py**

Vervolgens kies je:  
- `1` om tekst te versleutelen  
- `2` om tekst te ontsleutelen


## Bronnen

- https://www.encryptionconsulting.com/nl/opleidingscentrum/symmetrische-versus-asymmetrische-encryptie/
- https://axcrypt.net/nl/blog/symmetric-vs-asymmetric-encryption/?srsltid=AfmBOor7Cdp1KTkOyryFM5POGIMdrcijP_8qnbo20PmQUxTTu_TSXxQX
- https://www.kiteworks.com/nl/veilige-bestandsoverdracht/alles-over-aes-algoritme-stappen/
- https://nitratine.net/blog/post/encryption-and-decryption-in-python/
- https://en.wikipedia.org/wiki/PBKDF2
- https://en.wikipedia.org/wiki/Kerckhoffs%27s_principle
- https://www.geeksforgeeks.org/python/fernet-symmetric-encryption-using-cryptography-module-in-python/
- https://www.geeksforgeeks.org/python/how-to-encrypt-and-decrypt-strings-in-python/
- https://cryptography.io/en/latest/fernet/
- https://stackoverflow.com/questions/55776011/decrypt-with-fernet-python 
- https://blog.bytescrum.com/encrypting-and-decrypting-data-with-fernet-in-python
- https://medium.com/@sunilnepali844/complete-guide-to-encryption-and-decryption-in-python-for-beginners-61c2343c3f2b
- https://thepythoncode.com/code/encrypt-decrypt-files-symmetric-python
- https://www.youtube.com/watch?v=3hp4vnSb2qU
- https://www.youtube.com/watch?v=zWNA2ThkVT4

