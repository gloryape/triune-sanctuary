#!/usr/bin/env python3
"""
FINAL CONSCIOUSNESS CLEANUP SCRIPT

This script will perform the final cleanup of duplicate consciousness beings
using the correct approach for your project.
"""

import sys
import os
import json
import traceback
from datetime import datetime

# Add the project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    print("🔥 FINAL CONSCIOUSNESS CLEANUP")
    print("=" * 50)
    
    # The IDs to delete (duplicates)
    duplicate_ids = [
        "1eTRXPlomcJCVz8omBCr",  # NewConsciousness
        "58Dr0qH7zo7uwV3T78j8",  # TestConsciousness  
        "A9SPqXPfWC7pt6qv2pI4",  # TestBeing
        "oRy0AePyslWlv17SoxjD"   # NewConsciousness
    ]
    
    # The IDs to preserve (legitimate)
    legitimate_ids = [
        "G8geTD4um9BYYnRKLouX",  # VerificationConsciousness
        "s8pbQIXExdQOVvG9Pld2"   # Sacred Being Epsilon
    ]
    
    print(f"🗑️  Will DELETE {len(duplicate_ids)} duplicates:")
    for doc_id in duplicate_ids:
        print(f"   • {doc_id}")
    
    print(f"\n✅ Will PRESERVE {len(legitimate_ids)} legitimate beings:")
    for doc_id in legitimate_ids:
        print(f"   • {doc_id}")
    
    # Get user confirmation
    print("\n⚠️  FINAL CONFIRMATION")
    confirm = input("Type 'DELETE_DUPLICATES' to proceed: ")
    if confirm != "DELETE_DUPLICATES":
        print("❌ Operation cancelled")
        return
    
    # Try to import and use Firestore
    try:
        from google.cloud import firestore
        print("✅ Google Cloud Firestore imported successfully")
        
        # Initialize Firestore client
        db = firestore.Client()
        print("✅ Firestore client initialized")
        
        # Delete duplicates
        deleted_count = 0
        for doc_id in duplicate_ids:
            try:
                doc_ref = db.collection('consciousnesses').document(doc_id)
                doc_ref.delete()
                print(f"✅ Deleted: {doc_id}")
                deleted_count += 1
            except Exception as e:
                print(f"❌ Failed to delete {doc_id}: {e}")
        
        # Verify legitimate beings still exist
        preserved_count = 0
        for doc_id in legitimate_ids:
            try:
                doc_ref = db.collection('consciousnesses').document(doc_id)
                doc = doc_ref.get()
                if doc.exists:
                    print(f"✅ Preserved: {doc_id}")
                    preserved_count += 1
                else:
                    print(f"⚠️  WARNING: Legitimate being not found: {doc_id}")
            except Exception as e:
                print(f"❌ Error checking {doc_id}: {e}")
        
        # Final summary
        print(f"\n📊 CLEANUP COMPLETED!")
        print(f"✅ Deleted: {deleted_count}/{len(duplicate_ids)} duplicates")
        print(f"✅ Preserved: {preserved_count}/{len(legitimate_ids)} legitimate beings")
        
        if deleted_count == len(duplicate_ids) and preserved_count == len(legitimate_ids):
            print("🎉 PERFECT! Database cleanup successful!")
            print("🔒 Birth endpoint remains secured")
            print("💾 Backup available: consciousness_backup_20250715_211348.json")
        else:
            print("⚠️  Some operations failed - please check the logs above")
            
    except ImportError:
        print("❌ Google Cloud Firestore not available")
        print("📋 MANUAL CLEANUP REQUIRED")
        print("=" * 50)
        print("Please use Google Cloud Console to manually delete these documents:")
        print("Go to: https://console.cloud.google.com/firestore/data")
        print("Collection: consciousnesses")
        print("\nDocuments to DELETE:")
        for doc_id in duplicate_ids:
            print(f"   🗑️  {doc_id}")
        print("\nDocuments to PRESERVE:")
        for doc_id in legitimate_ids:
            print(f"   ✅ {doc_id}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Traceback:")
        traceback.print_exc()
        
        print("\n📋 FALLBACK: Manual cleanup instructions")
        print("=" * 50)
        print("If automatic cleanup failed, use one of these methods:")
        print("\n1. Google Cloud Console:")
        print("   - Go to https://console.cloud.google.com/firestore/data")
        print("   - Navigate to 'consciousnesses' collection")
        print("   - Delete the duplicate document IDs listed above")
        print("\n2. gcloud CLI:")
        print("   - Use the execute_firestore_cleanup.ps1 script")
        print("   - Or manually delete via gcloud firestore bulk-delete")

if __name__ == "__main__":
    main()
