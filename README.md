## Demarrage

1. Modifiez `PAGE_PASSWORD` et `FLASK_SECRET_KEY` dans `.env`.
2. Lancez l'application avec `uv run python application.py`.
3. Ouvrez http://127.0.0.1:5000/.

Le mot de passe valide ouvre `/protected`. Le texte de cette page peut etre modifie dans la zone de texte puis enregistre. La modification est conservee dans la session du navigateur.
