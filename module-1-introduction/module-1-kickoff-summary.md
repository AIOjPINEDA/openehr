**Summary and Organization of OpenEHR Bootcamp Class module 1- kickoff**

This document summarizes the key concepts, discussions, assignments, tools, resources, and questions addressed in the second session of the OpenEHR bootcamp with Sidhart Ramesh. The primary focus of this session was to introduce the first practical assignment, discuss modeling tools, clarify fundamental OpenEHR concepts, and address various participant questions regarding the OpenEHR ecosystem, standards, and comparison with other technologies.

**1. Introduction and Assignment 1 Overview**

*   **Context:** This session serves as the kickoff for the first practical module of the bootcamp. It's designed for participants to begin working on the assignment and address any initial questions or roadblocks.
*   **Assignment 1:**
    *   **Goal:** Model and post your first OpenEHR template.
    *   **Use Case:** Capture patient vital signs (pulse, BP, SPO2, height, weight) from a nurse's perspective in a hospital visit context. The design depends heavily on this specific context.
    *   **Deliverables:**
        1.  A modeled OpenEHR template capturing the specified vital signs.
        2.  The template ID must include your name for identification. Use standard English characters to avoid potential issues with special characters or emojis.
        3.  Post the template to the bootcamp's shared OpenEHR server using the provided Postman collection and APIs.
    *   **Timeline:** The assignment is due by the next session (demo day).

**2. OpenEHR Core Concepts (Briefly Touched Upon)**

*   **Archetypes:** Reusable, fine-grained clinical concepts (e.g., Pulse, Blood Pressure, Height, Weight, SPO2). They define the maximum possible data structure for a concept.
*   **Templates:** Constrained sets of archetypes or parts of archetypes combined for a specific clinical use case or form (e.g., "Nursing Vital Signs Form"). They define the *minimum* dataset required and allow for local variations (cardinality, terminology bindings). Templates are the fundamental interoperability blocks in OpenEHR when posting data.
*   **Entry Types:** Different categories of clinical data structures within archetypes, used in compositions:
    *   **Observation:** Data obtained through observation (e.g., vital signs, signs/symptoms reported by patient).
    *   **Evaluation:** A clinical decision or judgment based on observations (e.g., diagnosis).
    *   **Instruction:** A plan or request for action (e.g., prescription order, procedure request).
    *   **Action:** The execution of an instruction (e.g., administering medication, performing a procedure).
    *   **Admin Entry:** Miscellaneous administrative or non-clinical data.
*   **Clusters:** Reusable groups of data points that describe a specific aspect, often used *within* other Entry types (e.g., "Level of Exertion" cluster used within a Blood Pressure observation, "Circular Anatomical Location" cluster describing a body site). A cluster is a general concept that is not typically recorded on its own but in the context of another entry.

**3. OpenEHR Modeling Tools and Resources**

*   **Assignment Requirement:** Participants *must* use an OpenEHR modeling tool to create the template.
*   **Recommended Tool (for tutorials):**
    *   **Better Archetype Designer (tools.openehr.org):** A web-based tool, chosen for tutorials due to ease of access across different operating systems.
        *   Requires account creation.
        *   Supports local repositories or Git synchronization.
        *   Sidhart uses it professionally partly due to its Git integration for version control and collaboration.
        *   *Note:* While hosted on openEHR.org, the specific hosting provider wasn't confirmed in the discussion. It is *not* open source.
*   **Other Tools Mentioned (from openehr.org/modelling-tools):**
    *   ADL Workbench (Free & Open Source)
    *   Archetype Editor (Free & Open Source)
    *   Ocean Template Designer (Commercial, but also developed CKM)
    *   Link EHR Studio (Free & Open Source - pronounced "Linker")
    *   NeedApp Visual Studio (Commercial, primarily used by NeedApp)
    *   *Key Takeaway:* You are free to use any tool that produces a valid OpenEHR template (OPT) that meets the assignment criteria.
*   **Clinical Knowledge Manager (CKM):** The central repository for openEHR archetypes and some templates. Users need to search and download relevant archetypes from CKM into their modeling tool to build templates. CKM archetype pages contain documentation, including "use and misuse" sections.
*   **Template Formats:**
    *   **OPT (Operational Template) XML:** The primary output format from modeling tools. It's verbose and not easy to read or troubleshoot directly. It's a compiled artifact meant to be consumed by systems, not manually edited.
    *   **Web Template:** An alternative, more human-readable format (often JSON) derived from the OPT, which is easier for diffing and troubleshooting. Available via APIs from some CDRs (like Airbase) after posting the OPT. Sidhart recommends using this for debugging if needed, rather than the raw OPT XML.
*   **General Modeling Guidance:** While the CKM provides guidance within individual archetype documentation, there isn't a single, comprehensive "how-to" website for modeling every specific clinical scenario. The process involves understanding the archetypes and applying them to the use case, often iteratively. Capturing complex lab results (like liver panels or urine tests) can often be done with a single generic template using the `Lab Test Result` and `Lab Analyte Result` archetypes, rather than one template per test type, although front-end forms might require specific logic.

**4. OpenEHR Specification Versions (ADL & AQL)**

*   **ADL (Archetype Definition Language):** The language used to define archetypes and templates.
    *   **ADL 1.x (1.1, 1.2, 1.4):** Successive versions added features without breaking backward compatibility. ADL 1.4 became the widely adopted standard by most vendors.
    *   **ADL 2.0:** Introduced by Thomas Beale, it included breaking changes, most notably affecting **AQL (Archetype Query Language)** paths.
    *   **Impact of ADL 2.0 Breaking Changes:** Vendors faced significant challenges and resistance migrating production data due to the AQL path changes.
    *   **Vendor Adoption of ADL 2.0:** Only NeedApp (a company in the Netherlands) fully implemented ADL 2.0.
    *   **Current Roadmap/Status:** Due to vendor resistance and migration difficulties, the community has largely decided to skip ADL 2.0 and move from ADL 1.4 directly to ADL 3 (which is still under development). ADL 2.0 is effectively deprecated.
    *   **EHRBase & ADL 2.0:** EHRBase's API might show ADL 2.0 endpoints, but internally, they often convert ADL 2.0 templates to 1.4 representation for storage to maintain compatibility with existing data structures.
    *   **Recommendation:** For practical purposes and current implementations, **stick with ADL 1.4**.
    *   **Relation to Archetype Designer:** Modeling tools like Better might show capabilities for ADL 2.0, but the current interoperability standard being used by most production systems (and recommended for the bootcamp) is 1.4.

**5. OpenEHR Platforms and Servers**

*   **Open-Source Options:**
    *   **Airbase:** The server used for the bootcamp. Described as the most well-maintained, fully implemented (according to the REST API spec), and properly vetted open-source OpenEHR server.
    *   **EHR Server:** Another open-source option (in Java) but does not implement the REST API spec 100%.
    *   **Ethersys:** A predecessor to Airbase, less actively maintained (last commit several years ago) and not up-to-date with the current spec.
*   **Commercial Vendors:** Numerous companies provide OpenEHR based platforms and tools (Better, Code24, NeedApp, Ocean, etc.). A list is available on openehr.org under "Tools and Products".
*   **OpenEHR Ecosystem Overview:** Includes modeling tools, clinical decision support (CDS) tools/repositories (like GDL2 editors and repositories of CDS apps based on GDL - Guideline Decision Language), knowledge management tools, and the CDR platforms themselves.

**6. Comparison with Other Technologies (FHIR, Data Lakes)**

*   **FHIR vs. OpenEHR Usability in Real-World Applications:**
    *   **Sidhart's Perspective:**
        *   OpenEHR excels in capturing deep, complex clinical semantics and building longitudinal health records from diverse sources with varying granularity. The two-level modeling (archetypes + templates) handles this well.
        *   Example: Different departments capturing the *same* vital signs data but with *different* forms/additional fields. OpenEHR handles this better than systems that require remodeling the structure each time.
        *   OpenEHR's requirement to model templates *before* writing data ensures upfront clinical questions are answered, preventing data inconsistencies (unlike FHIR where similar data might be put in different resources or structures).
        *   However, for *application developers* building front-end applications, FHIR is generally considered easier and quicker to work with initially compared to OpenEHR. OpenEHR's complexity (though improved with flat formats) presents a steeper learning curve for developers.
*   **Integration of OpenEHR and FHIR:**
    *   This is a common need.
    *   Sidhart mentioned an **upcoming open-source engine** being released (by Medblocks, implied by the context, though not explicitly named in this snippet).
    *   This engine aims to provide **bidirectional conversion** between OpenEHR and FHIR.
    *   It supports various integration patterns:
        *   **Facade:** Presenting a FHIR interface on top of an OpenEHR CDR for reads/writes.
        *   **Synchronization:** Keeping data in both OpenEHR and FHIR servers in sync.
        *   **Hybrid:** Combining approaches.
    *   The engine uses declared mappings between AQL paths (OpenEHR) and FHIR paths.
    *   *Note:* Sidhart shared a link privately, emphasizing it was not yet publicly announced at the time of the recording. It was presented as a tool to simplify this integration.
*   **OpenEHR vs. Data Lakes (AWS Health Lake, Azure One Lake, Apache Iceberg, Parquet):**
    *   **Sidhart's Perspective:**
        *   OpenEHR is fundamentally a *standard* for clinical data modeling and storage structure, not a specific storage technology itself.
        *   An OpenEHR CDR could potentially be implemented *on top of* a data lake infrastructure (like S3 with Parquet/Iceberg).
        *   Data lakes (like AWS Health Lake, Azure One Lake) and OpenEHR CDRs are currently often separate solutions. Hyperscaler health data products (like Google BigQuery's FHIR support) are starting to bridge this.
        *   The comparison is between how you query the data: OpenEHR uses AQL (or SQL on flattened views), while data lakes typically use SQL on formats optimized for large-scale analytics.
    *   **Apache Iceberg & Parquet:**
        *   Stefan shared his experience using S3 with **Parquet** files (a columnar storage format) and querying with AWS Athena or Glue.
        *   **Apache Iceberg** is a table format standard that sits on top of file storage (like S3) to manage large datasets stored in formats like Parquet. It adds database-like features (schema evolution, hidden partitioning, time travel) and manages files efficiently (e.g., compaction).
        *   Iceberg allows using S3 more like a database, enabling updates and more efficient queries compared to just raw Parquet files.
        *   Sidhart acknowledges that converting OpenEHR data (perhaps flattened) into a format compatible with Iceberg/Parquet is a viable strategy for integrating OpenEHR data into a data lake for large-scale analytics using SQL tools.

**7. Troubleshooting and Learning**

*   Stefan shared his experience finding template authoring error-prone, taking multiple versions to get right, often due to missed cardinality constraints or forgetting to exclude optional nodes. He finds inspecting the flat JSON composition format easier for troubleshooting than the verbose OPT XML.
*   Sidhart agreed that direct OPT XML manipulation is not recommended; tooling should be used. He also highlighted the web template format as being much better for reviewing changes (diffing).
*   He encouraged participants to try building the template and reach out for help if stuck.

**8. Next Steps and Support**

*   The goal is for everyone to complete Assignment 1 and be ready to demonstrate their template and explain their work in the next session.
*   If participants get stuck, they should ask questions on **Slack** (or email if necessary).

---

This structured summary covers the main points of the class and directly addresses the specific questions you highlighted. Remember that the information about the FHIR-OpenEHR integration engine was presented with a caveat about its release status at the time of the recording.