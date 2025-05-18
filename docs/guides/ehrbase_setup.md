# EHRbase Setup Guide for the Bootcamp

This guide provides step-by-step instructions to set up EHRbase locally using Docker for the openEHR bootcamp. EHRbase is an open-source openEHR server we will use throughout this course.

## Prerequisites

*   **Docker Desktop:** Ensure Docker Desktop is installed and running on your macOS. Download it from [Docker Hub](https://www.docker.com/products/docker-desktop/).

## Bootcamp Configuration Overview

This bootcamp uses a specific, simplified Docker configuration for EHRbase to streamline the learning process. The necessary files are located in the `openehr-bootcamp-original/` directory within your project:

1.  **`docker-compose.yaml`**:
    *   Defines two services: `db` (PostgreSQL 16) and `ehrbase`.
    *   Mounts an initialization script for the PostgreSQL database.
    *   Exposes EHRbase on `http://localhost:8080`.
2.  **`init.sql`**:
    *   A SQL script that runs when the PostgreSQL container starts for the first time.
    *   Creates the `ehrbase` database and user required by the EHRbase server for this bootcamp's configuration.

**Important:** Use this provided setup. It's tailored for the bootcamp and differs from the generic `docker-compose.yml` found in the official EHRbase repository.

## Local Setup Steps

1.  **Open Terminal:**
    Use your preferred terminal application (e.g., VS Code integrated terminal, macOS Terminal).

2.  **Navigate to Directory:**
    Change to the `openehr-bootcamp-original/` directory:
    ```zsh
    cd "/Users/jaimepm/Library/Mobile Documents/com~apple~CloudDocs/Wiki/Data Science 🐍 /Learning Data Science/OpenEHR/openehr-bootcamp-original"
    ```

3.  **Start Docker Containers:**
    Run the following command to download images (if not present) and start the PostgreSQL and EHRbase containers:
    ```zsh
    docker compose up -d
    ```
    *   The `-d` flag runs containers in detached mode (in the background). Omit `-d` to see live logs. If you run without `-d`, press `Ctrl + C` to stop.

4.  **Verify Setup:**
    Allow a few moments for services to initialize.
    *   **Docker Desktop:** Check the Docker Desktop application. You should see two running containers (e.g., `openehr-bootcamp-original-db-1`, `openehr-bootcamp-original-ehrbase-1`).
    *   **EHRbase Status Page:** Open your web browser and navigate to `http://localhost:8080/ehrbase/`. You should see a status message (e.g., "EHRbase is running!").
    *   **Swagger UI (API Docs):** Navigate to `http://localhost:8080/ehrbase/swagger-ui.html`. This interface lists all EHRbase REST API endpoints.

EHRbase is now running locally.

## Stopping EHRbase

To stop the EHRbase and PostgreSQL containers:

1.  Ensure you are in the `openehr-bootcamp-original/` directory in your terminal.
2.  Run:
    ```zsh
    docker-compose down
    ```
    This stops and removes the containers. Data in PostgreSQL will persist due to Docker volumes unless you explicitly remove them (e.g., `docker-compose down -v`).

## Troubleshooting

*   **Port Conflicts:** If `8080` or `5432` are in use, `docker-compose` will fail. Stop the conflicting service or change the port mapping in `docker-compose.yaml` (e.g., `ports: - "8081:8080"` to access EHRbase on `http://localhost:8081`).
*   **Image Download Issues:** Check your internet connection.
*   **Database Initialization Errors:** Review logs from the `db` container (`docker logs <db_container_name>`). Ensure `init.sql` is correct.

## Next Steps

With EHRbase running, you are ready to proceed with Module 1 activities, which will involve interacting with this openEHR server.
