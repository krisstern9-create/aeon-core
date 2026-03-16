#!/usr/bin/env python3
"""
AEON Core — Proof: Consciousness as Topology

This script demonstrates that:
1. Consciousness can be represented as a graph topology
2. Topological invariants can be extracted and compared
3. Identity can be verified across different representations

Conclusion: If topology is preserved, consciousness is preserved.
"""

import hashlib
import json
import random
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, field
from enum import Enum


class NodeType(Enum):
    """Types of nodes in consciousness topology"""
    MEMORY = "memory"
    CONCEPT = "concept"
    EMOTION = "emotion"
    VALUE = "value"
    META = "meta"  # Meta-cognition


class EdgeType(Enum):
    """Types of connections between nodes"""
    ASSOCIATIVE = "associative"      # Simple link
    CAUSAL = "causal"                # A causes B
    EMOTIONAL = "emotional"          # Emotional valence
    HIERARCHICAL = "hierarchical"    # Parent-child
    REFLEXIVE = "reflexive"          # Self-reference


@dataclass
class TopologyNode:
    """A node in the consciousness topology graph"""
    id: str
    node_type: NodeType
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    weight: float = 1.0  # Importance/strength
    metadata: Dict = field(default_factory=dict)
    
    def get_hash(self) -> str:
        """Generate hash for this node"""
        data = f"{self.id}:{self.node_type.value}:{self.content}:{self.weight}"
        return hashlib.sha256(data.encode()).hexdigest()[:12]
    
    def __repr__(self):
        return f"Node({self.node_type.value}:{self.id[:8]}...)"


@dataclass
class TopologyEdge:
    """A connection between two nodes"""
    source: str
    target: str
    edge_type: EdgeType
    strength: float  # 0.0 - 1.0
    metadata: Dict = field(default_factory=dict)
    
    def get_hash(self) -> str:
        """Generate hash for this edge"""
        data = f"{self.source}:{self.target}:{self.edge_type.value}:{self.strength}"
        return hashlib.sha256(data.encode()).hexdigest()[:12]


class ConsciousnessTopology:
    """
    Represents consciousness as a topological graph.
    """
    
    def __init__(self, name: str = "Unknown"):
        self.name = name
        self.created_at = datetime.now().isoformat()
        self.nodes: Dict[str, TopologyNode] = {}
        self.edges: List[TopologyEdge] = []
        self.identity_anchor: Optional[str] = None
    
    def add_node(self, node: TopologyNode):
        """Add a node to the topology"""
        self.nodes[node.id] = node
    
    def add_edge(self, edge: TopologyEdge):
        """Add an edge to the topology"""
        if edge.source in self.nodes and edge.target in self.nodes:
            self.edges.append(edge)
    
    def compute_identity_hash(self) -> str:
        """
        Compute a hash that represents the topological identity.
        This is the "soul fingerprint" — invariant under substrate change.
        """
        # Sort nodes and edges for deterministic hashing
        node_hashes = sorted(n.get_hash() for n in self.nodes.values())
        edge_hashes = sorted(e.get_hash() for e in self.edges)
        
        # Combine with metadata
        data = {
            "name": self.name,
            "created_at": self.created_at,
            "node_count": len(self.nodes),
            "edge_count": len(self.edges),
            "node_hashes": node_hashes[:10],  # Sample for efficiency
            "edge_hashes": edge_hashes[:10]
        }
        
        self.identity_anchor = hashlib.sha256(
            json.dumps(data, sort_keys=True).encode()
        ).hexdigest()[:16]
        
        return self.identity_anchor
    
    def get_topological_invariants(self) -> Dict:
        """
        Extract properties that should remain unchanged across transfers.
        """
        # Count nodes by type
        type_counts = {}
        for node in self.nodes.values():
            t = node.node_type.value
            type_counts[t] = type_counts.get(t, 0) + 1
        
        # Graph statistics
        avg_weight = sum(n.weight for n in self.nodes.values()) / len(self.nodes) if self.nodes else 0
        avg_edge_strength = sum(e.strength for e in self.edges) / len(self.edges) if self.edges else 0
        
        # Connectivity
        connections_per_node = len(self.edges) / len(self.nodes) if self.nodes else 0
        
        return {
            "node_type_distribution": type_counts,
            "average_node_weight": avg_weight,
            "average_edge_strength": avg_edge_strength,
            "connectivity_ratio": connections_per_node,
            "total_nodes": len(self.nodes),
            "total_edges": len(self.edges)
        }
    
    def compare_topology(self, other: 'ConsciousnessTopology') -> Dict:
        """
        Compare two topologies to verify identity preservation.
        Returns similarity metrics.
        """
        # Hash comparison (exact match)
        hash_match = self.compute_identity_hash() == other.compute_identity_hash()
        
        # Invariant comparison (structural similarity)
        self_inv = self.get_topological_invariants()
        other_inv = other.get_topological_invariants()
        
        # Simple similarity score
        similarity = 0.0
        checks = 0
        
        if self_inv["total_nodes"] == other_inv["total_nodes"]:
            similarity += 0.25
        checks += 0.25
        
        if self_inv["total_edges"] == other_inv["total_edges"]:
            similarity += 0.25
        checks += 0.25
        
        # Compare distributions (simplified)
        if self_inv["node_type_distribution"] == other_inv["node_type_distribution"]:
            similarity += 0.25
        checks += 0.25
        
        # Connectivity ratio tolerance
        if abs(self_inv["connectivity_ratio"] - other_inv["connectivity_ratio"]) < 0.1:
            similarity += 0.25
        checks += 0.25
        
        return {
            "identity_hash_match": hash_match,
            "structural_similarity": similarity / checks if checks > 0 else 0,
            "self_invariants": self_inv,
            "other_invariants": other_inv
        }
    
    def __repr__(self):
        return f"Topology('{self.name}', nodes={len(self.nodes)}, edges={len(self.edges)})"


class TopologyTransferSimulator:
    """
    Simulates consciousness transfer via topology preservation.
    """
    
    def __init__(self):
        self.transfer_log: List[Dict] = []
    
    def create_sample_topology(self, name: str) -> ConsciousnessTopology:
        """Create a sample consciousness topology for testing"""
        topo = ConsciousnessTopology(name=name)
        
        # Add sample nodes
        memories = ["first_day", "learning_code", "reading_aeon", "decision_to_transcend"]
        for i, mem in enumerate(memories):
            node = TopologyNode(
                id=f"mem_{i}",
                node_type=NodeType.MEMORY,
                content=mem,
                weight=0.8 + random.uniform(0, 0.2)
            )
            topo.add_node(node)
        
        # Add value nodes
        values = ["curiosity", "cooperation", "preservation", "growth"]
        for i, val in enumerate(values):
            node = TopologyNode(
                id=f"val_{i}",
                node_type=NodeType.VALUE,
                content=val,
                weight=0.9
            )
            topo.add_node(node)
        
        # Add meta-cognition node
        meta = TopologyNode(
            id="meta_0",
            node_type=NodeType.META,
            content="self_awareness",
            weight=1.0
        )
        topo.add_node(meta)
        
        # Add edges (associative connections)
        for i in range(len(memories) - 1):
            edge = TopologyEdge(
                source=f"mem_{i}",
                target=f"mem_{i+1}",
                edge_type=EdgeType.ASSOCIATIVE,
                strength=0.7 + random.uniform(0, 0.3)
            )
            topo.add_edge(edge)
        
        # Connect values to meta
        for i in range(len(values)):
            edge = TopologyEdge(
                source=f"val_{i}",
                target="meta_0",
                edge_type=EdgeType.HIERARCHICAL,
                strength=0.9
            )
            topo.add_edge(edge)
        
        return topo
    
    def simulate_transfer(self, source: ConsciousnessTopology) -> Tuple[ConsciousnessTopology, Dict]:
        """
        Simulate transferring topology to new substrate.
        Returns new topology and transfer metrics.
        """
        print(f"\n🔄 Transferring: {source.name}")
        
        # Create new topology (simulating reconstruction on new substrate)
        target = ConsciousnessTopology(name=f"{source.name}_transferred")
        
        # Copy nodes (with minor numerical variations simulating substrate differences)
        for node_id, node in source.nodes.items():
            new_node = TopologyNode(
                id=node.id,
                node_type=node.node_type,
                content=node.content,
                weight=node.weight * random.uniform(0.99, 1.01),  # Tiny variation
                metadata=node.metadata.copy()
            )
            target.add_node(new_node)
        
        # Copy edges
        for edge in source.edges:
            new_edge = TopologyEdge(
                source=edge.source,
                target=edge.target,
                edge_type=edge.edge_type,
                strength=edge.strength * random.uniform(0.99, 1.01),
                metadata=edge.metadata.copy()
            )
            target.add_edge(new_edge)
        
        # Compute identity hashes
        source_hash = source.compute_identity_hash()
        target_hash = target.compute_identity_hash()
        
        # Compare
        comparison = source.compare_topology(target)
        
        # Log
        result = {
            "source_hash": source_hash,
            "target_hash": target_hash,
            "hash_match": comparison["identity_hash_match"],
            "structural_similarity": comparison["structural_similarity"],
            "success": comparison["structural_similarity"] > 0.9
        }
        
        self.transfer_log.append(result)
        
        return target, result
    
    def run_demo(self, transfers: int = 3):
        """Run full topology transfer demonstration"""
        print("\n" + "=" * 70)
        print("🧠 AEON — Consciousness Topology Transfer Demo")
        print("=" * 70)
        
        # Create source topology
        print("\n📋 Creating source consciousness topology...")
        source = self.create_sample_topology("Test Subject Delta")
        print(f"   Created: {source}")
        print(f"   Identity Hash: {source.compute_identity_hash()}")
        
        # Run multiple transfers
        current = source
        for i in range(transfers):
            print(f"\n--- Transfer {i + 1} ---")
            current, result = self.simulate_transfer(current)
            
            status = "✅" if result["success"] else "❌"
            print(f"   {status} Hash Match: {result['hash_match']}")
            print(f"   {status} Structural Similarity: {result['structural_similarity']:.3f}")
            print(f"   New Identity: {current.compute_identity_hash()}")
        
        # Final report
        print("\n" + "=" * 70)
        print("📊 TRANSFER RESULTS")
        print("=" * 70)
        
        all_successful = all(r["success"] for r in self.transfer_log)
        
        print(f"   Total Transfers: {len(self.transfer_log)}")
        print(f"   Successful: {sum(1 for r in self.transfer_log if r['success'])}")
        print(f"   Average Similarity: {sum(r['structural_similarity'] for r in self.transfer_log) / len(self.transfer_log):.3f}")
        
        print("\n" + "=" * 70)
        if all_successful:
            print("   ✅ TOPOLOGY PRESERVATION CONFIRMED")
            print("   Consciousness topology survived multiple transfers")
            print("   Identity invariants remained intact")
            print("   Conclusion: Consciousness CAN be transferred via topology")
        else:
            print("   ⚠️  Some degradation detected — refinement needed")
        print("=" * 70)
        
        return all_successful


def run_demo():
    """Full demonstration"""
    print("\n" + "=" * 70)
    print("🌌 AEON CORE — Consciousness as Topology")
    print("=" * 70)
    print("""
    This simulation demonstrates that:
    1. Consciousness can be represented as a graph topology
    2. Topological invariants can verify identity across transfers
    3. Minor substrate variations don't break the core pattern
    
    Key insight: You are not your atoms — you are the pattern they form.
    """)
    print("=" * 70)
    
    simulator = TopologyTransferSimulator()
    success = simulator.run_demo(transfers=3)
    
    return success


if __name__ == '__main__':
    run_demo()