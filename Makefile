_checkfiles = imgdeliver/
checkfiles = $(_checkfiles) *.py
mypy_flags = --ignore-missing-imports --follow-imports=silent --check-untyped-defs --warn-no-return --warn-unused-ignores --warn-redundant-casts --show-error-context --show-column-numbers

help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    up          Updates dependencies"
	@echo  "    deps        Ensure dev dependencies are installed"
	@echo  "    check	Checks that build is sane"
	@echo  "    lint	Reports pylint violations"
	@echo  "    test	Runs all tests"
	@echo  "    redb	Rebuilds the dev DB"
	@echo  "    run 	Runs the devserver"

up:
	@cp etc/requirements.in requirements.txt
	@pip-compile -o requirements_dev.txt etc/requirements_dev.in -U

deps:
	@pip-sync requirements_dev.txt

check: deps
	@pylint -E $(checkfiles)
	@mypy $(mypy_flags) --incremental $(_checkfiles)
	@python setup.py check -mrs
	@flake8 $(checkfiles)

lint: deps
	@-pylint $(checkfiles)

test: deps
	@echo "Not Implemented"

run: deps
	@echo "Not Implemented"

doc: deps
	@echo "Not Implemented"

bench: deps
	@echo "Not Implemented"

