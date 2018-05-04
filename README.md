# Web_Service_Assignment
 Microservice avec une API REST pour la création d’une application web de gestion immobilière.

Exemple:
http://localhost:5000/api/User avec une requête http POST

2) Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme (nom, prénom, date de naissance)

3) Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière

4) Fonctionnalité bonus : Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.

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
