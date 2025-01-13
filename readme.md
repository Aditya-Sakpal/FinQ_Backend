# FinQ middle backend


## Introduction 

FinQ middle backend serves apis for serves api for frontend as well as it acts as an intermediatary between frontend and ai backend . It is developed in python and every request is authenticated via Clerk middleware and every webhook is authenticated via Svix middleware 
## Installation

### Prerequisites

- **Python 3.10+**: Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/).
### Steps to Install

#### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/Statsplex/FinQ_middle_backend
```
##### Setting Up the Virtual Environment 

*Option 1: Using venv (Recommended for simplicity)*

Create a Virtual Environment (macOS/Linux/Windows)
```bash
python3 -m venv venv 
```
Activate the Virtual Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

*Option 2: Using Conda*

If you prefer Conda, follow these steps:

Create a Conda Environment
```bash
conda create --name [env_name] python=[python_version]
```
Activate the Conda Environment
```bash
conda activate [env_name]
```

##### Install Dependencies

Once the environment is activated, install the required dependencies from requirements.txt:
```bash
pip install -r requirements.txt 
```

##### Create credentials.py file in the root folder by taking reference from credentials.py.example file and then replace all the values in it 

##### Run the project
```bash
uvicorn main:app --reload
```





## Deployed version 
https://finqbackendtest.wonderfuldesert-c038cc22.westus2.azurecontainerapps.io/


# FinQ middle backend


## Introduction 

FinQ middle backend serves apis for serves api for frontend as well as it acts as an intermediatary between frontend and ai backend . It is developed in python and every request is authenticated via Clerk middleware and every webhook is authenticated via Svix middleware 
## Installation

### Prerequisites

- **Python 3.10+**: Ensure Python is installed on your system. [Download Python](https://www.python.org/downloads/).
### Steps to Install

#### 1. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/Statsplex/FinQ_middle_backend
```
##### Setting Up the Virtual Environment 

*Option 1: Using venv (Recommended for simplicity)*

Create a Virtual Environment (macOS/Linux/Windows)
```bash
python3 -m venv venv 
```
Activate the Virtual Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate
```

*Option 2: Using Conda*

If you prefer Conda, follow these steps:

Create a Conda Environment
```bash
conda create --name [env_name] python=[python_version]
```
Activate the Conda Environment
```bash
conda activate [env_name]
```

##### Install Dependencies

Once the environment is activated, install the required dependencies from requirements.txt:
```bash
pip install -r requirements.txt 
```

##### Create credentials.py file in the root folder by taking reference from credentials.py.example file and then replace all the values in it 

##### Run the project
```bash
uvicorn main:app --reload
```





## Deployed version 
https://finqbackendtest.wonderfuldesert-c038cc22.westus2.azurecontainerapps.io/