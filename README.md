![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Impact Crater Depth-Diameter Calculator
 
*For planetary geoscientists and crater analysts: enter crater diameter and type (simple/complex) to instantly compute expected depth and see the crater on a scaling diagram.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Planetary Geoscience
 
The user provides (a) Crater Diameter in kilometers (float, 0.01–500 km), (b) Crater Type selected from a dropdown ('Simple' or 'Complex'), and (c) Target Body (optional, for reference labels: Moon, Mars, Earth). The core calculation uses classic power-law scaling relationships: for Simple craters, depth = 0.2 * diameter (linear); for Complex craters, depth = 0.1 * sqrt(diameter). These are standard empirical fits from Pike (1974) and Melosh (1989). The tool also computes a crude volume estimate using a paraboloid approximation: volume = (π/3) * (depth) * (diameter/2)^2, output in km³. The Gradio UI shows: a number input for diameter, dropdowns for crater type and target body, and a 'Calculate' button. The output displays: (1) Calculated Depth (km) with two decimal places, (2) Volume estimate (km³) in scientific notation, (3) A textual classification: 'Shallow' if depth < 0.8 * expected depth, 'Normal' if within ±20%, 'Deep' if > 1.2 * expected depth, based on comparison with the computed depth. (4) A static matplotlib plot showing a reference depth-diameter scaling curve (for both simple and complex regimes) with the input crater plotted as a red dot. The reference curves are generated from the same formulas over a range of diameters from 0.1 to 200 km. The plot has log-log axes, labeled axes (Depth (km) vs Diameter (km)), and a legend for transition. No AI/ML component is used.
 
## Run it
 
```bash
docker build -t impact-crater-depth-diameter-calculator .
docker run -p 7860:7860 impact-crater-depth-diameter-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-25.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
