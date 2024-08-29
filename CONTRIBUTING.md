# Contributing to the Beer Project

Thank you for your interest in contributing to the Beer project! We welcome contributions from everyone. This document will guide you through the process of setting up your development environment and submitting your contributions.

## Getting Started

### Fork, Clone, and Branch

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/your-username/beer.git
   cd beer
   ```
3. Create a new branch for your contribution:
   ```
   git checkout -b your-feature-branch
   ```

### Setting up the Development Environment

We use `pyproject.toml` to manage project dependencies. Here's how to set up your development environment:

1. Ensure you have Python 3.12 installed on your system.

2. Install `uv` if you haven't already:
   ```
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

3. Create a new virtual environment and install dependencies:
   ```
   uv venv
   source .venv/bin/activate  # On Unix or MacOS
   .venv\Scripts\activate  # On Windows
   uv pip install -e ".[dev,lint]"
   ```

This will install the project along with its dependencies, including development and linting tools.

## Adding Content

### Adding a New Problem

1. Create a new Markdown file in the appropriate directory (e.g., `docs/fifty/` for the Fifty Challenging Problems).
2. Use the following template for your problem:

   ```markdown
   # Problem Title

   ## Problem

   ???+ question "Question"

       === "English"

           [English version of the problem]

       === "中文"

           [Chinese version of the problem]

   ## Tip

   ??? tip "Tip"

       === "English"

           [English version of the tip]

       === "中文"

           [Chinese version of the tip]

   ## Solutions

   ### Solution1: Analysis
   ??? success "Solution1: Analysis"

       === "English"

           [Detailed solution explanation in English]

       === "中文"

           [Detailed solution explanation in Chinese]

   ### Solution2: Simulation

   ??? success "Solution2: Simulation"

       === "English"

           [Simulation approach explanation in English]

           ```python exec="true" source="material-block" session="problem-id"
           --8<-- "docs/fifty/snippet/problem_file.py:solution2"
           ```

           [Explanation of simulation results]

       === "中文"

           [Simulation approach explanation in Chinese]

           ```python exec="true" source="material-block" session="problem-id"
           --8<-- "docs/fifty/snippet/problem_file.py:solution2"
           ```

           [Explanation of simulation results in Chinese]
   ```

3. Ensure you provide both English and Chinese versions for all sections.
4. Include clear and detailed solutions, with both analytical and simulation approaches when applicable.
5. Use code blocks with the `exec="true"` attribute for runnable Python code.
6. Place Python code snippets in separate files under the `docs/fifty/snippet/` directory and include them using the `--8<--` syntax.

### Updating Existing Content

When updating existing problems or solutions:

1. Maintain the bilingual format for all sections.
2. Ensure mathematical correctness in both languages.
3. Provide clear explanations for both analytical and simulation approaches.
4. If adding or modifying code implementations, ensure they are correct, efficient, and follow the project's coding style.
5. Update any related code snippets in the `docs/fifty/snippet/` directory.

## Testing Locally

Before submitting your changes, test them locally using MkDocs:

1. Make sure you're in the project root directory.
2. Run the following command to start a local preview server:
   ```
   mkdocs serve
   ```
3. Open your web browser and go to `http://127.0.0.1:8000/` to view the site.
4. Make sure your changes appear correctly and don't introduce any errors.

## Submitting Your Contribution

1. Commit your changes:
   ```
   git add .
   git commit -m "Your descriptive commit message"
   ```
2. Push your changes to your fork:
   ```
   git push origin your-feature-branch
   ```
3. Go to the original Beer repository on GitHub and create a new pull request from your feature branch.
4. Fill out the pull request template with all relevant information.
5. Wait for the maintainers to review your pull request. They may ask for changes or clarifications.

## Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms. You can find the full text of the Code of Conduct in the [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.

Thank you for contributing to the Beer project!
