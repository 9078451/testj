import logging
import pywifi
from pywifi import const 
class e:
                # Créez un objet de point d'accès Wi-Fi
    wifi = pywifi.PyWiFi()

        # Obtenez l'interface Wi-Fi (adaptateur)
    iface = wifi.interfaces()[0]  # Utilisez [0] si vous avez une seule interface Wi-Fi
    list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"'","#","{","(","[","-","|","è","`","_","ç","^","à","@",")","°","]","=","+","}","^","¨","$","£","¤","ù","%","*","µ","!","§",":","/",";",".","?",",",")"]
    chaine = str()
    logging.basicConfig(level=logging.INFO,
        filename="modules/dataworldpass20.txt",
        filemode="a",
        encoding='utf-8',
        format='%(message)s')               

    for l in list:
        chaine = l   
        for l2 in list:
            chaine = l + l2 
            for l3 in list:
                chaine = l + l2 + l3
                for l4 in list:
                    chaine = l + l2 + l3 + l4
                    for l5 in list:
                        chaine = l + l2 + l3 + l4+ l5
                        for l6 in list:
                            chaine = l + l2 + l3 + l4+ l5+l6
                            for l7 in list:
                                chaine = l + l2 + l3 + l4+ l5+l6+l7
                                for l8 in list:
                                    chaine = l + l2 + l3 + l4+ l5+l6+l7+l8          
                                    for l9 in list:
                                        chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9   
                                        for l10 in list:
                                            chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10   
                                            for l11 in list:
                                                chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11
                                                for l12 in list:
                                                    chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12  
                                                    for l13 in list:
                                                        chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13 
                                                        for l14 in list:
                                                            chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14   
                                                            for l15 in list:
                                                                chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15  
                                                                for l16 in list:
                                                                    chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15+l16  
                                                                    for l17 in list:
                                                                        chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15+l16+l17 
                                                                        for l18 in list:
                                                                            chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15+l16+l17+l18
                                                                            for l19 in list:
                                                                                chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15+l16+l17+l18+l19  
                                                                                for l20 in list:
                                                                                    chaine = l + l2 + l3 + l4+ l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15+l16+l17+l18+l19+l20                                                                                                                                                        
                                                                                    print(chaine)
                                                                                    logging.info(chaine)
    print("prosses fini and dataWorldPass is now finish")