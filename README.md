# Encryptie
Een applicatie waarmee gebruikers eenvoudig tekst kunnen versleutelen en ontsleutelen. 
Dit is een applicatie met een CLI waarmee gebruikers tekst kunnen versleutelen en ontsleutelen met symmetrische encryptie.  
Het doel is om gevoelige informatie veilig opteslaan en overtedragen op basis van een gebruikerswachtwoord.


## Functionaliteit
- **Versleutelen van tekst:** Voer een tekst en een wachtwoord in: De applicatie genereert dan een veilige versleuteld token dat salt en ciphertext combineert.  
- **Ontsleutelen van tekst:** Voer het versleutelde token en het zelfde wachtwoord in: De originele tekst wordt hersteld.  
- **Veilige key derivatie:**  Het wachtwoord wordt omgezet in een encryptiesleutel via PBKDF2HMAC met SHA-256 en een random salt.


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

