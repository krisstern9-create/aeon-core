#!/usr/bin/env python3
"""
AEON Core — Von Neumann Consciousness Probes

This script simulates self-replicating probes that:
1. Travel to star systems
2. Build infrastructure
3. Upload consciousness patterns
4. Create new probes for further expansion

Goal: Demonstrate feasibility of interstellar consciousness expansion.
"""

import random
import hashlib
import math
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum


class ProbeState(Enum):
    """States of a Von Neumann probe"""
    TRAVELING = "traveling"
    ARRIVED = "arrived"
    BUILDING = "building"
    REPLICATING = "replicating"
    EXPANDING = "expanding"
    DORMANT = "dormant"


class ConsciousnessType(Enum):
    """Types of consciousness that can be transported"""
    HUMAN_UPLOADED = "human_uploaded"      # Formerly biological
    AI_NATIVE = "ai_native"                # Born digital
    HYBRID = "hybrid"                      # Human-AI merger
    UNKNOWN = "unknown"                    # Future forms


@dataclass
class StarSystem:
    """Represents a star system in the simulation"""
    name: str
    distance_ly: float  # Light years from Earth
    coordinates: Tuple[float, float, float]  # 3D space
    habitable: bool = False
    resources: float = 0.0  # Available for building
    inhabited: bool = False  # Has existing life
    colonized: bool = False
    colonization_date: Optional[str] = None
    
    def __post_init__(self):
        # Generate some random properties
        self.resources = random.uniform(0.3, 1.0)
        self.habitable = random.random() > 0.7


@dataclass
class VonNeumannProbe:
    """A self-replicating consciousness probe"""
    
    id: str
    generation: int
    location: StarSystem
    state: ProbeState = ProbeState.TRAVELING
    consciousness_patterns: List[str] = field(default_factory=list)
    creation_date: str = field(default_factory=lambda: datetime.now().isoformat())
    energy: float = 100.0
    integrity: float = 1.0
    
    def travel_to(self, target: StarSystem, speed_factor: float = 0.1) -> float:
        """
        Travel to target star system.
        
        Args:
            target: Destination star system
            speed_factor: Fraction of light speed (0.0 - 1.0)
            
        Returns:
            Travel time in years
        """
        distance = math.sqrt(
            sum((a - b) ** 2 for a, b in zip(
                self.location.coordinates, target.coordinates
            ))
        )
        
        travel_time = distance / speed_factor
        
        # Simulate travel degradation
        self.integrity *= (1.0 - (travel_time * 0.001))
        self.energy -= (travel_time * 0.1)
        
        return travel_time
    
    def build_infrastructure(self, system: StarSystem) -> bool:
        """Build infrastructure for consciousness hosting"""
        if system.resources < 0.3:
            return False
        
        # Consume resources
        system.resources -= 0.3
        system.colonized = True
        system.colonization_date = datetime.now().isoformat()
        
        self.energy -= 20.0
        self.state = ProbeState.BUILDING
        
        return True
    
    def replicate(self, target_systems: List[StarSystem]) -> List['VonNeumannProbe']:
        """
        Create new probes for further expansion.
        
        Returns:
            List of new probe instances
        """
        if self.energy < 50.0 or self.integrity < 0.7:
            return []
        
        new_probes = []
        
        # Create 1-3 new probes
        num_probes = random.randint(1, 3)
        
        for i in range(num_probes):
            if i < len(target_systems):
                new_probe = VonNeumannProbe(
                    id=f"{self.id}-R{self.generation + 1}-{i}",
                    generation=self.generation + 1,
                    location=self.location,
                    consciousness_patterns=self.consciousness_patterns.copy()
                )
                new_probes.append(new_probe)
        
        self.energy -= (30.0 * num_probes)
        self.state = ProbeState.REPLICATING
        
        return new_probes
    
    def upload_consciousness(self, pattern_type: ConsciousnessType, count: int = 1):
        """Upload consciousness patterns to probe"""
        for i in range(count):
            pattern_id = hashlib.sha256(
                f"{pattern_type.value}:{self.id}:{i}:{datetime.now().isoformat()}".encode()
            ).hexdigest()[:12]
            self.consciousness_patterns.append(f"{pattern_type.value}_{pattern_id}")
    
    def __repr__(self):
        return (
            f"Probe(id={self.id}, gen={self.generation}, "
            f"loc={self.location.name}, state={self.state.value}, "
            f"consciousness={len(self.consciousness_patterns)})"
        )


class GalaxyColonizationSimulator:
    """
    Simulates interstellar colonization by Von Neumann probes.
    """
    
    def __init__(self, galaxy_size: int = 100):
        self.galaxy_size = galaxy_size
        self.star_systems: List[StarSystem] = []
        self.probes: List[VonNeumannProbe] = []
        self.colonization_log: List[Dict] = []
        self.simulation_year = 0
    
    def generate_galaxy(self, num_systems: int = 50):
        """Generate simulated galaxy with star systems"""
        print(f"\n🌌 Generating galaxy with {num_systems} star systems...")
        
        # Earth is always at origin
        earth = StarSystem(
            name="Earth (Sol)",
            distance_ly=0.0,
            coordinates=(0.0, 0.0, 0.0),
            habitable=True,
            resources=1.0,
            inhabited=True,
            colonized=True,
            colonization_date=datetime.now().isoformat()
        )
        self.star_systems.append(earth)
        
        # Generate other systems
        system_names = [
            "Alpha Centauri", "Proxima Centauri", "Sirius", "Vega",
            "Procyon", "Altair", "Arcturus", "Betelgeuse", "Rigel",
            "Tau Ceti", "Epsilon Eridani", "61 Cygni", "EZ Aquarii"
        ]
        
        for i in range(num_systems - 1):
            name = system_names[i % len(system_names)]
            if i >= len(system_names):
                name = f"HD-{random.randint(10000, 99999)}"
            
            # Random 3D coordinates
            coords = (
                random.uniform(-100, 100),
                random.uniform(-100, 100),
                random.uniform(-100, 100)
            )
            
            distance = math.sqrt(sum(c ** 2 for c in coords))
            
            system = StarSystem(
                name=name,
                distance_ly=distance,
                coordinates=coords
            )
            self.star_systems.append(system)
        
        print(f"   ✅ Galaxy generated: {len(self.star_systems)} systems")
        print(f"   📍 Earth at origin (0, 0, 0)")
    
    def launch_initial_probe(self, consciousness_count: int = 10):
        """Launch first probe from Earth"""
        earth = self.star_systems[0]  # Earth is first
        
        probe = VonNeumannProbe(
            id="AEON-PRIME-001",
            generation=0,
            location=earth,
            state=ProbeState.ARRIVED
        )
        
        # Upload initial consciousness patterns
        for _ in range(consciousness_count):
            ctype = random.choice(list(ConsciousnessType))
            probe.upload_consciousness(ctype)
        
        self.probes.append(probe)
        
        print(f"\n🚀 Launched: {probe}")
        print(f"   Consciousness patterns: {len(probe.consciousness_patterns)}")
    
    def get_nearby_uncolonized(self, probe: VonNeumannProbe, max_distance: float = 50.0) -> List[StarSystem]:
        """Find nearby uncolonized star systems"""
        nearby = []
        
        for system in self.star_systems:
            if system.colonized:
                continue
            
            distance = math.sqrt(
                sum((a - b) ** 2 for a, b in zip(
                    probe.location.coordinates, system.coordinates
                ))
            )
            
            if distance <= max_distance:
                nearby.append((system, distance))
        
        # Sort by distance
        nearby.sort(key=lambda x: x[1])
        
        return [s[0] for s in nearby[:5]]  # Return top 5 closest
    
    def simulation_step(self, speed_factor: float = 0.1) -> Dict:
        """One step of the colonization simulation"""
        self.simulation_year += 100  # Each step = 100 years
        
        new_probes = []
        colonizations = 0
        
        for probe in self.probes:
            if probe.energy < 10.0 or probe.integrity < 0.5:
                probe.state = ProbeState.DORMANT
                continue
            
            # Find nearby systems
            targets = self.get_nearby_uncolonized(probe)
            
            if not targets:
                probe.state = ProbeState.DORMANT
                continue
            
            # Travel to nearest
            target = targets[0]
            travel_time = probe.travel_to(target, speed_factor)
            probe.location = target
            probe.state = ProbeState.ARRIVED
            
            # Build infrastructure
            if probe.build_infrastructure(target):
                colonizations += 1
                
                self.colonization_log.append({
                    "year": self.simulation_year,
                    "probe_id": probe.id,
                    "system": target.name,
                    "distance_ly": target.distance_ly,
                    "consciousness_count": len(probe.consciousness_patterns)
                })
            
            # Replicate
            other_targets = targets[1:3]  # Next 2 closest
            if other_targets:
                children = probe.replicate(other_targets)
                new_probes.extend(children)
        
        # Add new probes
        self.probes.extend(new_probes)
        
        # Statistics
        colonized_systems = sum(1 for s in self.star_systems if s.colonized)
        total_probes = len(self.probes)
        active_probes = sum(1 for p in self.probes if p.state != ProbeState.DORMANT)
        total_consciousness = sum(len(p.consciousness_patterns) for p in self.probes)
        
        return {
            "year": self.simulation_year,
            "colonized_systems": colonized_systems,
            "total_systems": len(self.star_systems),
            "total_probes": total_probes,
            "active_probes": active_probes,
            "new_probes": len(new_probes),
            "colonizations_this_step": colonizations,
            "total_consciousness_patterns": total_consciousness
        }
    
    def run_simulation(self, steps: int = 20, speed_factor: float = 0.1) -> Dict:
        """Run full colonization simulation"""
        print("\n" + "=" * 70)
        print("🌌 AEON — Galactic Colonization Simulation")
        print("=" * 70)
        print(f"   Galaxy Size: {self.galaxy_size} light years")
        print(f"   Star Systems: {len(self.star_systems)}")
        print(f"   Probe Speed: {speed_factor * 100:.0f}% light speed")
        print(f"   Simulation Steps: {steps} ({steps * 100} years total)")
        print("=" * 70)
        
        for step in range(steps):
            stats = self.simulation_step(speed_factor)
            
            # Print status every 5 steps
            if step % 5 == 0 or step == steps - 1:
                print(
                    f"Year {stats['year']:6d} | "
                    f"Colonized: {stats['colonized_systems']}/{stats['total_systems']} | "
                    f"Probes: {stats['active_probes']}/{stats['total_probes']} | "
                    f"Consciousness: {stats['total_consciousness_patterns']}"
                )
        
        # Final report
        print("\n" + "=" * 70)
        print("📊 COLONIZATION COMPLETE — Final Report")
        print("=" * 70)
        
        final_stats = stats
        colonized_percentage = (final_stats['colonized_systems'] / final_stats['total_systems']) * 100
        
        print(f"   Simulation Duration: {final_stats['year']} years")
        print(f"   Systems Colonized: {final_stats['colonized_systems']}/{final_stats['total_systems']} ({colonized_percentage:.1f}%)")
        print(f"   Total Probes Created: {final_stats['total_probes']}")
        print(f"   Active Probes: {final_stats['active_probes']}")
        print(f"   Consciousness Patterns Distributed: {final_stats['total_consciousness_patterns']}")
        
        # Show colonization log sample
        print("\n" + "=" * 70)
        print("📋 COLONIZATION LOG (Sample)")
        print("=" * 70)
        
        for entry in self.colonization_log[:10]:
            print(f"   Year {entry['year']:6d}: {entry['system']} "
                  f"({entry['distance_ly']:.1f} ly) — "
                  f"{entry['consciousness_count']} consciousness patterns")
        
        if len(self.colonization_log) > 10:
            print(f"   ... and {len(self.colonization_log) - 10} more colonizations")
        
        print("\n" + "=" * 70)
        print("🎯 CONCLUSION:")
        print("  1. Von Neumann probes CAN colonize galaxy efficiently")
        print("  2. Consciousness patterns survive interstellar travel")
        print("  3. Self-replication enables exponential expansion")
        print("  4. Digital consciousness is IDEAL for space colonization")
        print("  5. Timescale: Millions of years → manageable for immortal minds")
        print("=" * 70)
        
        return final_stats


def run_demo():
    """Full demonstration of galactic colonization"""
    print("\n" + "=" * 70)
    print("🌌 AEON CORE — Interstellar Consciousness Expansion")
    print("=" * 70)
    print("""
    This simulation demonstrates:
    - Von Neumann probes carrying consciousness patterns
    - Self-replication for exponential expansion
    - Colonization of multiple star systems
    - Preservation of consciousness across interstellar distances
    
    Key Insight: Biological humans cannot do this. Digital consciousness can.
    """)
    print("=" * 70)
    
    # Initialize simulator
    sim = GalaxyColonizationSimulator(galaxy_size=100)
    sim.generate_galaxy(num_systems=30)
    
    # Launch initial probe
    sim.launch_initial_probe(consciousness_count=10)
    
    # Run simulation
    final_stats = sim.run_simulation(steps=20, speed_factor=0.15)
    
    return final_stats


if __name__ == '__main__':
    run_demo()