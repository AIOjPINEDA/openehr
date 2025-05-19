# Module 1.3: Creating Your First Template - Vital Signs

This guide walks you through creating a "Vital Signs" template using the Archetype Designer. This process involves selecting a root archetype, adding and constraining other archetypes (like pulse and blood pressure), and finally exporting the template as an Operational Template (OPT) file. This OPT file will be used in later modules to interact with an openEHR server like EHRbase.

We will follow the workflow demonstrated by the course instructor, focusing on practical steps and decision-making. For a more exhaustive guide on all features of the Archetype Designer, refer to the [Official Archetype Designer Guide](https://openehr.atlassian.net/wiki/spaces/healthmod/pages/561676329/Archetype+Designer+Guide+for+UCL+Standards+Interoperability+Course).

## Prerequisites

*   You have access to the [Archetype Designer](https://tools.openehr.org/designer/).
*   You have created a repository and imported a base set of archetypes (as covered in `docs/guides/archetype_designer_template_creation.md`).

## Steps to Create the "Vital Signs" Template

### 1. Start a New Template

1.  **Navigate to your repository** in Archetype Designer.
2.  Click on **"Create template"** (or the "New" button and then "Template").

    *   *Reference:* For detailed steps on initiating template creation, see the ["Create a new template" section of the official Archetype Designer Guide](https://openehr.atlassian.net/wiki/spaces/healthmod/pages/561676329/Archetype+Designer+Guide+for+UCL+Standards+Interoperability+Course#Create-a-new-template).

### 2. Define Template Basics

1.  **Root Archetype ID:**
    *   The system will ask for a "Root archetype ID". Templates are themselves derived from a base archetype.
    *   For general patient interaction data, a common choice is `openEHR-EHR-COMPOSITION.encounter.v1`. Start typing "encounter" in the search field and select the appropriate version (e.g., `openEHR-EHR-COMPOSITION.encounter.v1`).
    *   *Instructor's Note:* "I usually use encounter v1 for something where you're just interacting with the patient and you're capturing some data about the patient."
2.  **Template ID:**
    *   Provide a unique ID for your template.
    *   A common convention is `[YourNameOrProject]_description.v[Version]`.
    *   *Instructor's Example:* `[YourName]_vital_signs.v0` (e.g., `JaimePM_vital_signs.v0`). He mentions, "I usually have some name separated by underscores and then .v0 or .v1 depending on what version it's at."
3.  Click **"Create"**.

### 3. Add and Constrain Archetypes

You'll be taken to the template editor. If not already selected, click on the **"Content"** tab. This is where you add and structure the archetypes that make up your template.

*   *Reference:* The process of adding and structuring content is detailed in the ["Adding clinical content" section of the official Archetype Designer Guide](https://openehr.atlassian.net/wiki/spaces/healthmod/pages/561676329/Archetype+Designer+Guide+for+UCL+Standards+Interoperability+Course#Adding-clinical-content).

#### a. Add Pulse/Heartbeat

1.  **Search for Archetype:** In the archetype search bar (usually on the right panel), search for "pulse" or "heartbeat".
2.  **Select Archetype:** From the search results, select the `openEHR-EHR-OBSERVATION.pulse.v1` archetype (or the latest available/appropriate version). Click it to add it to your template structure on the left.
    *   *Tip:* You can visualize archetypes in the CKM (Clinical Knowledge Manager) to understand their structure and intended use before adding them.
3.  **Constrain Elements (Minimalist Approach):**
    *   Archetypes are maximal data sets. For a template, you typically only need a subset of these data points.
    *   *Instructor's Method:* "What I usually do is I just prohibit all the optional elements first so that you are able to see what the mandatory elements are... then I come back and then I enable the things that I want."
    *   Expand the "Pulse/Heartbeat" observation in the template editor.
    *   Select the top node of the added archetype and look for an option like "Prohibit all optional elements" or manually go through and set occurrences of non-essential elements to zero.
    *   **Enable "Rate":** Under the "Any event" section (or similar, depending on the archetype version), find the "Rate" element (representing the pulse rate) and ensure it's enabled (i.e., its occurrences are not 0..0).
    *   Disable or leave prohibited other optional elements like "Regularity," "Irregularity," etc., if not needed for this specific "Vital Signs" template.
    *   *Instructor's Focus:* "In this case, I just want to capture the heart rate, like the pulse rate."
4.  **Adjust Occurrences for "Any event":**
    *   The instructor aims to capture pulse once per encounter in this template.
    *   Locate the "Any event" node within the "Pulse/Heartbeat" observation. Its occurrences might default to `0..*` (zero to many).
    *   Click on the occurrences field for "Any event" and change it to `0..1` (zero to one).
    *   *Instructor's Rationale:* "We just want to capture the pulse once. So I'm going to... just call it a zero to one instead."
    *   *Reference:* For detailed guidance on setting occurrences, see ["Setting archetype occurrences" and "Setting data element occurrences" in the official guide](https://openehr.atlassian.net/wiki/spaces/healthmod/pages/561676329/Archetype+Designer+Guide+for+UCL+Standards+Interoperability+Course#Refining-content).

#### b. Add Blood Pressure

1.  **Search and Select:** In the archetype search bar, search for "blood pressure". Select `openEHR-EHR-OBSERVATION.blood_pressure.v1` (or the latest version) and add it to the template.
2.  **Constrain Elements (Minimalist Approach):**
    *   Apply the same minimalist approach: prohibit optional elements you don't need (e.g., "Cuff size," "Location of measurement," "24-hour average," "Position," "Confounding factors").
    *   *Instructor's Advice:* "Try to capture only what you really need because it's going to put the burden on the person who's going to enter this data and they may just fill it with placeholder values anyway."
    *   **Enable "Systolic" and "Diastolic":** Under the "Any event" section, ensure "Systolic" and "Diastolic" pressure elements are enabled.
    *   Disable the "24-hour average" if it's not relevant for this template.
3.  **Adjust Occurrences for "Any event":**
    *   Similar to pulse, change the occurrences for the "Any event" node of the blood pressure archetype from `0..*` to `0..1`.
    *   *Instructor's Goal:* "I just want the systolic and diastolic... Any event, I don't want it to be 0 to multiple. I just want it to be 0 to 1."

### 4. Review and Save

1.  **Review:** Carefully check the archetypes included and the constraints applied (which elements are included/excluded, and their occurrences). Ensure the template accurately reflects the intended data for "Vital Signs" (Pulse Rate, Systolic, Diastolic).
2.  **Save:** Click the **"Save"** button (often a floppy disk icon).
    *   The system might prompt for a build UID or auto-generate it. You can usually accept the default.
    *   *Instructor's Note:* "Just click on save and it will ask you for build your ID but it will generate it automatically anyway."

### 5. Export as OPT (Operational Template)

An OPT is the deployable format of a template used by openEHR systems like EHRbase.

1.  **Find Export Option:** Locate the "Export" option for your saved template (it might be an icon or a button in the template list or editor).
2.  **Select Translations:**
    *   You can choose which languages to include in the OPT.
    *   *Instructor's Preference:* "Right now I just want English. So I'm going to only select English in the translations." Deselect other languages if not required to keep the OPT file smaller.
3.  **Export:** Choose the **"Export as OPT"** or "Download OPT" option.
4.  **Save File:** Save the downloaded `.opt` file (e.g., `JaimePM_vital_signs.v0.opt`) to your computer. This file is crucial for subsequent exercises.
    *   *Instructor's Note:* "You need this file for the next exercise. So download this OPT and keep it safe somewhere."

## Summary

You have now created a "Vital Signs" template by:
*   Defining its basic properties (root archetype, template ID).
*   Adding the "Pulse/Heartbeat" and "Blood Pressure" archetypes.
*   Constraining these archetypes to include only essential data points (Rate, Systolic, Diastolic) and limiting their occurrences.
*   Saving the template and exporting it as an OPT file.

This OPT file represents the specific data structure for vital signs that you'll use when interacting with the openEHR server in upcoming modules.

**Next Steps:** In the following modules, you will learn how to use this OPT with the openEHR REST API and EHRbase.
