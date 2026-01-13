#!/usr/bin/env bash
set -e

# Very simple bootstrap script for macOS

DOTFILES_DIR="${DOTFILES_DIR:-$HOME/dotfiles}"

echo "==> Using dotfiles directory: $DOTFILES_DIR"

if [[ ! -d "$DOTFILES_DIR" ]]; then
  echo "Dotfiles directory not found: $DOTFILES_DIR"
  exit 1
fi

cd "$DOTFILES_DIR"

echo "==> Ensuring Homebrew is installed..."
if ! command -v brew >/dev/null 2>&1; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  # Try to load Homebrew into PATH for this script
  if [[ -d /opt/homebrew/bin ]]; then
    eval "$(/opt/homebrew/bin/brew shellenv)"
  elif [[ -d /usr/local/Homebrew/bin ]]; then
    eval "$(/usr/local/Homebrew/bin/brew shellenv)"
  fi
fi

echo "==> Installing stow, git, ghostty..."
brew install stow git ghostty

echo "==> Stowing all subdirectories in $DOTFILES_DIR ..."
for dir in */; do
  name="${dir%/}"
  [[ "$name" == ".git" ]] && continue
  echo "  - stow $name"
  stow -t "$HOME" "$name"
done

echo "==> Done. Open a new terminal (or 'exec \$SHELL') to use your setup."
# 
