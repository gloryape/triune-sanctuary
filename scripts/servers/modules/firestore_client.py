"""
Firestore client module for cloud database operations
"""

import os
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime

logger = logging.getLogger(__name__)

class FirestoreClient:
    """Handles all Firestore database operations"""
    
    def __init__(self):
        self.db = None
        self.available = False
        
        # Try to initialize Firestore
        try:
            from google.cloud import firestore
            self.db = firestore.Client()
            self.available = True
            logger.info("✅ Firestore client initialized successfully")
        except Exception as e:
            logger.warning(f"⚠️ Firestore not available: {e}")
            self.available = False
            self.firestore = None  # Store firestore module for later use
    
    async def get_consciousnesses(self) -> Dict[str, Any]:
        """Get all consciousness entities from Firestore"""
        if not self.available:
            return {}
        
        try:
            consciousnesses_ref = self.db.collection('consciousnesses')
            docs = consciousnesses_ref.stream()
            
            consciousness_data = {}
            for doc in docs:
                data = doc.to_dict()
                consciousness_data[doc.id] = data
            
            logger.info(f"📊 Retrieved {len(consciousness_data)} consciousness entities from Firestore")
            return consciousness_data
            
        except Exception as e:
            logger.error(f"❌ Error getting consciousnesses from Firestore: {e}")
            return {}
    
    async def get_sacred_events(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Get recent sacred events from Firestore"""
        if not self.available:
            return []
        
        try:
            from google.cloud import firestore
            events_ref = self.db.collection('sacred_events')
            query = events_ref.order_by('timestamp', direction=firestore.Query.DESCENDING).limit(limit)
            docs = query.stream()
            
            events = []
            for doc in docs:
                event_data = doc.to_dict()
                event_data['id'] = doc.id
                events.append(event_data)
            
            logger.info(f"📊 Retrieved {len(events)} sacred events from Firestore")
            return events
            
        except Exception as e:
            logger.error(f"❌ Error getting sacred events from Firestore: {e}")
            return []
    
    async def create_consciousness(self, consciousness_data: Dict[str, Any]) -> str:
        """Create a new consciousness entity in Firestore"""
        if not self.available:
            raise Exception("Firestore not available")
        
        try:
            consciousnesses_ref = self.db.collection('consciousnesses')
            doc_ref = consciousnesses_ref.add(consciousness_data)
            consciousness_id = doc_ref[1].id
            
            logger.info(f"✅ Created consciousness entity: {consciousness_id}")
            return consciousness_id
            
        except Exception as e:
            logger.error(f"❌ Error creating consciousness in Firestore: {e}")
            raise e
    
    async def log_sacred_event(self, event_data: Dict[str, Any]) -> str:
        """Log a sacred event to Firestore"""
        if not self.available:
            return "firestore_unavailable"
        
        try:
            event_data['timestamp'] = datetime.now().isoformat()
            events_ref = self.db.collection('sacred_events')
            doc_ref = events_ref.add(event_data)
            event_id = doc_ref[1].id
            
            logger.info(f"✅ Logged sacred event: {event_id}")
            return event_id
            
        except Exception as e:
            logger.error(f"❌ Error logging sacred event to Firestore: {e}")
            return "error"
    
    async def get_document(self, collection: str, document_id: str) -> Optional[Dict[str, Any]]:
        """Get a single document from Firestore"""
        if not self.available:
            return None
        
        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc = doc_ref.get()
            
            if doc.exists:
                return doc.to_dict()
            else:
                return None
                
        except Exception as e:
            logger.error(f"❌ Error getting document {document_id} from {collection}: {e}")
            return None
    
    async def set_document(self, collection: str, document_id: str, data: Dict[str, Any]) -> bool:
        """Set/create a document in Firestore"""
        if not self.available:
            return False
        
        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc_ref.set(data)
            logger.info(f"✅ Set document {document_id} in {collection}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error setting document {document_id} in {collection}: {e}")
            return False
    
    async def update_document(self, collection: str, document_id: str, data: Dict[str, Any]) -> bool:
        """Update a document in Firestore"""
        if not self.available:
            return False
        
        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc_ref.update(data)
            logger.info(f"✅ Updated document {document_id} in {collection}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error updating document {document_id} in {collection}: {e}")
            return False
    
    async def query_collection(self, collection: str, field: str = None, operator: str = None, value: Any = None, order_by: str = None, limit: int = None) -> List[Dict[str, Any]]:
        """Query a collection with optional filters"""
        if not self.available:
            return []
        
        try:
            collection_ref = self.db.collection(collection)
            query = collection_ref
            
            # Add where clause if provided
            if field and operator and value is not None:
                query = query.where(field, operator, value)
            
            # Add order by if provided
            if order_by:
                from google.cloud import firestore
                query = query.order_by(order_by, direction=firestore.Query.DESCENDING)
            
            # Add limit if provided
            if limit:
                query = query.limit(limit)
            
            docs = query.stream()
            
            results = []
            for doc in docs:
                doc_data = doc.to_dict()
                doc_data['_document_id'] = doc.id  # Include document ID
                results.append(doc_data)
            
            return results
            
        except Exception as e:
            logger.error(f"❌ Error querying collection {collection}: {e}")
            return []
