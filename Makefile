.PHONY: validate validate-json self-check-link help

help:  ## Zeigt diese Hilfe
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

validate:  ## Validiert alle JSON-Dateien im Repo
	@python3 src/validate/validate_json.py --path .

validate-json:  ## Validiert mit JSON-Report nach stdout
	@python3 src/validate/validate_json.py --path . --json-report -

self-check-link:  ## Führt Self-Check für link_nodes aus
	@python3 src/tools/self_check_link_nodes.py