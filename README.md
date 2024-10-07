## Pytest-Playwright Python Saucedemo
Automation Testing with Pytest-Playwright Python on Saucedemo Web

### Installation
To install the required libraries, run:

```bash
pip install requirements.txt
```

To install the required browsers, run:
```bash
playwright install
```

### Running The Test

If you want to see the browser window while running the tests, use the `--headed` option. To create a report in HTML format, use `--html=report.html`
```bash
pytest test_saucedemo.py --headed --html=report.html
```