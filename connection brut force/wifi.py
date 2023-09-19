# -*- coding: utf-8 -*-
import logging
import pywifi
from pywifi import const
import time
logging.basicConfig(level=logging.DEBUG,
                filename="t/mdpUse.txt",
                filemode="a",
                format='%(asctime)s - %(levelname)s - %(message)s')

# Créez un objet de point d'accès Wi-Fi
wifi = pywifi.PyWiFi()

# Obtenez l'interface Wi-Fi (adaptateur)
iface = wifi.interfaces()[0]  # Utilisez [0] si vous avez une seule interface Wi-Fi

# Définissez le profil Wi-Fi (SSID et mot de passe)
while True:


        # Ouvrez le fichier en mode lecture
    with open('mdp0.txt', 'r', encoding='utf-8') as fichier:
        # Parcourez chaque ligne du fichier
        for ligne in fichier:
            # Faites quelque chose avec la ligne, par exemple, l'afficher
          
            ssid = "AndroidAP"  # Remplacez par le nom de votre réseau Wi-Fi
            mot_de_passe = ligne.split  # Remplacez par le mot de passe de votre réseau Wi-Fi
            print(ligne.strip())
            
            # Supprimez toutes les anciennes connexions Wi-Fi
            iface.scan()
            iface.disconnect()

            # Créez un profil Wi-Fi
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN  # Utilisez const.AUTH_ALG_SHARED pour les réseaux sécurisés WEP
            profile.akm.append(const.AKM_TYPE_WPA2PSK)  # Utilisez const.AKM_TYPE_WPAPSK pour WPA
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = mot_de_passe

            # Ajoutez le profil
            iface.remove_all_network_profiles()
            profile_id = iface.add_network_profile(profile)

            # Connectez-vous au réseau Wi-Fi
            iface.connect(profile_id)

            # Attendez un moment pour vous connecter
          
            time.sleep(5)

            # Vérifiez l'état de la connexion
            if iface.status() == const.IFACE_CONNECTED:
                print("Connecté au réseau Wi-Fi avec succès!")
                break
            else:
                print("Échec de la connexion au réseau Wi-Fi.")

            # Vous êtes maintenant connecté au réseau Wi-Fi. Vous pouvez effectuer des opérations supplémentaires si nécessaire.

            # Pour déconnecter
            iface.disconnect()
