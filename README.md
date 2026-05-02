# eulercodelab-data

This repository is a local-first data collection project for Project Euler problem statements and Python solutions. It does not include video rendering, Puppeteer, or FFmpeg workflows.

## Sources

Project Euler problem statements are taken from Project Euler.  
Source: https://projecteuler.net/  
License: CC BY-NC-SA 4.0

Python solutions are collected from EulerSolve.  
Source: https://eulersolve.org/

## Output structure

```text
project-euler/
  001/
    problem.md
    solution.py
  002/
    problem.md
    solution.py

metadata/
  001.json
  002.json

failed/
  failed.json
```

## Usage

Default test range:

```powershell
node fetch_data.js
```

Explicit range in PowerShell:

```powershell
$env:START_PROBLEM=1
$env:END_PROBLEM=10
node fetch_data.js
```

The script:

- reads Project Euler archive pages for IDs and titles
- fetches each problem statement from the Project Euler minimal endpoint
- converts HTML to Markdown with `turndown`
- fetches the Python solution URL from the EulerSolve problem page
- saves outputs under padded problem folders such as `project-euler/001/problem.md`
- continues processing even if an individual problem fails
- records failures in `failed/failed.json`
- waits 700-1000 ms between requests
