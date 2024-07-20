from json import loads
from sys import argv
from base64 import b64encode

# based off: https://github.com/hashcat/hashcat/issues/2551

def main():
    data = open(argv[1], 'r').read().replace("UUID(", "").replace("),", ",")
    json_data = loads(data)

    user = b64encode(json_data['user'].encode()).decode()
    
    i = 0
    credentials = json_data['credentials']['SCRAM-SHA-1']
    iterations  = credentials['iterationCount']
    salt        = credentials['salt']
    serverKey   = credentials['serverKey']
    
    print("${0}$*{1}*{2}*{3}*{4}*{5}".format("mongodb-scram", i, user, iterations, salt, serverKey))

    i = 1
    credentials = json_data['credentials']['SCRAM-SHA-256']
    iterations  = credentials['iterationCount']
    salt        = credentials['salt']
    serverKey   = credentials['serverKey']
    
    print("${0}$*{1}*{2}*{3}*{4}*{5}".format("mongodb-scram", i, user, iterations, salt, serverKey))

if __name__ == '__main__':
    main()
