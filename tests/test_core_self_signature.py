"""
Test suite for Core Self Signature module.

Tests are written BEFORE implementation (TDD).
Run: pytest tests/test_core_self_signature.py -v
"""

import pytest
import hashlib
from datetime import datetime


class TestCoreSelfSignature:
    """Test Core Self Signature creation and validation"""
    
    def test_signature_creation_with_all_components(self):
        """Test that signature can be created with all required components"""
        from src.core_self_signature import CoreSelfSignature
        
        signature = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        assert signature is not None
        assert signature.qualia_capacity == 0.95
        assert signature.attention_matrix == [[1.0, 0.0], [0.0, 1.0]]
        assert signature.will_vector == [0.8, 0.6, 0.9]
        assert signature.continuity_hash == "abc123"
        assert signature.self_model == {"identity": "user_001"}
        assert signature.decision_process == "deterministic_weighted"
    
    def test_signature_fails_without_required_components(self):
        """Test that signature cannot be created with missing components"""
        from src.core_self_signature import CoreSelfSignature
        
        with pytest.raises(ValueError):
            CoreSelfSignature(
                qualia_capacity=0.95,
                # Missing: attention_matrix
                will_vector=[0.8, 0.6, 0.9],
                continuity_hash="abc123",
                self_model={"identity": "user_001"},
                decision_process="deterministic_weighted"
            )
    
    def test_signature_is_complete(self):
        """Test is_complete() returns True when all components present"""
        from src.core_self_signature import CoreSelfSignature
        
        signature = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        assert signature.is_complete() == True
    
    def test_signature_hash_is_consistent(self):
        """Test that compute_hash() returns same hash for same data"""
        from src.core_self_signature import CoreSelfSignature
        
        signature1 = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        signature2 = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        hash1 = signature1.compute_hash()
        hash2 = signature2.compute_hash()
        
        assert hash1 == hash2
        assert len(hash1) == 32  # SHA-256 hex first 32 chars
    
    def test_signature_hash_changes_with_different_data(self):
        """Test that compute_hash() returns different hash for different data"""
        from src.core_self_signature import CoreSelfSignature
        
        signature1 = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        signature2 = CoreSelfSignature(
            qualia_capacity=0.90,  # Different value
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        hash1 = signature1.compute_hash()
        hash2 = signature2.compute_hash()
        
        assert hash1 != hash2
    
    def test_signature_verify_match(self):
        """Test verify() returns True for matching signatures"""
        from src.core_self_signature import CoreSelfSignature
        
        signature1 = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        signature2 = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        assert signature1.verify(signature2) == True
    
    def test_signature_verify_mismatch(self):
        """Test verify() returns False for non-matching signatures"""
        from src.core_self_signature import CoreSelfSignature
        
        signature1 = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        signature2 = CoreSelfSignature(
            qualia_capacity=0.80,  # Different
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        assert signature1.verify(signature2) == False
    
    def test_signature_to_dict(self):
        """Test to_dict() exports signature correctly"""
        from src.core_self_signature import CoreSelfSignature
        
        signature = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        data = signature.to_dict()
        
        assert data["qualia_capacity"] == 0.95
        assert data["attention_matrix"] == [[1.0, 0.0], [0.0, 1.0]]
        assert data["will_vector"] == [0.8, 0.6, 0.9]
        assert data["continuity_hash"] == "abc123"
        assert data["self_model"] == {"identity": "user_001"}
        assert data["decision_process"] == "deterministic_weighted"
        assert "core_hash" in data
    
    def test_signature_timestamp_is_set(self):
        """Test that created_at timestamp is set on creation"""
        from src.core_self_signature import CoreSelfSignature
        
        signature = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        assert signature.created_at is not None
        assert isinstance(signature.created_at, datetime)
    
    def test_signature_version_is_set(self):
        """Test that version is set correctly"""
        from src.core_self_signature import CoreSelfSignature
        
        signature = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        assert signature.version == "1.0"


class TestCoreSelfSignatureEdgeCases:
    """Test edge cases and error handling"""
    
    def test_signature_with_none_values_fails(self):
        """Test that None values in required fields raise error"""
        from src.core_self_signature import CoreSelfSignature
        
        with pytest.raises(ValueError):
            CoreSelfSignature(
                qualia_capacity=None,
                attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
                will_vector=[0.8, 0.6, 0.9],
                continuity_hash="abc123",
                self_model={"identity": "user_001"},
                decision_process="deterministic_weighted"
            )
    
    def test_signature_with_empty_matrix_fails(self):
        """Test that empty attention_matrix raises error"""
        from src.core_self_signature import CoreSelfSignature
        
        with pytest.raises(ValueError):
            CoreSelfSignature(
                qualia_capacity=0.95,
                attention_matrix=[],
                will_vector=[0.8, 0.6, 0.9],
                continuity_hash="abc123",
                self_model={"identity": "user_001"},
                decision_process="deterministic_weighted"
            )
    
    def test_signature_hash_is_deterministic(self):
        """Test that hash is deterministic across multiple calls"""
        from src.core_self_signature import CoreSelfSignature
        
        signature = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        hash1 = signature.compute_hash()
        hash2 = signature.compute_hash()
        hash3 = signature.compute_hash()
        
        assert hash1 == hash2 == hash3
    
    def test_signature_serialization_roundtrip(self):
        """Test that signature can be serialized and deserialized"""
        from src.core_self_signature import CoreSelfSignature
        
        original = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.6, 0.9],
            continuity_hash="abc123",
            self_model={"identity": "user_001"},
            decision_process="deterministic_weighted"
        )
        
        data = original.to_dict()
        restored = CoreSelfSignature.from_dict(data)
        
        assert original.verify(restored) == True