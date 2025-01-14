6GEN723 - LABO1

# 7)
## a. Faites une capture d’écran

![image](https://github.com/user-attachments/assets/46b9f6c7-1b8a-44b3-866b-34855ff7c539)

## b. Quel était le message donné par le navigateur?

Le message donné par le navigateur est une erreur 404 qui signifie que l'adresse n'a pas été trouvé

## c. Expliquez ce qui s’est passé en quelques phrases.

On essaye de se connecyter à notre application web à partir de l'IP 127.0.0.1 qui est la machine locale, mais avec le port 8080. Notre application flask run sur le port 3000 et donc c'est normal que nous ne sommes pas capable d'acceder notre application sur le port 8080 qui nous donne une erreur 404.

## d. À partir des détails de paquet, trouvez les champs pertinents du protocole (message, contenu, navigateur, autres champs, etc.)

REQUETE:

![image](https://github.com/user-attachments/assets/14ac73bd-825d-427d-bd1d-2a421d9b9f0e)

RÉPONSE:

![image](https://github.com/user-attachments/assets/180a27f5-8394-4864-b3ea-7b12aa8b5abe)

######################Premièrement, 

# 8)

## a. Faites une capture d’écran

![image](https://github.com/user-attachments/assets/18e4bdbf-8e25-49b6-a435-bd7067dd49c9)

## b. Quel était le message donné par le navigateur?

Le message donné par le navigateur est le contenu de ce qui est dans le code flask qui est "Hello, World!, From AMZJ: 172.16.14.33"

## c.Expliquez ce qui s’est passé en quelques phrases.

Maintenant que nous nous connectons à l'IP avec le bon port où que l'application run, nous sommes capable de se connecter et avoir les réponses de flask.

## d.À partir des détails de paquet, trouvez les champs pertinents du protocole (message, contenu, navigateur, autres champs, etc.)

REQUETE:

![image](https://github.com/user-attachments/assets/db9ea6e0-3102-40da-99de-75701d7048a0)

RÉPONSE:

![image](https://github.com/user-attachments/assets/0d40fa9e-4438-4931-ab4d-e3ca92bb9c9b)

########################

# 9)

## a. Faites une capture d’écran

![image](https://github.com/user-attachments/assets/9000c867-5c70-4c51-9552-33e5431b7129)


## b. Quel était le message donné par le navigateur?

Le message donné par le navigateur est qu'il y a un internal server error qui est un code 500.

##c.Expliquez ce qui s’est passé en quelques phrases.

Quand nous nous sommes connecté au serveur flask et que le serveur appel la fonction pour la page d'acceuil, le code execute la division par zéro qui n'est pas autorisé. Ceci fait en sorte qu'il y a une erreur du coté du serveur qui entraine l'envoie d'un code 500 et Internal server error

## d.À partir des détails de paquet, trouvez les champs pertinents du protocole (message, contenu, navigateur, autres champs, etc.)

REQUETE:

![image](https://github.com/user-attachments/assets/91e768db-cf0f-4df2-9e75-40b2cb389881)

RÉPONSE:

![image](https://github.com/user-attachments/assets/a9675018-a9c0-4543-88d5-ebb5d19af071)



# 11)

## a. Faites une capture d’écran

![image](https://github.com/user-attachments/assets/acb5f881-b822-4cee-8859-0694a810e172)

## b. Quel était le message donné par le navigateur?

Nous voyons le contenu de l'application flask de nos collègues qui travaillent sur une autre machine.

## c.Expliquez ce qui s’est passé en quelques phrases.

Nous nous sommes connecté à une autre machine dans le laboratoire avec leur adresse IP. Le serveur a renvoyé le contenu de la page web qui est le string affiché en HTML

## d.À partir des détails de paquet, trouvez les champs pertinents du protocole (message, contenu, navigateur, autres champs, etc.)

REQUETE:

![image](https://github.com/user-attachments/assets/52b6ef20-72f4-4f8c-b40c-a3f4856d1f43)

RÉPONSE:

![image](https://github.com/user-attachments/assets/c562b060-9346-46b3-8159-9b8b48d7be5e)

Quand une autre équipe se connecte à notre serveur ceci sont les requetes et réponses de notre serveur.


# 2 - DNS

PAQUETS:
![image](https://github.com/user-attachments/assets/742c9f89-e147-466d-9f7b-67a517fc8335)


