# set default python
export PATH="/usr/local/opt/python@3.11/libexec/bin:$PATH"

export PFUNIT_DIR="/Users/rblack/lib/NASA"
export FC="gfortran"

# normal command search path
export PATH=/usr/local/sbin:$PATH
export PATH=/Users/rblack/bin:$PATH

# xfoil and X11 live here
export PATH=/opt/bin:$PATH

# access tokens
export GITHUB_ACCESS_TOKEN=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
export SUDOPW=pj42x925

# direnv 
eval "$(direnv hook zsh)"

# XCode command manager
XCBASE=`xcrun --show-sdk-path`
export C_INCLUDE_PATH=$XCBASE/usr/include
export CPLUS_INCLUDE_PATH=$XCBASE/usr/include
export LIBRARY_PATH=$XCBASE/usr/lib
export OMP_NUM_THREADS=4

# load aliases
. ~/.zsh_aliases
export DISPLAY=:0.0

export PATH="/usr/local/opt/ssh-copy-id/bin:$PATH"

# Created by `pipx` on 2022-11-21 11:07:15
export PATH="$PATH:/Users/rblack/.local/bin"

[ -f "/Users/rblack/.ghcup/env" ] && source "/Users/rblack/.ghcup/env" # ghcup-env
export PATH="/usr/local/opt/postgresql@15/bin:$PATH"
export LSCOLORS="EHfxcxdxBxegecabagacad"
