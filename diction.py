bailey = {
    'name': 'bailey anderson',
    'age':'31 years old',
    'birthplace':'US of A #unclesam',
    'favorite language': 'Pro Tools'

}
def bailey_bio(key, value):
    for k, val in bailey.iteritems():
            print"My",k,"is",val
      
bailey_bio('hobby', 'coding')

def bailey_bio(key, value):
    for k, val in bailey.iteritems():
        if bailey.has_key(key):
            print"My",k,"is",val
        else:
            bailey[key] = value 
            print"My",k,"is",val
            return bailey    
bailey_bio('hobby', 'coding')
