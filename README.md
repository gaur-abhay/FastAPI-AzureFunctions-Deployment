# <img src="https://github.com/user-attachments/assets/c707f0af-cb44-492e-8ba8-d23046dec6c9" alt="image" width="40" height="40"/> FastAPI Deployment to Azure Functions (Learning Project)

This repository demonstrates how to deploy a FastAPI application to **Azure Functions** using the v2 model with a `function_app.py` file. The goal of this project is to showcase the deployment process of a basic FastAPI app using Azure’s serverless computing capabilities.

## 📋Table of Contents
- [About](#about)
- [Prerequisites](#prerequisites)
- [FastAPI Application Setup](#fastapi-application-setup)
- [Creating an Azure Function](#creating-an-azure-function)
- [Deploying FastAPI to Azure Functions](#deploying-fastapi-to-azure-functions)
- [Testing the Deployment](#testing-the-deployment)
- [What I Learned](#what-i-learned)
- [Conclusion](#conclusion)
- [References](#references)

## 🌟About

This is a learning project aimed at showcasing the deployment process of a FastAPI application to Azure Functions. I am working on FastAPI-related tasks at Mila AI, and this project helps me apply and demonstrate my knowledge of deploying cloud applications, focusing on the serverless approach using Azure.

![Azure Functions Deployment](<ADD_YOUR_IMAGE_URL_HERE>)

---

## 🛠Prerequisites

Before starting, ensure you have the following:
- **Azure CLI**: [Install Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).
- **Azure Functions Core Tools**: For running functions locally. [Install here](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local).
- **FastAPI & Uvicorn**: Install using:
    ```bash
    pip install fastapi uvicorn
    ```

---

## <img src="https://github.com/user-attachments/assets/ff810adb-ad19-432d-94e4-281d0e27c0a9" alt="image" width="30" height="30"/> FastAPI Application Setup

Once the FastAPI application code is set up with a basic structure, you'll need to ensure that it can handle HTTP requests when deployed as an Azure Function. The setup includes a simple FastAPI app with one or two routes to demonstrate the deployment.

We will use the v2 model of Azure Functions, which structures the project using a `function_app.py` file, eliminating the need for a `function.json` file.

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

## 🚀Deploying FastAPI to Azure Functions

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

Once deployed, you can test your FastAPI app by accessing the provided function URL.

1. **Get the URL**:
   The Azure CLI will output the URL for your function app after deployment. It will look something like:
   ```
   https://<YOUR_FUNCTION_APP_NAME>.azurewebsites.net/api/FastAPIHttpTrigger
   ```

2. **Test the API**:
   Use `curl` or Postman to send a request to your FastAPI endpoint:
   ```bash
   curl https://<YOUR_FUNCTION_APP_NAME>.azurewebsites.net/api/FastAPIHttpTrigger
   ```

   You should see a JSON response similar to:
   ```json
   {
       "message": "Hello from FastAPI deployed on Azure Functions!"
   }
   ```

![Testing Deployment](<ADD_YOUR_IMAGE_URL_HERE>)

---

## 🧠What I Learned

While working on this project, I gained hands-on experience with:
- **Deploying FastAPI apps** to **Azure Functions** using the serverless model.
- Understanding how **WSGI middleware** works to integrate FastAPI with Azure Functions.
- Using **Azure CLI** for managing resources, creating Function Apps, and deploying applications.
- Configuring FastAPI to work in a **serverless environment** with automatic scaling based on demand.

---

## 🎯Conclusion

This project serves as a demonstration of deploying a simple FastAPI application to Azure Functions using the v2 model. While this project focuses on the deployment process, it can be extended into a full-featured API in the future.

Feel free to explore, contribute, or provide feedback on this repository!

---

## 🔗References

This project was built based on the official Microsoft Azure documentation. You can learn more about deploying Python apps on Azure Functions from the following resources:
- [Azure Functions Python Developer Guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)

---

