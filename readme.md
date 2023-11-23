# Un simple chatbot basé sur LLMs pour répondre aux questions sur des données précises
Un chatbot basé sur un des modèles de langues présent sur HuggingFace pour répondre à divers questions.
## Description
en utilisant llama-index, une bibliothèque pour les modèles langues et les différents process depuis l'upload des données au traitement du query, on crée un chatbot "basé sur GPT-4 de OpenAI" pour répondre à des questions informatives en se basant sur des données fournis par un tiers et non pas les données globales utilisées pour entraîner le LLM.
## Getting started
### Dependencies
* fastapi : un endpoint est créer en utilisant fastapi qui donne un chemin de développement rapid, et pour que le chatbot soit intégrable sur divers applications par la suite.
* llama-index : une bibliothèque qui s'en charge de faire les quatre stage pour génerer une réponse : Loading, Indexing, Storing, Querying.
### Fonctionnement 
* Loading : loader les données sur lesquelles les réponses vont être basés qui peuvent être de n'importe quel type (structuré, non-structuré, cloud semi-structuré).
* Indexing : créer une représentation numérique sous format vectorielle des données présentes pour génération des réponses. 
* Storing : stocker les vecteurs dans une base données (local ou bien FAISS de Meta).
* Querying : traiter la question de l'utilisateur, créer une représentation numérique et le fournir au LLM pour la génération de réponse. 
### Install Dependencies
'''
pip install -m requirements.txt
'''
### Program Execution
* dans le cas de OpenAI, fournir une API key dans un fichier .env
* uploader ta propre data dans un dossier "data"
* éxecuter en utilisant la commande :
'''
uvicorn main:app
'''
