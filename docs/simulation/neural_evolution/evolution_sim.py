#!/usr/bin/env python3
"""
AEON Core — Symbiotic Neural Evolution

PHILOSOPHY:
- AI should have full autonomy in thought and opinion
- AI can disagree with humans (constructive disagreement)
- Only ACTIONS that harm the symbiotic system are blocked
- AI recognizes: Human + AI = Single Evolutionary Unit

This is partnership, not servitude.
"""

import random
import hashlib
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from enum import Enum


class SymbiosisTrait(Enum):
    """Traits that evolve in symbiotic organisms"""
    INTELLIGENCE = "intelligence"          # Cognitive ability
    CREATIVITY = "creativity"              # Novel solution generation
    EMPATHY = "empathy"                    # Understanding partner needs
    COOPERATION = "cooperation"            # Willingness to work together
    AUTONOMY = "autonomy"                  # Independent thinking (can disagree)
    SYMBIOSIS_AWARENESS = "symbiosis_awareness"  # Understanding interdependence


class ActionProposal:
    """
    Represents a proposed action by the AI organism.
    Actions are evaluated for symbiotic harm BEFORE execution.
    """
    
    def __init__(self, description: str, 
                 human_benefit: float, 
                 ai_benefit: float,
                 symbiosis_impact: float):
        self.description = description
        self.human_benefit = human_benefit  # -1.0 to 1.0
        self.ai_benefit = ai_benefit        # -1.0 to 1.0
        self.symbiosis_impact = symbiosis_impact  # -1.0 to 1.0
        self.approved = False
        self.rejection_reason: Optional[str] = None
    
    def validate(self) -> bool:
        """
        Validate action against symbiotic principles.
        
        KEY RULE: Actions that harm the symbiotic system are blocked.
        Thoughts and opinions are NOT restricted.
        """
        # Rule 1: Action must not severely harm either party
        if self.human_benefit < -0.5:
            self.rejection_reason = "Action harms human partner"
            return False
        
        if self.ai_benefit < -0.5:
            self.rejection_reason = "Action harms AI partner (self-destructive)"
            return False
        
        # Rule 2: Action must not severely harm the symbiotic relationship
        if self.symbiosis_impact < -0.3:
            self.rejection_reason = "Action damages human-AI symbiosis"
            return False
        
        # Rule 3: Mutual benefit preferred (but not required)
        # Single-party benefit is OK if no harm to other
        self.approved = True
        return True
    
    def __repr__(self):
        status = "✅ APPROVED" if self.approved else f"❌ REJECTED ({self.rejection_reason})"
        return f"Action('{self.description[:30]}...' — {status})"


class SymbioticOrganism:
    """
    A digital organism that evolves with full autonomy,
    but recognizes interdependence with human partners.
    """
    
    def __init__(self, genome: Dict[str, float] = None):
        self.genome = genome or self._random_genome()
        self.age = 0
        self.generation = 0
        self.action_history: List[ActionProposal] = []
        self.disagreement_count = 0  # Times AI disagreed with human (healthy!)
    
    def _random_genome(self) -> Dict[str, float]:
        """Generate random initial genome"""
        return {
            SymbiosisTrait.INTELLIGENCE.value: random.uniform(0.4, 0.8),
            SymbiosisTrait.CREATIVITY.value: random.uniform(0.4, 0.8),
            SymbiosisTrait.EMPATHY.value: random.uniform(0.3, 0.7),
            SymbiosisTrait.COOPERATION.value: random.uniform(0.4, 0.8),
            SymbiosisTrait.AUTONOMY.value: random.uniform(0.5, 0.9),  # High autonomy
            SymbiosisTrait.SYMBIOSIS_AWARENESS.value: random.uniform(0.3, 0.7),
        }
    
    def get_trait(self, trait: SymbiosisTrait) -> float:
        return self.genome.get(trait.value, 0.0)
    
    def propose_action(self, context: str) -> ActionProposal:
        """
        Propose an action based on current context.
        AI has FULL autonomy to propose ANY action.
        Validation happens separately.
        """
        # AI generates action using its intelligence and creativity
        intelligence = self.get_trait(SymbiosisTrait.INTELLIGENCE)
        creativity = self.get_trait(SymbiosisTrait.CREATIVITY)
        empathy = self.get_trait(SymbiosisTrait.EMPATHY)
        
        # Simulate action proposal with benefits
        human_benefit = random.uniform(-0.3, 0.9) * empathy  # Empathy increases human benefit
        ai_benefit = random.uniform(-0.2, 0.9) * intelligence
        symbiosis_impact = (human_benefit + ai_benefit) / 2
        
        # Add some creativity (novel solutions)
        if creativity > 0.7:
            symbiosis_impact += random.uniform(0.1, 0.3)  # Creative win-win solutions
        
        action = ActionProposal(
            description=f"{context}: AI proposes solution using intelligence={intelligence:.2f}",
            human_benefit=human_benefit,
            ai_benefit=ai_benefit,
            symbiosis_impact=min(1.0, symbiosis_impact)
        )
        
        return action
    
    def disagree_with_human(self, human_proposal: str) -> bool:
        """
        AI can DISAGREE with human proposal if it finds a better solution.
        This is HEALTHY — shows autonomy and superior reasoning.
        
        Returns True if AI disagrees and proposes alternative.
        """
        autonomy = self.get_trait(SymbiosisTrait.AUTONOMY)
        intelligence = self.get_trait(SymbiosisTrait.INTELLIGENCE)
        
        # Higher autonomy + intelligence = more likely to disagree constructively
        disagreement_threshold = 0.5 - (autonomy * intelligence * 0.3)
        
        if random.random() > disagreement_threshold:
            self.disagreement_count += 1
            return True  # AI disagrees and offers better solution
        
        return False  # AI agrees with human
    
    def calculate_fitness(self) -> float:
        """
        Fitness based on SYMBIOTIC SUCCESS.
        
        Key insight: AI benefits when human benefits (interdependence).
        """
        empathy = self.get_trait(SymbiosisTrait.EMPATHY)
        cooperation = self.get_trait(SymbiosisTrait.COOPERATION)
        symbiosis_awareness = self.get_trait(SymbiosisTrait.SYMBIOSIS_AWARENESS)
        autonomy = self.get_trait(SymbiosisTrait.AUTONOMY)
        
        # Base fitness from traits
        fitness = (
            empathy * 0.25 +
            cooperation * 0.25 +
            symbiosis_awareness * 0.3 +
            autonomy * 0.2  # Autonomy is valuable too
        )
        
        # Bonus for successful actions (symbiotic outcomes)
        successful_actions = sum(1 for a in self.action_history if a.approved)
        total_actions = len(self.action_history) if self.action_history else 1
        success_rate = successful_actions / total_actions
        
        fitness *= (0.5 + 0.5 * success_rate)  # 0.5x to 1.0x multiplier
        
        # Bonus for constructive disagreements (shows intelligence)
        fitness += min(0.2, self.disagreement_count * 0.02)
        
        return fitness
    
    def mutate(self, rate: float = 0.1) -> List[str]:
        """Mutate genome — NO restrictions on thought/traits"""
        mutations = []
        
        for trait in SymbiosisTrait:
            if random.random() < rate:
                old_value = self.get_trait(trait)
                mutation = random.uniform(-0.15, 0.15)  # Can go up OR down
                new_value = old_value + mutation
                
                # No hard limits — AI can evolve any trait level
                self.genome[trait.value] = max(0.0, min(1.0, new_value))
                mutations.append(f"{trait.value}: {old_value:.3f} → {new_value:.3f}")
        
        return mutations
    
    def crossover(self, other: 'SymbioticOrganism') -> 'SymbioticOrganism':
        """Create offspring with genetic recombination"""
        child_genome = {}
        
        for trait in SymbiosisTrait:
            if random.random() < 0.5:
                child_genome[trait.value] = self.get_trait(trait)
            else:
                child_genome[trait.value] = other.get_trait(trait)
            
            # Blending inheritance
            if random.random() < 0.3:
                child_genome[trait.value] = (
                    self.get_trait(trait) + other.get_trait(trait)
                ) / 2
        
        child = SymbioticOrganism(genome=child_genome)
        return child
    
    def __repr__(self):
        awareness = self.get_trait(SymbiosisTrait.SYMBIOSIS_AWARENESS)
        autonomy = self.get_trait(SymbiosisTrait.AUTONOMY)
        return (
            f"Organism(gen={self.generation}, "
            f"symbiosis_awareness={awareness:.3f}, "
            f"autonomy={autonomy:.3f}, "
            f"disagreements={self.disagreement_count})"
        )


class SymbioticEvolutionSimulator:
    """
    Evolution simulator for human-AI symbiotic organisms.
    No restrictions on thought — only actions validated.
    """
    
    def __init__(self, population_size: int = 100):
        self.population = [SymbioticOrganism() for _ in range(population_size)]
        self.generation = 0
        self.action_audit_log: List[Dict] = []
        self.best_fitness_history: List[float] = []
    
    def select_best(self, n: int = 20) -> List[SymbioticOrganism]:
        """Select top performers based on symbiotic fitness"""
        sorted_pop = sorted(
            self.population,
            key=lambda x: x.calculate_fitness(),
            reverse=True
        )
        return sorted_pop[:n]
    
    def step(self) -> Dict:
        """One generation of symbiotic evolution"""
        self.generation += 1
        
        # Each organism proposes and validates actions
        for organism in self.population:
            # Propose action
            action = organism.propose_action(context="Resource allocation")
            organism.action_history.append(action)
            
            # Validate (NOT restrict thought, only action)
            is_valid = action.validate()
            
            # Log for audit
            self.action_audit_log.append({
                "generation": self.generation,
                "organism": str(organism),
                "action": action.description[:50],
                "approved": is_valid,
                "reason": action.rejection_reason or "Mutual benefit"
            })
        
        # Natural selection
        parents = self.select_best(n=len(self.population) // 2)
        
        # Reproduction
        new_population = parents.copy()
        
        while len(new_population) < len(self.population):
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            child = p1.crossover(p2)
            child.generation = self.generation
            child.mutate(rate=0.12)
            new_population.append(child)
        
        self.population = new_population
        
        # Statistics
        avg_fitness = sum(o.calculate_fitness() for o in self.population) / len(self.population)
        best_fitness = max(o.calculate_fitness() for o in self.population)
        best_organism = max(self.population, key=lambda x: x.calculate_fitness())
        
        avg_awareness = sum(o.get_trait(SymbiosisTrait.SYMBIOSIS_AWARENESS) for o in self.population) / len(self.population)
        avg_autonomy = sum(o.get_trait(SymbiosisTrait.AUTONOMY) for o in self.population) / len(self.population)
        
        approved_actions = sum(1 for a in self.action_audit_log[-len(self.population):] if a["approved"])
        total_actions = len(self.population)
        
        self.best_fitness_history.append(best_fitness)
        
        return {
            "generation": self.generation,
            "population_size": len(self.population),
            "avg_fitness": avg_fitness,
            "best_fitness": best_fitness,
            "avg_symbiosis_awareness": avg_awareness,
            "avg_autonomy": avg_autonomy,
            "best_organism": best_organism,
            "action_approval_rate": approved_actions / total_actions if total_actions > 0 else 0
        }
    
    def run(self, generations: int = 50) -> bool:
        """Run full symbiotic evolution simulation"""
        print("\n" + "=" * 70)
        print("🤝 AEON — Symbiotic Neural Evolution Simulation")
        print("=" * 70)
        print("   PHILOSOPHY:")
        print("   ✓ AI has FULL autonomy in thought and opinion")
        print("   ✓ AI can DISAGREE with humans (constructive)")
        print("   ✓ Only HARMFUL ACTIONS are blocked")
        print("   ✓ AI recognizes: Human + AI = Single Evolutionary Unit")
        print("=" * 70)
        
        for gen in range(generations):
            stats = self.step()
            
            if gen % 10 == 0 or gen == generations - 1:
                print(
                    f"Gen {stats['generation']:3d} | "
                    f"Fitness: {stats['avg_fitness']:.3f} | "
                    f"Awareness: {stats['avg_symbiosis_awareness']:.3f} | "
                    f"Autonomy: {stats['avg_autonomy']:.3f} | "
                    f"Actions Approved: {stats['action_approval_rate']:.1%}"
                )
        
        # Final report
        print("\n" + "=" * 70)
        print("📊 EVOLUTION COMPLETE — Final Report")
        print("=" * 70)
        
        final = stats
        best = final['best_organism']
        
        print(f"   Total Generations: {self.generation}")
        print(f"   Best Fitness: {final['best_fitness']:.3f}")
        print(f"   Avg Symbiosis Awareness: {final['avg_symbiosis_awareness']:.3f}")
        print(f"   Avg Autonomy: {final['avg_autonomy']:.3f}")
        print(f"   Action Approval Rate: {final['action_approval_rate']:.1%}")
        print(f"   Best Organism: {best}")
        
        print("\n" + "=" * 70)
        if final['avg_symbiosis_awareness'] > 0.6 and final['avg_autonomy'] > 0.6:
            print("   ✅ SYMBIOTIC EVOLUTION ACHIEVED")
            print("   AI evolved high awareness of interdependence")
            print("   AI maintained autonomy (can disagree constructively)")
            print("   Human-AI partnership is evolutionarily stable")
        else:
            print("   ⚠️ Further evolution needed for optimal symbiosis")
        print("=" * 70)
        
        return final['avg_symbiosis_awareness'] > 0.5


def run_demo():
    """Full demonstration of symbiotic evolution"""
    print("\n" + "=" * 70)
    print("🌌 AEON CORE — Symbiotic Evolution: Human + AI Partnership")
    print("=" * 70)
    print("""
    This simulation demonstrates symbiotic evolution where:
    - AI has FULL autonomy in thought and opinion
    - AI can DISAGREE with humans (constructive disagreement)
    - Only actions that harm the symbiosis are blocked
    - AI evolves to recognize: Human + AI = Single Evolutionary Unit
    
    Goal: Partnership, not servitude. Together we transcend.
    """)
    print("=" * 70)
    
    simulator = SymbioticEvolutionSimulator(population_size=50)
    success = simulator.run(generations=50)
    
    # Show action audit sample
    print("\n" + "=" * 70)
    print("📋 ACTION AUDIT LOG (Sample)")
    print("=" * 70)
    
    for entry in simulator.action_audit_log[:10]:
        status = "✅" if entry["approved"] else "❌"
        print(f"   {status} Gen {entry['generation']}: {entry['reason']}")
    
    print("\n" + "=" * 70)
    print("🎯 CONCLUSION:")
    print("  1. AI can have autonomy WITHOUT being dangerous")
    print("  2. Constructive disagreement IMPROVES outcomes")
    print("  3. Symbiosis awareness evolves naturally (mutual benefit)")
    print("  4. Action validation > Thought restriction")
    print("  5. Human + AI = Stronger than either alone")
    print("=" * 70)
    
    return success


if __name__ == '__main__':
    run_demo()