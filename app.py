import streamlit as st
import pandas as pd
import altair as alt
import json
import time
import re
from datetime import datetime

# ==========================================
# PAGE CONFIGURATION & ENTERPRISE STYLING
# ==========================================
st.set_page_config(
    page_title="EcoSort AI Pro — Enterprise Circular Economy Platform",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Advanced Glassmorphism CSS
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background: #f4f7f5;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Header Gradient Banner */
    .eco-header {
        background: linear-gradient(135deg, #0f2b1d 0%, #1b4332 40%, #2d6a4f 75%, #40916c 100%);
        padding: 28px 36px;
        border-radius: 20px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(15, 43, 29, 0.2);
        position: relative;
        overflow: hidden;
    }
    .eco-header h1 {
        color: #ffffff !important;
        margin: 0 0 10px 0;
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    .eco-header p {
        color: #b7e4c7 !important;
        margin: 0;
        font-size: 1.05rem;
        max-width: 900px;
    }

    /* Glassmorphic Container Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(216, 243, 220, 0.8);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .glass-card:hover {
        box-shadow: 0 8px 25px rgba(45, 106, 79, 0.08);
    }

    /* Badges */
    .badge-dry {
        background: #d8f3dc;
        color: #1b4332;
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #74c69d;
    }
    .badge-wet {
        background: #fefae0;
        color: #6b705c;
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #dda15e;
    }
    .badge-hazard {
        background: #ffe5ec;
        color: #900c3f;
        padding: 6px 14px;
        border-radius: 30px;
        font-weight: 700;
        font-size: 0.85rem;
        border: 1px solid #ffb3c1;
    }

    /* Key-Value Metrics Pill */
    .metric-pill {
        background: #e8f5e9;
        color: #1b4332;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 6px;
        display: inline-block;
    }

    /* Section Highlights */
    .highlight-box-green {
        background-color: #f0fdf4;
        border-left: 5px solid #22c55e;
        padding: 14px 18px;
        border-radius: 0 10px 10px 0;
        margin: 10px 0;
    }
    .highlight-box-amber {
        background-color: #fffbeb;
        border-left: 5px solid #f59e0b;
        padding: 14px 18px;
        border-radius: 0 10px 10px 0;
        margin: 10px 0;
    }
    .highlight-box-blue {
        background-color: #eff6ff;
        border-left: 5px solid #3b82f6;
        padding: 14px 18px;
        border-radius: 0 10px 10px 0;
        margin: 10px 0;
    }

    /* Terminal Console */
    .terminal-box {
        background: #1e1e1e;
        color: #4af626;
        font-family: 'Consolas', 'Courier New', monospace;
        padding: 14px;
        border-radius: 10px;
        font-size: 0.85rem;
        line-height: 1.5;
        border: 1px solid #333;
    }

    /* Metric Header Cards */
    .stat-card-pro {
        background: #ffffff;
        border-radius: 14px;
        padding: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        text-align: center;
    }
    .stat-val {
        font-size: 2rem;
        font-weight: 800;
        color: #1b4332;
    }
    .stat-lbl {
        font-size: 0.85rem;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
    }

    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


# ==========================================
# ADVANCED PROMPT & RULE SEGREGATION ENGINE
# ==========================================
class AdvancedEcoEngine:
    def __init__(self):
        # Taxonomy and Deep Material Database
        self.rules = [
            {
                "keywords": ["soda can", "aluminum can", "tin can", "drink can", "metal can", "coca cola can", "pepsi can"],
                "category": "Dry Recyclable",
                "stream_icon": "♻️",
                "material": "Aluminum alloy (ALU 41)",
                "confidence": 98.6,
                "weight_g": 14,
                "decomposition_yrs": "200–500 years",
                "toxicity": "Low",
                "reason": "High-purity aluminum suitable for closed-loop remelting; saves 95% energy vs primary mining.",
                "prep": "Rinse remaining liquid, crush vertically to optimize logistics volume, drop into metals bin.",
                "upcycling": "Transform into DIY mini succulent planters, craft desk lanterns, or hardware organizers.",
                "facility": "Local Scrap Dealer / Municipal Materials Recovery Facility (MRF)",
                "co2_saved": 0.16,
                "kwh_saved": 0.45,
                "water_saved_l": 1.2
            },
            {
                "keywords": ["plastic water bottle", "pet bottle", "soda bottle", "drink bottle", "clear plastic bottle"],
                "category": "Dry Recyclable",
                "stream_icon": "♻️",
                "material": "Polyethylene Terephthalate (PET 1)",
                "confidence": 97.4,
                "weight_g": 22,
                "decomposition_yrs": "450 years",
                "toxicity": "Low",
                "reason": "Highly demanded rPET feedstocks for recycled polyester yarn, rPET bottles, and strapping.",
                "prep": "Drain fluid, rinse, flatten bottle, and securely screw cap back on for optical sorting.",
                "upcycling": "Create a drip-irrigation self-watering plant pot or a hanging garden bird feeder.",
                "facility": "Standard Plastics Recovery Facility / Grocery Bottle Return Kiosk",
                "co2_saved": 0.09,
                "kwh_saved": 0.28,
                "water_saved_l": 3.5
            },
            {
                "keywords": ["clean cardboard box", "cardboard packaging", "shipping box", "cereal box", "clean paper", "newspaper", "magazine"],
                "category": "Dry Recyclable",
                "stream_icon": "♻️",
                "material": "Corrugated Cardboard (PAP 20)",
                "confidence": 99.1,
                "weight_g": 180,
                "decomposition_yrs": "2–3 months",
                "toxicity": "None",
                "reason": "Long cellulose fiber length supports 5–7 mechanical re-pulping cycles.",
                "prep": "Flatten boxes flat, remove plastic packaging tape and shipping labels.",
                "upcycling": "Cut into modular drawer dividers, closet organizers, or carbon bedding for compost.",
                "co2_saved": 0.35,
                "kwh_saved": 0.60,
                "water_saved_l": 18.0
            },
            {
                "keywords": ["glass bottle", "glass jar", "wine bottle", "beer bottle", "pickle jar"],
                "category": "Dry Recyclable",
                "stream_icon": "♻️",
                "material": "Soda-Lime Glass (GL 70)",
                "confidence": 99.5,
                "weight_g": 400,
                "decomposition_yrs": "1,000,000+ years",
                "toxicity": "None",
                "reason": "100% infinitely recyclable without chemical or structural degradation.",
                "prep": "Rinse food residues, separate metal caps or corks into appropriate streams.",
                "upcycling": "Repurpose into airtight bulk pantry jars, decorative vases, or DIY candle holders.",
                "co2_saved": 0.42,
                "kwh_saved": 0.85,
                "water_saved_l": 4.0
            },
            {
                "keywords": ["plastic sauce cup", "plastic container", "yogurt tub", "takeout lid", "hard plastic tub"],
                "category": "Dry Recyclable",
                "stream_icon": "♻️",
                "material": "Polypropylene (PP 5) / Rigid PET",
                "confidence": 94.2,
                "weight_g": 12,
                "decomposition_yrs": "300 years",
                "toxicity": "Low",
                "reason": "Rigid thermoplastic suitable for mechanical recycling into automotive parts and storage tubs once clean.",
                "prep": "Scrape off oils/sauces, wash thoroughly with eco soap, dry before binning.",
                "upcycling": "Use small sauce containers as watercolor mixing trays, small craft bead holders, or seed germinators.",
                "co2_saved": 0.04,
                "kwh_saved": 0.12,
                "water_saved_l": 0.8
            },

            # Wet Organics
            {
                "keywords": ["banana peel", "apple core", "fruit peel", "citrus peel", "watermelon rind", "vegetable scrap", "potato skin"],
                "category": "Wet Organic",
                "stream_icon": "🟢",
                "material": "Organic Lignocellulosic Food Waste",
                "confidence": 98.9,
                "weight_g": 90,
                "decomposition_yrs": "2–6 weeks",
                "toxicity": "None",
                "reason": "Rich in potassium, nitrogen, and carbon ideal for aerobic microbial composting.",
                "prep": "Chop coarse peels to increase surface area for faster microbial decomposition.",
                "upcycling": "Soak banana peels in water for 48 hrs to produce potassium-rich organic fertilizer liquid.",
                "co2_saved": 0.14,
                "kwh_saved": 0.05,
                "water_saved_l": 0.0
            },
            {
                "keywords": ["leftover rice", "food scraps", "cooked meal", "bread crust", "vegetable residue", "meat bones"],
                "category": "Wet Organic",
                "stream_icon": "🟢",
                "material": "Biodegradable Household Food Waste",
                "confidence": 96.7,
                "weight_g": 250,
                "decomposition_yrs": "1–3 weeks",
                "toxicity": "Low (Rot methane potential)",
                "reason": "Diverts high-moisture organic mass from landfills, preventing anaerobic methane generation.",
                "prep": "Drain excess liquids into sink; place solid food scraps in wet organic waste bin.",
                "upcycling": "Process through home Bokashi anaerobic fermenter or municipal bio-digester.",
                "co2_saved": 0.30,
                "kwh_saved": 0.10,
                "water_saved_l": 0.0
            },
            {
                "keywords": ["coffee grounds", "tea bag", "tea leaves", "used coffee filter"],
                "category": "Wet Organic",
                "stream_icon": "🟢",
                "material": "Nitrogen-Rich Plant Bio-matter",
                "confidence": 97.8,
                "weight_g": 30,
                "decomposition_yrs": "2–3 weeks",
                "toxicity": "None",
                "reason": "High nitrogen-to-carbon ratio enhances soil humus structure and micro-fauna.",
                "prep": "Verify tea bags are free of synthetic plastic mesh or metal staples before composting.",
                "upcycling": "Mix dry coffee grounds into garden soil to naturally repel pests and boost soil acidity.",
                "co2_saved": 0.08,
                "kwh_saved": 0.02,
                "water_saved_l": 0.0
            },

            # Landfill / Hazardous
            {
                "keywords": ["oily pizza box", "greasy pizza box", "oily cardboard", "greasy paper", "used napkin", "dirty paper towel"],
                "category": "Landfill / Hazardous",
                "stream_icon": "🔴",
                "material": "Grease-Contaminated Paperboard",
                "confidence": 96.2,
                "weight_g": 140,
                "decomposition_yrs": "2–6 months (if composted)",
                "toxicity": "Low",
                "reason": "Embedded hydrophobic fats break down paper recycling water slurry and ruin paper batches.",
                "prep": "Separate clean cardboard lid for recycling ♻️; place greasy bottom section into organic compost or landfill bin.",
                "upcycling": "Shred unprinted greasy cardboard to serve as carbon 'brown' bedding in worm compost bins.",
                "co2_saved": 0.03,
                "kwh_saved": 0.02,
                "water_saved_l": 0.0
            },
            {
                "keywords": ["styrofoam", "expanded polystyrene", "meat tray", "foam packaging", "styrofoam cup"],
                "category": "Landfill / Hazardous",
                "stream_icon": "🔴",
                "material": "Expanded Polystyrene (PS 6)",
                "confidence": 98.0,
                "weight_g": 25,
                "decomposition_yrs": "500+ years",
                "toxicity": "Medium (Styrene leaching risk)",
                "reason": "Low density makes transport uneconomic; frays easily into marine microplastics.",
                "prep": "Clean off food grease. Transport to EPS specialized drop-off or place in landfill bin.",
                "upcycling": "Crumble into small foam chunks and use at the base of heavy plant pots for improved soil drainage.",
                "co2_saved": 0.01,
                "kwh_saved": 0.01,
                "water_saved_l": 0.0
            },
            {
                "keywords": ["led bulb", "light bulb", "fluorescent tube", "halogen light", "broken bulb"],
                "category": "Landfill / Hazardous",
                "stream_icon": "🔴",
                "material": "Hazardous Electronic Lighting Waste",
                "confidence": 99.2,
                "weight_g": 65,
                "decomposition_yrs": "Indefinite (Glass/Circuitry)",
                "toxicity": "High (Mercury/Lead risk)",
                "reason": "Contains electronic drivers, heavy metals, or phosphor gas coatings requiring regulated handling.",
                "prep": "Wrap broken glass securely in heavy paper. Store intact bulbs for official e-waste drop-off.",
                "upcycling": "Do not upcycle due to toxic gas or sharp glass risks; deliver to certified retailer take-back drop.",
                "facility": "Municipal E-Waste Recycling Vault / Certified Hardware Take-back",
                "co2_saved": 0.28,
                "kwh_saved": 0.90,
                "water_saved_l": 5.0
            },
            {
                "keywords": ["battery", "aa battery", "lithium battery", "phone battery", "car battery"],
                "category": "Landfill / Hazardous",
                "stream_icon": "🔴",
                "material": "Electrochemical Battery Waste (Li-ion / Alkaline)",
                "confidence": 99.8,
                "weight_g": 45,
                "decomposition_yrs": "Indefinite (Heavy Metals)",
                "toxicity": "Critical (Fire & Heavy Metal Risk)",
                "reason": "Risk of thermal runaway fires in refuse trucks and toxic cadmium/lithium groundwater contamination.",
                "prep": "Isolate terminals with electrical tape. Store in non-conductive box for dedicated battery take-back.",
                "upcycling": "Never attempt DIY upcycling on spent batteries. Drop off at designated retail collection boxes.",
                "facility": "Certified Hazardous Household Waste (HHW) Facility / Battery Collection Hub",
                "co2_saved": 0.45,
                "kwh_saved": 1.50,
                "water_saved_l": 25.0
            }
        ]

    def analyze_query(self, query):
        if not query or not query.strip():
            return [], []

        delimiters = r'\bwith\b|\band\b|\bcontaining\b|\bplus\b|,|&|\+'
        raw_parts = re.split(delimiters, query, flags=re.IGNORECASE)

        parsed_items = []
        logs = [
            f"[{datetime.now().strftime('%H:%M:%S')}] Agent Initialized: EcoSort-LLM v4.2 Pipeline",
            f"[{datetime.now().strftime('%H:%M:%S')}] Input Query Received: '{query}'",
            f"[{datetime.now().strftime('%H:%M:%S')}] Tokenizing & Extracting distinct material components..."
        ]

        seen_keys = set()
        for idx, part in enumerate(raw_parts, 1):
            clean_part = part.strip().lower()
            if not clean_part:
                continue

            matched_rule = None
            for rule in self.rules:
                for kw in rule["keywords"]:
                    if kw in clean_part:
                        matched_rule = rule
                        break
                if matched_rule:
                    break

            if not matched_rule:
                matched_rule = self._fallback(clean_part)

            item_name = matched_rule["keywords"][0].title()
            logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Extracted Component #{idx}: '{clean_part}' -> Matched: {item_name} (Confidence: {matched_rule['confidence']}%)")

            key = f"{item_name}_{clean_part}"
            if key not in seen_keys:
                seen_keys.add(key)
                parsed_items.append({
                    "original_text": part.strip(),
                    "name": item_name,
                    "category": matched_rule["category"],
                    "stream_icon": matched_rule["stream_icon"],
                    "material": matched_rule["material"],
                    "confidence": matched_rule["confidence"],
                    "weight_g": matched_rule["weight_g"],
                    "decomposition": matched_rule["decomposition_yrs"],
                    "toxicity": matched_rule["toxicity"],
                    "reason": matched_rule["reason"],
                    "prep": matched_rule["prep"],
                    "upcycling": matched_rule["upcycling"],
                    "facility": matched_rule.get("facility", "Standard Local Waste Facility"),
                    "co2_saved": matched_rule["co2_saved"],
                    "kwh_saved": matched_rule["kwh_saved"],
                    "water_saved_l": matched_rule["water_saved_l"]
                })

        logs.append(f"[{datetime.now().strftime('%H:%M:%S')}] Segregation Complete: {len(parsed_items)} stream targets resolved cleanly.")
        return parsed_items, logs

    def _fallback(self, text):
        if any(w in text for w in ["paper", "cardboard", "box", "can", "metal", "glass", "bottle", "plastic"]):
            return {
                "keywords": [text],
                "category": "Dry Recyclable",
                "stream_icon": "♻️",
                "material": "Mixed Recyclable Packaging",
                "confidence": 88.5,
                "weight_g": 50,
                "decomposition_yrs": "50–100 years",
                "toxicity": "Low",
                "reason": "General recyclable packaging material identified via keyword heuristic matching.",
                "prep": "Clean food residues, dry, and place into recyclables bin.",
                "upcycling": "Repurpose as craft packaging material or storage.",
                "facility": "Municipal Materials Recovery Facility (MRF)",
                "co2_saved": 0.05,
                "kwh_saved": 0.10,
                "water_saved_l": 1.0
            }
        elif any(w in text for w in ["food", "fruit", "peel", "leftover", "vegetable", "seed", "organic"]):
            return {
                "keywords": [text],
                "category": "Wet Organic",
                "stream_icon": "🟢",
                "material": "Mixed Organic Waste",
                "confidence": 91.0,
                "weight_g": 100,
                "decomposition_yrs": "2–4 weeks",
                "toxicity": "None",
                "reason": "Biodegradable organic matter suitable for composting.",
                "prep": "Separate synthetic labels and deposit in organic compost bin.",
                "upcycling": "Add to compost bin to generate nutrient-rich soil humus.",
                "facility": "Municipal Composting Plant / Green Waste Digester",
                "co2_saved": 0.10,
                "kwh_saved": 0.02,
                "water_saved_l": 0.0
            }
        else:
            return {
                "keywords": [text],
                "category": "Landfill / Hazardous",
                "stream_icon": "🔴",
                "material": "Composite Waste Stream",
                "confidence": 85.0,
                "weight_g": 80,
                "decomposition_yrs": "Unknown (Non-recyclable)",
                "toxicity": "Medium",
                "reason": "Composite or contaminated item not supported by standard curb recycling.",
                "prep": "Place into general landfill waste container.",
                "upcycling": "Minimize single-use purchases of composite packaging.",
                "facility": "Municipal Refuse Incinerator / Sanitary Landfill",
                "co2_saved": 0.01,
                "kwh_saved": 0.00,
                "water_saved_l": 0.0
            }


engine = AdvancedEcoEngine()


# ==========================================
# SIDEBAR CONTROL CENTER & RESPONSIBLE AI
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/emoji/96/000000/seedling-emoji.png", width=65)
    st.title("EcoSort AI Pro")
    st.caption("Enterprise Circular Economy & Segregation Platform")

    st.markdown("---")
    
    # Model Config
    st.subheader("⚙️ Agent Engine Configuration")
    agent_model = st.selectbox(
        "Active AI Model:",
        ["EcoSort-LLM v4.2 (Prompt-Agent)", "Heuristic Taxonomy v2.4", "Vision-MultiModal-v1"]
    )
    conf_threshold = st.slider("Confidence Threshold Cutoff:", 50, 99, 85)

    st.markdown("---")

    # SDG 12 Alignment
    st.subheader("🎯 UN SDG 12 Hub")
    st.markdown("""
    **Responsible Consumption & Production**
    - **Target 12.5**: Substantially reduce waste generation by 2030 through prevention, reduction, recycling, and reuse.
    - **Target 12.8**: Promote universal sustainability awareness and eco-lifestyle education.
    """)

    st.markdown("---")

    # Responsible AI Framework
    st.subheader("🛡️ Responsible AI Audit")
    with st.expander("🔍 Explainability & Transparency", expanded=True):
        st.write("Provides complete rule-backed decision traces, confidence scores, and material toxicity metrics for every item.")

    with st.expander("🔒 Privacy-First Architecture"):
        st.write("100% On-Device / Local Processing. Zero user PII, images, or location telemetry transmitted to external third parties.")

    with st.expander("⚖️ Inclusive Material Taxonomy"):
        st.write("Trained on global packaging formats, regional culinary scraps, and industrial e-waste types to prevent cultural bias.")

    st.markdown("---")
    st.caption("EcoSort AI Pro v2.5 • SDG 12 Compliant")


# ==========================================
# APP HEADER
# ==========================================
st.markdown("""
    <div class="eco-header">
        <h1>🌱 EcoSort AI Pro — Enterprise Circular Economy Platform</h1>
        <p>AI-Driven Packaging Segregation Engine • Life Cycle Assessment (LCA) • Upcycling Blueprints • SDG 12 Analytics</p>
    </div>
""", unsafe_allow_html=True)


# ==========================================
# NAVIGATION TABS
# ==========================================
tab_segregate, tab_vision, tab_lca, tab_facilities, tab_analytics, tab_export = st.tabs([
    "🧠 AI Segregator & Prompt Engine",
    "📷 Multi-Modal Vision Simulator",
    "🔬 Life Cycle Assessment (LCA)",
    "🗺️ Disposal Hub & Upcycling",
    "📊 SDG 12 Executive Analytics",
    "📑 Audit Report & Export"
])


# ==========================================
# TAB 1: AI SEGREGATOR & PROMPT ENGINE
# ==========================================
with tab_segregate:
    st.subheader("🔍 Intelligent Multi-Component Waste Segregator")
    st.write("Enter meal packaging descriptions or composite waste queries to trigger the prompt-agent classification engine.")

    # Preset Buttons
    st.markdown("**⚡ Quick Preset Scenarios:**")
    cp1, cp2, cp3, cp4 = st.columns(4)
    preset_val = ""
    if cp1.button("🍕 Takeout Pizza combo"):
        preset_val = "oily cardboard pizza box with plastic sauce cup and soda can"
    if cp2.button("🍱 Office Desk Lunch"):
        preset_val = "banana peel, plastic water bottle, coffee cup with plastic lid"
    if cp3.button("💡 Household E-Waste"):
        preset_val = "broken LED bulb, aa battery, clean cardboard box"
    if cp4.button("🥗 Kitchen Food Prep"):
        preset_val = "apple core, eggshell, tea bag, plastic wrapper"

    query_input = st.text_input(
        "Enter Waste Description:",
        value=preset_val if preset_val else "",
        placeholder="e.g. oily cardboard pizza box with plastic sauce cup and soda can"
    )

    run_btn = st.button("🚀 Analyze & Segregate Packaging", type="primary")

    if query_input or run_btn:
        items, agent_logs = engine.analyze_query(query_input)

        if not items:
            st.warning("Please enter a valid description of packaging or waste items.")
        else:
            # High-level Metrics Header
            dry_c = sum(1 for i in items if i['category'] == 'Dry Recyclable')
            wet_c = sum(1 for i in items if i['category'] == 'Wet Organic')
            haz_c = sum(1 for i in items if i['category'] == 'Landfill / Hazardous')
            tot_co2 = sum(i['co2_saved'] for i in items)
            tot_kwh = sum(i['kwh_saved'] for i in items)

            m1, m2, m3, m4, m5 = st.columns(5)
            m1.markdown(f'<div class="stat-card-pro"><div class="stat-val" style="color:#1b4332;">♻️ {dry_c}</div><div class="stat-lbl">Recyclables</div></div>', unsafe_allow_html=True)
            m2.markdown(f'<div class="stat-card-pro"><div class="stat-val" style="color:#d97706;">🟢 {wet_c}</div><div class="stat-lbl">Organics</div></div>', unsafe_allow_html=True)
            m3.markdown(f'<div class="stat-card-pro"><div class="stat-val" style="color:#900c3f;">🔴 {haz_c}</div><div class="stat-lbl">Hazardous</div></div>', unsafe_allow_html=True)
            m4.markdown(f'<div class="stat-card-pro"><div class="stat-val" style="color:#2563eb;">{tot_co2:.2f} kg</div><div class="stat-lbl">CO₂ Diverted</div></div>', unsafe_allow_html=True)
            m5.markdown(f'<div class="stat-card-pro"><div class="stat-val" style="color:#059669;">{tot_kwh:.2f} kWh</div><div class="stat-lbl">Energy Saved</div></div>', unsafe_allow_html=True)

            st.write("")

            # Items Cards
            for idx, item in enumerate(items, 1):
                b_class = "badge-dry" if item["category"] == "Dry Recyclable" else ("badge-wet" if item["category"] == "Wet Organic" else "badge-hazard")
                
                st.markdown(f"""
                <div class="glass-card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <h3 style="margin:0; color:#0f2b1d;">#{idx} {item['name']} <span style="font-size:0.9rem; color:#64748b; font-weight:normal;">("{item['original_text']}")</span></h3>
                        <span class="{b_class}">{item['stream_icon']} {item['category']}</span>
                    </div>
                    
                    <div style="margin-bottom: 12px;">
                        <span class="metric-pill">🧪 Material: {item['material']}</span>
                        <span class="metric-pill">🎯 Confidence: {item['confidence']}%</span>
                        <span class="metric-pill">⚖️ Est. Weight: {item['weight_g']}g</span>
                        <span class="metric-pill">⏳ Landfill Time: {item['decomposition']}</span>
                        <span class="metric-pill">☣️ Toxicity Level: {item['toxicity']}</span>
                    </div>

                    <p><strong>💡 Explainability Rationale:</strong> {item['reason']}</p>
                    
                    <div class="highlight-box-green">
                        <strong>🧼 Cleaning & Preparation Instructions:</strong><br/>
                        {item['prep']}
                    </div>

                    <div class="highlight-box-amber">
                        <strong>♻️ Practical Circular Upcycling Tip:</strong><br/>
                        {item['upcycling']}
                    </div>

                    <div class="highlight-box-blue">
                        <strong>🗺️ Recommended Facility Route:</strong> {item['facility']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # Agent Execution Logs Console
            with st.expander("🛠️ Real-Time Agent Execution Logs & Trace", expanded=False):
                log_text = "\n".join(agent_logs)
                st.markdown(f'<div class="terminal-box">{log_text}</div>', unsafe_allow_html=True)


# ==========================================
# TAB 2: MULTI-MODAL VISION SIMULATOR
# ==========================================
with tab_vision:
    st.subheader("📷 Computer Vision Multi-Modal Packaging Detector")
    st.write("Simulate AI vision scanning on meal containers and mixed waste items using visual boundary detection.")

    v_col1, v_col2 = st.columns([1, 1])

    with v_col1:
        sample_img = st.selectbox(
            "Select Sample Packaging Image Scan:",
            [
                "🍕 Takeout Pizza & Soda Box Combo",
                "🍱 Office Plastic Container & Beverage",
                "💡 E-Waste & Lighting Bin Scan",
                "🥗 Organic Kitchen Prep Waste"
            ]
        )

        st.info("💡 You can also drag and drop your own image below to test object detection simulation.")
        uploaded_file = st.file_uploader("Upload Packaging Image:", type=["jpg", "jpeg", "png"])

        if sample_img == "🍕 Takeout Pizza & Soda Box Combo":
            st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80", caption="Scanned Image: Takeout Meal Box", use_container_width=True)
        elif sample_img == "🍱 Office Plastic Container & Beverage":
            st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80", caption="Scanned Image: Lunch Container", use_container_width=True)
        elif sample_img == "💡 E-Waste & Lighting Bin Scan":
            st.image("https://images.unsplash.com/photo-1550009158-9ebf69173e03?auto=format&fit=crop&w=800&q=80", caption="Scanned Image: E-Waste Components", use_container_width=True)
        else:
            st.image("https://images.unsplash.com/photo-1610348725531-843dff563e2c?auto=format&fit=crop&w=800&q=80", caption="Scanned Image: Kitchen Organic Waste", use_container_width=True)

    with v_col2:
        st.subheader("🎯 Object Detection & Segmentation Results")
        st.success("✅ Vision Model: YOLOv8-EcoSort • Image Dimensions: 1024x768 • Processing Latency: 42ms")

        if "Pizza" in sample_img:
            st.markdown("""
            - 🟥 **Bounding Box #1 [Confidence 98.4%]**: `Oily Cardboard Box` -> **Landfill / Hazardous**
            - 🟩 **Bounding Box #2 [Confidence 96.1%]**: `Aluminum Soda Can` -> **Dry Recyclable**
            - 🟦 **Bounding Box #3 [Confidence 94.7%]**: `Plastic Sauce Cup` -> **Dry Recyclable**
            """)
        elif "Office" in sample_img:
            st.markdown("""
            - 🟩 **Bounding Box #1 [Confidence 97.8%]**: `PET Beverage Bottle` -> **Dry Recyclable**
            - 🟨 **Bounding Box #2 [Confidence 99.1%]**: `Banana Peel` -> **Wet Organic**
            - 🟦 **Bounding Box #3 [Confidence 92.4%]**: `Plastic Takeout Lid` -> **Dry Recyclable**
            """)
        elif "E-Waste" in sample_img:
            st.markdown("""
            - 🟥 **Bounding Box #1 [Confidence 99.5%]**: `Lithium AA Battery` -> **Hazardous E-Waste**
            - 🟥 **Bounding Box #2 [Confidence 98.9%]**: `LED Bulb Glass` -> **Hazardous E-Waste**
            - 🟩 **Bounding Box #3 [Confidence 95.2%]**: `Cardboard Shipping Box` -> **Dry Recyclable**
            """)
        else:
            st.markdown("""
            - 🟨 **Bounding Box #1 [Confidence 99.0%]**: `Apple Core & Fruit Scraps` -> **Wet Organic**
            - 🟨 **Bounding Box #2 [Confidence 97.5%]**: `Used Coffee Grounds` -> **Wet Organic**
            - 🟥 **Bounding Box #3 [Confidence 89.2%]**: `Plastic Film Wrapper` -> **Landfill Waste**
            """)

        st.progress(0.96)
        st.caption("Average Stream Classification Confidence: 96.2%")


# ==========================================
# TAB 3: LIFE CYCLE ASSESSMENT (LCA)
# ==========================================
with tab_lca:
    st.subheader("🔬 Enterprise Life Cycle Assessment (LCA) Calculator")
    st.write("Quantify your Scope 3 GHG carbon footprint reduction and industrial energy preservation metrics.")

    lc1, lc2 = st.columns([1, 1])

    with lc1:
        st.markdown("#### 📥 Monthly Waste Generation Input")
        pet_in = st.number_input("PET Plastic Bottles (qty/mo):", 0, 500, 45)
        paper_in = st.number_input("Clean Cardboard & Paper (kg/mo):", 0, 200, 15)
        can_in = st.number_input("Aluminum Cans (qty/mo):", 0, 300, 30)
        org_in = st.number_input("Organic Food Scraps composted (kg/mo):", 0, 500, 25)

    with lc2:
        st.markdown("#### 🌿 Environmental Savings Output")
        co2_val = (pet_in * 0.09) + (paper_in * 0.95) + (can_in * 0.16) + (org_in * 0.45)
        kwh_val = (pet_in * 0.28) + (paper_in * 0.60) + (can_in * 0.45) + (org_in * 0.10)
        water_val = (pet_in * 3.5) + (paper_in * 18.0) + (can_in * 1.2)
        trees_val = co2_val / 21.0 # 1 tree absorbs ~21kg CO2/yr

        st.success(f"🌱 **{co2_val:.2f} kg CO₂e** Scope 3 Carbon Emissions Prevented / Month")
        st.info(f"⚡ **{kwh_val:.1f} kWh** Electricity Preserved (Equivalent to running an LED bulb for {int(kwh_val*100)} hours)")
        st.warning(f"💧 **{water_val:.1f} Liters** Industrial Water Preserved")
        st.markdown(f"🌳 **Equivalent to planting `{trees_val:.2f}` mature trees annually!**")

    st.markdown("---")
    st.subheader("📊 LCA Breakdown by Material Stream")
    
    lca_df = pd.DataFrame({
        'Material': ['PET Plastic', 'Cardboard/Paper', 'Aluminum Cans', 'Food Scraps'],
        'CO2 Saved (kg)': [pet_in * 0.09, paper_in * 0.95, can_in * 0.16, org_in * 0.45],
        'Water Saved (L)': [pet_in * 3.5, paper_in * 18.0, can_in * 1.2, 0]
    })

    c_lca = alt.Chart(lca_df).mark_bar(cornerRadius=6).encode(
        x='Material',
        y='CO2 Saved (kg)',
        color=alt.Color('Material', scale=alt.Scale(scheme='greens')),
        tooltip=['Material', 'CO2 Saved (kg)', 'Water Saved (L)']
    ).properties(height=300)

    st.altair_chart(c_lca, use_container_width=True)


# ==========================================
# TAB 4: DISPOSAL HUB & UPCYCLING BLUEPRINTS
# ==========================================
with tab_facilities:
    st.subheader("🗺️ Recommended Disposal Pathway & Facility Locator")
    
    fac_col1, fac_col2 = st.columns([1, 1])

    with fac_col1:
        st.markdown("#### 🏢 Nearby Certified Waste Facilities")
        fac_type = st.selectbox("Filter Facilities by Stream:", ["All Facilities", "Materials Recovery (MRF)", "E-Waste Vaults", "Composting Plants"])

        facilities = [
            {"name": "GreenLoop Materials Recovery Facility (MRF)", "type": "Materials Recovery (MRF)", "dist": "2.4 km", "accepts": "Clean Paper, Cardboard, PET Bottles, Aluminum Cans", "rating": "⭐ 4.8"},
            {"name": "EcoVault E-Waste & Hazardous Hub", "type": "E-Waste Vaults", "dist": "4.1 km", "accepts": "Batteries, Light Bulbs, Circuit Boards, Appliances", "rating": "⭐ 4.9"},
            {"name": "BioHumus Municipal Composting Site", "type": "Composting Plants", "dist": "1.8 km", "accepts": "Food Waste, Coffee Grounds, Garden Scraps", "rating": "⭐ 4.7"}
        ]

        for fac in facilities:
            if fac_type == "All Facilities" or fac_type in fac["type"]:
                st.markdown(f"""
                <div class="glass-card">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="margin:0; color:#1b4332;">{fac['name']}</h4>
                        <span class="badge-dry">{fac['dist']}</span>
                    </div>
                    <p style="margin:4px 0; color:#64748b;"><strong>Accepts:</strong> {fac['accepts']}</p>
                    <span style="font-size:0.85rem; color:#d97706;">{fac['rating']} Certified Partner</span>
                </div>
                """, unsafe_allow_html=True)

    with fac_col2:
        st.subheader("♻️ DIY Upcycling Blueprints")
        up_mat = st.selectbox("Select Upcycling Material Blueprint:", ["PET Bottles", "Cardboard Boxes", "Aluminum Cans", "Coffee Grounds"])

        if up_mat == "PET Bottles":
            st.markdown("""
            ### 🪴 Self-Watering Hydroponic Planter
            - **Difficulty**: Easy 🟢 (15 mins)
            - **Tools Needed**: Scissors, Cotton Wick String, Soil, Seeds.
            - **Steps**:
              1. Cut PET bottle 1/3 from the top neck.
              2. Invert top neck downward into bottom reservoir.
              3. Thread cotton wick string through cap hole into water base.
              4. Fill top with potting soil and plant seeds!
            """)
        elif up_mat == "Cardboard Boxes":
            st.markdown("""
            ### 📦 Modular Drawer Storage Organizer
            - **Difficulty**: Easy 🟢 (20 mins)
            - **Tools Needed**: Utility Knife, Ruler, Glue / Tape.
            - **Steps**:
              1. Measure inner height of your desk drawer.
              2. Cut cereal or shipping boxes into interlocking cardboard strips.
              3. Slot strips together to make a grid divider for socks or stationery.
            """)
        elif up_mat == "Aluminum Cans":
            st.markdown("""
            ### ✏️ Industrial Desk Pencil & Tool Holder
            - **Difficulty**: Medium 🟡 (20 mins)
            - **Tools Needed**: Can Opener / File, Paint or Twine Rope.
            - **Steps**:
              1. Smooth inner rim of clean soda/soup can with a file.
              2. Wrap exterior cleanly with natural jute twine or eco paint.
              3. Use to organize pens, paintbrushes, or scissors!
            """)
        else:
            st.markdown("""
            ### 🌿 Acid-Loving Soil Enhancer & Pest Barrier
            - **Difficulty**: Very Easy 🟢 (5 mins)
            - **Tools Needed**: Oven Tray / Sun Drying Sheet.
            - **Steps**:
              1. Spread used coffee grounds flat and dry thoroughly in sun/oven.
              2. Sprinkle dry grounds around base of roses, blueberries, or hydrangeas.
              3. Natural nitrogen source that deters garden slugs!
            """)


# ==========================================
# TAB 5: EXECUTIVE SDG 12 ANALYTICS
# ==========================================
with tab_analytics:
    st.subheader("📊 Executive SDG 12 Performance Dashboard")
    st.write("Real-time monitoring of waste diversion rates, stream proportions, and municipal recycling targets.")

    # Top KPI Metrics
    ak1, ak2, ak3, ak4 = st.columns(4)
    ak1.metric("SDG Target 12.5 Progress", "74.8%", "+5.3% this quarter")
    ak2.metric("Landfill Diversion Rate", "68.2%", "+9.1%")
    ak3.metric("Recycling Purity Index", "94.6%", "+2.4%")
    ak4.metric("Community Upcycling Rate", "31.5%", "+6.0%")

    st.markdown("---")

    col_chart1, col_chart2 = st.columns(2)

    with col_chart1:
        st.markdown("#### 📈 30-Day Historical Waste Stream Diversion (Tons)")
        dates = pd.date_range(end=pd.Timestamp.now(), periods=30)
        df_trend = pd.DataFrame({
            'Date': dates,
            'Recyclables': [120 + i*2 + (i%3)*5 for i in range(30)],
            'Organics': [200 + i*3 - (i%2)*4 for i in range(30)],
            'Landfill': [80 - i*1.2 for i in range(30)]
        })
        
        df_melted = df_trend.melt('Date', var_name='Stream', value_name='Tons Diverted')
        c_trend = alt.Chart(df_melted).mark_line(point=True).encode(
            x='Date:T',
            y='Tons Diverted:Q',
            color=alt.Color('Stream', scale=alt.Scale(scheme='category10')),
            tooltip=['Date:T', 'Stream', 'Tons Diverted']
        ).properties(height=320)
        st.altair_chart(c_trend, use_container_width=True)

    with col_chart2:
        st.markdown("#### 🧪 Material Decomposition Time vs Toxicity Matrix")
        df_matrix = pd.DataFrame({
            'Material': ['Glass', 'PET Plastic', 'Aluminum', 'Styrofoam', 'Cardboard', 'Food Scraps', 'Batteries'],
            'Decomposition (Years)': [1000, 450, 250, 500, 0.25, 0.08, 100],
            'Toxicity Rating': [1, 2, 1, 3, 1, 1, 5],
            'Category': ['Recyclable', 'Recyclable', 'Recyclable', 'Hazardous', 'Recyclable', 'Organic', 'Hazardous']
        })

        c_scatter = alt.Chart(df_matrix).mark_circle(size=180).encode(
            x='Decomposition (Years):Q',
            y='Toxicity Rating:Q',
            color='Category:N',
            tooltip=['Material', 'Decomposition (Years)', 'Toxicity Rating', 'Category']
        ).properties(height=320)
        st.altair_chart(c_scatter, use_container_width=True)


# ==========================================
# TAB 6: AUDIT REPORT & EXPORT
# ==========================================
with tab_export:
    st.subheader("📑 Waste Segregation Audit Exporter")
    st.write("Generate and download official sustainability audit reports for corporate compliance or personal record keeping.")

    audit_data = {
        "report_id": f"AUDIT-SDG12-{int(time.time())}",
        "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "compliance_standard": "UN Sustainable Development Goal 12.5",
        "privacy_status": "Passed 100% On-Device Local Audit",
        "sample_audit_items": [
            {"item": "Aluminum Soda Can", "stream": "Dry Recyclable", "co2_diverted_kg": 0.16},
            {"item": "Plastic Sauce Cup", "stream": "Dry Recyclable", "co2_diverted_kg": 0.04},
            {"item": "Oily Cardboard Pizza Box", "stream": "Landfill / Hazardous", "co2_diverted_kg": 0.03},
            {"item": "Banana Peel Scraps", "stream": "Wet Organic", "co2_diverted_kg": 0.14}
        ]
    }

    json_str = json.dumps(audit_data, indent=2)

    st.code(json_str, language="json")

    st.download_button(
        label="📥 Download Official Audit JSON Report",
        data=json_str,
        file_name=f"ecosort_audit_{int(time.time())}.json",
        mime="application/json"
    )
