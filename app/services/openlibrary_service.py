import requests
from typing import Optional, Dict

OPENLIBRARY_URL = "https://openlibrary.org/works/"

def get_livro_data(olid: str):
    autor_name = "Autor Desconhecido"
    url = f"{OPENLIBRARY_URL}{olid}.json"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    
    data = response.json()
    
    autores = data.get("authors", [])
    
    if autores and autores[0].get("author", {}).get("key"):
        author_key = autores[0]["author"]["key"]
        author_url = f"https://openlibrary.org{author_key}.json"
        
        autor_response = requests.get(author_url, timeout=5)
        
        autor_response.raise_for_status()
        
        autor_data = autor_response.json()
        autor_name = autor_data.get("name", autor_name)
        
    return {
        "olid": olid,
        "titulo": data.get("title", "Título Desconhecido"),
        "autor": autor_name
    }





