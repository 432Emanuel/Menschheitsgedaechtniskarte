#!/usr/bin/env python3
"""
JSON Validator for Menschheitsgedächtniskarte

This script validates JSON files across the entire repository, including:
- New data structures (data/)
- Legacy structures (modules/, zeitgeist_module/, etc.)
- Custom schemas for each module type

Usage:
    python validate_json.py                    # Validate all JSON files
    python validate_json.py --path <path>       # Validate specific path
    python validate_json.py --schema <schema>   # Validate against specific schema
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import argparse

try:
    from jsonschema import validate, ValidationError
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False
    ValidationError = Exception


class LegacyAdapter:
    """Adapter for legacy JSON structures to standard format"""
    
    @staticmethod
    def adapt_node_v2(data: Dict) -> Dict:
        """Adapt legacy node_schema_v2 format to standard"""
        adapted = {
            "id": data.get("id", ""),
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "type": data.get("type", "unknown"),
            "metadata": data.get("metadata", {})
        }
        
        # Extract epistemic and resonance layers
        if "metadata" in data:
            adapted["epistemic_layer"] = data["metadata"].get("epistemic_layer", "L2")
            adapted["resonance_layer"] = data["metadata"].get("resonance_layer", "R0")
        else:
            adapted["epistemic_layer"] = "L2"
            adapted["resonance_layer"] = "R0"
        
        # Map links to connections
        if "links" in data:
            adapted["connections"] = data["links"]
        
        return adapted
    
    @staticmethod
    def adapt_imperium_entity(data: Dict) -> Dict:
        """Adapt Imperium entity format to standard"""
        return {
            "id": data.get("id", ""),
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "type": data.get("type", "entity"),
            "metadata": data.get("metadata", {}),
            "epistemic_layer": "L2",
            "resonance_layer": "R0"
        }
    
    @staticmethod
    def adapt_candidate(data: Dict) -> Dict:
        """Adapt candidate format to standard"""
        return {
            "id": data.get("id", ""),
            "name": data.get("name", ""),
            "description": data.get("description", ""),
            "type": "candidate",
            "metadata": data.get("metadata", {}),
            "epistemic_layer": "L3",
            "resonance_layer": "R2"
        }


class JSONValidator:
    """Validator for Menschheitsgedächtniskarte JSON files"""
    
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path).resolve()
        self.errors: List[Tuple[str, str]] = []
        self.warnings: List[Tuple[str, str]] = []
        self.total_files = 0
        self.valid_files = 0
        
        # Schema definitions
        self.schemas = {
            "standard_node": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "description": {"type": "string"},
                    "type": {"type": "string"},
                    "metadata": {"type": "object"},
                    "epistemic_layer": {"type": "string", "pattern": "^L[0-4]$"},
                    "resonance_layer": {"type": "string", "pattern": "^R[0-5]$"}
                }
            },
            "human_cartography_individual": {
                "type": "object",
                "required": ["individual_id", "name", "potential_position"],
                "properties": {
                    "individual_id": {"type": "string"},
                    "name": {"type": "string"},
                    "birth_year": {"type": "integer"},
                    "nationality": {"type": "string"},
                    "potential_position": {"type": "object"},
                    "world_edges": {"type": "array"},
                    "metadata": {"type": "object"}
                }
            },
            "build_on_old": {
                "type": "object",
                "required": ["metadata"],
                "properties": {
                    "concepts": {"type": "array"},
                    "patterns": {"type": "array"},
                    "rules": {"type": "array"},
                    "metadata": {"type": "object"}
                }
            }
        }
    
    def validate_file(self, file_path: Path) -> bool:
        """Validate a single JSON file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.total_files += 1
            
            # Determine schema based on file path
            schema = self._determine_schema(file_path)
            
            # Adapt if legacy format
            adapted_data = self._adapt_if_legacy(file_path, data)
            
            # Validate
            if HAS_JSONSCHEMA:
                try:
                    validate(instance=adapted_data, schema=schema)
                    self.valid_files += 1
                    return True
                except ValidationError as e:
                    self.errors.append((str(file_path), f"Validation error: {e.message}"))
                    return False
            else:
                # Basic validation without jsonschema
                return self._basic_validate(file_path, adapted_data, schema)
                
        except json.JSONDecodeError as e:
            self.errors.append((str(file_path), f"JSON decode error: {e.msg} at line {e.lineno}"))
            return False
        except Exception as e:
            self.errors.append((str(file_path), f"Unexpected error: {str(e)}"))
            return False
    
    def _determine_schema(self, file_path: Path) -> Dict:
        """Determine which schema to use based on file path"""
        path_str = str(file_path)
        
        if "human_cartography/individuals" in path_str:
            return self.schemas["human_cartography_individual"]
        elif "build_on_old" in path_str:
            return self.schemas["build_on_old"]
        elif "node_schema_v2" in path_str:
            return self.schemas["standard_node"]
        else:
            return self.schemas["standard_node"]
    
    def _adapt_if_legacy(self, file_path: Path, data: Dict) -> Dict:
        """Adapt legacy formats to standard if needed"""
        path_str = str(file_path)
        
        # Legacy node_schema_v2 format
        if "modules/imperium/entities" in path_str or \
           "modules/mythos_und_verwaltung" in path_str or \
           "knowledge/places" in path_str:
            return LegacyAdapter.adapt_node_v2(data)
        
        # Candidate format
        if "shared/candidates/items" in path_str:
            return LegacyAdapter.adapt_candidate(data)
        
        return data
    
    def _basic_validate(self, file_path: Path, data: Dict, schema: Dict) -> bool:
        """Basic validation without jsonschema library"""
        required = schema.get("required", [])
        properties = schema.get("properties", {})
        
        for field in required:
            if field not in data:
                self.errors.append((str(file_path), f"Missing required field: {field}"))
                return False
        
        for field, field_schema in properties.items():
            if field in data:
                value = data[field]
                field_type = field_schema.get("type")
                
                if field_type == "string" and not isinstance(value, str):
                    self.errors.append((str(file_path), f"Field '{field}' should be string, got {type(value).__name__}"))
                    return False
                elif field_type == "integer" and not isinstance(value, int):
                    self.errors.append((str(file_path), f"Field '{field}' should be integer, got {type(value).__name__}"))
                    return False
                elif field_type == "array" and not isinstance(value, list):
                    self.errors.append((str(file_path), f"Field '{field}' should be array, got {type(value).__name__}"))
                    return False
                elif field_type == "object" and not isinstance(value, dict):
                    self.errors.append((str(file_path), f"Field '{field}' should be object, got {type(value).__name__}"))
                    return False
        
        self.valid_files += 1
        return True
    
    def validate_directory(self, directory: Path):
        """Validate all JSON files in a directory recursively"""
        if not directory.exists():
            print(f"Error: Directory {directory} does not exist")
            return False
        
        json_files = list(directory.rglob("*.json"))
        print(f"Found {len(json_files)} JSON files to validate\n")
        
        for json_file in json_files:
            self.validate_file(json_file)
        
        return True
    
    def print_results(self):
        """Print validation results"""
        print("\n" + "="*60)
        print("VALIDATION RESULTS")
        print("="*60)
        print(f"Total files: {self.total_files}")
        print(f"Valid files: {self.valid_files}")
        print(f"Errors: {len(self.errors)}")
        print(f"Warnings: {len(self.warnings)}")
        
        if self.errors:
            print("\n" + "-"*60)
            print("ERRORS:")
            print("-"*60)
            for file_path, error in self.errors:
                print(f"  {file_path}:")
                print(f"    {error}")
        
        if self.warnings:
            print("\n" + "-"*60)
            print("WARNINGS:")
            print("-"*60)
            for file_path, warning in self.warnings:
                print(f"  {file_path}:")
                print(f"    {warning}")
        
        if not self.errors and self.total_files > 0:
            print("\n✓ All files validated successfully!")
            return 0
        else:
            print("\n✗ Validation failed!")
            return 1


def main():
    parser = argparse.ArgumentParser(
        description="Validate JSON files in Menschheitsgedächtniskarte"
    )
    parser.add_argument(
        "--path",
        type=str,
        default=".",
        help="Path to validate (default: current directory)"
    )
    parser.add_argument(
        "--schema",
        type=str,
        choices=["standard_node", "human_cartography_individual", "build_on_old"],
        help="Specific schema to validate against"
    )
    
    args = parser.parse_args()
    
    if not HAS_JSONSCHEMA:
        print("Warning: jsonschema library not found. Using basic validation.")
        print("Install with: pip install jsonschema\n")
    
    validator = JSONValidator(args.path)
    validator.validate_directory(Path(args.path))
    
    sys.exit(validator.print_results())


if __name__ == "__main__":
    main()
