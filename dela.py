dela = []

def strToDelo(line):
    if line[-1] == '\n':
        line = line[:-1]
    naziv, glumac, autor, reziser, mesta = line.split("|")
    delo = {
        'naziv': naziv,
        'glumac': glumac,
        'autor': autor,
        'reziser': reziser,
        'mesta' : mesta
    }
    return delo

def loadDelo():
    for line in open("dela", 'r').readlines():
        if len(line) > 1:
            delo = strToDelo(line)
            dela.append(delo)
        
def deloToStr(delo):
    return '|'.join((delo['naziv'], delo['glumac'], delo['autor'], delo['reziser'], delo['mesta']))


def sortDela():
    kljuc = input("Unesite po kom kriterijumu zelite sortirana dela. (naziv, glumac, autor, reziser) >> \n")
    print("Sortirana dela po kriterijumu " + kljuc + " :\n")
    if kljuc == 'naziv':
        sortiranaDela = sorted(dela, key = lambda delo: delo['naziv'])
    elif kljuc == 'glumac':
        sortiranaDela = sorted(dela, key = lambda delo: delo['glumac'])
    elif kljuc == 'autor':
        sortiranaDela = sorted(dela, key = lambda delo: delo['autor'])
    elif kljuc == 'reziser':
        sortiranaDela = sorted(dela, key = lambda delo: delo['reziser'])
    for delo in sortiranaDela:
        print("Naziv dela: " + delo['naziv'] + ", glumac - " + delo['glumac'] + ", autor - " + delo['autor'] + ", reziser - " + delo['reziser'] + "\n")
    
def nadjiPredstavu(nazivDela):
    for delo in dela:
        if delo['naziv'] == nazivDela:
            return delo
    return -1  