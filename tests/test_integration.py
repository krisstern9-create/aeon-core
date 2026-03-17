"""
Integration Tests for AEON Core
Tests interaction between components and full workflow simulation.
"""
import pytest
from src.core_self_signature import CoreSelfSignature


class TestIntegrationWorkflow:
    """Integration tests for full consciousness transfer workflow."""

    def test_full_signature_lifecycle(self):
        """Test: Create → Serialize → Deserialize → Verify."""
        # Arrange
        original = CoreSelfSignature(
            qualia_capacity=0.95,
            attention_matrix=[[1.0, 0.0], [0.0, 1.0]],
            will_vector=[0.8, 0.2],
            continuity_hash="test_continuity_001",
            self_model={"identity": "test_user"},
            decision_process="deterministic"
        )
        
        # Act: Serialize
        serialized = original.serialize()
        
        # Act: Deserialize
        restored = CoreSelfSignature.deserialize(serialized)
        
        # Assert: Identity preserved
        assert original.signature == restored.signature
        assert original.version == restored.version
        assert original.is_complete() == restored.is_complete()

    def test_signature_uniqueness_across_instances(self):
        """Test: Two different instances must have different signatures."""
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
        assert sig1.signature != sig2.signature, "Different data must produce different signatures"

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
        serialized = original.serialize()
        
        # Act: Corrupt data (simulate transmission error)
        corrupted = serialized.replace("test_continuity_001", "CORRUPTED")
        
        # Act: Try to restore
        restored = CoreSelfSignature.deserialize(corrupted)
        
        # Assert: Verification should fail
        assert original.signature != restored.signature, "Corrupted data must fail verification"
        assert not original.verify(restored), "Verification must reject mismatched signatures"

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
            continuity_hash=sig_v1.signature[:16],  # Link to previous
            self_model={"identity": "chain_test"},
            decision_process="deterministic"
        )
        
        # Assert: Both are valid, but different
        assert sig_v1.is_complete()
        assert sig_v2.is_complete()
        assert sig_v1.signature != sig_v2.signature
        # Continuity link is preserved in hash structure
        assert sig_v1.signature[:16] in sig_v2.continuity_hash or sig_v2.continuity_hash.startswith(sig_v1.signature[:16])

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
        serialized = sig.serialize()
        
        # Assert: Size constraints (not too small, not too large)
        assert len(serialized) > 100, "Signature too small — possible data loss"
        assert len(serialized) < 10000, "Signature too large — possible bloat"
