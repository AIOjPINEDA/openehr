# EHRbase Setup Guide

This guide provides step-by-step instructions for setting up EHRbase, an open-source clinical data repository based on the openEHR Reference Model.

## Prerequisites

- Docker and Docker Compose installed
- 4GB+ RAM available for Docker
- Git installed
- Basic command line knowledge

## Quick Setup with Docker

The fastest way to get EHRbase running is using Docker Compose:

```bash
# Clone the EHRbase repository
git clone https://github.com/ehrbase/ehrbase.git
cd ehrbase

# Start EHRbase using Docker Compose
docker-compose up -d
```

This will start:
- PostgreSQL database
- EHRbase server
- Swagger UI for API documentation

## Verifying the Installation

1. Check that containers are running:
   ```bash
   docker-compose ps
   ```

2. Access the Swagger UI:
   - Open a browser and navigate to: http://localhost:8080/ehrbase/swagger-ui.html
   - You should see the EHRbase API documentation

3. Test a basic API call:
   ```bash
   curl -X GET http://localhost:8080/ehrbase/status
   ```
   You should receive a JSON response with status information.

## Configuration Options

### Basic Authentication

To enable basic authentication:

1. Edit the `docker-compose.yml` file:
   ```yaml
   services:
     ehrbase:
       environment:
         SECURITY_AUTHTYPE: BASIC
         SECURITY_AUTHUSER: ehrbase-user
         SECURITY_AUTHPASSWORD: SuperSecretPassword
   ```

2. Restart the containers:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

### Persistent Storage

By default, the PostgreSQL data is stored in a Docker volume. For production use, you may want to configure a persistent volume:

1. Edit the `docker-compose.yml` file:
   ```yaml
   services:
     ehrbase-db:
       volumes:
         - ./pgdata:/var/lib/postgresql/data
   ```

2. Restart the containers:
   ```bash
   docker-compose down
   docker-compose up -d
   ```

## Advanced Setup

### Manual Installation (Without Docker)

For production environments or advanced configurations, you may want to install EHRbase manually:

1. **Set up PostgreSQL**:
   ```bash
   # Install PostgreSQL
   sudo apt-get install postgresql
   
   # Create database and user
   sudo -u postgres psql
   CREATE DATABASE ehrbase;
   CREATE USER ehrbase WITH PASSWORD 'ehrbase';
   GRANT ALL PRIVILEGES ON DATABASE ehrbase TO ehrbase;
   \q
   ```

2. **Install Java**:
   ```bash
   sudo apt-get install openjdk-11-jdk
   ```

3. **Download and configure EHRbase**:
   ```bash
   # Download the latest release
   wget https://github.com/ehrbase/ehrbase/releases/download/v0.18.3/ehrbase-0.18.3.jar
   
   # Create application.yml configuration
   cat > application.yml << EOF
   server:
     port: 8080
     servlet:
       context-path: /ehrbase
   
   spring:
     datasource:
       url: jdbc:postgresql://localhost:5432/ehrbase
       username: ehrbase
       password: ehrbase
       driver-class-name: org.postgresql.Driver
   EOF
   ```

4. **Run EHRbase**:
   ```bash
   java -jar ehrbase-0.18.3.jar --spring.config.location=file:application.yml
   ```

### Configuring HTTPS

For production environments, you should enable HTTPS:

1. Generate a self-signed certificate (for testing only):
   ```bash
   keytool -genkeypair -alias ehrbase -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore ehrbase.p12 -validity 3650
   ```

2. Configure HTTPS in `application.yml`:
   ```yaml
   server:
     port: 8443
     ssl:
       key-store: ehrbase.p12
       key-store-password: your-password
       key-store-type: PKCS12
       key-alias: ehrbase
   ```

3. Run EHRbase with HTTPS:
   ```bash
   java -jar ehrbase-0.18.3.jar --spring.config.location=file:application.yml
   ```

## Troubleshooting

### Common Issues

1. **Database connection errors**:
   - Check PostgreSQL is running: `docker-compose ps` or `systemctl status postgresql`
   - Verify database credentials in configuration
   - Ensure PostgreSQL is accepting connections: `pg_isready -h localhost -p 5432`

2. **Port conflicts**:
   - Check if port 8080 is already in use: `netstat -tuln | grep 8080`
   - Change the port in configuration if needed

3. **Memory issues**:
   - Increase Docker memory allocation
   - Add Java memory options: `java -Xmx2g -jar ehrbase-0.18.3.jar`

4. **Permission issues**:
   - Check file permissions for configuration files
   - Ensure Docker has proper permissions

## References

- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [EHRbase GitHub Repository](https://github.com/ehrbase/ehrbase)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
