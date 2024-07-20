#!/bin/bash

# Deploy the trained model on AI Platform
gcloud ai models upload --region=your-region --display-name=predictive_model --artifact-uri=gs://your-bucket/predictive_model.h5
