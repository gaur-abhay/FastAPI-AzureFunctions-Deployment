# <img src="https://github.com/user-attachments/assets/c707f0af-cb44-492e-8ba8-d23046dec6c9" alt="image" width="40" height="40"/> FastAPI Deployment to Azure Functions (Learning Project)

This repository demonstrates how to deploy a FastAPI application to **Azure Functions** using the v2 model with a `function_app.py` file. The goal of this project is to showcase the deployment process of a basic FastAPI app using Azure’s serverless computing capabilities.

## 🔗 GitHub Repository
[GitHub Repository Link](https://github.com/gaur-abhay/FastAPI-AzureFunctions-Deployment) 

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

1. Initialize a new Azure Function in your project directory:
    ```bash
    func init --worker-runtime python
    ```

3. Create an HTTP-triggered function:
    ```bash
    func new --name HttpTrigger --template "HTTP trigger" --authlevel "anonymous"
    ```

4. Modify `function_app.py` to route requests to FastAPI app (as given in codebase).

---

## 🚀Deploying FastAPI to Azure Functions

Deploying the FastAPI app to Azure Functions involves the following steps:

1. **Login to Azure** via CLI:
    ```bash
    az login
    ```

2. **Deploy the App**:

   - First, create a ZIP file of your function app:
     ```bash
     zip -r function.zip .
     ```

   - Then, deploy the ZIP file to your Azure Function App:
     ```bash
     az functionapp deployment source config-zip --name <YOUR_FUNCTION_APP_NAME> --resource-group <YOUR_RESOURCE_GROUP_NAME> --src function.zip
     ```

![image](https://github.com/user-attachments/assets/1864296b-7a76-4a05-a5ba-8743bdd7505c)


---

## Testing the Deployment

Once deployed, you can test your FastAPI app by accessing the provided function URL.

1. **Get the URL**:
   The Azure CLI will output the URL for function app after deployment. It will look something like:
   ```
   https://<YOUR_FUNCTION_APP_NAME>.azurewebsites.net/HttpTrigger
   ```

2. **Test the API**:
   Use `curl` or Postman to send a request to your FastAPI endpoint:
   ```bash
   curl https://<YOUR_FUNCTION_APP_NAME>.azurewebsites.net/HttpTrigger
   ```

   You should see a JSON response similar to:
   ```json
   {
       "message": "Hello from FastAPI deployed on Azure Functions!"
   }
   ```

![image](https://github.com/user-attachments/assets/0b4d52bb-a6e6-40a1-9873-9617e8b2a63b)


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

