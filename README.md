# 🌱 EcoSort AI — Waste Segregation & Circular Economy Advisor

> **AI-Powered Waste Segregation, Prep Instructions, Upcycling Guidance & SDG 12 Impact Tracking**

EcoSort AI is an interactive, web-based prototype designed to help individuals, households, and organizations make informed waste disposal decisions. By combining multi-component packaging parsing, rule-backed explainable classification, cleaning instructions, and circular economy upcycling tips, EcoSort AI advances sustainable consumption and production practices in line with **UN Sustainable Development Goal (SDG) 12**.

---

## 🚀 Quickstart Guide (Running in VS Code)

Follow these simple steps to run EcoSort AI directly from VS Code terminal:

### 1. Open VS Code Terminal
Open VS Code, press `` Ctrl + ` `` (or `Ctrl + ~`), and navigate to the project directory:
```bash
cd d:\ecosort-ai
```

### 2. Install Required Dependencies
Install Streamlit, Pandas, and Altair using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Launch the Application
Run the Streamlit application:
```bash
streamlit run app.py
```

VS Code will automatically open your web browser at `http://localhost:8501`. If it doesn't open automatically, click the link shown in the terminal.

---

## ✨ Key Features

1. **🔍 Smart Waste Segregator**:
   - **Multi-Item Decomposition**: Parses composite items and takeaway meal packaging descriptions (e.g., *"oily cardboard pizza box with plastic sauce cup and soda can"*).
   - **Stream Categorization**: Automatically categorizes components into:
     - ♻️ **Dry Recyclable**: Clean cardboard, PET bottles, aluminum cans, glass.
     - 🟢 **Wet Organic**: Food waste, fruit peels, coffee grounds, eggshells.
     - 🔴 **Landfill / Hazardous / Special Waste**: Greasy cardboard, styrofoam, batteries, e-waste, expired medicine.
   - **Explainability**: Clear reasoning for every stream decision.
   - **Cleaning & Prep Checklist**: Actionable steps to prevent batch contamination.
   - **Upcycling Tips**: Creative DIY ideas for repurposing items.

2. **♻️ Upcycling Catalog & Material Calculator**:
   - Searchable repository of upcycling ideas organized by material.
   - **Material Circularity Calculator**: Calculates personal monthly CO₂ emissions saved, water preserved, and landfill waste diverted.

3. **📊 SDG 12 Impact Dashboard**:
   - Visualizes municipal waste stream diversion.
   - Highlights the Waste Management Hierarchy (*Reduce > Reuse > Recycle > Recover > Landfill*).

4. **🛡️ Responsible AI Framework & Sidebar**:
   - **Explainability**: Clear rule-backed transparency.
   - **Privacy-First**: 100% local processing; zero data uploaded or tracked.
   - **Bias Avoidance**: Broad taxonomy covering diverse global packaging formats and food waste types.

---

## 🎯 UN SDG 12 Alignment

EcoSort AI directly supports **SDG 12: Responsible Consumption & Production**:

- **Target 12.5**: *By 2030, substantially reduce waste generation through prevention, reduction, recycling and reuse.*
- **Target 12.8**: *By 2030, ensure that people everywhere have the relevant information and awareness for sustainable development and lifestyles in harmony with nature.*

---

## 📁 File Structure

```
d:\ecosort-ai\
├── app.py              # Main Streamlit application & EcoSort AI engine
├── requirements.txt    # Python dependencies (streamlit, pandas, altair)
└── README.md           # Documentation & VS Code guide
```

---

## 🧪 Sample Prompts to Try

- `"oily cardboard pizza box with plastic sauce cup and soda can"`
- `"banana peel, plastic water bottle, coffee cup with plastic lid"`
- `"broken LED bulb, aa battery, clean cardboard box"`
- `"apple core, eggshell, tea bag, plastic wrapper"`

---

*Built for sustainable living and circular economy innovation.* 🌍
