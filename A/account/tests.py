

def show(name):
    def subshow():
        return f'hello {name}'
    return subshow()

print(show('moji'))

#for i in map(show, ['amir'.upper(), str.lower('moji'), str.capitalize('moji')]):
    #print(i)

