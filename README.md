# Modular pre-commit git hooks built in python3

See https://gist.github.com/carlos-jenkins/89da9dcf9e0d528ac978311938aade43 for the original script

A new folder .githooks contains the main pre-commit script that calls the sub hooks in pre-commit.d

pre-commit listens to git status for file changes and passes the list of files to each sub-hook.

A Makefile makes sure that all hooks are executable and changes the repository default folder for git hooks to .githooks

Currently the script doesn't differentiate between staged and unstaged changes.
And it hates the README file.

use `git commit --no-verify` to commit without checks
