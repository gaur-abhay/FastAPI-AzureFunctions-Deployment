# FastAPI Deployment to Azure Functions (Learning Project)

This repository showcases how to deploy a FastAPI application to **Azure Functions**, demonstrating my learning of cloud deployment and serverless architecture. The FastAPI app is kept minimal for demonstration purposes.

## Table of Contents
- [About](#about)
- [Prerequisites](#prerequisites)
- [FastAPI Application Setup](#fastapi-application-setup)
- [Creating an Azure Function](#creating-an-azure-function)
- [Deploying FastAPI to Azure Functions](#deploying-fastapi-to-azure-functions)
- [Testing the Deployment](#testing-the-deployment)
- [What I Learned](#what-i-learned)
- [Conclusion](#conclusion)

## About

This is a learning project aimed at showcasing the deployment process of a FastAPI application to Azure Functions. I am working on FastAPI-related tasks at Mila AI, and this project helps me apply and demonstrate my knowledge of deploying cloud applications, focusing on the serverless approach using Azure.

![Azure Functions Deployment](<ADD_YOUR_IMAGE_URL_HERE>)

---

## Prerequisites

Before you begin, ensure you have the following installed:
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Azure Functions Core Tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- [Python 3.7+](https://www.python.org/downloads/)
- FastAPI (`pip install fastapi uvicorn`)

---

## FastAPI Application Setup

To start, we create a minimal FastAPI app with one endpoint.

```bash
mkdir fastapi-azure-functions-sample
cd fastapi-azure-functions-sample
pip install fastapi uvicorn
```

In `main.py`, we’ll define a basic FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Azure Functions!"}
```

---

## Creating an Azure Function

Next, we’ll initialize the Azure Function and set up the HTTP trigger to route requests to our FastAPI app.

1. Install Azure Functions Core Tools if you haven't already:
    ```bash
    npm install -g azure-functions-core-tools@4 --unsafe-perm true
    ```

2. Initialize a new Azure Function in your project directory:
    ```bash
    func init --worker-runtime python --language python
    ```

3. Create an HTTP-triggered function:
    ```bash
    func new --template "HTTP trigger" --name "FastAPIHttpTrigger"
    ```

4. Modify `FastAPIHttpTrigger/__init__.py` to route requests to your FastAPI app (as shown earlier).

---

## Deploying FastAPI to Azure Functions

Deploying the FastAPI app to Azure Functions involves the following steps:

1. **Login to Azure** via CLI:
    ```bash
    az login
    ```

2. **Create a resource group** (if needed):
    ```bash
    az group create --name fastapi-azure-function-rg --location westus
    ```

3. **Create a Function App**:
    ```bash
    az functionapp create --resource-group fastapi-azure-function-rg --consumption-plan-location westus --runtime python --functions-version 4 --name <YOUR_FUNCTION_NAME> --storage-account <YOUR_STORAGE_ACCOUNT_NAME>
    ```

4. **Deploy the app**:
    ```bash
    func azure functionapp publish <YOUR_FUNCTION_NAME>
    ```

---

## Testing the Deployment

You can test the deployment by accessing the provided function URL:

```bash
curl https://<YOUR_FUNCTION_NAME>.azurewebsites.net/api/FastAPIHttpTrigger
```

Expected response:
```json
{
  "message": "Hello from FastAPI deployed on Azure Functions!"
}
```

---

## What I Learned

During this project, I learned how to:
- Deploy a **FastAPI** app to **Azure Functions**.
- Use **Azure CLI** for resource management and deployments.
- Manage Azure Functions triggers for handling HTTP requests.
- Configure serverless infrastructure and understand how it scales based on demand.

This project was a great opportunity to apply my knowledge of serverless architecture while working on other FastAPI-related tasks at my company.

---

## Conclusion

This sample project demonstrates how to deploy a FastAPI application on Azure Functions. While it’s a minimal app, the process can be easily extended to more complex applications. Feel free to explore and contribute!

---
