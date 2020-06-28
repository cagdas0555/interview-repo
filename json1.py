# -*- coding: utf-8 -*-


import csv
 
def csv_oku(d_obj):
    """
    CSV dosyasini okumak - - csv.DictReader Yontemi
    :param d_obj:
    :return:
    """
    sayac=0;
    iliskilendirmesayac=0;
    schoolName="amesia";
    skor=0
    enbuyuk=0;
    k=0
    i=0
    j=0
    t=0
    enbuyukisim=""
    enkucukelestirel=1000
    enkucukelestirelisim=""
    enbuyukelestirel=0
    enbuyukelestirelisim=""
    enkucukmat=1000
    enkucukmatisim=""
    enbuyukmat=0
    enbuyukmatisim=""
    enyuksekortalama=0.0
    enyuksekortisim=""
    kisibasınaortalamapuan=0.0
    enkucukortalama=0.0
    endusukortisim=""

    
    
    reader = csv.DictReader(d_obj, delimiter = ',')
   
    for line in reader:
        
      
        if schoolName!=line["School Name"]:
            sayac=sayac+1
        
        print(line["DBN"])
        print(line["School Name"])
        print(line["Number of Test Takers"])
        print(line["Critical Reading Mean"])
        print(line["Mathematics Mean"])
        print(line["Writing Mean"])
        
        try:
            i=int(line["Critical Reading Mean"])
            j=int(line["Mathematics Mean"])
            k=int(line["Writing Mean"])
            t=int(line["Number of Test Takers"])
            if enkucukelestirel>int(line["Critical Reading Mean"]):
                enkucukelestirel=int(line["Critical Reading Mean"])
                enkucukelestirelisim=line["School Name"]
            if enbuyukelestirel<int(line["Critical Reading Mean"]):
                enbuyukelestirel=int(line["Critical Reading Mean"])
                enbuyukelestirelisim=line["School Name"]
            if enbuyukmat<int(line["Mathematics Mean"]):
                enbuyukmat=int(line["Mathematics Mean"])
                enbuyukmatisim=line["School Name"]
            if enkucukmat>int(line["Mathematics Mean"]):
                enkucukmat=int(line["Mathematics Mean"])
                enkucukmatisim=line["School Name"]
            kisibasınaortalamapuan=(i+j+k)/t
            if enyuksekortalama<kisibasınaortalamapuan:
                enyuksekortalama=kisibasınaortalamapuan
                enyuksekortisim=line["School Name"]
            if enyuksekortalama<kisibasınaortalamapuan:
                enyuksekortalama=kisibasınaortalamapuan
                enyuksekortisim=line["School Name"]
            if enkucukortalama<kisibasınaortalamapuan:
                enkucukortalama=kisibasınaortalamapuan
                endusukortisim=line["School Name"]
            
            
        except ValueError:
            pass 
        skor=i+j+k
        if enbuyuk<skor:
            enbuyuk=skor
            enbuyukisim=line["School Name"]
        if line["Number of Test Takers"] =="" or line["Critical Reading Mean"]==""  or  line["Mathematics Mean"]=="" or line["Writing Mean"]=="":
            iliskilendirmesayac=iliskilendirmesayac+1;
    
    print("izlenilen okul sayısı= " + str(sayac))
    print("ilişkendirilmemiş okul sayisi = "+str(iliskilendirmesayac))
    print("en basarılı okul ismi ="+enbuyukisim ) 
    print("en basarılı okulun toplam puanı = "+str(skor))
    print("matematik ortalamalarında en farklı 2 okuldan en yüksek ortalamaya sahip olan "+str(enbuyukmatisim)+"puanı="+str(enbuyukmat))
    print("en yüksek ortalamaya sahip olan = "+str(enkucukmatisim)+"puanı "+str(enkucukmat))
    print("eleştirel okuma ortalamalarında en farklı 2 okuldan en yüksek ortalamaya sahip olan "+str(enbuyukelestirelisim)+"puanı="+str(enbuyukelestirel))
    print("en yüksek ortalamaya sahip olan = "+str(enkucukelestirelisim)+"puanı "+str(enkucukelestirel))
    print("kisi basına ortalama en yüksek puan düşen okulun ismi= "+str(enyuksekortisim)+"ortalama puan="+str(enyuksekortalama))
    print("kisi basına ortalama en düşük puan düşen okulun ismi= "+str(endusukortisim)+"ortalama puan="+str(enkucukortalama))
if __name__ == "__main__":
    csv_path = "staj.csv"
    with open(csv_path, "r") as d_oku:
        csv_oku(d_oku)