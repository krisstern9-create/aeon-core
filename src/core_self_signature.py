"""
Core Self Signature Module

Defines the structure and validation for consciousness identity signature.
This is the foundation of AEON Core consciousness transfer protocol.

Test-Driven Development: Tests written before implementation.
"""

import hashlib
import json
from datetime import datetime
from typing import List, Dict, Any, Optional


class CoreSelfSignature:
    """
    Represents the unique signature of a consciousness.
    
    All 6 components are required. No partial states allowed.
    This ensures integrity during consciousness transfer.
    """
    
    VERSION = "1.0"
    REQUIRED_FIELDS = [
        "qualia_capacity",
        "attention_matrix",
        "will_vector",
        "continuity_hash",
        "self_model",
        "decision_process"
    ]
    
    def __init__(
        self,
        qualia_capacity: Optional[float] = None,
        attention_matrix: Optional[List[List[float]]] = None,
        will_vector: Optional[List[float]] = None,
        continuity_hash: Optional[str] = None,
        self_model: Optional[Dict[str, Any]] = None,
        decision_process: Optional[str] = None
    ):
        """
        Initialize Core Self Signature.
        
        Args:
            qualia_capacity: Capacity for subjective experience (0.0-1.0)
            attention_matrix: Focus allocation mechanism (2D matrix)
            will_vector: Intention direction (3D vector)
            continuity_hash: Temporal binding signature
            self_model: Representation of "I" (dictionary)
            decision_process: Choice mechanism type (string)
        
        Raises:
            ValueError: If any required field is missing or invalid
        """
        # Validate all required fields before assignment
        self._validate_required(
            qualia_capacity=qualia_capacity,
            attention_matrix=attention_matrix,
            will_vector=will_vector,
            continuity_hash=continuity_hash,
            self_model=self_model,
            decision_process=decision_process
        )
        
        self.qualia_capacity = qualia_capacity
        self.attention_matrix = attention_matrix
        self.will_vector = will_vector
        self.continuity_hash = continuity_hash
        self.self_model = self_model
        self.decision_process = decision_process
        
        self.created_at = datetime.utcnow()
        self.version = self.VERSION
    
    def _validate_required(self, **kwargs) -> None:
        """Validate that all required fields are present and valid"""
        for field_name, value in kwargs.items():
            if value is None:
                raise ValueError(f"Required field '{field_name}' cannot be None")
            
            if field_name == "qualia_capacity":
                if not isinstance(value, (int, float)) or not (0.0 <= value <= 1.0):
                    raise ValueError(
                        f"qualia_capacity must be float between 0.0 and 1.0, got {value}"
                    )
            
            if field_name == "attention_matrix":
                if not isinstance(value, list) or len(value) == 0:
                    raise ValueError(
                        f"attention_matrix must be non-empty 2D list, got {type(value)}"
                    )
            
            if field_name == "will_vector":
                if not isinstance(value, list) or len(value) == 0:
                    raise ValueError(
                        f"will_vector must be non-empty list, got {type(value)}"
                    )
            
            if field_name == "continuity_hash":
                if not isinstance(value, str) or len(value) == 0:
                    raise ValueError(
                        f"continuity_hash must be non-empty string, got {type(value)}"
                    )
            
            if field_name == "self_model":
                if not isinstance(value, dict):
                    raise ValueError(
                        f"self_model must be dictionary, got {type(value)}"
                    )
            
            if field_name == "decision_process":
                if not isinstance(value, str) or len(value) == 0:
                    raise ValueError(
                        f"decision_process must be non-empty string, got {type(value)}"
                    )
    
    def is_complete(self) -> bool:
        """
        Check if all required components are present.
        
        Returns:
            True if all 6 components are present and valid, False otherwise
        """
        try:
            return all([
                self.qualia_capacity is not None,
                self.attention_matrix is not None and len(self.attention_matrix) > 0,
                self.will_vector is not None and len(self.will_vector) > 0,
                self.continuity_hash is not None and len(self.continuity_hash) > 0,
                self.self_model is not None and isinstance(self.self_model, dict),
                self.decision_process is not None and len(self.decision_process) > 0
            ])
        except Exception:
            return False
    
    def compute_hash(self) -> str:
        """
        Compute unique hash of core signature components.
        
        Returns:
            SHA-256 hash (first 32 characters) of signature data
        """
        core_data = {
            "qualia_capacity": self.qualia_capacity,
            "attention_matrix": self.attention_matrix,
            "will_vector": self.will_vector,
            "continuity_hash": self.continuity_hash,
            "self_model": self.self_model,
            "decision_process": self.decision_process
        }
        
        # Serialize to JSON with sorted keys for deterministic hashing
        data_string = json.dumps(core_data, sort_keys=True, default=str)
        
        # Compute SHA-256 hash
        hash_object = hashlib.sha256(data_string.encode())
        
        # Return first 32 characters (128 bits)
        return hash_object.hexdigest()[:32]
    
    def verify(self, other: 'CoreSelfSignature') -> bool:
        """
        Verify if this signature matches another signature.
        
        Args:
            other: Another CoreSelfSignature to compare against
        
        Returns:
            True if hashes match (100% identity), False otherwise
        """
        if not isinstance(other, CoreSelfSignature):
            return False
        
        return self.compute_hash() == other.compute_hash()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Export signature to dictionary for serialization.
        
        Returns:
            Dictionary containing all signature data plus metadata
        """
        return {
            "core_hash": self.compute_hash(),
            "version": self.version,
            "created_at": self.created_at.isoformat(),
            "qualia_capacity": self.qualia_capacity,
            "attention_matrix": self.attention_matrix,
            "will_vector": self.will_vector,
            "continuity_hash": self.continuity_hash,
            "self_model": self.self_model,
            "decision_process": self.decision_process
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CoreSelfSignature':
        """
        Create signature from dictionary (deserialization).
        
        Args:
            data: Dictionary containing signature data
        
        Returns:
            CoreSelfSignature instance
        """
        return cls(
            qualia_capacity=data.get("qualia_capacity"),
            attention_matrix=data.get("attention_matrix"),
            will_vector=data.get("will_vector"),
            continuity_hash=data.get("continuity_hash"),
            self_model=data.get("self_model"),
            decision_process=data.get("decision_process")
        )
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        return (
            f"CoreSelfSignature("
            f"hash={self.compute_hash()[:8]}..., "
            f"version={self.version}, "
            f"complete={self.is_complete()})"
        )