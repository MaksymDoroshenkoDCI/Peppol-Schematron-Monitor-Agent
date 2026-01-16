#!/bin/bash

# Configuration
PROJECT_ID="agentic-peppol-monitor"
REGION="us-central1"
REPO_NAME="peppol-repo"
SERVICE_NAME="agentic-peppol-monitor"
IMAGE_PATH="$REGION-docker.pkg.dev/$PROJECT_ID/$REPO_NAME/$SERVICE_NAME"

echo "Deploying $SERVICE_NAME to GCP Project: $PROJECT_ID in Region: $REGION..."

# 1. Build and Submit to Cloud Build
echo "Step 1: Building container image via Cloud Build in project $PROJECT_ID..."
gcloud builds submit --project $PROJECT_ID --tag $IMAGE_PATH .

# 2. Deploy to Cloud Run
echo "Step 2: Deploying to Cloud Run in project $PROJECT_ID..."
gcloud run deploy $SERVICE_NAME \
    --project $PROJECT_ID \
    --image $IMAGE_PATH \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated \
    --set-env-vars GOOGLE_API_KEY=AIzaSyChofjJiGGIWfLMzuoqDprGYvswMyicL-s

echo "Deployment complete!"
gcloud run services describe $SERVICE_NAME --platform managed --region $REGION --format 'value(status.url)'
