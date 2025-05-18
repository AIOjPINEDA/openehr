# Archetype Designer Setup and Vital Signs Template Creation

This guide walks you through setting up the Archetype Designer, importing necessary archetypes, and creating a "Vital Signs" template as demonstrated in the bootcamp. The Archetype Designer is a web-based tool for creating and managing openEHR archetypes and templates.

## 1. Accessing and Setting Up Archetype Designer

1.  **Open Archetype Designer:**
    *   Navigate to the [Archetype Designer website](https://tools.openehr.org/designer/#/).
    *   If you don't have an account, sign up using one of the provided options (e.g., Google, GitHub). If you have an account, sign in.

2.  **Create a New Repository:**
    *   Once signed in, you'll be on the main page.
    *   Click on "Create new repository".
    *   Choose the "Local folder" option (this stores the repository definition in your browser's local storage).
    *   Enter a name for your repository (e.g., `OpenEHRBootcampCourse` or `[YourName]CourseRepo`). The instructor used `OpenAirTechnicalCourse`.
    *   Click "Create".

3.  **Importing Archetypes:**
    *   **Obtain Archetypes:** You'll need a ZIP file containing a collection of archetypes. The bootcamp instructor mentions performing a bulk export from the CKM (Clinical Knowledge Manager) of all non-rejected/non-deprecated archetypes. The CKM is a public repository of openEHR archetypes. For this guide, we assume you have already obtained such a `.zip` file.
    *   **Navigate to Your Repository:** In Archetype Designer, click on the name of the repository you just created.
    *   **Import:**
        *   Click the "Import" button (often an upward arrow icon or labeled "Import archetypes").
        *   Drag and drop the downloaded archetype `.zip` file into the designated area or use the file browser to select it.
        *   Click "Upload". This process might take a few moments as it imports all the archetypes into your repository.

## 2. Creating a "Vital Signs" Template

Once the archetypes are imported into your repository, you can create a template. Templates combine several archetypes to define a specific clinical data structure.

1.  **Start a New Template:**
    *   Inside your repository in Archetype Designer, click on "Create template".

2.  **Define Template Basics:**
    *   **Root Archetype ID:** For the "Root archetype ID", you need to select a `COMPOSITION` archetype. Start typing `COMPOSITION` in the search field. A common choice for clinical encounters is `openEHR-EHR-COMPOSITION.encounter.v1`. The instructor mentions using "encounter v1" as a general term for this concept. Select the appropriate version from the list.
    *   **Template ID:** Enter a unique ID for your template. A common convention is `[YourNameOrProject]_description.v[Version]` (e.g., `JaimePM_vital_signs.v0`). The instructor suggests a name separated by underscores, followed by `.v0` or `.v1`.
    *   Click "Create".

3.  **Add Content (Archetypes) to the Template:**
    *   You'll be taken to the template editor. If not already selected, click on the "Content" tab.
    *   This interface allows you to search for imported archetypes and add them to your template.

    *   **a. Add Pulse/Heartbeat:**
        *   In the archetype search bar (usually on the right panel), search for "pulse" or "heartbeat".
        *   From the search results, select the `openEHR-EHR-OBSERVATION.pulse.v1` archetype (or the latest version available). Click it to add it to your template structure on the left.
        *   **Constrain Elements:**
            *   Archetypes are maximal datasets. For a specific template, you'll often want to include only a subset of an archetype's data points.
            *   The instructor's approach: First, prohibit all optional elements to get a minimal view. Then, selectively enable what's needed.
            *   For the "Pulse/Heartbeat" observation, expand its structure in the template editor.
            *   Focus on the "Any event" section. Enable the "Rate" element (representing the pulse rate). Disable or leave prohibited other optional elements like "Regularity" if not needed for this template.
            *   **Occurrences:** The instructor aims to capture pulse once per encounter in this specific template.
                *   Locate the "Any event" node within the "Pulse/Heartbeat" observation.
                *   Its occurrences might be `[0..*]` (zero to many). To restrict it to a single optional recording, click on the occurrences field and change it to `[0..1]` (zero to one).

    *   **b. Add Blood Pressure:**
        *   In the archetype search bar, search for "blood pressure".
        *   Select `openEHR-EHR-OBSERVATION.blood_pressure.v1` (or the latest version). Add it to the template.
        *   **Constrain Elements:**
            *   Again, prohibit optional elements you don't need (e.g., "Cuff size", "Location of measurement", "24-hour average", "Position", "Confounding factors").
            *   Enable "Systolic" and "Diastolic" under the "Any event" section.
            *   **Occurrences:** Similar to pulse, change the occurrences for the "Any event" node of blood pressure from `[0..*]` to `[0..1]`.

4.  **Review and Save:**
    *   Carefully review the archetypes included in your template and the constraints applied (which elements are included/excluded, and their occurrences).
    *   Ensure the template reflects the intended data for "Vital Signs" (Pulse Rate, Systolic, Diastolic).
    *   Click the "Save" button (often a floppy disk icon). The system might auto-generate a more detailed internal ID.

5.  **Export as OPT (Operational Template):**
    *   An OPT (Operational Template) is the deployable format of a template used by openEHR systems.
    *   Find the "Export" option for your saved template (it might be an icon or a button in the template list or editor).
    *   **Translations:** Before exporting, you can select which languages to include in the OPT. If "English" is the primary language, ensure it's selected. Deselect others if not required to keep the OPT file smaller.
    *   Choose the "Export as OPT" or "Download OPT" option.
    *   Save the downloaded `.opt` file (e.g., `JaimePM_vital_signs.v0.opt`) to your computer. This file is crucial for subsequent steps in the bootcamp, such as using it with EHRbase.

You have now successfully set up Archetype Designer, imported a base set of archetypes, created a new "Vital Signs" template by combining and constraining existing archetypes, and exported it as an OPT file.
