# Module 1.02 – Reference Model, Archetypes, and Templates

## 1. Introduction

In this session, we explore how openEHR balances expressivity and interoperability in healthcare data modeling by introducing three foundational components: the Reference Model (RM), Archetypes, and Templates. This separation of concerns allows flexibility for application developers while preserving semantic consistency across systems.

---

## 2. Core Components

### 2.1 Reference Model (RM)

| Aspect | Details |
|:------|:--------|
| **Definition** | A blueprint describing the allowed data structures and types, without including clinical meanings. |
| **Purpose** | Provides a stable technical foundation for storing all healthcare data. |
| **Implementation** | Can be implemented over diverse database technologies such as PostgreSQL, Cassandra, or MongoDB. |
| **Scope** | Focuses purely on technical constructs (e.g., quantities, coded texts, dates) — no clinical models like blood pressure yet. |

---

### 2.2 Archetypes

| Aspect | Details |
|:------|:--------|
| **Definition** | Maximal reusable clinical models for specific concepts (e.g., Blood Pressure, Body Weight). |
| **Purpose** | Represent complete clinical knowledge for a domain concept. |
| **Development** | Created independently from database implementations but based strictly on RM data types. |
| **Repository** | Managed within the Clinical Knowledge Manager (CKM), hosting close to 1000 archetypes. |

---

### 2.3 Templates

| Aspect | Details |
|:------|:--------|
| **Definition** | Context-specific assemblies of one or more archetypes tailored for real-world use cases. |
| **Purpose** | Enable applications to adapt archetypes to particular workflows while preserving semantic interoperability. |
| **Role** | Act as a contract between the application and the data platform, specifying what data is captured and how. |

---

## 3. Comparative Summary Table

| Component        | Purpose                                                      | Characteristics                                                                                                   | Role in Interoperability                                                                 |
|------------------|--------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Reference Model (RM)** | Defines the structure and types of data without clinical semantics. | - Stable and generic.<br>- Implemented in various databases (e.g., PostgreSQL, MongoDB). | Provides the technical foundation for consistent data representation. |
| **Archetypes**   | Encapsulate clinical knowledge as reusable models.           | - Maximal datasets for specific clinical concepts.<br>- Developed based on RM types. | Standardize clinical semantics across applications.   |
| **Templates**    | Customize archetypes for specific clinical workflows.        | - Combine multiple archetypes.<br>- Define constraints and optionality for specific use cases. | Enable flexible yet standardized clinical workflows. |

---

## 4. Practical Example of Reuse and Interoperability

Two applications — an outpatient system and an inpatient system — can both use the same Blood Pressure archetype but configure it differently through their respective templates.
This allows them to share and interpret patient blood pressure data consistently while adapting to their workflow needs.

---

## 5. Visual Representation
pending to add

## 6. Additional Resources

- [Reference Model Specification (Latest Release)](https://specifications.openehr.org/releases/RM/latest/)
- [Archetypes and Templates - Architecture Overview](https://specifications.openehr.org/releases/BASE/latest/architecture_overview.html#_archetypes_and_templates)
- [openEHR Clinical Knowledge Manager (CKM)](https://ckm.openehr.org/ckm/)
- [What is openEHR and How Do I use it?](https://www.youtube.com/watch?v=Zn4Muj2IOlM) (YouTube)
- [openEHR step by step tutorial](https://www.youtube.com/watch?v=mqV6QQ-aaDA) (YouTube)

---

## 7. Conclusion

Understanding the roles of the Reference Model, Archetypes, and Templates is essential for mastering openEHR's architecture.
This framework enables healthcare data platforms to achieve a powerful balance between application flexibility and data interoperability, ensuring robust, patient-centric healthcare information systems.

---