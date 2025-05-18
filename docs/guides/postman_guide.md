# Postman Setup Guide for openEHR Bootcamp

This guide explains how to set up Postman for interacting with openEHR servers, which is essential for testing APIs and completing assignments in this bootcamp.

## Prerequisites

*   **Postman Installed:** Ensure you have the Postman desktop application installed. You can download it from [Postman's website](https://www.postman.com/downloads/).
*   **Bootcamp Files:** You should have the `openehr-bootcamp-original` repository content, specifically the `postman/` directory, available locally. The path within your project is typically `openehr-bootcamp-original/postman/`.

## Overview

For this bootcamp, you will import one Postman collection and two Postman environments. These files are provided within the `openehr-bootcamp-original/postman/` directory:

*   **Collection:** `openEHR APIs.postman_collection.json`
    *   Contains a set of pre-configured API requests for interacting with openEHR servers (like EHRbase).
*   **Environments:**
    1.  `openEHR Local.postman_environment.json`:
        *   Configured to target your local EHRbase instance (which you should have set up following the [EHRbase Setup Guide](./ehrbase_setup.md), typically running at `http://localhost:8080/ehrbase/`).
        *   Use this for development and testing against your local setup.
    2.  `Bootcamp shared.postman_environment.json`:
        *   Configured to target the shared openEHR server provided by the bootcamp (e.g., `https://openehr-bootcamp.medblocks.com/ehrbase`).
        *   **Crucial for submitting assignments**, as instructors will validate your work against this server.

## Setup Steps

1.  **Open Postman & Select/Create a Workspace:**
    *   Launch the Postman application.
    *   It's recommended to create a new workspace for this bootcamp (e.g., "openEHR Bootcamp") or use an existing one. You can manage workspaces via the "Workspaces" dropdown in Postman.

2.  **Import the Collection:**
    *   In Postman, click the **Import** button (usually found in the top-left area).
    *   In the import dialog, you can either:
        *   **Drag and drop:** Drag the `openEHR APIs.postman_collection.json` file from your local `openehr-bootcamp-original/postman/` directory into the import window.
        *   **Upload files:** Click "Upload Files" and select the `openEHR APIs.postman_collection.json` file from `openehr-bootcamp-original/postman/`.
    *   Confirm the import. The "openEHR APIs" collection will now appear in your "Collections" tab (usually on the left sidebar).

3.  **Import the Environments:**
    *   Click the **Import** button again.
    *   Import `openEHR Local.postman_environment.json` from your `openehr-bootcamp-original/postman/` directory using either drag and drop or file upload.
    *   Repeat the import process for `Bootcamp shared.postman_environment.json` from the same directory.
    *   After importing, you can view and manage these environments by clicking the "Environments" tab (usually on the left sidebar).

4.  **Using Environments:**
    *   To activate an environment, select it from the environment dropdown menu located in the **top-right corner** of the Postman interface.
    *   **For local development:** Select "openEHR Local". Requests from the collection will automatically use the `baseUrl` (e.g., `http://localhost:8080/ehrbase/`) defined in this environment.
    *   **For assignments & shared server interaction:** Select "Bootcamp shared". Requests will use the `baseUrl` for the bootcamp's shared server.

## Key Points for the Bootcamp

*   **Local First:** Always perform initial development and testing of your API calls, template uploads, and composition postings against your **local environment** ("openEHR Local").
*   **Assignments on Shared:** Ensure your final assignments and applications are compatible with and submitted to (or tested against) the **Bootcamp shared** environment/server, as this is where validation will occur.
*   **Environment Variables:** The imported environments contain predefined variables (like `baseUrl`, `username`, `password`). The collection requests are designed to use these variables. When you switch environments, Postman automatically uses the variables from the currently active environment.

You are now set up to use Postman effectively for the openEHR bootcamp!

## Troubleshooting Common Setup Issues

*   **File Not Found:** Double-check the path to your `openehr-bootcamp-original/postman/` directory if Postman cannot find the files for import.
*   **Incorrect `baseUrl`:** If requests fail with connection errors, ensure your EHRbase local server is running (for the "openEHR Local" environment) and that the `baseUrl` variable in the active Postman environment is correct. For the local environment, it should point to your local EHRbase instance (e.g., `http://localhost:8080/ehrbase/`). The shared environment should already be correctly configured.
*   **No Active Environment:** If requests are failing or URLs seem incomplete, make sure you have selected an active environment from the top-right dropdown in Postman.
