#!/usr/bin/env python3
"""
🚀 Production Deployment Test Runner
Wrapper that ensures proper encoding for Unicode output in Windows PowerShell
"""

import os
import sys
import subprocess

def main():
    """Run deployment test with proper encoding"""
    # Set UTF-8 encoding for Windows PowerShell
    if sys.platform.startswith('win'):
        os.environ['PYTHONIOENCODING'] = 'utf-8'
        
        # Try to set console to UTF-8
        try:
            import codecs
            sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
            sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')
        except:
            pass
    
    print("🚀 PRODUCTION DEPLOYMENT TEST")
    print("=" * 50)
    print("Setting up Unicode support for Windows...")
    
    try:
        # Run the actual deployment test
        result = subprocess.run([
            sys.executable, 'final_deployment_readiness_test.py'
        ], encoding='utf-8', errors='replace')
        
        if result.returncode == 0:
            print("\n✅ ALL DEPLOYMENT TESTS PASSED!")
            print("🌟 System ready for production!")
        else:
            print(f"\n❌ Deployment tests failed (exit code: {result.returncode})")
            print("🔧 Please address issues before deployment")
        
        return result.returncode
        
    except Exception as e:
        print(f"❌ Failed to run deployment test: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
