import jwt
encoded = jwt.encode({'role': 'admin'}, 'secret_key', algorithm='HS256')
print (encoded)
