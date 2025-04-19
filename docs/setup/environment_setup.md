# OpenEHR Bootcamp Environment Setup

This document describes how to set up and manage the development environment for the OpenEHR Bootcamp using Conda and other required tools.

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) installed
- [Git](https://git-scm.com/downloads) installed
- [Java Development Kit (JDK)](https://adoptium.net/) - Version 11 or higher
- [Node.js](https://nodejs.org/) - Latest LTS version
- [Postman](https://www.postman.com/downloads/) - Latest version
- [Docker](https://www.docker.com/products/docker-desktop/) (optional but recommended) - For running EHRbase
- Internet access to download packages

## Initial Environment Setup

The `environment.yml` file in the repository root contains all the necessary dependencies for the bootcamp. To create and activate the environment:

```bash
# Create the environment from the environment.yml file
conda env create -f environment.yml

# Activate the environment
conda activate openehr-bootcamp

# Verify the installation
python --version
node --version
npm --version
```

## Environment Files

- `environment.yml`: Complete Conda environment configuration with all dependencies needed for all modules
- `.env`: File for local environment variables (not included in version control)
- `.env.example`: Example configuration of environment variables

## Environment Variables Configuration

To configure the necessary environment variables:

```bash
# Copy the example file to .env
cp .env.example .env

# Edit the .env file with your preferred editor
# For example:
vi .env  # or nano .env, code .env, etc.
```

## Updating the Environment

If you need to add new dependencies as you progress through the bootcamp:

```bash
# Update from the environment.yml file
conda env update -f environment.yml
```

## Verifying the Environment

To verify that your environment is correctly configured:

```bash
# Make sure the environment is activated
conda activate openehr-bootcamp

# Run the verification script
python verify_environment.py
```

## Managing JavaScript Dependencies

For modules that require web development with JavaScript/TypeScript:

```bash
# Navigate to the module directory
cd module-X-*

# Install Node.js dependencies
npm install
```

## Exporting the Environment

If you need to share your exact environment configuration:

```bash
# Export the environment to a YAML file
conda env export -n openehr-bootcamp > environment-exported.yml
```

## Removing the Environment

If you need to remove the environment for any reason:

```bash
# Deactivate the environment first if it's active
conda deactivate

# Remove the environment
conda env remove -n openehr-bootcamp
```

## Troubleshooting

### Dependency Conflicts

If you encounter dependency conflicts:

```bash
# Try installing dependencies one by one
conda install -n openehr-bootcamp <package-name>
```

### Node.js Issues

If you experience issues with Node.js in the Conda environment, consider installing Node.js directly using [nvm](https://github.com/nvm-sh/nvm) (for Unix/Linux/macOS) or [nvm-windows](https://github.com/coreybutler/nvm-windows) (for Windows).

### Permission Issues

If you encounter permission issues when running Conda commands:

```bash
# On Unix/Linux/macOS systems
chmod +x verify_environment.py
```

## Additional Tool Setup

### Postman for OpenEHR

To set up Postman for working with OpenEHR APIs:

1. Install Postman from [postman.com/downloads](https://www.postman.com/downloads/)
2. Import the OpenEHR collection template:
   - In Postman, click "Import" > "Link"
   - Enter: `https://www.postman.com/collections/856f491b8b75b7fbb696`
   - Save the collection
3. Configure environment variables:
   - Create a new environment
   - Add variables for `baseUrl` (e.g., `http://localhost:8080/ehrbase/`)
   - Add variables for authentication if needed

### EHRbase Setup

To run EHRbase locally using Docker:

```bash
# Clone the EHRbase repository
git clone https://github.com/ehrbase/ehrbase.git
cd ehrbase

# Start EHRbase using Docker Compose
docker-compose up -d
```

Verify EHRbase is running by accessing `http://localhost:8080/ehrbase/swagger-ui.html`

### Svelte Development Environment

For modules that use Svelte for frontend development:

```bash
# Create a new Svelte project
npm create svelte@latest my-svelte-app
cd my-svelte-app

# Install dependencies
npm install

# Start development server
npm run dev
```

## Sources

This environment configuration is based on:

- [Official Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Python Environment Best Practices](https://docs.python-guide.org/dev/virtualenvs/)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [Medblocks OpenEHR Bootcamp Technical Requirements](https://medblocks.com/openehr-bootcamp)
- [Postman Documentation](https://learning.postman.com/docs/getting-started/introduction/)
- [Svelte Documentation](https://svelte.dev/docs)
