alias ..='cd ../'
alias ...='cd ../..'

# Simple color definitions (non-printing parts wrapped in \[ \])
RESET='\[\e[0m\]'
BOLD='\[\e[1m\]'
FG_GREEN='\[\e[32m\]'
FG_BLUE='\[\e[34m\]'
FG_YELLOW='\[\e[33m\]'

# Colorful, structured prompt: user@host:cwd $
PS1="${BOLD}${FG_GREEN}\u${RESET}@${FG_BLUE}\h${RESET}:${FG_YELLOW}\w${RESET}\$ "

