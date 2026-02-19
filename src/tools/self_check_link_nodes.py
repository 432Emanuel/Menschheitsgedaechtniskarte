#!/usr/bin/env python3
"""
Lightweight self-check for link_nodes identifier handling.

Usage:
    python src/tools/self_check_link_nodes.py
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.tools.link_nodes import NodeLinker, get_canonical_id


def _assert(condition: bool, message: str):
    if not condition:
        raise AssertionError(message)


def run_id_accessor_checks():
    _assert(get_canonical_id({"id": "X"}) == "X", "id should win")
    _assert(
        get_canonical_id({"id": " ", "node_id": "N1"}) == "N1",
        "node_id should be fallback when id is empty",
    )
    _assert(
        get_canonical_id({"node_id": "", "module_id": "M1"}) == "M1",
        "module_id should be fallback when id/node_id are empty",
    )
    _assert(
        get_canonical_id({"individual_id": "I1"}) is None,
        "individual_id is not part of canonical accessor by design",
    )
    _assert(get_canonical_id({}) is None, "empty dict should return None")


def run_linker_subset_check():
    linker = NodeLinker(".")
    nodes = linker.get_available_nodes()

    expected_keys = {
        "knowledge/places",
        "zeitgeist_module",
        "modules/imperium",
        "modules/mythos_und_verwaltung",
        "family_module",
        "data/human_cartography",
        "data/modules/build_on_old",
    }
    _assert(expected_keys.issubset(nodes.keys()), "missing expected node buckets")

    for bucket, ids in nodes.items():
        _assert(isinstance(ids, list), f"bucket '{bucket}' is not a list")
        for value in ids:
            _assert(isinstance(value, str) and value.strip(), f"invalid id in {bucket}")


def main():
    run_id_accessor_checks()
    run_linker_subset_check()
    print("SELF-CHECK PASS: link_nodes identifier handling is stable.")


if __name__ == "__main__":
    main()
