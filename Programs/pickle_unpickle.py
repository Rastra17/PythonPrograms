import pickle
def save():
    shyam = {'key': 'shyam', 'name': 'shyam khatiwada', 'age': 30}
    ram = {'key': 'ram', 'name': 'ram baral', 'age': 27}

    db={}
    db['shyam']=shyam
    db['ram']=ram

    file=open('xyz.txt','ab')
    pickle.dump(db,file)
    file.close()
def load():
    file = open('xyz.txt', 'rb')
    db=pickle.load(file)
    for keys in db:
        print(keys,':',db[keys])
        file.close()
save()
load()