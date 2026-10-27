#!/usr/bin/env bash
set -euo pipefail
recipe_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$recipe_dir/../../scripts/launch.py" "$recipe_dir/recipe.json" "$@"
