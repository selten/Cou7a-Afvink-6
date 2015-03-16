#Auteurs: Renske Wever, Elaine Hodenius en Peter Selten
#Datum: 16-03-2015
#Functie: Leest een bestand en geeft een rapport met de sequentie en gc percentage.
#Bekende bugs: geen

def main():
    sequentie = leesBestand('m_p53.gb')
    gc_percentage = bepaalGCpercentage(sequentie)
    html = schrijfHTMLrapport (gc_percentage, sequentie, bestandsnaam)

def leesBestand(bestandsnaam):
    #retourneert de sequentie uit het bestand
    
    try:
        file = open(bestandsnaam)

        string = ""
        for line in file:
            string = string+"\n"+line
        file.close()

        while "  " in string or '\t' in string:
            string = string.replace('  ',' ').replace('\t','')
        regel_array = string.split("\n")

        CDS = ['','']
        start_check = 0
        Coding = "";

        for r in regel_array:
            if "CDS" in r:
                CDS[0] = int(r.split(" ")[2].split('..')[0].replace('<',''))
                CDS[1] = int(r.split(" ")[2].split('..')[1].replace('>',''))
            elif r == "ORIGIN ":
                start_check = 1
            elif r == "//":
                start_check = 0
            if start_check == 1:
                k = r.split(" ")
                Coding = Coding+"".join(k[2:len(k)])
        return Coding[CDS[0]-1:CDS[1]]
    except IOError:
        print("Kan bestand niet lezen")
    except Exception:
        #print("ERROR")
        print(traceback.format_exc())
        print(sys.exc_info()[0])

def bepaalGCpercentage(sequentie):
    #retourneert het GC percentage
    sequentie = sequentie.upper()
    aantal_c = sequentie.count('C')
    aantal_g = sequentie.count('G')
    percentage = ((aantal_c + aantal_g )/len(sequentie)*100) 
    
    return(percentage)
def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):
    #schrijft html rapport
    f = open(bestandsnaam + '_rapport.html','w')
    f.write("<html>")
    f.write("Sequentie is:" + sequentie)
    f.write("GC Percentage is: " + gcPercentage)
    f.write("<html>")
    f.close()

main()
