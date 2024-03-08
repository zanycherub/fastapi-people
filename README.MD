## LOCAL TESTING
1. Run the application using uvicorn, automatically reload the app when a change was done.
    ```
    uvicorn main:app --reload
    ```

## DOCKER DEPLOYMENT

1. Build the Docker Image:
    Open a terminal and navigate to the directory containing your Dockerfile.
    Run the following command to build the Docker image (replace people-fastapi-app with your desired image name):
    ```
    docker build -t people-fastapi-app .
    ```

2. Run the Docker Container:
    Once the image is built, you can create and run a container from it:
    ```
    docker run -d -p 8000:8000 people-fastapi-app
    ```

    This command starts a container in detached mode (-d) and maps port 8000 from the host to port 8000 in the container.


3. Access Your FastAPI App:
Open a web browser or use a tool like curl to access your FastAPI app at http://localhost:8000.