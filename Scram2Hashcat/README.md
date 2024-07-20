<h3> Scram To Hashcat Converter </h3>

### About SCRAM

MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL).

MongoDB supports multiple authentication mechnanisms. Salted Challenge Response Authentication Mechanism (SCRAM) is the default authentication mechanism for MongoDB. SCRAM is based on the IETF RFC 5802 standard that defines best practices for implementation of challenge-response mechanisms for authenticating users with passwords.

RFC 5802 describes the challenge-response usage of SCRAM. Having admin access to the database, we only need to focus on the credential generation and storage part (and not the challenge-response mechanism, meaning the serverKey and signature parts are not needed). 

How does MongoDB implement SCRAM and create the user password hash (storedkey)?

See the RFC 5802 for the general overview and description of the protocol. Technically MongoDB implemented this in the following way:

    Passphrase = md5(username:mongo:password)
    SaltedPassword = pbkdf2(Passphrase, salt, iterations, key size)
    clientKey = hmac_sha-1 (saltedPassword,"Client Key")
    storedKey = sha1(clientKey))

The salt (base64 encoded), number of iterations and storedKey (base64 encoded) are listed in the database (see example below)

Please note that the iteration count (used in the pbkdf2 function) can be adjusted; default for SHA-1 is 10000 and for SHA2 is 15000. 

### About TOOL

Scram2Hashcat is a tool which converts a SCRAM credential file to a format hashcat can understand

Hashcat has the hash [mode](https://hashcat.net/wiki/doku.php?id=example_hashes) which can crack the hash, but there are not many tools that can convert it to hash

### How to run?

```
python3 scram2hashcat.py creds.json
```




























