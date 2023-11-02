#!/usr/bin/env bash
echo -e "installing homebrew\n"
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
echo -e "installing python\n"
brew install python
echo -e "installing dep\n"
python -m pip install -r requirements.txt

