import jwt
eiei = jwt.encode({'role': 'admin'}, 'test', algorithm='HS256')
print (eiei)
