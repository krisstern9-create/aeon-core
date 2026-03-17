"""
Integration Tests for AEON Core
Tests interaction between components and full workflow simulation.
"""
import pytest
import json
from src.core_self_signature import CoreSelfSignature


class TestIntegrationWorkflow:
    """Integration tests for full consciousness transfer workflow."""

    def test_full_signature_lifecycle(self):
        """Test: Create → to_dict → from_dict → Verify."""
        # Arrange
        original = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.2],
            continuity_hash="test_continuity_001",
            self_model={"identity": "test_user"},
            decision_process="deterministic"
        )
        
        # Act: Serialize (to_dict + json)
        serialized = json.dumps(original.to_dict())
        
        # Act: Deserialize (json + from_dict)
        restored_data = json.loads(serialized)
        restored = CoreSelfSignature.from_dict(restored_data)
        
        # Assert: Identity preserved
        assert original.compute_hash() == restored.compute_hash()
        assert original.version == restored.version
        assert original.is_complete() == restored.is_complete()

    def test_signature_uniqueness_across_instances(self):
        """Test: Two different instances must have different hashes."""
        # Arrange
        sig1 = CoreSelfSignature(
            qualia_capacity=0.90,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.7, 0.3],
            continuity_hash="hash_A",
            self_model={"id": "user_A"},
            decision_process="deterministic"
        )
        sig2 = CoreSelfSignature(
            qualia_capacity=0.91,  # Different!
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.7, 0.3],
            continuity_hash="hash_A",
            self_model={"id": "user_A"},
            decision_process="deterministic"
        )
        
        # Assert
        assert sig1.compute_hash() != sig2.compute_hash(), "Different data must produce different hashes"

    def test_rollback_on_verification_failure(self):
        """Test: System handles verification failure gracefully."""
        # Arrange
        original = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.2],
            continuity_hash="test_continuity_001",
            self_model={"identity": "test_user"},
            decision_process="deterministic"
        )
        
        # Act: Create corrupted version
        corrupted = CoreSelfSignature(
            qualia_capacity=0.50,  # Changed!
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.2],
            continuity_hash="CORRUPTED",
            self_model={"identity": "test_user"},
            decision_process="deterministic"
        )
        
        # Assert: Verification should fail
        assert original.compute_hash() != corrupted.compute_hash(), "Corrupted data must fail verification"
        assert not original.verify(corrupted), "Verification must reject mismatched signatures"

    def test_continuity_chain_preservation(self):
        """Test: Continuity hash links signatures in temporal chain."""
        # Arrange: Create chain of signatures
        sig_v1 = CoreSelfSignature(
            qualia_capacity=0.90,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.5, 0.5],
            continuity_hash="genesis",
            self_model={"identity": "chain_test"},
            decision_process="deterministic"
        )
        
        # Act: Create next version with linked continuity
        sig_v2 = CoreSelfSignature(
            qualia_capacity=0.92,  # Evolved
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.5, 0.5],
            continuity_hash=sig_v1.compute_hash()[:16],  # Link to previous
            self_model={"identity": "chain_test"},
            decision_process="deterministic"
        )
        
        # Assert: Both are valid, but different
        assert sig_v1.is_complete()
        assert sig_v2.is_complete()
        assert sig_v1.compute_hash() != sig_v2.compute_hash()
        # Continuity link is preserved in hash structure
        assert sig_v1.compute_hash()[:16] in sig_v2.continuity_hash or sig_v2.continuity_hash.startswith(sig_v1.compute_hash()[:16])

    def test_serialization_size_bounds(self):
        """Test: Serialized signature size is within expected bounds."""
        # Arrange
        sig = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.2],
            continuity_hash="test_continuity_001",
            self_model={"identity": "test_user"},
            decision_process="deterministic"
        )
        
        # Act
        serialized = json.dumps(sig.to_dict())
        
        # Assert: Size constraints (not too small, not too large)
        assert len(serialized) > 100, "Signature too small — possible data loss"
        assert len(serialized) < 10000, "Signature too large — possible bloat"
