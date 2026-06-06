#!/usr/bin/env bash
# deploy.sh — публикация лендинга на GitHub Pages.
# Использование: ./deploy.sh ["commit message"]
# Pages раздаёт ветку gh-pages → https://namebogsecret.github.io/tutoring-landing/
# (кастомный домен аккаунта: http://git.podlevskikh.com/tutoring-landing/)
set -euo pipefail
cd "$(dirname "$0")"
git add -A
if git diff --cached --quiet; then
  echo "Нечего деплоить — нет изменений."
  exit 0
fi
git -c user.email="armenia.mail.vladimir@gmail.com" -c user.name="Vladimir Podlevskikh" \
  commit -qm "${1:-update landing}"
git push -q origin gh-pages
echo "✓ Запушено. Pages пересоберётся за ~1 мин:"
echo "  https://namebogsecret.github.io/tutoring-landing/"
