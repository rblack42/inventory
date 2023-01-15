Ubuntu 20.04 Setup
##################

..	code-block::

	chmod 700 ~/.ssh
	chmod 644 ~/.ssh/id_rsa.pub
    chmod 600 ~/.ssh/id_rsa

	eval ""$(ssh-agent -s)"
	ssh-add ~/.ssh/id_rsa

	sudo apt install terminator zsh
	sh-c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

	git clone https://github.com/powerline/fonts.git --depth=1
	cd fonts
	./install.sh
	cd ..
	rm -rf fonts

	nano ~/.zshrc

	ZSH_THEME="agnoster"

	<sve/exit

	
