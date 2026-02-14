#!/usr/bin/env python3
"""
MGK MACHINE STRUCTURE EXTRACTOR
================================

Extrahiert reine Strukturdaten aus der Menschheitsgedächtniskarte.
Ignoriert Semantik. Extrahiert nur:
- Knoten (Nodes)
- Kanten (Edges)
- Typen
- Verbindungsmuster
- Dichte
- Zyklen

KEINE menschliche Lesbarkeit.
"""

import json
import os
from pathlib import Path
from collections import defaultdict, Counter
import hashlib
from typing import Dict, List, Set, Tuple, Any

class MachineStructureExtractor:
    """Reine Strukturextraktion ohne menschliche Interpretation."""
    
    def __init__(self, base_path: str = "../../"):
        self.base_path = Path(base_path)
        self.nodes = {}  # id -> node_data
        self.edges = []  # list of edge_data
        self.node_types = Counter()
        self.edge_types = Counter()
        self.connection_counts = defaultdict(int)
        self.orphan_nodes = set()
        self.cycle_candidates = set()
        
    def scan_json_files(self):
        """Scannt rekursiv alle JSON-Dateien."""
        print("[SCAN] Starte rekursiven JSON-Scan...")
        
        json_files = list(self.base_path.rglob("*.json"))
        print(f"[SCAN] {len(json_files)} JSON-Dateien gefunden")
        
        for file_path in json_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.process_data(data, str(file_path))
            except Exception as e:
                # Ignoriere nicht-JSON-Dateien
                continue
        
        print(f"[EXTRACT] {len(self.nodes)} Nodes extrahiert")
        print(f"[EXTRACT] {len(self.edges)} Edges extrahiert")
        
    def process_data(self, data: Any, source: str):
        """Verarbeitet JSON-Daten und extrahiert Struktur."""
        
        # Node-Erkennung
        if isinstance(data, dict):
            if self.is_node(data):
                node_id = data.get('id', self.generate_id(data))
                self.nodes[node_id] = {
                    'id': node_id,
                    'type': data.get('type', 'unknown'),
                    'source': source,
                    'has_connections': bool(data.get('connections')),
                    'connection_count': len(data.get('connections', [])),
                    'epistemic_layer': data.get('metadata', {}).get('epistemic_layer', 'L0'),
                    'resonance_layer': data.get('metadata', {}).get('resonance_layer', 'R0')
                }
                self.node_types[data.get('type', 'unknown')] += 1
                
                # Connections extrahieren
                for conn in data.get('connections', []):
                    edge = {
                        'from': node_id,
                        'to': conn.get('target_id'),
                        'type': conn.get('type', 'UNKNOWN'),
                        'strength': conn.get('strength', 0.5),
                        'direction': conn.get('direction', 'directed')
                    }
                    if edge['to']:
                        self.edges.append(edge)
                        self.edge_types[edge['type']] += 1
                        self.connection_counts[node_id] += 1
            
            # Edge-Erkennung (auch als separates Objekt)
            elif self.is_edge(data):
                edge = {
                    'from': data.get('from'),
                    'to': data.get('to'),
                    'type': data.get('type', 'UNKNOWN'),
                    'strength': data.get('strength', 0.5),
                    'direction': data.get('direction', 'directed')
                }
                if edge['from'] and edge['to']:
                    self.edges.append(edge)
                    self.edge_types[edge['type']] += 1
                    self.connection_counts[edge['from']] += 1
        
        # Rekursiv in verschachtelten Strukturen
        elif isinstance(data, list):
            for item in data:
                self.process_data(item, source)
    
    def is_node(self, data: dict) -> bool:
        """Prüft, ob Daten ein Node sind."""
        return bool(
            isinstance(data, dict) and
            'id' in data and
            'type' in data and
            data.get('type') in ['individual', 'place', 'concept', 'event', 
                                   'pattern', 'institution', 'document', 
                                   'candidate', 'marker', 'rubric', 
                                   'vocabulary', 'zeitgeist_witness']
        )
    
    def is_edge(self, data: dict) -> bool:
        """Prüft, ob Daten eine Edge sind."""
        return bool(
            isinstance(data, dict) and
            'from' in data and
            'to' in data and
            'type' in data
        )
    
    def generate_id(self, data: dict) -> str:
        """Generiert ID aus Hash der Daten."""
        data_str = json.dumps(data, sort_keys=True)
        return hashlib.md5(data_str.encode()).hexdigest()[:12]
    
    def analyze_structure(self):
        """Analysiert die extrahierte Struktur."""
        print("[ANALYSIS] Berechne strukturelle Metriken...")
        
        # Orphan Nodes (keine Connections)
        all_connected = set()
        for edge in self.edges:
            all_connected.add(edge['from'])
            all_connected.add(edge['to'])
        
        self.orphan_nodes = set(self.nodes.keys()) - all_connected
        
        # Zyklus-Kandidaten (Nodes, die aufeinander verweisen)
        for edge in self.edges:
            from_node = edge['from']
            to_node = edge['to']
            # Prüfe, ob es auch eine Rückverbindung gibt
            for other_edge in self.edges:
                if other_edge['from'] == to_node and other_edge['to'] == from_node:
                    self.cycle_candidates.add(tuple(sorted([from_node, to_node])))
        
        # Dichte-Analyse
        self.density_metrics = {
            'avg_connections': sum(self.connection_counts.values()) / len(self.connection_counts) if self.connection_counts else 0,
            'max_connections': max(self.connection_counts.values()) if self.connection_counts else 0,
            'isolated_nodes': len(self.orphan_nodes),
            'cycle_count': len(self.cycle_candidates)
        }
        
        print(f"[ANALYSIS] Durchschnittliche Verbindungen: {self.density_metrics['avg_connections']:.2f}")
        print(f"[ANALYSIS] Maximale Verbindungen: {self.density_metrics['max_connections']}")
        print(f"[ANALYSIS] Isolierte Nodes: {self.density_metrics['isolated_nodes']}")
        print(f"[ANALYSIS] Zyklus-Kandidaten: {self.density_metrics['cycle_count']}")
    
    def export_graph_json(self, output_path: str):
        """Exportiert Graph im JSON-Format."""
        graph_data = {
            'nodes': [
                {
                    'id': n['id'],
                    'type': n['type'],
                    'degree': self.connection_counts.get(n['id'], 0),
                    'epistemic_layer': n['epistemic_layer'],
                    'resonance_layer': n['resonance_layer']
                }
                for n in self.nodes.values()
            ],
            'edges': self.edges,
            'metrics': self.density_metrics,
            'type_distribution': dict(self.node_types),
            'edge_distribution': dict(self.edge_types)
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(graph_data, f, indent=2)
        print(f"[EXPORT] Graph-Daten exportiert: {output_path}")
    
    def export_gephi_nodes(self, output_path: str):
        """Exportiert Nodes im Gephi-CSV-Format."""
        lines = ['id,type,degree,epistemic_layer,resonance_layer']
        for node in self.nodes.values():
            lines.append(f"{node['id']},{node['type']},{self.connection_counts.get(node['id'], 0)},{node['epistemic_layer']},{node['resonance_layer']}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"[EXPORT] Gephi Nodes exportiert: {output_path}")
    
    def export_gephi_edges(self, output_path: str):
        """Exportiert Edges im Gephi-CSV-Format."""
        lines = ['source,target,type,strength,direction']
        for edge in self.edges:
            lines.append(f"{edge['from']},{edge['to']},{edge['type']},{edge['strength']},{edge['direction']}")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        print(f"[EXPORT] Gephi Edges exportiert: {output_path}")
    
    def generate_structure_report(self, output_path: str):
        """Generiert strukturellen Metabericht."""
        report = []
        report.append("# MACHINE VIEW STRUCTURE REPORT")
        report.append("=" * 50)
        report.append("")
        report.append("## STRUKTURELLE METRIKEN")
        report.append(f"- Nodes: {len(self.nodes)}")
        report.append(f"- Edges: {len(self.edges)}")
        report.append(f"- Orphan Nodes: {len(self.orphan_nodes)}")
        report.append(f"- Cycle Candidates: {len(self.cycle_candidates)}")
        report.append(f"- Avg Degree: {self.density_metrics['avg_connections']:.2f}")
        report.append(f"- Max Degree: {self.density_metrics['max_connections']}")
        report.append("")
        report.append("## TYPE DISTRIBUTION")
        for node_type, count in self.node_types.most_common():
            pct = (count / len(self.nodes)) * 100
            report.append(f"- {node_type}: {count} ({pct:.1f}%)")
        report.append("")
        report.append("## EDGE TYPE DISTRIBUTION")
        for edge_type, count in self.edge_types.most_common():
            pct = (count / len(self.edges)) * 100 if self.edges else 0
            report.append(f"- {edge_type}: {count} ({pct:.1f}%)")
        report.append("")
        report.append("## HOCHVERNETZTE NODES (>10 Connections)")
        high_degree = [(n, d) for n, d in self.connection_counts.items() if d > 10]
        high_degree.sort(key=lambda x: x[1], reverse=True)
        for node_id, degree in high_degree[:20]:
            node_type = self.nodes.get(node_id, {}).get('type', 'unknown')
            report.append(f"- {node_id} ({node_type}): {degree} connections")
        report.append("")
        report.append("## ISOLIERTTE FRAGMENTE")
        report.append(f"- {len(self.orphan_nodes)} Nodes ohne Verbindungen")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(report))
        print(f"[EXPORT] Structure Report exportiert: {output_path}")

if __name__ == "__main__":
    extractor = MachineStructureExtractor()
    extractor.scan_json_files()
    extractor.analyze_structure()
    
    # Exporte
    os.makedirs("output", exist_ok=True)
    extractor.export_graph_json("output/machine_graph.json")
    extractor.export_gephi_nodes("output/gephi_nodes.csv")
    extractor.export_gephi_edges("output/gephi_edges.csv")
    extractor.generate_structure_report("output/STRUCTURE_ANALYSIS.md")
    
    print("\n[DONE] Strukturextraktion abgeschlossen.")