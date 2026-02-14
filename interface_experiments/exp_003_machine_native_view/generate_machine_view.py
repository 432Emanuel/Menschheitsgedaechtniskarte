#!/usr/bin/env python3
"""
MGK MACHINE VIEW GENERATOR
===========================

Erzeugt rein maschinenorientierte Visualisierungen der MGK-Struktur.
KEINE menschliche Lesbarkeit. Nur Form, Dichte, Relation.
"""

import json
import random
import math
from pathlib import Path

class MachineViewGenerator:
    """Generiert maschinelle Strukturvisualisierungen."""
    
    def __init__(self, graph_file: str):
        with open(graph_file, 'r', encoding='utf-8') as f:
            self.graph = json.load(f)
        self.nodes = self.graph['nodes']
        self.edges = self.graph['edges']
        self.stats = self.graph['statistics']
        
    def generate_svg_force_directed(self, output_path: str, width: int = 2400, height: int = 1800):
        """Erzeugt Force-Directed Graph SVG ohne menschliche Labels."""
        
        # Positionen berechnen (einfache Force-Directed Simulation)
        positions = self.compute_force_layout(width, height)
        
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
        svg_parts.append('<rect width="100%" height="100%" fill="#0a0a0a"/>')
        
        # Edges zeichnen (nur Linien, keine Labels)
        for edge in self.edges:
            source = positions.get(edge['source'])
            target = positions.get(edge['target'])
            if source and target:
                # Farbe nach Typ
                edge_type = edge.get('type', 'unknown')
                if edge_type == 'directory_structure':
                    color = '#1a1a2e'
                    width = 0.5
                    opacity = 0.3
                elif edge_type == 'schema_reference':
                    color = '#16213e'
                    width = 1.5
                    opacity = 0.6
                elif edge_type == 'index_reference':
                    color = '#0f3460'
                    width = 1.0
                    opacity = 0.5
                else:
                    color = '#1a1a1a'
                    width = 0.3
                    opacity = 0.2
                
                svg_parts.append(
                    f'<line x1="{source["x"]}" y1="{source["y"]}" '
                    f'x2="{target["x"]}" y2="{target["y"]}" '
                    f'stroke="{color}" stroke-width="{width}" opacity="{opacity}"/>'
                )
        
        # Nodes zeichnen (nur Kreise, keine Labels)
        for node in self.nodes:
            pos = positions.get(node['id'])
            if not pos:
                continue
            
            # Größe nach Level (Tiefe im Verzeichnisbaum)
            level = node.get('level', 0)
            radius = 2 + (6 - level) * 1.5
            
            # Farbe nach Typ
            node_type = node.get('type', 'unknown')
            if node_type == 'root':
                color = '#e94560'
            elif node_type == 'directory':
                color = '#0f4c75'
            elif node_type == 'file':
                color = '#3282b8'
            else:
                color = '#bbe1fa'
            
            svg_parts.append(
                f'<circle cx="{pos["x"]}" cy="{pos["y"]}" r="{radius}" '
                f'fill="{color}" opacity="0.7"/>'
            )
        
        svg_parts.append('</svg>')
        
        svg_content = '\n'.join(svg_parts)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"[VISUAL] SVG exportiert: {output_path}")
    
    def compute_force_layout(self, width: int, height: int, iterations: int = 500):
        """Einfache Force-Directed Layout-Berechnung."""
        positions = {}
        
        # Initial: Zufällige Positionen
        for node in self.nodes:
            positions[node['id']] = {
                'x': random.uniform(width * 0.1, width * 0.9),
                'y': random.uniform(height * 0.1, height * 0.9)
            }
        
        # Force-Directed Iterationen
        for _ in range(iterations):
            # Repulsion (Nodes stoßen sich ab)
            for i, n1 in enumerate(self.nodes):
                for n2 in self.nodes[i+1:]:
                    pos1 = positions[n1['id']]
                    pos2 = positions[n2['id']]
                    dx = pos1['x'] - pos2['x']
                    dy = pos1['y'] - pos2['y']
                    dist = math.sqrt(dx*dx + dy*dy) + 0.1
                    force = 1000 / (dist * dist)
                    pos1['x'] += (dx / dist) * force
                    pos1['y'] += (dy / dist) * force
                    pos2['x'] -= (dx / dist) * force
                    pos2['y'] -= (dy / dist) * force
            
            # Attraction (Edges ziehen zusammen)
            for edge in self.edges:
                pos1 = positions.get(edge['source'])
                pos2 = positions.get(edge['target'])
                if pos1 and pos2:
                    dx = pos2['x'] - pos1['x']
                    dy = pos2['y'] - pos1['y']
                    dist = math.sqrt(dx*dx + dy*dy) + 0.1
                    force = dist * 0.01
                    pos1['x'] += (dx / dist) * force
                    pos1['y'] += (dy / dist) * force
                    pos2['x'] -= (dx / dist) * force
                    pos2['y'] -= (dy / dist) * force
            
            # Center Gravity (zum Zentrum ziehen)
            center_x, center_y = width / 2, height / 2
            for node in self.nodes:
                pos = positions[node['id']]
                dx = center_x - pos['x']
                dy = center_y - pos['y']
                pos['x'] += dx * 0.01
                pos['y'] += dy * 0.01
        
        return positions
    
    def generate_circular_packing(self, output_path: str, width: int = 2000, height: int = 2000):
        """Erzeugt kreisförmige Packung nach Level."""
        
        center_x, center_y = width / 2, height / 2
        max_radius = min(width, height) / 2 - 50
        
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">')
        svg_parts.append('<rect width="100%" height="100%" fill="#050505"/>')
        
        # Nodes nach Level gruppieren
        nodes_by_level = {}
        for node in self.nodes:
            level = node.get('level', 0)
            if level not in nodes_by_level:
                nodes_by_level[level] = []
            nodes_by_level[level].append(node)
        
        # Kreise von außen nach innen zeichnen
        max_level = max(nodes_by_level.keys()) if nodes_by_level else 0
        
        for level in range(max_level + 1):
            nodes = nodes_by_level.get(level, [])
            if not nodes:
                continue
            
            # Radius für dieses Level
            ring_radius = (max_level - level) / (max_level + 1) * max_radius
            
            # Nodes auf diesem Kreis platzieren
            angle_step = 2 * math.pi / len(nodes)
            
            for i, node in enumerate(nodes):
                angle = i * angle_step
                x = center_x + ring_radius * math.cos(angle)
                y = center_y + ring_radius * math.sin(angle)
                
                # Größe nach Dateityp
                node_type = node.get('type', 'unknown')
                if node_type == 'root':
                    size = 20
                elif node_type == 'directory':
                    size = 8
                elif node_type == 'file':
                    size = 4
                else:
                    size = 2
                
                # Farbe nach Kategorie
                category = node.get('category', 'unknown')
                if category == 'index':
                    color = '#ff6b6b'
                elif category == 'schema':
                    color = '#4ecdc4'
                elif category == 'data':
                    color = '#45b7d1'
                elif category == 'template':
                    color = '#96ceb4'
                elif category == 'documentation':
                    color = '#ffd93d'
                elif category == 'code':
                    color = '#6c5ce7'
                else:
                    color = '#a8e6cf'
                
                svg_parts.append(
                    f'<circle cx="{x}" cy="{y}" r="{size}" fill="{color}" opacity="0.8"/>'
                )
                
                # Verbindung zum Zentrum für Root
                if node_type == 'root':
                    svg_parts.append(
                        f'<line x1="{center_x}" y1="{center_y}" x2="{x}" y2="{y}" '
                        f'stroke="#e94560" stroke-width="2" opacity="0.3"/>'
                    )
        
        svg_parts.append('</svg>')
        
        svg_content = '\n'.join(svg_parts)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"[VISUAL] Circular Packing exportiert: {output_path}")
    
    def generate_density_map(self, output_path: str, width: int = 100, height: int = 100):
        """Erzeugt Dichtekarte als Heatmap."""
        
        # Raster initialisieren
        grid = [[0 for _ in range(width)] for _ in range(height)]
        
        # Nodes auf Raster projizieren
        for node in self.nodes:
            level = node.get('level', 0)
            # Einfache Projektion: Level -> Y-Position, zufällig -> X-Position
            y = int((level / 6) * height)
            x = hash(node['id']) % width
            
            # Dichte erhöhen (mit Radius)
            radius = 3
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    ny = (y + dy) % height
                    nx = (x + dx) % width
                    grid[ny][nx] += 1
        
        # Maximalwert für Normalisierung
        max_density = max(max(row) for row in grid) if grid else 1
        
        # SVG mit Rechtecken (Pixel)
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width*10} {height*10}">')
        svg_parts.append('<rect width="100%" height="100%" fill="#000000"/>')
        
        for y in range(height):
            for x in range(width):
                density = grid[y][x]
                if density > 0:
                    # Farbe nach Dichte (von Blau nach Rot)
                    intensity = min(1.0, density / max_density)
                    r = int(255 * intensity)
                    b = int(255 * (1 - intensity))
                    color = f'rgb({r},0,{b})'
                    
                    svg_parts.append(
                        f'<rect x="{x*10}" y="{y*10}" width="10" height="10" fill="{color}" opacity="0.8"/>'
                    )
        
        svg_parts.append('</svg>')
        
        svg_content = '\n'.join(svg_parts)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"[VISUAL] Density Map exportiert: {output_path}")
    
    def generate_connection_matrix(self, output_path: str, size: int = 500):
        """Erzeugt Verbindungsmatrix als Pixelbild."""
        
        # Node-ID zu Index-Mapping
        node_ids = [n['id'] for n in self.nodes]
        node_index = {nid: i for i, nid in enumerate(node_ids)}
        n = len(node_ids)
        
        # Matrix initialisieren
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        # Verbindungen eintragen
        for edge in self.edges:
            source_idx = node_index.get(edge['source'])
            target_idx = node_index.get(edge['target'])
            if source_idx is not None and target_idx is not None:
                matrix[source_idx][target_idx] += 1
        
        # SVG mit Pixeln
        pixel_size = size / n
        svg_parts = []
        svg_parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">')
        svg_parts.append('<rect width="100%" height="100%" fill="#000000"/>')
        
        max_connections = max(max(row) for row in matrix) if matrix else 1
        
        for i in range(n):
            for j in range(n):
                connections = matrix[i][j]
                if connections > 0:
                    intensity = connections / max_connections
                    gray = int(255 * intensity)
                    color = f'rgb({gray},{gray},{gray})'
                    
                    svg_parts.append(
                        f'<rect x="{j*pixel_size}" y="{i*pixel_size}" '
                        f'width="{pixel_size-0.5}" height="{pixel_size-0.5}" fill="{color}"/>'
                    )
        
        svg_parts.append('</svg>')
        
        svg_content = '\n'.join(svg_parts)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"[VISUAL] Connection Matrix exportiert: {output_path}")

if __name__ == "__main__":
    generator = MachineViewGenerator("../../repo_structure_network.json")
    
    # Output-Verzeichnis
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Verschiedene Visualisierungen generieren
    print("[GEN] Generiere maschinelle Visualisierungen...")
    generator.generate_svg_force_directed(output_dir / "machine_view_force_directed.svg")
    generator.generate_circular_packing(output_dir / "machine_view_circular_packing.svg")
    generator.generate_density_map(output_dir / "machine_view_density_map.svg")
    generator.generate_connection_matrix(output_dir / "machine_view_connection_matrix.svg")
    
    print("\n[DONE] Alle Visualisierungen generiert.")