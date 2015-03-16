def main():
    sequentie = leesBestand('m_p53.gb');



def leesBestand(bestandsnaam):
    #retourneert de sequentie uit het bestand
    
    try:
        file = open(bestand)

        string = ""
        for line in file:
            string = string+"\n"+line
        file.close()


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
    except:
        print("ERROR")

def bepaalGCpercentage(sequentie):
    #retourneert het GC percentage

def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):
    #schrijft html rapport

main()
