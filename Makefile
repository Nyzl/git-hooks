init:
	git config core.hooksPath .githooks
	chmod +x .githooks/pre-commit
	chmod +x .githooks/pre-commit.d/*
