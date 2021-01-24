import dela
radnici = []
ulogovan = {}

def loginRadnik(username, password):
    global ulogovan
    for radnik in radnici:
        if radnik['username'] == username and radnik['password'] == password:
            ulogovan = radnik
            return True
    return False

def ucitajRadnike():
    global radnici
    for line in open('radnici', 'r').readlines():
        if len(line) > 1:
            radnik = strToRadnik(line)
            radnici.append(radnik)
    
def strToRadnik(line):
    if line[-1] == "\n":
        line = line[:-1]
    ime, prezime, username, password = line.split("|")
    radnik = {
        'ime': ime,
        'prezime': prezime,
        'username': username,
        'password': password
        }
    return radnik

def obrisiPredstavu(nazivDela):
    deloBrisi = dela.nadjiPredstavu(nazivDela)
    if deloBrisi != -1:
        rewriteFile = open('dela', 'w')
        for delo in dela.dela:
            if delo == deloBrisi:
                continue
            else:
                deloStr = dela.deloToStr(delo)
                rewriteFile.write(deloStr + "\n")
        rewriteFile.close()
        return True
    else:
        return False
    
def dodajPredstavu(delo):
    appendFile = open('dela', 'a')
    appendFile.write("\n" + delo)
    appendFile.close()
    dela.dela.append(delo)
            
def izmeniPredstavu(nazivDela, brojZauzetihMesta):
    index = dela.nadjiPredstavu(nazivDela)
    if int(brojZauzetihMesta) < int(index['mesta']):
        index['mesta'] = str(int(index['mesta']) - int(brojZauzetihMesta))
        print("Novi broj preostalih mesta je " + index['mesta'])
        rewriteFile = open('dela', 'w')
        for delo in dela.dela:
            deloStr = dela.deloToStr(delo)
            rewriteFile.write(deloStr + "\n")
        rewriteFile.close()
    elif int(index['mesta']) == 0:
        print("Nema vise slobodnih mesta.") 
    else:
        print("Nema dovoljan broj slobodnih mesta za ovu prodaju.")
    
def proveraSlobodnihMesta(nazivDela):
    index = dela.nadjiPredstavu(nazivDela)
    if int(index['mesta']) > 0:
        print("Preostalo je jos slobodnih " + index['mesta'] + " mesta.")
    else:
        print("Nazalost nema slobodnih mesta.")
      
#def radnikToStr(radnik):
#    return '|'.join([radnik['ime'], radnik['prezime'], radnik['username'], radnik['password']])
