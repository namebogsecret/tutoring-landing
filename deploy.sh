#!/usr/bin/env bash
# deploy.sh — выкладка tutor.podlevskikh.com.
# Схема (с 08.11.2026): ветка main = исходники (build.py, src/, tests/),
# ветка gh-pages = ТОЛЬКО отдаваемые файлы. Исходники и тесты публично не раздаются
# (в тестах лежат стоп-слова — их нельзя отдавать краулерам).
# Использование: ./deploy.sh ["сообщение"]   (из чистого дерева main)
set -euo pipefail
cd "$(dirname "$0")"
SRC=$(pwd)
[ -z "$(git status --porcelain)" ] || { echo "✗ дерево грязное — сначала коммит"; exit 1; }

python3 build.py
[ -z "$(git status --porcelain)" ] || { echo "✗ build.py изменил файлы — закоммить пересборку"; git status --short; exit 1; }
for t in tests/test_*.py; do python3 "$t" >/dev/null || { echo "✗ тест $t"; exit 1; }; done
python3 -m unittest discover -s tests -q

SHA=$(git rev-parse --short HEAD)
WT=$(mktemp -d)
trap 'git worktree remove --force "$WT" >/dev/null 2>&1 || true' EXIT
git fetch -q origin gh-pages
git worktree add -q --detach "$WT" origin/gh-pages
# чистим всё, кроме .git, и кладём отдаваемое
find "$WT" -mindepth 1 -maxdepth 1 ! -name .git -exec rm -rf {} +
git ls-files -z | grep -zvE '^(tests/|src/)|\.py$|\.md$|^deploy\.sh$|^\.gitignore$' \
  | (cd "$SRC" && xargs -0 cp --parents -t "$WT")
cd "$WT"
git add -A
if git diff --cached --quiet; then echo "Нечего деплоить."; exit 0; fi
git -c user.email="vladimir@podlevskikh.com" -c user.name="Vladimir Podlevskikh" \
  commit -qm "${1:-deploy} (main $SHA)"
git push -q origin HEAD:gh-pages
echo "✓ gh-pages ← main $SHA. Pages пересоберётся за ~1 мин: https://tutor.podlevskikh.com/"
