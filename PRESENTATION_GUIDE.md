# Presentation Guide

This guide explains how to use and export the Jupyter slides presentation.

## Files

- **`Presentation.ipynb`**: The main presentation notebook with slides configured
- **`setup_slides.py`**: Script to configure slide metadata (already run)

## Viewing the Presentation

### Option 1: Using RISE (Recommended for Live Presentations)

RISE allows you to present directly from Jupyter Notebook.

1. **Install RISE:**
   ```bash
   pip install rise
   jupyter-nbextension install rise --py --sys-prefix
   jupyter-nbextension enable rise --py --sys-prefix
   ```

2. **Open the notebook:**
   ```bash
   jupyter notebook Presentation.ipynb
   ```

3. **Enter slideshow mode:**
   - Click the "Enter/Exit RISE Slideshow" button in the toolbar
   - Or press `Alt + R` (Windows/Linux) or `Option + R` (Mac)

### Option 2: Using nbconvert (For HTML Export)

1. **Convert to HTML slides:**
   ```bash
   jupyter nbconvert Presentation.ipynb --to slides --reveal-prefix=https://cdn.jsdelivr.net/npm/reveal.js@4.3.1
   ```

2. **Open the generated HTML file** (`Presentation.slides.html`) in a browser

## Exporting to PDF

### Method 1: Using Chrome/Chromium (Recommended)

1. **Convert to HTML first:**
   ```bash
   jupyter nbconvert Presentation.ipynb --to slides --reveal-prefix=https://cdn.jsdelivr.net/npm/reveal.js@4.3.1
   ```

2. **Open `Presentation.slides.html` in Chrome/Chromium**

3. **Print to PDF:**
   - Press `Ctrl+P` (Windows/Linux) or `Cmd+P` (Mac)
   - Select "Save as PDF" as the destination
   - **Important:** Set layout to "Landscape"
   - **Important:** Check "Background graphics" to include colors
   - Click "Save"

### Method 2: Using DeckTape (For Automated PDF Export)

1. **Install DeckTape:**
   ```bash
   npm install -g decktape
   ```

2. **Convert HTML to PDF:**
   ```bash
   # First convert to HTML
   jupyter nbconvert Presentation.ipynb --to slides --reveal-prefix=https://cdn.jsdelivr.net/npm/reveal.js@4.3.1
   
   # Then convert HTML to PDF
   decktape reveal Presentation.slides.html Presentation.pdf
   ```

### Method 3: Using Python Script

Create a script to automate PDF export:

```python
import subprocess
import webbrowser
import time
import os

# Convert to HTML
subprocess.run([
    'jupyter', 'nbconvert', 
    'Presentation.ipynb', 
    '--to', 'slides',
    '--reveal-prefix=https://cdn.jsdelivr.net/npm/reveal.js@4.3.1'
])

print("HTML slides created. Please:")
print("1. Open Presentation.slides.html in Chrome")
print("2. Press Ctrl+P (Cmd+P on Mac)")
print("3. Select 'Save as PDF'")
print("4. Set layout to Landscape")
print("5. Check 'Background graphics'")
print("6. Save as Presentation.pdf")
```

## Presentation Structure

The presentation contains **16 slides** covering:

1. Title slide
2. Client overview (Erin Robinson)
3. Methodology overview
4. Methodology (continued)
5. Key Insight #1: Geographic Patterns
6. Key Insight #2: Renovation Opportunity
7. Key Insight #3: Price Per Square Foot Advantage
8. Key Insight #4: Property Size Matters
9. Recommendation #1: Target Affordable Zipcodes
10. Recommendation #2: Focus on Unrenovated Properties
11. Recommendation #3: Optimize Property Size
12. Top 3 Property Recommendations
13. Social Impact Potential
14. Key Assumptions
15. Summary & Next Steps
16. Thank You slide

## Duration

The presentation is designed for **10 minutes** of presentation time, followed by **5 minutes** of discussion.

## Tips

- **Practice timing**: Each slide should take approximately 30-60 seconds
- **Focus on key points**: Highlight the main insights and recommendations
- **Be ready for questions**: Review the detailed EDA notebook (`EDA.ipynb`) for deeper analysis
- **Customize as needed**: Feel free to modify slides based on client feedback

## Troubleshooting

### RISE not working?
- Make sure you've enabled the extension: `jupyter-nbextension enable rise --py --sys-prefix`
- Restart Jupyter after installation
- Check that you're using a compatible Jupyter version

### PDF export issues?
- Make sure to use Chrome/Chromium for best results
- Check that "Background graphics" is enabled in print settings
- Use Landscape orientation for proper slide layout

### Slides not displaying correctly?
- Make sure slide metadata is set (run `python setup_slides.py` if needed)
- Check that reveal.js is properly loaded (check browser console for errors)

