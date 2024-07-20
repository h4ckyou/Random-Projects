<h3> Scram To Hashcat Converter </h3>

### About SCRAM

MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL).

MongoDB supports multiple authentication mechnanisms. Salted Challenge Response Authentication Mechanism (SCRAM) is the default authentication mechanism for MongoDB. SCRAM is based on the IETF RFC 5802 standard that defines best practices for implementation of challenge-response mechanisms for authenticating users with passwords. See Mongo_scram.

### About T00L

While doing a machine I came across a JSON file that had an encrypted credentials

The format was in SCRAM which is what MongoDB uses and I didn't see tool I could easily make use of to convert it to a format which I can crack
