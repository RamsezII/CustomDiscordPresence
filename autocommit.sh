#!/bin/bash

# Vérifier si le message de commit est fourni en paramètre
if [ -z "$1" ]; then
    echo "Veuillez fournir un message de commit en paramètre."
    exit 1
fi

# Ajouter tous les fichiers modifiés à l'index
git add .

# Commit et pousser les modifications avec le message fourni en paramètre
git commit -m "$1"
git push

# Sortir avec succès
exit 0