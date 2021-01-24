import dela
korisnici = []
ulogovan = {}

def strToKor(line):
    if line[-1] == '\n':
        line = line[:-1]
    ime, prezime, e_mail, godine_starosti, username, password = line.split("|")
    korisnik = {
        'ime': ime,
        'prezime': prezime,
        'e_mail': e_mail,
        'godine_starosti': godine_starosti,
        'username': username,
        'password': password
    }
    return korisnik

def loadKor():
    global korisnici
    for line in open('korisnici', 'r').readlines():
        if len(line) > 1:
            korisnik = strToKor(line)
            korisnici.append(korisnik)
            
def loginKor(username, password):
    global ulogovan
    for korisnik in korisnici:
        if korisnik['username'] == username and korisnik['password'] == password:
            ulogovan = korisnik
            return True
    return False
        
def korToStr(korisnik):
    return '|'.join((korisnik['ime'], korisnik['prezime'], korisnik['e_mail'], korisnik['godine_starosti'], korisnik['username'], korisnik['password']))

def dodajKorisnika(ime, prezime, e_mail, godine_starosti, username, password):
    korisnik = {
        'ime': ime,
        'prezime': prezime,
        'e_mail': e_mail,
        'godine_starosti': godine_starosti,
        'username': username,
        'password': password
        }
    appendFile = open('korisnici', 'a')
    korisnikStr = korToStr(korisnik)
    appendFile.write("\n" + korisnikStr)
    appendFile.close()       
    
def ispisiPredstave():
    print("Naziv | glumac | autor | reziser | mesta")
    for predstava in dela.dela:
        print('{0:30} {0:30} {0:30} {0:30} {0:2d}'.format(predstava['naziv'], predstava['glumac'], predstava['autor'], predstava['reziser'], predstava['mesta']) )
    
def rezervisiKartu(nazivDela):
    delo = dela.nadjiPredstavu(nazivDela)
    if delo != -1:
        if int(delo['mesta']) > 0:
            print("Uspesno ste rezervisali kartu sa mestom broj: " + delo['mesta'])
            delo['mesta'] = str(int(delo['mesta']) - 1)
            rewriteFile = open('dela', 'w')
            for delo in dela.dela:
                deloStr = dela.deloToStr(delo)
                rewriteFile.write(deloStr + "\n")
            rewriteFile.close()
            return True
        else:
            print("Nema slobodnih mesta za ovu predstavu.")
            return False
    else:
        print("Delo ne postoji.")    
        
def izracunajPopust():
    if ulogovan == {}:
        print("Nije ulogovan ni jedan korisnik.")
    elif (int(ulogovan['godine_starosti']) < 20 or int(ulogovan['godine_starosti']) > 60):
        print("Na cenu karte ce vam se obracnuati 30% popusta.")
    else:
        print("Nemate pravo na popust.")
    
def ispisiPredstaveGlumac(glumac):
    print("Naziv | glumac | autor | reziser | mesta")
    brojac = 0
    for predstava in dela.dela:
        if predstava['glumac'] == glumac:
            print('{0:20} {1:20} {2:20} {3:20} {4:2}'.format(predstava['naziv'], predstava['glumac'], predstava['autor'], predstava['reziser'], predstava['mesta']) )
            brojac += 1
    if brojac == 0:
        print("Nema predstava za ovog glumca.")
    
        
        