import logging
import azure.functions as func
from azure.functions import AsgiMiddleware
from app import app  # Import existing FastAPI app

function_app = func.FunctionApp()

@function_app.route(route="HttpTrigger", auth_level=func.AuthLevel.ANONYMOUS)
def HttpTrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse("Hello from FastAPI deployed on Azure Functions!", status_code=200)


# Create an ASGI middleware for the FastAPI app
asgi_middleware = AsgiMiddleware(app)

# Define an ASGI route
@function_app.route(route="/{*path}", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET", "POST", "PUT", "DELETE"])
async def asgi_handler(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await asgi_middleware.handle_async(req, context)
