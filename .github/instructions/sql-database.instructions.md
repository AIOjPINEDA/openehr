---
applyTo: "**/*.sql"
---

# SQL and Database Standards for OpenEHR

Use PostgreSQL as primary database for EHRbase and custom queries.
Always use parameterized statements, never string concatenation.
Use proper escaping for all user inputs and dynamic values.
Implement proper indexing for performance optimization.

Use descriptive table and column names in snake_case format.
Add foreign key constraints to maintain referential integrity.
Use appropriate data types for OpenEHR-specific fields.
Include proper NULL constraints based on OpenEHR requirements.

Create database migration scripts for schema changes.
Use transactions for complex multi-table operations.
Implement proper error handling for database operations.
Log all database errors with contextual information.

Use AQL queries for OpenEHR-specific data extraction.
Implement proper escaping and parameterization for AQL.
Optimize queries for performance with large datasets.
Use appropriate indexes for frequently queried fields.
