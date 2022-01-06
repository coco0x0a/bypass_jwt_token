import jwt
encoded = jwt.encode({'role': 'admin'}, 'test', algorithm='HS256')
print (encoded)
