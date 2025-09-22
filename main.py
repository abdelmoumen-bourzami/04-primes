"""
Module permettant de vérifier si une chaîne de caractères est un palindrome.
Un palindrome est une séquence qui se lit de la même manière
de gauche à droite et de droite à gauche, indépendamment
des majuscules, accents, espaces et ponctuation.
"""

import unicodedata


def ispalindrome(text: str) -> bool:
    """
    Vérifie si la chaîne `text` est un palindrome.

    La fonction ignore :
    - les majuscules,
    - les accents,
    - les espaces,
    - la ponctuation.

    Args:
        text (str): La chaîne de caractères à tester.

    Returns:
        bool: True si `text` est un palindrome, False sinon.
    """
    # mettre en minuscules
    text = text.lower()

    # normaliser les accents (NFD sépare lettre + accent)
    text = unicodedata.normalize("NFD", text)

    # supprimer les accents (caractères de catégorie "Mn")
    text = "".join(ch for ch in text if unicodedata.category(ch) != "Mn")

    # ne garder que les caractères alphanumériques
    text = "".join(ch for ch in text if ch.isalnum())

    # comparer avec l'inverse
    return text == text[::-1]


def main() -> None:
    """
    Teste la fonction `ispalindrome()` sur quelques exemples simples.
    """
    examples = ["radar", "kayak", "level", "rotor", "civique", "deifie"]
    for word in examples:
        print(word, ispalindrome(word))


if __name__ == "__main__":
    main()
