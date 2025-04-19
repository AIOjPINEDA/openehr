# My OpenEHR Development Environment Setup

This document outlines my personal setup for the OpenEHR Bootcamp, including tools, configurations, and resources I'll be using throughout the learning journey.

## Development Tools

### Core Tools

- **Node.js and npm** - For JavaScript development and package management
- **Git** - For version control
- **VS Code** - As my primary code editor with extensions:
  - ESLint for code quality
  - Prettier for code formatting
  - REST Client for API testing

### Docker Setup

I'll be using Docker to run the EHRbase server locally. Here's my configuration:

```bash
# Create a Docker network for EHRbase components
docker network create ehrbase-net

# Start PostgreSQL (required by EHRbase)
docker run --name ehrdb \
  --network ehrbase-net \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_DB=ehrbase \
  -d postgres:13

# Start EHRbase
docker run --name ehrbase \
  --network ehrbase-net \
  -e DB_URL=jdbc:postgresql://ehrdb:5432/ehrbase \
  -e DB_USER=postgres \
  -e DB_PASS=postgres \
  -e SECURITY_AUTHTYPE=BASIC \
  -e SECURITY_AUTHUSER=ehrbase-user \
  -e SECURITY_AUTHPASSWORD=SuperSecretPassword \
  -e ADMINUSER_NAME=admin \
  -e ADMINUSER_PASSWORD=EvenMoreSecretPassword \
  -e SYSTEM_NAME=local.ehrbase.org \
  -p 8080:8080 \
  -d ehrbase/ehrbase:latest
```

Verify EHRbase is running: http://localhost:8080/ehrbase/status

### API Testing Tools

- **Postman** - For testing and documenting API endpoints
- **curl** - For command-line API testing

## OpenEHR Accounts and Resources

### Archetype Designer

- URL: [https://tools.openehr.org/designer](https://tools.openehr.org/designer)
- Username: [my-username]
- Projects:
  - Vitals Monitoring (Module 1)
  - Clinical Assessment (Module 3)

### Clinical Knowledge Manager (CKM)

- URL: [https://ckm.openehr.org/ckm/](https://ckm.openehr.org/ckm/)
- Username: [my-username]

## Web Development Stack

For the application development modules, I'll be using:

- **React** - For building user interfaces
- **TypeScript** - For type-safe JavaScript development
- **Vite** - For fast development and building
- **Tailwind CSS** - For styling

### Project Template

Basic setup for each application module:

```bash
# Create a new React project with Vite
npm create vite@latest [module-name] -- --template react-ts

# Navigate to project directory
cd [module-name]

# Install dependencies
npm install

# Add Tailwind CSS
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

# Start development server
npm run dev
```

## Learning Resources

### Documentation

- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [openEHR Specifications](https://specifications.openehr.org/)
- [Medblocks UI Documentation](https://docs.medblocks.com/)

### Tutorials and Guides

- [openEHR YouTube Playlist](https://www.youtube.com/watch?v=kOU2HGqK23o&list=PLUr-PTsPYKV4Cl7gUe5sPoCQEfRJ3FpWW)
- [Better Platform Documentation](https://docs.better.care/openehr-platform/)

## Module-Specific Setup Notes

I'll add specific setup instructions for each module as I progress through the bootcamp.

## Sources

This setup guide is based on:

- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [Docker Hub - EHRbase](https://hub.docker.com/r/ehrbase/ehrbase)
- [Medblocks OpenEHR Bootcamp](https://medblocks.com/openehr-bootcamp)
- [Vite Documentation](https://vitejs.dev/guide/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs/installation)
- Personal bootcamp reference document (bootcamp_reference.md)
