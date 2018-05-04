# Web_Service_Assignment
 Microservice avec une API REST pour la création d’une application web de gestion immobilière.

* **URL**
http://localhost:5000/api/

* **Requirements**
Ajouter 'user-id' en key header avec en valeur l'ID de l'utilisateur avant d'envoyer la requête.

**Modifications bien**
----
  Un utilisateur peut modifier les caractéristiques d’un bien (changer le nom, ajouter une pièce, etc…)
et Fonctionnalité bonus : Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.
* **URL**

  /Property/:property_id

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   `property_id=[integer]`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{
	"city": "Rennes",
	"rooms": 2,
	"description": "Appartement éclairé ...",
	"property_name": "Apt Rennes 1",
	"car_rooms": "caractéristiques des pièces",
	"owner_id": 2,
	"type_prop": "Appartement"
}`
 
* **Error Response:**

  * **Code:** 400 <br />
    **Content:** `{'message': 'Aucune donnée renseignée'}`

  OR

  * **Code:** 422  <br />
    **Content:** `{ "status": "error" }`

  OR
  **Content:** `{ "Aucun bien n'a ce numéro" }`

  OR
  **Content:** `{ "L'utilisateur n'est pas le propriétaire de ce bien." }`


**Modifications utilisateur**
----
  Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)
* **URL**

  /User/:user_id

* **Method:**
  `GET`
  `POST`
  
*  **URL Params**

   **Required:**
 
   `user_id=[integer]`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{
  "surname": "Jean",
  "name": "Pierre",
  "city_of_interest": "Paris",
  "birthDate": "01-01-1966"
}`
 
* **Error Response:**

  * **Code:** 400 <br />
    **Content:** `{'message': 'Aucune donnée entrée'}`

  OR

  * **Code:** 422  <br />
    **Content:** `{ "status": "error" }`

  OR
  **Content:** `{ "Cet utilisateur n'existe pas" }`

  OR
  **Content:** `{ "Vous n'etes pas sur votre page d'informations personnelles." }`

**Accès utilisateur restreint**
----
  Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière

* **URL**

  /Property

* **Method:**
  `GET`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{
  "surname": "Jean",
  "name": "Pierre",
  "city_of_interest": "Paris",
  "birthDate": "01-01-1966"
}`
 
* **Error Response:**

  * **Code:** 400 <br />
    **Content:** `{'message': 'Aucune donnée renseignée'}`

  OR

  * **Code:** 422  <br />
    **Content:** `{ "status": "error" }`

  OR
  **Content:** `{ "Le propriétaire n'a pas été trouvé" }`

