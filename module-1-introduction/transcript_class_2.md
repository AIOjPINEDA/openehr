
## Guide for Creating Your First OpenEHR Template

This guide synthesizes the key discussions, recommendations, and troubleshooting tips from the second class of the OpenEHR bootcamp, focusing on creating your first template using the Archetype Designer.

### 1. Understanding Templates and Archetypes

* **Decoupling:** Remember the importance of decoupling the visual form (how it looks) from the underlying data models (archetypes and templates). The template defines the data structure.
* **Goal:** The aim is for consistent modeling. Different people modeling the same clinical concept should ideally arrive at similar modeling conclusions using standardized archetypes.

### 2. Using the Archetype Designer Tool

* **Environment Access:** Ensure you have proper access to the learning platform/environment provided for the bootcamp. If you face issues, contact the support team (like Vipin mentioned in the transcript).
* **Finding Archetypes:**
    * The main search bar in Archetype Designer performs an exact text match, which might not find archetypes if you don't know the precise name (e.g., searching "SpO2" won't find "Pulse oximetry").
    * **Use "Find Resources" Tab:** This is a more powerful search. It searches across all fields (name, description, use, misuse) within the CKM (Clinical Knowledge Manager). Use this to find archetypes like "SpO2" by searching for the term; it will correctly lead you to the "Pulse oximetry" archetype.
    * **External Search:** Googling clinical terms (like "What is SpO2?") can help you identify the correct medical concept (Oximetry) to search for in the CKM or Archetype Designer.
* **Adding Archetypes:** Drag and drop archetypes from the right-hand panel onto your template canvas.
* **Importing Archetypes:**
    * You can import archetypes individually or in bulk.
    * **Caution with Bulk Import:** Be mindful that bulk imports might bring in outdated or incorrect versions of archetypes (e.g., Pulse v0 instead of the current Pulse v2).
    * **Recommendation:** For professional/critical work, import archetypes individually after verifying they are the correct and latest versions from the CKM. This gives you better control.

### 3. Configuring Archetypes within the Template

* **Cardinality:** Adjust the occurrence (cardinality) of archetypes and their elements as needed. For this task, many vital signs were set to `0..1` (optional) instead of the default `1..1` (mandatory).
    * Click on the archetype or element in the template structure.
    * Modify the "Occurrences" field (e.g., set max to 1).
* **Removing Unnecessary Elements:** Hide or remove elements within an archetype that are not required for your specific use case. You can do this by clicking on the element and setting its occurrence to `0..0` or using the "strike-out" / hide option. Sometimes sections might need manual removal (like the "24 hour average" mentioned).
* **Specific Archetype Notes (from the class):**
    * **SpO2:** Found within the "Pulse oximetry" archetype.
    * **Blood Pressure:** Contains Systolic and Diastolic measurements. A discussion arose about making Systolic mandatory (`1..1`) if *any* blood pressure data (like position or time) is entered, while Diastolic might remain optional (`0..1`) because it's not always measurable (e.g., via palpation). The template itself *cannot* enforce conditional mandatory fields like "make Systolic mandatory *only if* Position is entered." However, setting Systolic to `1..1` within the Blood Pressure archetype means *if* a Blood Pressure observation is recorded *at all*, Systolic must be included. The overall Blood Pressure observation archetype itself can remain optional (`0..1`) in the template.
    * **Pulse:** Be aware of versions. The class noted someone accidentally used "Pulse v0" instead of the current "Pulse v2". Using incorrect versions can cause interoperability issues later.

### 4. Organizing Your Template: Using Sections

* **What are Sections?** Sections use the "Ad Hoc Heading" archetype. They are primarily for organizational purposes within the Archetype Designer and the resulting template structure. They group related archetypes under a meaningful heading (e.g., grouping Body Temperature, Blood Pressure, Pulse under a "Vitals" section).
* **How to Use:** Add the "Ad Hoc Heading" archetype and rename it (e.g., to "Vitals"). Then, drag and drop other archetypes *under* this section heading in the hierarchy.
* **Benefits:** Makes large templates less messy and easier to navigate.
* **Querying:** While primarily organizational, you *can* use section names in AQL queries later (e.g., retrieve Body Temperature *only if* it's within the "Vitals" section).
* **Reusability:** Sections are key if you want to extract and reuse a *group* of archetypes together.

### 5. Reusing Template Components: Extraction

* **Extracting Sections/Archetypes:** You can extract a part of your template (like a configured archetype or a whole section with multiple archetypes) to make it a reusable component.
    * Click on the section or archetype you want to reuse.
    * Use the "Extract" icon (looked like a pop-up or box-with-arrow icon next to the download icon in the transcript description).
    * Give the extracted component a name (e.g., "Vitals Component").
* **Using Extracted Components:** This extracted piece will appear in your right-hand panel (like other archetypes) and can be dragged into other templates. This is very useful for complex, common structures like medication orders or vital signs groups.
* **Scope:** These extracted components are linked to your local Archetype Designer account/repository.

### 6. Managing Versions

* **Archetype Versions:** Always try to use the latest, validated version of an archetype from the CKM (e.g., Pulse v2). Check the archetype details and compare with CKM if unsure. The "Updates" button in Archetype Designer (if visible) might help but primarily works for semantic version updates (e.g., v2.0.1 to v2.0.2), not major version jumps (like v0 to v2) or different archetypes.
* **Template Versions:**
    * **Semantic Version (SemVer):** The Archetype Designer automatically handles minor semantic version changes (e.g., `1.0.0` to `1.0.1`) when you save changes.
    * **Template ID:** When uploading to an OpenEHR server (like the bootcamp's), you often need a *unique Template ID* for each distinct version, especially for breaking changes. This is why people often include the version number in the Template ID itself (e.g., `my_template_v1`, `my_template_v2`).
    * **Overwriting:** Be careful. If you modify a template in the Archetype Designer and save it without changing the Template ID, you might overwrite the previous version *in the designer*. However, on the server, you usually need a new ID to upload a new version unless using admin functions.

### 7. Exporting and Uploading the Template (OPT)

* **Export:** Once your template is ready, save it and export it as an OPT (Operational Template) file from the Archetype Designer.
* **Upload Tool (Postman/Insomnia):**
    * Use the provided collection for the bootcamp.
    * **Environment:** Ensure you have selected the correct environment in Postman/Insomnia (e.g., the "bootcamp shared" environment, not "no environment" or your local one). This was a common issue.
    * Use the correct API endpoint to upload the template (usually a POST request).
* **Template ID Uniqueness:** Remember the server often requires unique Template IDs. If you upload a template, make changes, export again, and try to upload with the *same* Template ID, it might fail unless the server allows overwrites (often requires admin rights). This is why versioning the Template ID (e.g., `...v1.1`) is common practice.
* **Public vs. Private:** Templates uploaded to the bootcamp server are likely accessible to others in the bootcamp but not publicly indexed or searchable on the web.

### 8. Troubleshooting Common Issues

* **Platform Access Denied:** Contact support/instructors.
* **Cannot Find Archetype (e.g., SpO2):** Use the "Find Resources" tab in Archetype Designer or search externally (Google) to identify the correct archetype name ("Pulse oximetry").
* **Incorrect Archetype Version Used:** Double-check archetype versions against CKM. Avoid bulk imports if unsure. Import verified archetypes individually.
* **Template Versioning Confusion:** Understand the difference between SemVer in the designer and the need for unique Template IDs on the server. Use unique IDs for server uploads.
* **Template Upload Failed (Postman/Insomnia):** Check if the correct environment is selected. Verify the Template ID doesn't already exist on the server (unless overwriting).
* **Accidentally Created Duplicate Templates on Server:** Deleting templates usually requires admin access via a separate Admin API, as the standard OpenEHR REST API doesn't support deletion (due to potential data linkage). Be careful when initially uploading. If duplicates happen in the bootcamp, you might need instructor help to clean up.
* **Saving/Overwriting Templates in Designer:** If you modify and save a template without changing its ID, you overwrite the previous version *in the designer*. Reloading might show only the latest saved version.

By following these steps and keeping the common pitfalls in mind, you should be well-prepared to create your first OpenEHR template tomorrow! Good luck!