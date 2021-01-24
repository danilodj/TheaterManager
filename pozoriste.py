import radnik
import korisnici
import dela

def printMenu():
    print("\nIzaberite opciju: ")
    print(" 1 - Sortiranje predstava po nekom kriterijumu.")
    print(" 2 - Pronadji odredjeno delo.")
    print(" 3 - Rezervisi kartu za predstavu.")
    print(" 4 - Pronadji predstave u kojima glumi odredjeni glumac.")
    print(" EXIT - izlazak iz programa")

def menu():
    printMenu()
    opcija = input("Opcija: ")
    while opcija.upper() not in ('1', '2', '3', '4', 'EXIT'):
        print("Izabrana opcija ne postoji. Pokusajte ponovo.")
        printMenu()
        opcija = input("Opcija: ")
    return opcija

def printUprava():
    print("\nIzaberite opciju: ")
    print(" 1 - Obrisi predstavu.")
    print(" 2 - Dodaj predstavu.")
    print(" 3 - Izmeni predstavu.")
    print(" 4 - Proveri slobodna mesta za neku predstavu.")
    print(" EXIT - izlazak iz programa")

def uprava():
    printUprava()
    opcija = input("Opcija: ")
    while opcija.upper() not in ('1', '2', '3', '4', 'EXIT'):
        print("Izabrana opcija ne postoji. Pokusajte ponovo.")
        printUprava()
        opcija = input("Opcija: ")
    return opcija

def loginMain(login):
    if login == 1:
        return loginKorisnik()
    elif login == 0:
        return loginRadnik()
        
def loginRadnik():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return radnik.loginRadnik(username, password)

def loginKorisnik():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return korisnici.loginKor(username, password)

def Pozoriste():
    print("Dobrodosli u pozoriste")
    dela.loadDelo()
    korisnici.loadKor()
    radnik.ucitajRadnike()
    login = eval(input("Unesite broj 1 za korisnika, broj 0 za radnika ili broj 2 ukoliko zelite da se registrujete kao novi korisnik: "))
    if login == 0:
        if loginMain(login) == True:
            print("Ulogovani ste kao radnik")
            opcijaRadnik = uprava()
            while opcijaRadnik != 'EXIT':
                print("Odabrali ste opciju " + opcijaRadnik)
                if opcijaRadnik == '1':
                    nazivDela = input("Unesite naziv dela za brisanje.")
                    radnik.obrisiPredstavu(nazivDela)  # brisanje dela
                elif opcijaRadnik == '2':
                    delo = input ("Unesite delo u formatu naziv|glumac|autor|reziser|mesta i ono ce biti dodato.")
                    radnik.dodajPredstavu(delo)  # dodavanje dela
                elif opcijaRadnik == '3':
                    nazivDela, brojZauzetihMesta = input("Unesite naziv predstave i koliko karata zelite da prodate za datu predstavu.").split()
                    radnik.izmeniPredstavu(nazivDela, brojZauzetihMesta)
                elif opcijaRadnik == '4':
                    nazivDela = input("Unesite naziv dela za koje zelite da proverite koliko je slobodnih mesta preostalo.")
                    radnik.proveraSlobodnihMesta(nazivDela)
                opcijaRadnik = uprava()
    elif login == 2:       
        ime, prezime, e_mail, godine_starosti, username, password = input("Odabrali ste registraciju novog korisnika.\nUnesite,redom, vase ime, prezime, e-mail, godine starosti, username i password.").split(',')
        korisnici.dodajKorisnika(ime, prezime, e_mail, godine_starosti, username, password)
        print("Molimo vas da ponovo pokrenete program kako biste se ulogovali sa novim nalogom.")
        return
    elif login == 1:
        if loginMain(login) == True:
            print("Ulogovani ste kao korisnik.")
            opcijaKorisnik = menu()
            while opcijaKorisnik != 'EXIT':
                print("Odabrali ste opciju " + opcijaKorisnik)
                if opcijaKorisnik == '1': # Ispis sortiranih dela po nekom kriterijumu
                    dela.sortDela() 
                elif opcijaKorisnik == '2': # Pronalazenje predstave
                    nazivDela = input("Unesite naziv predstave koju zelite da pronadjete.")
                    delo = dela.nadjiPredstavu(nazivDela)
                    if delo != -1:  
                        print("Naziv dela: " + delo['naziv'] + ", glumac - " + delo['glumac'] + ", autor - " + delo['autor'] + ", reziser - " + delo['reziser'] + ", mesta - " + delo['mesta'] + "\n")
                    else:
                        print("Predstava sa zadatim nazivom ne postoji.")
                elif opcijaKorisnik == '3': # Rezervisanje karte
                    nazivDela = input("Unesite naziv predstave za koju zelite da rezervisete kartu.")
                    if korisnici.rezervisiKartu(nazivDela):
                        korisnici.izracunajPopust()
                elif opcijaKorisnik == '4': # Pronalazenje svih predstava odredjenog glumca
                    glumac = input("Unesite naziv glumca cije predstave zelite da vidite.")
                    korisnici.ispisiPredstaveGlumac(glumac)
                opcijaKorisnik = menu()
    elif not loginMain(login):
        print("\nNiste uneli dobro korisnicko ime i lozinku.")
    else:
        print("Niste uneli dobru opciju. Zavrsavanje programa.")
        
if __name__ == '__main__':
    Pozoriste()

