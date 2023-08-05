# Tara, Gig!
A gig directory app project

## Getting Started

### Prerequisites

- Python 3.11.3 or higher
- Node.js and npm

### Installation

1. Clone the repository:

    ```shell
    git clone <repository-url>
    ```

2. Change into the project directory:

    ```shell
    cd tara-gig
    ```

3. Create and activate a virtual environment `myenv`:

    ```shell
    python3 -m venv myenv
    ```

    **Mac/Linux:**
    ```shell
    source myenv/bin/activate
    ```

    **Windows:**
    
    ```shell
    myenv/Scripts/activate
    ```
    
4. Install Python dependencies:

    ```shell
    pip install -r requirements.txt
    ```

5. Install the Node.js dependencies:

    ```shell
    npm install
    ```

### Usage

To start the development server:

```shell
npm start
```

To run the Tailwind compiler:

```shell
npm run watch:css
```

### Development

During development, use the following commands:

- To activate the virtual environment:

    ```shell
    tgenv/Scripts/activate
    ```

- To compile TailwindCSS styles:

    ```shell
    npx tailwindcss-cli@latest build -o static/css/styles.css
    ```

- To start the Django development server:

    ```shell
    django runserver
    ```