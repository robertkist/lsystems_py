RM := rm
ECHO := echo
TEE := tee
UIC := /opt/homebrew/Cellar/qt@5/5.15.2_1/bin/uic -g=python

# Runs mypy test on a specific file or directory
define run_mypy
	mypy \
	--disallow-any-generics \
	--ignore-missing-imports \
	--no-incremental \
	--strict-equality \
	--disallow-incomplete-defs \
	--disallow-redefinition \
	--disallow-untyped-globals \
	--no-implicit-optional \
	--no-implicit-reexport \
	--warn-redundant-casts \
	--warn-unused-ignores \
	--warn-unreachable \
	--warn-no-return \
	--disallow-untyped-calls \
	--disallow-untyped-defs \
	--check-untyped-defs \
	--disallow-any-generics \
	--warn-return-any \
	$(1) | $(TEE) -a ./mypy.out
endef

# Runs pylint test on a specific file or directory
define run_pylint
	pylint \
	--reports=n \
	--score=n \
	--ignore-patterns=.*_ui.py \
	--extension-pkg-whitelist=PySide2,shiboken2 \
	--msg-template="{path}:{module}:{line}: [{msg_id}({symbol}), {obj}] {msg}"\
	--jobs=0 \
	-d unsubscriptable-object \
	-d consider-iterating-dictionary \
	-d missing-module-docstring \
	-d too-many-instance-attributes \
	-d too-few-public-methods \
	-d too-many-public-methods \
	-d too-many-arguments \
	-d too-many-locals \
	-d too-many-statements \
	-d too-many-lines \
	-d duplicate-code \
	-d invalid-name \
	-d no-self-use \
	-d import-error \
	-d line-too-long \
	-d fixme \
	-d ungrouped-imports \
	-d raise-missing-from \
	-d consider-using-enumerate \
	-d too-many-branches \
	-d too-many-nested-blocks \
	-d bad-continuation \
	$(1) | $(TEE) -a ./pylint.out
endef

# Runs flake8 test on a specific file or directory
define run_flake8
	flake8 \
	--ignore E501,F401,F403,C901,W504,E722,E129,E126,E127 \
	--format=pylint \
	$(1) | $(TEE) -a ./flake8.out
endef

.PHONY: all
all:
	@$(ECHO) "This Makefile has the following targets:"
	@$(ECHO) "* test - runs all the tests"
	@$(ECHO) "* gui  - builds the Qt GUI from the .ui file"

.PHONY: gui
gui:
	@$(UIC) "src/gui/mainwindow_ui.ui" -o "src/gui/mainwindow_ui.py"

.PHONY: test
test:
	-@$(RM) -f ./mypy.out
	-@$(RM) -f ./pylint.out
	-@$(RM) -f ./flake8.out
	-@$(call run_mypy, ./src/lsys/lturtle.py)
	-@$(call run_mypy, ./src/lsys/lsystem.py)
	-@$(call run_pylint, ./src/lsys/lturtle.py)
	-@$(call run_pylint, ./src/lsys/lsystem.py)
	-@$(call run_flake8, ./src/lsys/lturtle.py)
	-@$(call run_flake8, ./src/lsys/lsystem.py)
	-@$(call run_flake8, ./src/main_gui.py)