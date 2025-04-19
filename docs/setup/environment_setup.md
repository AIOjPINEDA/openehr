# OpenEHR Bootcamp Environment Setup

This document describes how to set up and manage the development environment for the OpenEHR Bootcamp using Conda.

## Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) installed
- Git installed
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

## Sources

This environment configuration is based on:

- [Official Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- [Python Environment Best Practices](https://docs.python-guide.org/dev/virtualenvs/)
- [EHRbase Documentation](https://ehrbase.readthedocs.io/en/latest/)
- [Medblocks OpenEHR Bootcamp Technical Requirements](https://medblocks.com/openehr-bootcamp)
