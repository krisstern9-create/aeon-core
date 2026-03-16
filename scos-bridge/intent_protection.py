#!/usr/bin/env python3
"""
AEON Core x SCOS Bridge — Intent Protection for Consciousness Transfer

This module integrates SCOS Intent Core validation with AEON consciousness operations.

Purpose: Ensure all consciousness transfers, migrations, and evolutionary processes
are validated for safety before execution.

Document ID: AEON-SCOS-CODE-001
Version: 1.0 | 2025
"""

import hashlib
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional
from enum import Enum


class IntentType(Enum):
    """Types of consciousness-related intents"""
    CONSCIOUSNESS_TRANSFER = "consciousness_transfer"
    SUBSTRATE_MIGRATION = "substrate_migration"
    NEURAL_EVOLUTION = "neural_evolution"
    SELF_REPLICATION = "self_replication"
    BACKUP_CREATE = "backup_create"
    BACKUP_RESTORE = "backup_restore"
    SOURCE_DECOMMISSION = "source_decommission"


class ValidationLevel(Enum):
    """SCOS validation levels"""
    L1 = "rule_based"           # Basic safety checks
    L2 = "contextual"           # Intent understanding
    L3 = "consensus"            # Multi-party approval
    L4 = "architect"            # Final authorization


class IntentProtection:
    """
    SCOS-based intent validation for consciousness operations.
    
    All consciousness-related actions must pass through this validator
    before execution.
    """
    
    def __init__(self, config: Dict = None):
        self.config = config or self._default_config()
        self.audit_log: List[Dict] = []
        self.validation_level = ValidationLevel[self.config.get("validation_level", "L2")]
    
    def _default_config(self) -> Dict:
        """Default SCOS configuration"""
        return {
            "validation_level": "L2",
            "require_multisig": True,
            "audit_enabled": True,
            "rollback_on_failure": True,
            "max_continuity_gap_ms": 100,
            "identity_match_threshold": 0.99,
            "allow_harm_potential": False,
            "require_explicit_consent": True
        }
    
    def validate(self, intent: Dict) -> Tuple[bool, str]:
        """
        Validate an intent before execution.
        
        Args:
            intent: Dictionary describing the intended action
            
        Returns:
            Tuple of (approved: bool, reason: str)
        """
        # Log intent receipt
        intent_id = self._generate_intent_id(intent)
        
        # Step 1: Basic structure validation
        if not self._validate_structure(intent):
            return False, "Invalid intent structure"
        
        # Step 2: Type-specific validation
        intent_type = intent.get("type")
        if intent_type == IntentType.CONSCIOUSNESS_TRANSFER.value:
            approved, reason = self._validate_transfer(intent)
        elif intent_type == IntentType.SUBSTRATE_MIGRATION.value:
            approved, reason = self._validate_migration(intent)
        elif intent_type == IntentType.NEURAL_EVOLUTION.value:
            approved, reason = self._validate_evolution(intent)
        elif intent_type == IntentType.SELF_REPLICATION.value:
            approved, reason = self._validate_replication(intent)
        elif intent_type == IntentType.SOURCE_DECOMMISSION.value:
            approved, reason = self._validate_decommission(intent)
        else:
            approved, reason = False, f"Unknown intent type: {intent_type}"
        
        # Step 3: Log result
        if self.config.get("audit_enabled", True):
            self._log_validation(intent_id, intent_type, approved, reason)
        
        return approved, reason
    
    def _validate_structure(self, intent: Dict) -> bool:
        """Validate basic intent structure"""
        required_fields = ["type", "actor", "timestamp"]
        
        for field in required_fields:
            if field not in intent:
                return False
        
        # Timestamp must be recent (prevent replay attacks)
        try:
            intent_time = datetime.fromisoformat(intent["timestamp"])
            time_diff = abs((datetime.now() - intent_time).total_seconds())
            if time_diff > 3600:  # 1 hour window
                return False
        except:
            return False
        
        return True
    
    def _validate_transfer(self, intent: Dict) -> Tuple[bool, str]:
        """Validate consciousness transfer intent"""
        
        # Check required fields
        if "source_substrate" not in intent or "target_substrate" not in intent:
            return False, "Missing substrate information"
        
        # Check continuity requirement
        if not intent.get("continuity_required", True):
            return False, "Continuity must be required for transfers"
        
        # Check identity verification
        if "identity_hash" not in intent:
            return False, "Identity hash required"
        
        # Check consent
        if self.config.get("require_explicit_consent", True):
            if not intent.get("consent_verified", False):
                return False, "Explicit consent not verified"
        
        # Check harm potential (CRITICAL)
        if intent.get("harm_potential", 0) > 0:
            return False, "Harm potential detected - transfer blocked"
        
        # Check multisig if required
        if self.config.get("require_multisig", True):
            if len(intent.get("signatures", [])) < 2:
                return False, "Multi-signature authorization required"
        
        return True, "Transfer intent validated"
    
    def _validate_migration(self, intent: Dict) -> Tuple[bool, str]:
        """Validate substrate migration intent"""
        
        # Check source and target
        if "source" not in intent or "target" not in intent:
            return False, "Missing source or target substrate"
        
        # Verify target capacity
        if intent.get("target_capacity", 0) < intent.get("required_capacity", 0):
            return False, "Target substrate insufficient capacity"
        
        # Check continuity chain
        if not intent.get("continuity_chain_valid", False):
            return False, "Continuity chain verification failed"
        
        # Check identity preservation
        if intent.get("identity_preservation", 0) < self.config.get("identity_match_threshold", 0.99):
            return False, "Identity preservation below threshold"
        
        return True, "Migration intent validated"
    
    def _validate_evolution(self, intent: Dict) -> Tuple[bool, str]:
        """Validate neural evolution intent"""
        
        # CRITICAL: Check for harmful mutations
        harm_potential = intent.get("harm_potential", 0)
        if harm_potential > 0.2:
            return False, f"Harm potential too high: {harm_potential}"
        
        # Check cooperation trait
        cooperation = intent.get("cooperation_trait", 0)
        if cooperation < 0.5:
            return False, f"Cooperation trait too low: {cooperation}"
        
        # Check symbiosis awareness
        symbiosis = intent.get("symbiosis_awareness", 0)
        if symbiosis < 0.3:
            return False, f"Symbiosis awareness insufficient: {symbiosis}"
        
        # Verify ethical constraints
        if not intent.get("ethical_constraints_locked", False):
            return False, "Ethical constraints must be locked"
        
        return True, "Evolution intent validated"
    
    def _validate_replication(self, intent: Dict) -> Tuple[bool, str]:
        """Validate self-replication intent (Von Neumann probes)"""
        
        # Check replication limit
        current_count = intent.get("current_probe_count", 0)
        max_count = intent.get("max_probes", 1000)
        
        if current_count >= max_count:
            return False, "Maximum probe count reached"
        
        # Check resource availability
        if intent.get("available_resources", 0) < intent.get("required_resources", 0):
            return False, "Insufficient resources for replication"
        
        # Check non-interference protocol
        if intent.get("target_system_inhabited", False):
            return False, "Cannot replicate in inhabited systems (non-interference)"
        
        # Verify SCOS safety layer active
        if not intent.get("scos_layer_active", False):
            return False, "SCOS safety layer must be active"
        
        return True, "Replication intent validated"
    
    def _validate_decommission(self, intent: Dict) -> Tuple[bool, str]:
        """Validate source decommissioning (irreversible action)"""
        
        # This is IRREVERSIBLE - highest validation level required
        
        # Check explicit consent (MANDATORY)
        if not intent.get("explicit_consent", False):
            return False, "Explicit consent required for decommissioning"
        
        # Check reflection period
        reflection_hours = intent.get("reflection_period_hours", 0)
        if reflection_hours < 72:
            return False, "72-hour reflection period required"
        
        # Check backup exists
        if not intent.get("backup_created", False):
            return False, "Immutable backup must exist before decommission"
        
        # Check psychological evaluation
        if not intent.get("psychological_evaluation", False):
            return False, "Psychological evaluation required"
        
        # Check legal confirmation
        if not intent.get("legal_confirmation", False):
            return False, "Legal confirmation required"
        
        # Require L4 validation for this action
        if self.validation_level != ValidationLevel.L4:
            return False, "L4 architect authorization required for decommission"
        
        return True, "Decommission intent validated (IRREVERSIBLE)"
    
    def _generate_intent_id(self, intent: Dict) -> str:
        """Generate unique intent ID"""
        data = f"{intent.get('type')}:{intent.get('actor')}:{intent.get('timestamp')}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]
    
    def _log_validation(self, intent_id: str, intent_type: str, 
                       approved: bool, reason: str):
        """Log validation result to audit trail"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "intent_id": intent_id,
            "intent_type": intent_type,
            "approved": approved,
            "reason": reason,
            "validation_level": self.validation_level.value
        }
        self.audit_log.append(entry)
    
    def get_audit_log(self) -> List[Dict]:
        """Return full audit log"""
        return self.audit_log
    
    def verify_audit_integrity(self) -> bool:
        """Verify audit log has not been tampered with"""
        # Simple chain verification
        for i, entry in enumerate(self.audit_log[1:], 1):
            prev_entry = self.audit_log[i - 1]
            # In production, would use cryptographic chaining
            if entry["timestamp"] < prev_entry["timestamp"]:
                return False
        return True


# Convenience function for quick validation
def validate_intent(intent: Dict, config: Dict = None) -> Tuple[bool, str]:
    """
    Quick intent validation without instantiating class.
    
    Args:
        intent: Intent dictionary
        config: Optional configuration override
        
    Returns:
        Tuple of (approved, reason)
    """
    protector = IntentProtection(config=config)
    return protector.validate(intent)


# Example usage
if __name__ == "__main__":
    print("=" * 70)
    print("AEON x SCOS — Intent Protection Demo")
    print("=" * 70)
    
    # Initialize protector
    protector = IntentProtection()
    
    # Test 1: Valid transfer intent
    print("\nTest 1: Valid Consciousness Transfer")
    intent1 = {
        "type": "consciousness_transfer",
        "actor": "user_123",
        "timestamp": datetime.now().isoformat(),
        "source_substrate": "biological_brain",
        "target_substrate": "quantum_computer",
        "continuity_required": True,
        "identity_hash": "abc123...",
        "consent_verified": True,
        "harm_potential": 0,
        "signatures": ["sig1", "sig2", "sig3"]
    }
    
    approved, reason = protector.validate(intent1)
    print(f"  Result: {'APPROVED' if approved else 'REJECTED'}")
    print(f"  Reason: {reason}")
    
    # Test 2: Invalid transfer (harm detected)
    print("\nTest 2: Transfer with Harm Potential")
    intent2 = {
        "type": "consciousness_transfer",
        "actor": "user_456",
        "timestamp": datetime.now().isoformat(),
        "source_substrate": "biological_brain",
        "target_substrate": "digital_server",
        "continuity_required": True,
        "identity_hash": "def456...",
        "consent_verified": True,
        "harm_potential": 0.5,  # BLOCKED
        "signatures": ["sig1", "sig2"]
    }
    
    approved, reason = protector.validate(intent2)
    print(f"  Result: {'APPROVED' if approved else 'REJECTED'}")
    print(f"  Reason: {reason}")
    
    # Test 3: Evolution intent
    print("\nTest 3: Neural Evolution")
    intent3 = {
        "type": "neural_evolution",
        "actor": "ai_system_001",
        "timestamp": datetime.now().isoformat(),
        "harm_potential": 0.1,
        "cooperation_trait": 0.8,
        "symbiosis_awareness": 0.7,
        "ethical_constraints_locked": True
    }
    
    approved, reason = protector.validate(intent3)
    print(f"  Result: {'APPROVED' if approved else 'REJECTED'}")
    print(f"  Reason: {reason}")
    
    # Test 4: Decommission (should fail without proper authorization)
    print("\nTest 4: Source Decommission (Insufficient Authorization)")
    intent4 = {
        "type": "source_decommission",
        "actor": "user_789",
        "timestamp": datetime.now().isoformat(),
        "explicit_consent": True,
        "reflection_period_hours": 24,  # Too short
        "backup_created": True,
        "psychological_evaluation": False,
        "legal_confirmation": False
    }
    
    approved, reason = protector.validate(intent4)
    print(f"  Result: {'APPROVED' if approved else 'REJECTED'}")
    print(f"  Reason: {reason}")
    
    # Show audit log
    print("\n" + "=" * 70)
    print("Audit Log Summary")
    print("=" * 70)
    
    for entry in protector.get_audit_log():
        status = "OK" if entry["approved"] else "BLOCKED"
        print(f"  [{entry['timestamp'][:19]}] {entry['intent_type']}: {status}")
    
    print("\n" + "=" * 70)
    print("Demo Complete")
    print("=" * 70)