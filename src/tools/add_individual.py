#!/usr/bin/env python3
"""
Add Individual Tool for Human Cartography

This script helps add new individuals to the human_cartography system.
It validates input against humanity_potential_space.json and creates
appropriate edges to world nodes.

Usage:
    python add_individual.py                    # Interactive mode
    python add_individual.py --batch <file>    # Batch mode from JSON file
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional


class IndividualCreator:
    """Creator for new human_cartography individuals"""
    
    def __init__(self, root_path: str = "."):
        self.root_path = Path(root_path).resolve()
        self.hc_path = self.root_path / "data" / "human_cartography"
        self.individuals_path = self.hc_path / "individuals"
        self.edges_path = self.hc_path / "edges"
        self.potential_space = self._load_potential_space()
        
    def _load_potential_space(self) -> Dict:
        """Load humanity_potential_space.json"""
        hps_file = self.hc_path / "humanity_potential_space.json"
        if not hps_file.exists():
            print(f"Error: {hps_file} not found")
            sys.exit(1)
        
        with open(hps_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _calculate_zone_affinity(self, position: Dict) -> Optional[Dict]:
        """Calculate which zone this position aligns with"""
        zones = self.potential_space.get("potential_zones", [])
        
        best_zone = None
        best_score = 0
        
        for zone in zones:
            zone_profile = zone.get("dimension_profile", {})
            score = 0
            
            # Calculate simple distance score
            for dim in ["resonance_capacity", "order_tolerance", "ritual_sensitivity", 
                       "memory_depth", "edge_tolerance"]:
                if dim in position and dim in zone_profile:
                    diff = abs(position[dim] - zone_profile[dim])
                    score += (1 - diff)  # Higher score = better match
            
            if score > best_score:
                best_score = score
                best_zone = zone
        
        return best_zone
    
    def _generate_individual_id(self, name: str, birth_year: int, nationality: str) -> str:
        """Generate individual ID in format: XX-NAME-YYYY"""
        name_upper = name.upper().replace(" ", "-").replace("Ä", "AE").replace("Ö", "OE").replace("Ü", "UE")
        return f"{nationality.upper()}-{name_upper}-{birth_year}"
    
    def create_individual(self, data: Dict) -> bool:
        """Create a new individual file"""
        try:
            # Generate ID if not provided
            if "individual_id" not in data:
                if "name" not in data or "birth_year" not in data or "nationality" not in data:
                    print("Error: Missing required fields (name, birth_year, nationality)")
                    return False
                data["individual_id"] = self._generate_individual_id(
                    data["name"], data["birth_year"], data["nationality"]
                )
            
            # Validate potential_position
            if "potential_position" in data:
                zone = self._calculate_zone_affinity(data["potential_position"])
                if zone:
                    data["zone_affinity"] = zone["id"]
                    data["zone_name"] = zone["name"]
                    print(f"Zone affinity: {zone['name']}")
            
            # Add metadata
            if "metadata" not in data:
                data["metadata"] = {}
            data["metadata"].update({
                "module": "human_cartography",
                "file": f"individuals/{data['individual_id']}",
                "version": "0.1.0",
                "created": datetime.now().strftime("%Y-%m-%d"),
                "status": "active",
                "schema_version": "1.0.0"
            })
            
            # Create output file
            output_file = self.individuals_path / f"{data['individual_id']}.json"
            
            # Check if file exists
            if output_file.exists():
                overwrite = input(f"File {output_file} already exists. Overwrite? (y/N): ")
                if overwrite.lower() != 'y':
                    print("Aborted")
                    return False
            
            # Write file
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            print(f"\n✓ Created individual: {output_file}")
            
            # Ask about edges
            create_edges = input("\nCreate world edges? (y/N): ")
            if create_edges.lower() == 'y':
                self._create_edges_interactive(data["individual_id"])
            
            return True
            
        except Exception as e:
            print(f"Error creating individual: {e}")
            return False
    
    def _create_edges_interactive(self, individual_id: str):
        """Interactive edge creation"""
        edges = []
        
        print("\n--- Create World Edges ---")
        print("Available world nodes:")
        print("  knowledge/places/places_archaeoastronomy")
        print("  zeitgeist_module/ZG-001-memory-loss")
        print("  zeitgeist_module/ZG-002-order-powerlessness")
        print("  modules/imperium")
        print("  modules/mythos_und_verwaltung")
        print("  data/modules/build_on_old")
        print("  family_module/FM-001-family-core")
        
        while True:
            world_node = input("\nWorld node path (or 'done'): ")
            if world_node.lower() == 'done':
                break
            
            if not world_node:
                continue
            
            edge_type = input("Edge type (resonant/conflict/neutral/origin): ")
            if edge_type not in ["resonant", "conflict", "neutral", "origin"]:
                print("Invalid edge type")
                continue
            
            strength = input("Strength (0.0-1.0): ")
            try:
                strength = float(strength)
                if not 0.0 <= strength <= 1.0:
                    print("Strength must be between 0.0 and 1.0")
                    continue
            except ValueError:
                print("Invalid strength")
                continue
            
            description = input("Description: ")
            
            edges.append({
                "id": f"EDGE-{individual_id}-{len(edges)+1:03d}",
                "individual_id": individual_id,
                "world_node_id": world_node,
                "edge_type": edge_type,
                "strength": strength,
                "description": description,
                "timestamp": datetime.now().strftime("%Y-%m-%d"),
                "metadata": {
                    "verified": False,
                    "context": "manual_entry"
                }
            })
            
            print(f"✓ Added edge {len(edges)}")
        
        if edges:
            self._write_edges(individual_id, edges)
    
    def _write_edges(self, individual_id: str, edges: list):
        """Write edges to file"""
        edges_file = self.edges_path / "human_world_edges.json"
        
        # Load existing edges
        existing_edges = []
        if edges_file.exists():
            with open(edges_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                existing_edges = data.get("edges", [])
        
        # Merge edges
        all_edges = existing_edges + edges
        
        # Write back
        output_data = {
            "edges": all_edges,
            "metadata": {
                "module": "human_cartography",
                "file": "edges/human_world_edges",
                "version": "0.1.0",
                "updated": datetime.now().strftime("%Y-%m-%d"),
                "description": "Sammlung aller Verbindungen Individuum ↔ Welt",
                "schema_version": "1.0.0"
            }
        }
        
        with open(edges_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✓ Added {len(edges)} edges to {edges_file}")


def interactive_mode():
    """Run interactive mode"""
    print("\n" + "="*60)
    print("HUMAN CARTOGRAPHY - ADD INDIVIDUAL")
    print("="*60 + "\n")
    
    creator = IndividualCreator()
    
    data = {}
    
    # Collect basic info
    data["name"] = input("Name: ")
    data["birth_year"] = int(input("Birth year: "))
    data["nationality"] = input("Nationality (2-letter code, e.g., DE): ")
    data["description"] = input("Description: ")
    
    # Collect potential position
    print("\n--- Potential Position (0.0-1.0 for each dimension) ---")
    print("Dimensions:")
    print("  Resonance Capacity: Ability to resonate with collective memories")
    print("  Order Tolerance: Tolerance for hierarchical structures")
    print("  Ritual Sensitivity: Sensitivity to ritual structures")
    print("  Memory Depth: Accessibility of memory")
    print("  Edge Tolerance: Tolerance for threshold situations")
    
    data["potential_position"] = {
        "resonance_capacity": float(input("  Resonance Capacity (0.0-1.0): ")),
        "order_tolerance": float(input("  Order Tolerance (0.0-1.0): ")),
        "ritual_sensitivity": float(input("  Ritual Sensitivity (0.0-1.0): ")),
        "memory_depth": float(input("  Memory Depth (0.0-1.0): ")),
        "edge_tolerance": float(input("  Edge Tolerance (0.0-1.0): "))
    }
    
    # Perspective
    print("\n--- Perspective ---")
    data["perspective"] = {
        "primary_focus": input("Primary focus: "),
        "research_interests": input("Research interests (comma-separated): ").split(","),
        "methodological_approach": input("Methodological approach: "),
        "key_concepts": input("Key concepts (comma-separated): ").split(",")
    }
    
    # Create
    creator.create_individual(data)


def batch_mode(input_file: Path):
    """Run batch mode from JSON file"""
    print(f"\nBatch mode: {input_file}")
    
    if not input_file.exists():
        print(f"Error: {input_file} not found")
        sys.exit(1)
    
    with open(input_file, 'r', encoding='utf-8') as f:
        individuals = json.load(f)
    
    creator = IndividualCreator()
    
    if isinstance(individuals, list):
        for i, individual in enumerate(individuals):
            print(f"\n--- Individual {i+1}/{len(individuals)} ---")
            creator.create_individual(individual)
    else:
        creator.create_individual(individuals)


def main():
    parser = argparse.ArgumentParser(
        description="Add individual to human cartography"
    )
    parser.add_argument(
        "--batch",
        type=Path,
        help="Batch mode: read individuals from JSON file"
    )
    
    args = parser.parse_args()
    
    if args.batch:
        batch_mode(args.batch)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()
