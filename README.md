# 🛡️ Network Security Mechanism

## 📋 Overview

The **Network Security Mechanism** is a robust Machine Learning project designed to detect and classify network security threats. It leverages advanced data processing data pipelines and machine learning algorithms to identify anomalies and potential attacks in network traffic.

This application is built as a complete end-to-end MLOps solution, featuring a training pipeline for model updates and a prediction pipeline served via a fast and efficient API.

## 🚀 Key Features

- **🛡️ Threat Detection**: Classifies network traffic as benign or malicious/anomalous using a trained machine learning model.
- **🔄 End-to-End Training Pipeline**: Automated pipeline for data ingestion, validation, transformation, model training, and evaluation.
- **⚡ Fast API Serving**: API endpoints built with **FastAPI** for real-time inference and training triggers.
- **📊 MLOps Integration**: Uses **MLflow** and **DagsHub** for experiment tracking, model registry, and versioning.
- **🐳 Containerized**: Fully Dockerized application for consistent deployment across environments.
- **☁️ Cloud Ready**: Deployed using AWS services (ECR, EC2) with a CI/CD pipeline via GitHub Actions.

## 🛠️ Tech Stack

### Core

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Data Manipulation**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Database**: MongoDB (Atlas)

### MLOps & Infrastructure

- **Experiment Tracking**: MLflow, DagsHub
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Cloud Provider**: AWS (ECR, EC2/Runner)

## 📂 Project Structure

```
NetworkSecurity/
├── networksecurity/        # Main package
│   ├── components/         # Pipeline components (Ingestion, Validation, etc.)
│   ├── pipeline/           # Training and Prediction pipelines
│   ├── entity/             # Data classes and configuration entities
│   ├── constants/          # Project constants
│   ├── utils/              # Utility functions
│   └── exception/          # Custom exception handling
├── .github/workflows/      # CI/CD Workflows
├── app.py                  # API Entry point
├── requirements.txt        # Dependencies
├── Dockerfile              # Docker configuration
└── README.md               # Project documentation
```

## 🔌 API Endpoints

The application provides the following endpoints:

| Method | Endpoint   | Description                                                            |
| :----- | :--------- | :--------------------------------------------------------------------- |
| `GET`  | `/`        | Redirects to Swagger UI documentation.                                 |
| `GET`  | `/train`   | Triggers the Machine Learning Training Pipeline.                       |
| `POST` | `/predict` | Upload a CSV file to get predictions (returns HTML table & saves CSV). |
| `GET`  | `/docs`    | Interactive API documentation (Swagger UI).                            |

## ⚙️ Installation & Local Setup

### Prerequisites

- Python 3.8+
- MongoDB URL
- AWS Credentials (optional, for cloud features)

### 1. Clone the Repository

```bash
git clone https://github.com/DakshaMudumbai/NetworkSecurity.git
cd NetworkSecurity
```

### 2. Create a Virtual Environment

```bash
conda create -n networksecurity python=3.10 -y
conda activate networksecurity
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configuration

Create a `.env` file in the root directory and add your environment variables:

```env
MONGO_DB_URL="your_mongodb_connection_string"
AWS_ACCESS_KEY_ID="your_aws_access_key"
AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
AWS_REGION="us-east-1"
DAGSHUB_TOKEN="your_dagshub_token"
```

### 5. Run the Application

```bash
python app.py
```

Access the API at `http://localhost:8000/docs`.

## 🐳 Docker Usage

Build and run the container locally:

```bash
# Build the image
docker build -t networksecurity .

# Run the container
docker run -p 8080:8000 --env-file .env networksecurity
```

## 🔄 CI/CD Pipeline

The project implements a continuous integration and deployment pipeline using GitHub Actions:

1. **Continuous Integration**:
   - Triggers on push to `main`.
   - Lints code and runs unit tests.

2. **Continuous Delivery**:
   - Builds the Docker image.
   - Pushes the image to **AWS Elastic Container Registry (ECR)**.

3. **Continuous Deployment**:
   - Pulls the latest image from ECR on a self-hosted runner or EC2 instance.
   - Stops and removes the previous container.
   - Runs the new container with updated code.

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.
