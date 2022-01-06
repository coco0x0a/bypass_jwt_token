import jwt
encoded = jwt.encode({'role': 'admin'}, '', algorithm='HS256')
print (encoded)
