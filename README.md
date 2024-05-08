# Zeep_Backend


- Telecharger et instaler Doker et Doker Desktop
- Clonner Zeep_Backend
- ce possitionner dans le repertoire Zeep_Backend

-RUN

--- docker-compose build
    pour creer une image docker en local (on la mettra sur le hub si besoin)

--- pour nos commande habituelles
    - docker-compose run --r app sh -c "notre commande"

- docker-compose up :
     pour lancer le serveur

- pour ce rassurer de la clarté du code :
    docker-compose run --r app sh -c "notre commande"   : avec notre commande = "flake8"
    soit
    docker-compose run --r app sh -c "flake8"
 