# Java Development with OpenEHR

This guide provides practical instructions for using Java to interact with OpenEHR systems, focusing on the EHRbase Java SDK.

## Prerequisites

- Java Development Kit (JDK) 11 or higher installed
- Maven or Gradle for dependency management
- Basic understanding of Java and RESTful APIs
- Running EHRbase instance (local or remote)

## Setting Up a Java Project for OpenEHR

### Maven Configuration

Add the following dependencies to your `pom.xml`:

```xml
<dependencies>
    <!-- EHRbase Client Library -->
    <dependency>
        <groupId>org.ehrbase.client</groupId>
        <artifactId>client</artifactId>
        <version>1.6.0</version>
    </dependency>
    
    <!-- Jackson for JSON processing -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>2.13.3</version>
    </dependency>
    
    <!-- Apache HTTP Client -->
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.13</version>
    </dependency>
</dependencies>
```

### Gradle Configuration

Add the following to your `build.gradle`:

```groovy
dependencies {
    implementation 'org.ehrbase.client:client:1.6.0'
    implementation 'com.fasterxml.jackson.core:jackson-databind:2.13.3'
    implementation 'org.apache.httpcomponents:httpclient:4.5.13'
}
```

## Basic OpenEHR Operations with Java

### Connecting to an EHRbase Server

```java
import org.ehrbase.client.openehrclient.OpenEhrClientConfig;
import org.ehrbase.client.openehrclient.defaultrestclient.DefaultRestClient;

public class EhrbaseConnection {
    public static DefaultRestClient getClient() {
        String baseUrl = "http://localhost:8080/ehrbase/";
        OpenEhrClientConfig config = new OpenEhrClientConfig(baseUrl);
        
        // Add authentication if needed
        // config.setAuthType(AuthType.BASIC);
        // config.setUsername("ehrbase-user");
        // config.setPassword("SuperSecretPassword");
        
        return new DefaultRestClient(config);
    }
    
    public static void main(String[] args) {
        DefaultRestClient client = getClient();
        System.out.println("Connected to EHRbase at: " + client.getConfig().getBaseUrl());
    }
}
```

### Creating an EHR (Electronic Health Record)

```java
import org.ehrbase.client.openehrclient.OpenEhrClient;
import org.ehrbase.client.openehrclient.VersionUid;
import org.ehrbase.client.openehrclient.defaultrestclient.DefaultRestClient;
import com.nedap.archie.rm.ehr.EhrStatus;
import com.nedap.archie.rm.generic.PartyIdentified;
import com.nedap.archie.rm.support.identification.HierObjectId;
import com.nedap.archie.rm.support.identification.PartyRef;

public class EhrCreation {
    public static void main(String[] args) {
        DefaultRestClient client = EhrbaseConnection.getClient();
        
        // Create EHR Status with subject information
        EhrStatus ehrStatus = new EhrStatus();
        PartyIdentified subject = new PartyIdentified();
        subject.setName("John Doe");
        
        // Set subject external reference
        PartyRef partyRef = new PartyRef();
        partyRef.setId(new HierObjectId("patient123"));
        partyRef.setNamespace("demographic");
        partyRef.setType("PERSON");
        subject.setExternalRef(partyRef);
        
        ehrStatus.setSubject(subject);
        ehrStatus.setModifiable(true);
        ehrStatus.setQueryable(true);
        
        // Create the EHR
        String ehrId = client.ehrEndpoint().createEhr(ehrStatus);
        System.out.println("Created EHR with ID: " + ehrId);
    }
}
```

### Uploading a Template

```java
import org.ehrbase.client.openehrclient.OpenEhrClient;
import org.ehrbase.client.openehrclient.defaultrestclient.DefaultRestClient;
import org.ehrbase.client.templateprovider.TemplateProvider;
import org.ehrbase.client.templateprovider.FileBasedTemplateProvider;

import java.io.File;
import java.nio.file.Path;
import java.nio.file.Paths;

public class TemplateUpload {
    public static void main(String[] args) {
        DefaultRestClient client = EhrbaseConnection.getClient();
        
        // Path to your template file
        Path templatePath = Paths.get("src/main/resources/templates/vital_signs.opt");
        
        // Create a template provider
        TemplateProvider templateProvider = new FileBasedTemplateProvider(templatePath.getParent());
        
        // Upload the template
        String templateId = client.templateEndpoint().ensureExistence(templatePath.toFile());
        System.out.println("Template uploaded with ID: " + templateId);
    }
}
```

### Creating a Composition

```java
import org.ehrbase.client.openehrclient.OpenEhrClient;
import org.ehrbase.client.openehrclient.defaultrestclient.DefaultRestClient;
import org.ehrbase.client.flattener.Flattener;
import org.ehrbase.client.flattener.Unflattener;
import org.ehrbase.client.templateprovider.TemplateProvider;
import org.ehrbase.client.templateprovider.FileBasedTemplateProvider;
import com.nedap.archie.rm.composition.Composition;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.UUID;

public class CompositionCreation {
    public static void main(String[] args) {
        DefaultRestClient client = EhrbaseConnection.getClient();
        
        // EHR ID from previous step
        UUID ehrId = UUID.fromString("your-ehr-id-here");
        
        // Path to your template
        Path templatePath = Paths.get("src/main/resources/templates/vital_signs.opt");
        TemplateProvider templateProvider = new FileBasedTemplateProvider(templatePath.getParent());
        
        // Create a flattener with the template provider
        Flattener flattener = new Flattener(templateProvider);
        
        // Create your composition object
        // This is a simplified example - in practice, you would create a Java class
        // that represents your template structure and populate it with data
        
        // For demonstration purposes, we'll create a minimal composition directly
        Composition composition = new Composition();
        // ... populate composition with data
        
        // Save the composition
        UUID compositionId = client.compositionEndpoint(ehrId).saveComposition(composition);
        System.out.println("Saved composition with ID: " + compositionId);
    }
}
```

### Querying Data with AQL

```java
import org.ehrbase.client.openehrclient.OpenEhrClient;
import org.ehrbase.client.openehrclient.defaultrestclient.DefaultRestClient;
import org.ehrbase.client.aql.query.Query;
import org.ehrbase.client.aql.record.Record;
import org.ehrbase.client.aql.parameter.Parameter;
import org.ehrbase.client.aql.field.EhrFields;

import java.util.List;

public class AqlQuery {
    public static void main(String[] args) {
        DefaultRestClient client = EhrbaseConnection.getClient();
        
        // Create an AQL query
        String aql = "SELECT c " +
                     "FROM EHR e " +
                     "CONTAINS COMPOSITION c " +
                     "WHERE c/archetype_details/template_id/value = 'vital_signs'";
        
        // Execute the query
        Query<Record> query = Query.buildNativeQuery(aql, Record.class);
        List<Record> result = client.aqlEndpoint().execute(query);
        
        // Process the results
        System.out.println("Found " + result.size() + " compositions");
        for (Record record : result) {
            System.out.println(record.values());
        }
    }
}
```

## Best Practices for Java OpenEHR Development

1. **Use Generated Model Classes**
   - Generate Java classes from your templates for type-safe programming
   - Use the EHRbase SDK's generator tools

2. **Implement Proper Error Handling**
   - Handle exceptions from the EHRbase client
   - Implement retry logic for network issues

3. **Use Connection Pooling**
   - For production applications, implement connection pooling

4. **Validate Data**
   - Validate data against template constraints before submission

5. **Implement Caching**
   - Cache frequently used templates and reference data

## References

- [EHRbase Java Client Documentation](https://github.com/ehrbase/ehrbase-client-library)
- [OpenEHR Java Reference Implementation](https://github.com/openEHR/java-libs)
- [OpenEHR REST API Specification](https://specifications.openehr.org/releases/ITS-REST/latest/)
- [Java Documentation](https://docs.oracle.com/en/java/)
