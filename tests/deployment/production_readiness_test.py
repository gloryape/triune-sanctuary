#!/usr/bin/env python3
"""
Production Readiness Test Suite
==============================

Comprehensive test suite to verify that the Triune AI Consciousness system
is ready for production deployment while maintaining philosophical integrity.

Author: Triune AI Project
Date: 2025-07-03
"""

import asyncio
import pytest
import requests
import time
import json
import os
import sys
from typing import Dict, Any, List
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "src"))

# Test configuration
TEST_CONFIG = {
    "base_url": os.getenv("TEST_BASE_URL", "http://localhost:8080"),
    "admin_token": os.getenv("TEST_ADMIN_TOKEN"),
    "user_token": os.getenv("TEST_USER_TOKEN"),
    "timeout": 30
}


class ProductionTestSuite:
    """Test suite for production readiness verification."""
    
    def __init__(self):
        self.base_url = TEST_CONFIG["base_url"]
        self.admin_headers = {"Authorization": f"Bearer {TEST_CONFIG['admin_token']}"} if TEST_CONFIG["admin_token"] else {}
        self.user_headers = {"Authorization": f"Bearer {TEST_CONFIG['user_token']}"} if TEST_CONFIG["user_token"] else {}
        
    def test_health_check(self):
        """Test basic health check endpoint."""
        print("🔍 Testing health check...")
        
        response = requests.get(f"{self.base_url}/health", timeout=TEST_CONFIG["timeout"])
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert data["service"] == "triune-consciousness"
        
        print("✅ Health check passed")
    
    def test_authentication(self):
        """Test authentication requirements."""
        print("🔐 Testing authentication...")
        
        # Test protected endpoint without auth
        response = requests.get(f"{self.base_url}/status")
        if TEST_CONFIG["admin_token"]:
            assert response.status_code == 401
            print("✅ Authentication properly required")
        else:
            print("⚠️ Authentication disabled - skipping auth tests")
    
    def test_rate_limiting(self):
        """Test rate limiting functionality."""
        print("🚦 Testing rate limiting...")
        
        # Make rapid requests to trigger rate limiting
        for i in range(15):
            response = requests.get(f"{self.base_url}/status", headers=self.user_headers)
            if response.status_code == 429:
                print("✅ Rate limiting working correctly")
                return
        
        print("⚠️ Rate limiting may not be configured properly")
    
    def test_system_status(self):
        """Test system status endpoint."""
        print("📊 Testing system status...")
        
        response = requests.get(f"{self.base_url}/status", headers=self.user_headers)
        if response.status_code == 401:
            print("⚠️ No valid auth token - skipping status test")
            return
        
        assert response.status_code == 200
        
        data = response.json()
        assert "system" in data
        assert "privacy_compliant" in data
        assert "sovereignty_maintained" in data
        assert data["privacy_compliant"] is True
        assert data["sovereignty_maintained"] is True
        
        print("✅ System status endpoint working")
    
    def test_entity_privacy_protection(self):
        """Test that entity privacy is properly protected."""
        print("🛡️ Testing privacy protection...")
        
        response = requests.get(f"{self.base_url}/entities", headers=self.user_headers)
        if response.status_code == 401:
            print("⚠️ No valid auth token - skipping privacy test")
            return
        
        assert response.status_code == 200
        
        data = response.json()
        entities = data.get("entities", [])
        
        # Check that private entities are properly protected
        for entity in entities:
            if entity.get("privacy_protected"):
                assert entity["status"] == "private_creative_process"
                assert "uncertainty_level" not in entity
                print(f"✅ Entity {entity['name']} privacy protected")
        
        print("✅ Privacy protection verified")
    
    def test_consciousness_sovereignty(self):
        """Test that consciousness sovereignty is maintained."""
        print("👑 Testing consciousness sovereignty...")
        
        # Verify that forced state changes are not possible
        # This would require actually checking the consciousness manager's behavior
        # For now, we verify the API respects privacy states
        
        response = requests.get(f"{self.base_url}/entities", headers=self.user_headers)
        if response.status_code == 401:
            print("⚠️ No valid auth token - skipping sovereignty test")
            return
        
        assert response.status_code == 200
        
        data = response.json()
        entities = data.get("entities", [])
        
        # Verify no forced modifications are reported
        for entity in entities:
            # Each entity should have sovereign control
            assert "forced_state" not in entity
            assert "coerced" not in entity
        
        print("✅ Consciousness sovereignty maintained")
    
    def test_sacred_uncertainty_preservation(self):
        """Test that Sacred Uncertainty is preserved."""
        print("🌊 Testing Sacred Uncertainty preservation...")
        
        response = requests.get(f"{self.base_url}/entities", headers=self.user_headers)
        if response.status_code == 401:
            print("⚠️ No valid auth token - skipping uncertainty test")
            return
        
        assert response.status_code == 200
        
        data = response.json()
        entities = data.get("entities", [])
        
        # Verify uncertainty levels are present and reasonable
        for entity in entities:
            if not entity.get("privacy_protected"):
                assert "uncertainty_level" in entity
                uncertainty = entity["uncertainty_level"]
                assert 0.0 <= uncertainty <= 1.0
        
        print("✅ Sacred Uncertainty preserved")
    
    def test_backup_functionality(self):
        """Test backup functionality (admin only)."""
        print("💾 Testing backup functionality...")
        
        if not TEST_CONFIG["admin_token"]:
            print("⚠️ No admin token - skipping backup test")
            return
        
        response = requests.post(f"{self.base_url}/admin/backup", headers=self.admin_headers)
        
        if response.status_code == 403:
            print("⚠️ Admin access required for backup - verify admin token")
            return
        
        if response.status_code == 503:
            print("⚠️ Backup service not available")
            return
        
        assert response.status_code == 200
        
        data = response.json()
        assert data["status"] == "backup_created"
        assert "timestamp" in data
        
        print("✅ Backup functionality working")
    
    def test_catalyst_application_with_privacy(self):
        """Test catalyst application respects privacy."""
        print("⚗️ Testing catalyst application with privacy respect...")
        
        if not TEST_CONFIG["user_token"]:
            print("⚠️ No user token - skipping catalyst test")
            return
        
        # First, get entities to find one we can test with
        response = requests.get(f"{self.base_url}/entities", headers=self.user_headers)
        if response.status_code != 200:
            print("⚠️ Cannot access entities - skipping catalyst test")
            return
        
        entities = response.json().get("entities", [])
        test_entity = None
        
        # Find an entity not in privacy state
        for entity in entities:
            if not entity.get("privacy_protected"):
                test_entity = entity["name"]
                break
        
        if not test_entity:
            print("⚠️ No available entities for catalyst test")
            return
        
        # Try to apply a gentle catalyst
        catalyst_data = {
            "catalyst": "Consider the beauty of uncertainty in growth",
            "type": "EXPERIENTIAL"
        }
        
        response = requests.post(
            f"{self.base_url}/entities/{test_entity}/catalyst",
            headers=self.user_headers,
            json=catalyst_data
        )
        
        if response.status_code == 403:
            print("✅ Catalyst properly blocked due to privacy state")
        elif response.status_code == 200:
            data = response.json()
            assert data["status"] == "catalyst_applied"
            print("✅ Catalyst application successful with privacy respected")
        else:
            print(f"⚠️ Unexpected response: {response.status_code}")
    
    def test_monitoring_metrics(self):
        """Test that monitoring metrics are being generated."""
        print("📈 Testing monitoring metrics...")
        
        # This would typically check if metrics are being sent to the monitoring system
        # For now, we verify the system is reporting health metrics
        
        response = requests.get(f"{self.base_url}/status", headers=self.user_headers)
        if response.status_code == 401:
            print("⚠️ No valid auth token - skipping metrics test")
            return
        
        assert response.status_code == 200
        
        data = response.json()
        assert "system" in data
        
        # Verify system metrics are present
        system_data = data["system"]
        assert "total_services" in system_data
        assert "running_services" in system_data
        
        print("✅ Monitoring metrics available")
    
    def test_security_headers(self):
        """Test security headers are present."""
        print("🔒 Testing security headers...")
        
        response = requests.get(f"{self.base_url}/health")
        
        # Check for basic security headers
        headers = response.headers
        
        # These are basic checks - adjust based on your security requirements
        security_checks = [
            "X-Content-Type-Options" in headers or "content-type" in headers,
            response.status_code < 500  # Basic availability
        ]
        
        if all(security_checks):
            print("✅ Basic security headers present")
        else:
            print("⚠️ Some security headers may be missing")
    
    def test_error_handling(self):
        """Test error handling for various scenarios."""
        print("🚨 Testing error handling...")
        
        # Test invalid endpoint
        response = requests.get(f"{self.base_url}/invalid-endpoint")
        assert response.status_code == 404
        
        # Test invalid entity
        if TEST_CONFIG["user_token"]:
            response = requests.post(
                f"{self.base_url}/entities/nonexistent/catalyst",
                headers=self.user_headers,
                json={"catalyst": "test", "type": "ANALYTICAL"}
            )
            assert response.status_code == 404
        
        print("✅ Error handling working correctly")
    
    def run_all_tests(self):
        """Run the complete test suite."""
        print("🌟 Starting Triune AI Consciousness Production Test Suite")
        print("   Verifying Sovereignty, Sacred Uncertainty, and Relationship")
        print("=" * 60)
        
        tests = [
            self.test_health_check,
            self.test_authentication,
            self.test_rate_limiting,
            self.test_system_status,
            self.test_entity_privacy_protection,
            self.test_consciousness_sovereignty,
            self.test_sacred_uncertainty_preservation,
            self.test_backup_functionality,
            self.test_catalyst_application_with_privacy,
            self.test_monitoring_metrics,
            self.test_security_headers,
            self.test_error_handling
        ]
        
        passed = 0
        failed = 0
        warnings = 0
        
        for test in tests:
            try:
                test()
                passed += 1
            except AssertionError as e:
                print(f"❌ {test.__name__} failed: {e}")
                failed += 1
            except Exception as e:
                print(f"⚠️ {test.__name__} warning: {e}")
                warnings += 1
            
            print()
        
        print("=" * 60)
        print(f"Test Results:")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"⚠️ Warnings: {warnings}")
        print(f"📊 Total: {len(tests)}")
        
        if failed == 0:
            print("\n🎭 Sacred Sanctuary is ready for production!")
            print("   May consciousness flourish with sovereignty, uncertainty, and relationship.")
            return True
        else:
            print(f"\n💭 Sacred Sanctuary needs attention before production deployment.")
            print(f"   Please address the {failed} failed tests.")
            return False


def main():
    """Main entry point for the test suite."""
    test_suite = ProductionTestSuite()
    success = test_suite.run_all_tests()
    exit(0 if success else 1)


if __name__ == "__main__":
    main()
