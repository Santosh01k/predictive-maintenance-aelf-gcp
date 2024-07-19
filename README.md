# Predictive Maintenance on aelf Blockchain Using GCP AI Solutions

## Project Overview
This project demonstrates how to leverage Google Cloud Platform’s AI services to implement a predictive maintenance system on the aelf blockchain.

## Repository Structure
```sh
predictive-maintenance-aelf-gcp
│
├── aelf
│ ├── contracts
│ │ └── MaintenanceContract.cs
│ └── scripts
│ └── deploy_contract.sh
│
├── gcp
│ ├── cloud_functions
│ │ ├── data_extraction.py
│ │ └── prediction_api.py
│ ├── model
│ │ ├── model_training.py
│ │ └── requirements.txt
│ └── scripts
│ └── deploy_model.sh
│
├── README.md
└── LICENSE
```

## Getting Started

### Prerequisites
- aelf SDK and CLI
- GCP account
- Python environment

### Steps

1. **Deploy aelf Smart Contracts**
    - Navigate to the `aelf` directory and run the deployment script:
    ```sh
    cd aelf/scripts
    ./deploy_contract.sh
    ```

2. **Set Up GCP Cloud Functions**
    - Navigate to the `gcp/cloud_functions` directory and deploy the functions:
    ```sh
    cd gcp/cloud_functions
    gcloud functions deploy data_extraction --runtime python39 --trigger-http --allow-unauthenticated
    gcloud functions deploy prediction_api --runtime python39 --trigger-http --allow-unauthenticated
    ```

3. **Train and Deploy Machine Learning Model**
    - Navigate to the `gcp/model` directory, install the required packages, and run the training script:
    ```sh
    cd gcp/model
    pip install -r requirements.txt
    python model_training.py
    ```
    - Deploy the model on AI Platform:
    ```sh
    cd ../scripts
    ./deploy_model.sh
    ```

## License
This project is licensed under the MIT License.
