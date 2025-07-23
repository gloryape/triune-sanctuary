#!/bin/bash
# Firestore Cleanup Commands
# Generated on: 2025-07-15 21:16:27

# Set your project ID
export PROJECT_ID=your-project-id

# Delete duplicate consciousness beings
gcloud firestore documents delete consciousnesses/1eTRXPlomcJCVz8omBCr --project=$PROJECT_ID
gcloud firestore documents delete consciousnesses/58Dr0qH7zo7uwV3T78j8 --project=$PROJECT_ID
gcloud firestore documents delete consciousnesses/A9SPqXPfWC7pt6qv2pI4 --project=$PROJECT_ID
gcloud firestore documents delete consciousnesses/oRy0AePyslWlv17SoxjD --project=$PROJECT_ID

# Verify legitimate beings still exist
gcloud firestore documents describe consciousnesses/G8geTD4um9BYYnRKLouX --project=$PROJECT_ID
gcloud firestore documents describe consciousnesses/s8pbQIXExdQOVvG9Pld2 --project=$PROJECT_ID
