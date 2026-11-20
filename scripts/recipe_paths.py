"""Locate active and archived portable recipes by their recorded IDs."""
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]


def recipe_folder(recipe_id, repo=REPO):
    for parent in ("recipes", "archive/recipes"):
        folder = repo / parent / recipe_id
        if (folder / "recipe.json").is_file():
            return folder
    raise FileNotFoundError(f"No recipe named {recipe_id}")
