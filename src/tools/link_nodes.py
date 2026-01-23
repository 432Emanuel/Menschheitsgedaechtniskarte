#!/usr/bin/env python3
"""
Link Nodes Tool for Menschheitsgedächtniskarte

This script creates and manages crosslinks between all modules.
It supports both new data structures (data/) and legacy structures.

Usage:
    python link_nodes.py                    # Interactive mode
    python link_nodes.py --export <format>     # Export links
    python link_nodes.py --validate           # Validate existing links
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class NodeLinker:
    """Tool for creating crosslinks between nodes"""
    
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path).resolve()
        self.crosslinks_path = self.root_path / "shared" / "crosslinks"
        
    def get_available_nodes(self) -> Dict[str, List[str]]:
        """Get all available nodes organized by module"""
        nodes = {
            "knowledge/places": [],
            "zeitgeist_module": [],
            "modules/imperium": [],
            "modules/mythos_und_verwaltung": [],
            "family_module": [],
            "data/human_cartography": [],
            "data/modules/build_on_old": []
        }
        
        # Scan knowledge/places
        places_file = self.root_path / "knowledge" / "places" / "places_archaeoastronomy.json"
        if places_file.exists():
            with open(places_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and "nodes" in data:
                    nodes["knowledge/places"] = [n["id"] for n in data["nodes"]]
        
        # Scan modules
        for module_path in ["modules/imperium", "modules/mythos_und_verwaltung"]:
            module_dir = self.root_path / module_path
            if module_dir.exists():
                for json_file in module_dir.rglob("*.json"):
                    with open(json_file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        if isinstance(data, dict) and "id" in data:
                            nodes[module_path].append(data["id"])
        
        # Scan zeitgeist_module
        zg_index = self.root_path / "zeitgeist_module" / "Zeitgeist_index.json"
        if zg_index.exists():
            with open(zg_index, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "modules" in data:
                    nodes["zeitgeist_module"] = [m["id"] for m in data["modules"]]
        
        # Scan family_module
        fm_index = self.root_path / "family_module" / "index.json"
        if fm_index.exists():
            with open(fm_index, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "modules" in data:
                    nodes["family_module"] = [m["id"] for m in data["modules"]]
        
        # Scan data/human_cartography
        hc_individuals = self.root_path / "data" / "human_cartography" / "individuals"
        if hc_individuals.exists():
            for json_file in hc_individuals.glob("*.json"):
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, dict) and "individual_id" in data:
                        nodes["data/human_cartography"].append(data["individual_id"])
        
        # Scan data/modules/build_on_old
        bol_concepts = self.root_path / "data" / "modules" / "build_on_old" / "concepts.json"
        if bol_concepts.exists():
            with open(bol_concepts, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, dict) and "concepts" in data:
                    nodes["data/modules/build_on_old"] = [c["id"] for c in data["concepts"]]
        
        return nodes
    
    def print_available_nodes(self, nodes: Dict[str, List[str]]):
        """Print available nodes organized by module"""
        print("\n" + "="*60)
        print("AVAILABLE NODES")
        print("="*60)
        
        for module, node_list in nodes.items():
            if node_list:
                print(f"\n{module}:")
                for node_id in node_list[:10]:  # Show first 10
                    print(f"  - {node_id}")
                if len(node_list) > 10:
                    print(f"  ... and {len(node_list)-10} more")
    
    def create_link(self, link_data: Dict) -> bool:
        """Create a new crosslink"""
        try:
            # Validate required fields
            if not all(k in link_data for k in ["source_id", "target_id", "link_type"]):
                print("Error: Missing required fields (source_id, target_id, link_type)")
                return False
            
            # Add metadata
            if "metadata" not in link_data:
                link_data["metadata"] = {}
            link_data["metadata"].update({
                "created": datetime.now().strftime("%Y-%m-%d"),
                "verified": False,
                "context": "manual_entry"
            })
            
            # Generate ID if not provided
            if "id" not in link_data:
                link_data["id"] = f"LINK-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            # Add default strength
            if "strength" not in link_data:
                link_data["strength"] = 0.5
            
            # Validate strength
            if not 0.0 <= link_data["strength"] <= 1.0:
                print("Error: Strength must be between 0.0 and 1.0")
                return False
            
            # Validate link_type
            valid_types = ["supports", "contradicts", "informs", "analogous_to", 
                          "inspired_by", "resonant", "conflict", "neutral", "origin"]
            if link_data["link_type"] not in valid_types:
                print(f"Error: Invalid link_type. Valid types: {', '.join(valid_types)}")
                return False
            
            # Write to links.json
            links_file = self.crosslinks_path / "links.json"
            
            # Load existing links
            existing_links = []
            if links_file.exists():
                with open(links_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    existing_links = data.get("links", [])
            
            # Add new link
            existing_links.append(link_data)
            
            # Write back
            output_data = {
                "links": existing_links,
                "metadata": {
                    "module": "shared",
                    "file": "crosslinks/links",
                    "version": "0.1.0",
                    "created": datetime.now().strftime("%Y-%m-%d"),
                    "updated": datetime.now().strftime("%Y-%m-%d"),
                    "description": "Sammlung aller Crosslinks zwischen Modulen",
                    "schema_version": "1.0.0"
                }
            }
            
            with open(links_file, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n✓ Created link: {link_data['id']}")
            print(f"  {link_data['source_id']} --[{link_data['link_type']}]--> {link_data['target_id']}")
            print(f"  Strength: {link_data['strength']}")
            
            return True
            
        except Exception as e:
            print(f"Error creating link: {e}")
            return False
    
    def export_links(self, format: str = "json"):
        """Export all links in specified format"""
        links_file = self.crosslinks_path / "links.json"
        
        if not links_file.exists():
            print("Error: No links file found")
            return False
        
        with open(links_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if format == "json":
            print(json.dumps(data, indent=2))
        elif format == "csv":
            print("source_id,target_id,link_type,strength,description")
            for link in data.get("links", []):
                print(f"{link['source_id']},{link['target_id']},{link['link_type']},"
                      f"{link['strength']},\"{link.get('description', '')}\"")
        else:
            print(f"Error: Unknown format {format}")
            return False
        
        return True
    
    def validate_links(self):
        """Validate all existing links"""
        links_file = self.crosslinks_path / "links.json"
        
        if not links_file.exists():
            print("No links file found")
            return
        
        with open(links_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        links = data.get("links", [])
        nodes = self.get_available_nodes()
        all_nodes = []
        for node_list in nodes.values():
            all_nodes.extend(node_list)
        
        print("\n" + "="*60)
        print("LINK VALIDATION")
        print("="*60)
        print(f"Total links: {len(links)}")
        
        errors = 0
        warnings = 0
        
        for link in links:
            # Check if source exists
            if link.get("source_id") not in all_nodes:
                print(f"Warning: Source node '{link['source_id']}' not found")
                warnings += 1
            
            # Check if target exists
            if link.get("target_id") not in all_nodes:
                print(f"Warning: Target node '{link['target_id']}' not found")
                warnings += 1
            
            # Check strength range
            strength = link.get("strength", 0.5)
            if not 0.0 <= strength <= 1.0:
                print(f"Error: Invalid strength {strength} for link {link.get('id', 'unknown')}")
                errors += 1
            
            # Check link_type
            valid_types = ["supports", "contradicts", "informs", "analogous_to", 
                          "inspired_by", "resonant", "conflict", "neutral", "origin"]
            if link.get("link_type") not in valid_types:
                print(f"Error: Invalid link_type '{link.get('link_type')}' for link {link.get('id', 'unknown')}")
                errors += 1
        
        print(f"\nErrors: {errors}")
        print(f"Warnings: {warnings}")
        
        if errors == 0:
            print("✓ All links validated successfully!")
        else:
            print("✗ Validation failed!")
            sys.exit(1)


def interactive_mode():
    """Run interactive mode"""
    print("\n" + "="*60)
    print("LINK NODES TOOL")
    print("="*60 + "\n")
    
    linker = NodeLinker()
    
    # Show available nodes
    nodes = linker.get_available_nodes()
    linker.print_available_nodes(nodes)
    
    # Create links
    print("\n" + "-"*60)
    print("CREATE NEW LINK")
    print("-"*60)
    
    link_data = {}
    link_data["source_id"] = input("Source node ID: ")
    link_data["target_id"] = input("Target node ID: ")
    
    print("\nLink types: supports, contradicts, informs, analogous_to, inspired_by, resonant, conflict, neutral, origin")
    link_data["link_type"] = input("Link type: ")
    
    strength = input("Strength (0.0-1.0, default 0.5): ")
    if strength:
        link_data["strength"] = float(strength)
    
    link_data["description"] = input("Description: ")
    
    # Create link
    linker.create_link(link_data)


def main():
    parser = argparse.ArgumentParser(
        description="Create and manage crosslinks between nodes"
    )
    parser.add_argument(
        "--export",
        type=str,
        choices=["json", "csv"],
        help="Export links in specified format"
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Validate existing links"
    )
    
    args = parser.parse_args()
    
    linker = NodeLinker()
    
    if args.export:
        linker.export_links(args.export)
    elif args.validate:
        linker.validate_links()
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
