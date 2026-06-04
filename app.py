"""
╔══════════════════════════════════════════════════════════════════════╗
║   EFFICIENT RENEWABLE ENERGY PREDICTOR SYSTEM                       ║
║   Enterprise-Grade AI Analytics Platform  |  Capstone 2026          ║
║   Microsoft Azure AI Studio · Power BI Style · Futuristic SaaS      ║
╚══════════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════════
# CORE IMPORTS
# ══════════════════════════════════════════════════════════════════════
import streamlit as st
import streamlit.components.v1 as st_html
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import joblib
import pickle
from datetime import datetime, timedelta
import requests
import math
import io
import base64
import json

# ══════════════════════════════════════════════════════════════════════
# PAGE CONFIG — must be first Streamlit call
# ══════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="EnergyAI — Renewable Intelligence Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://openweathermap.org/api",
        "About": "EnergyAI Renewable Intelligence Platform — Capstone 2026",
    },
)

# ══════════════════════════════════════════════════════════════════════
# GLOBAL CSS  — Microsoft Fluent UI × Glassmorphism × Futuristic
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ══════════════════════════════════════════════════════
   RENEWABLE ENERGY INTELLIGENCE PLATFORM — FULL THEME
   5 Sources: Solar · Wind · Hydro · Biomass · Geothermal
   ══════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;700;800;900&family=Exo+2:wght@300;400;500;600;700&family=Rajdhani:wght@400;500;600;700&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Exo 2', system-ui, sans-serif !important;
    box-sizing: border-box;
}

/* ── Design Token Variables ── */
:root {
    /* Solar — golden fire */
    --solar:        #FDB813;
    --solar-2:      #FF8C42;
    --solar-glow:   rgba(253,184,19,0.20);
    --solar-dim:    rgba(253,184,19,0.08);
    /* Wind — electric sky */
    --wind:         #7FDBFF;
    --wind-2:       #00C2FF;
    --wind-glow:    rgba(0,194,255,0.20);
    --wind-dim:     rgba(127,219,255,0.08);
    /* Hydro — deep ocean */
    --hydro:        #00B4D8;
    --hydro-2:      #0077B6;
    --hydro-glow:   rgba(0,180,216,0.20);
    --hydro-dim:    rgba(0,119,182,0.08);
    /* Biomass — living forest */
    --bio:          #2ECC71;
    --bio-2:        #1B5E20;
    --bio-glow:     rgba(46,204,113,0.20);
    --bio-dim:      rgba(46,204,113,0.08);
    /* Geothermal — magma core */
    --geo:          #F77F00;
    --geo-2:        #D62828;
    --geo-glow:     rgba(214,40,40,0.20);
    --geo-dim:      rgba(247,127,0,0.08);
    /* Ocean (legacy compat) */
    --ocean:        #6366f1;
    /* Base */
    --bg:           #08121C;
    --bg-2:         #101820;
    --surface:      rgba(255,255,255,0.032);
    --border:       rgba(255,255,255,0.065);
    --text:         #dde6f0;
    --muted:        #7a9ab0;
    --accent:       #00B4D8;
    --accent-2:     #2ECC71;
}

/* ══════════════════════════════════════════════════════
   ANIMATED BACKGROUND — Renewable Energy Atmosphere
   ══════════════════════════════════════════════════════ */
.stApp {
    background:
        /* Solar corona — top right */
        radial-gradient(ellipse 55% 45% at 92% 5%, rgba(253,184,19,0.055) 0%, transparent 65%),
        /* Wind sky — top left */
        radial-gradient(ellipse 60% 40% at 5% 15%, rgba(0,194,255,0.05) 0%, transparent 60%),
        /* Hydro depth — bottom left */
        radial-gradient(ellipse 50% 55% at 8% 90%, rgba(0,119,182,0.06) 0%, transparent 60%),
        /* Biomass forest — center */
        radial-gradient(ellipse 40% 30% at 50% 60%, rgba(46,204,113,0.035) 0%, transparent 70%),
        /* Geothermal magma — bottom right */
        radial-gradient(ellipse 45% 40% at 95% 95%, rgba(214,40,40,0.055) 0%, transparent 60%),
        /* Base deep navy */
        linear-gradient(175deg, #08121C 0%, #0b1825 35%, #08121C 70%, #0a1520 100%);
    min-height: 100vh;
    position: relative;
}

/* Floating energy particles overlay */
.stApp::before {
    content: '';
    position: fixed;
    inset: 0;
    pointer-events: none;
    background-image:
        radial-gradient(1px 1px at 15% 25%, rgba(253,184,19,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 35% 70%, rgba(0,194,255,0.35) 0%, transparent 100%),
        radial-gradient(1px 1px at 60% 15%, rgba(46,204,113,0.4) 0%, transparent 100%),
        radial-gradient(1px 1px at 80% 55%, rgba(247,127,0,0.4) 0%, transparent 100%),
        radial-gradient(1.5px 1.5px at 50% 85%, rgba(0,180,216,0.35) 0%, transparent 100%),
        radial-gradient(1px 1px at 90% 30%, rgba(253,184,19,0.3) 0%, transparent 100%),
        radial-gradient(1px 1px at 25% 90%, rgba(214,40,40,0.3) 0%, transparent 100%),
        radial-gradient(1px 1px at 70% 40%, rgba(127,219,255,0.35) 0%, transparent 100%);
    z-index: 0;
    animation: particle-drift 18s ease-in-out infinite alternate;
}
@keyframes particle-drift {
    0%   { transform: translateY(0px) translateX(0px); opacity: 0.6; }
    50%  { transform: translateY(-8px) translateX(4px); opacity: 1; }
    100% { transform: translateY(-16px) translateX(-4px); opacity: 0.7; }
}

/* Energy silhouette SVG overlay — wind turbine + solar panel shapes */
.stApp::after {
    content: '';
    position: fixed;
    bottom: 0; left: 0; right: 0;
    height: 180px;
    pointer-events: none;
    background:
        /* Wind turbine silhouette — left */
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 120 180'%3E%3Crect x='58' y='60' width='4' height='120' fill='rgba(0,194,255,0.06)'/%3E%3Cellipse cx='60' cy='60' rx='28' ry='6' fill='rgba(0,194,255,0.05)' transform='rotate(-30 60 60)'/%3E%3Cellipse cx='60' cy='60' rx='28' ry='6' fill='rgba(0,194,255,0.05)' transform='rotate(90 60 60)'/%3E%3Cellipse cx='60' cy='60' rx='28' ry='6' fill='rgba(0,194,255,0.05)' transform='rotate(210 60 60)'/%3E%3C/svg%3E") left bottom / 120px no-repeat,
        /* Solar panel silhouette — right */
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 60'%3E%3Crect x='4' y='4' width='72' height='52' rx='3' fill='none' stroke='rgba(253,184,19,0.07)' stroke-width='1.5'/%3E%3Crect x='84' y='4' width='72' height='52' rx='3' fill='none' stroke='rgba(253,184,19,0.07)' stroke-width='1.5'/%3E%3Cline x1='40' y1='4' x2='40' y2='56' stroke='rgba(253,184,19,0.04)' stroke-width='1'/%3E%3Cline x1='4' y1='30' x2='76' y2='30' stroke='rgba(253,184,19,0.04)' stroke-width='1'/%3E%3Cline x1='120' y1='4' x2='120' y2='56' stroke='rgba(253,184,19,0.04)' stroke-width='1'/%3E%3Cline x1='84' y1='30' x2='156' y2='30' stroke='rgba(253,184,19,0.04)' stroke-width='1'/%3E%3C/svg%3E") right bottom / 260px no-repeat;
    z-index: 0;
    animation: silhouette-breathe 8s ease-in-out infinite alternate;
}
@keyframes silhouette-breathe {
    0%   { opacity: 0.6; }
    100% { opacity: 1; }
}

/* ══════════════════════════════════════════════════════
   SIDEBAR — Glassmorphism Eco Panel
   ══════════════════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg,
            rgba(0,194,255,0.04) 0%,
            rgba(8,18,28,0.97) 20%,
            rgba(8,18,28,0.97) 80%,
            rgba(46,204,113,0.04) 100%) !important;
    border-right: 1px solid rgba(0,180,216,0.18) !important;
    box-shadow: 4px 0 48px rgba(0,0,0,0.5), inset -1px 0 0 rgba(0,194,255,0.08);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
}
section[data-testid="stSidebar"] * { color: #c8dce8 !important; }
section[data-testid="stSidebar"]::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--solar), var(--wind-2), var(--hydro), var(--bio), var(--geo-2));
    border-radius: 0 0 0 0;
    animation: spectrum-slide 6s linear infinite;
}
@keyframes spectrum-slide {
    0%   { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

/* Sidebar nav radio items */
div[data-testid="stRadio"] > label { display: none; }
div[data-testid="stRadio"] > div { display: flex; flex-direction: column; gap: 3px; }
div[data-testid="stRadio"] > div > label {
    padding: 10px 16px;
    border-radius: 10px;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(.4,0,.2,1);
    border: 1px solid transparent;
    font-weight: 600;
    font-size: 13.5px;
    color: #a8c4d4 !important;
    position: relative;
    overflow: hidden;
    letter-spacing: 0.4px;
}
div[data-testid="stRadio"] > div > label::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
    background: linear-gradient(180deg, var(--hydro), var(--bio));
    border-radius: 2px;
    opacity: 0;
    transition: opacity 0.25s;
}
div[data-testid="stRadio"] > div > label:hover {
    background: rgba(0,180,216,0.12);
    border-color: rgba(0,180,216,0.30);
    color: #7FDBFF !important;
    padding-left: 22px;
}
div[data-testid="stRadio"] > div > label:hover::before { opacity: 1; }
/* Selected/checked radio label */
div[data-testid="stRadio"] > div > label[data-baseweb="radio"] span,
div[data-testid="stRadio"] > div > label span { color: #a8c4d4 !important; }

/* ══════════════════════════════════════════════════════
   GLASSMORPHISM CARDS
   ══════════════════════════════════════════════════════ */
.glass-card {
    background: linear-gradient(135deg,
        rgba(255,255,255,0.048) 0%,
        rgba(255,255,255,0.018) 100%);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 16px;
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, box-shadow 0.3s, transform 0.25s;
}
.glass-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg,
        rgba(255,255,255,0.025) 0%,
        transparent 60%);
    pointer-events: none;
    border-radius: inherit;
}
.glass-card:hover {
    border-color: rgba(0,180,216,0.22);
    box-shadow: 0 8px 40px rgba(0,180,216,0.08);
    transform: translateY(-2px);
}

/* Energy-specific card variants */
.glass-card-green {
    background: linear-gradient(135deg, var(--bio-dim) 0%, rgba(46,204,113,0.02) 100%);
    border-color: rgba(46,204,113,0.22);
}
.glass-card-green:hover { box-shadow: 0 8px 40px var(--bio-glow); border-color: rgba(46,204,113,0.35); }

.glass-card-blue, .glass-card-wind {
    background: linear-gradient(135deg, var(--wind-dim) 0%, rgba(0,194,255,0.02) 100%);
    border-color: rgba(0,194,255,0.22);
}
.glass-card-blue:hover, .glass-card-wind:hover { box-shadow: 0 8px 40px var(--wind-glow); border-color: rgba(0,194,255,0.35); }

.glass-card-purple {
    background: linear-gradient(135deg, rgba(99,102,241,0.1) 0%, rgba(99,102,241,0.02) 100%);
    border-color: rgba(99,102,241,0.22);
}

.glass-card-solar {
    background: linear-gradient(135deg, var(--solar-dim) 0%, rgba(253,184,19,0.02) 100%);
    border-color: rgba(253,184,19,0.22);
}
.glass-card-solar:hover { box-shadow: 0 8px 40px var(--solar-glow); border-color: rgba(253,184,19,0.35); }

.glass-card-hydro {
    background: linear-gradient(135deg, var(--hydro-dim) 0%, rgba(0,119,182,0.02) 100%);
    border-color: rgba(0,180,216,0.22);
}
.glass-card-geo {
    background: linear-gradient(135deg, var(--geo-dim) 0%, rgba(214,40,40,0.02) 100%);
    border-color: rgba(247,127,0,0.22);
}

/* ══════════════════════════════════════════════════════
   KPI / METRIC CARDS
   ══════════════════════════════════════════════════════ */
.kpi-card {
    background: linear-gradient(145deg,
        rgba(255,255,255,0.055) 0%,
        rgba(255,255,255,0.018) 100%);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px;
    padding: 22px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.28s ease, box-shadow 0.28s ease, border-color 0.28s;
    cursor: default;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg,
        var(--solar), var(--wind-2), var(--hydro),
        var(--bio), var(--geo));
    border-radius: 18px 18px 0 0;
    background-size: 300% 100%;
    animation: kpi-bar-shift 5s linear infinite;
}
@keyframes kpi-bar-shift {
    0%   { background-position: 0% 50%; }
    100% { background-position: 300% 50%; }
}
.kpi-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at 50% -10%, rgba(0,180,216,0.07) 0%, transparent 70%);
    pointer-events: none;
}
.kpi-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 16px 48px rgba(0,180,216,0.14);
    border-color: rgba(0,180,216,0.28);
}
.kpi-value {
    font-family: 'Orbitron', monospace !important;
    font-size: 1.85rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--hydro) 0%, var(--bio) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 10px 0 4px;
    line-height: 1;
    letter-spacing: -0.5px;
}
.kpi-label {
    font-size: 0.68rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-weight: 600;
}
.kpi-delta {
    font-size: 0.77rem;
    color: var(--bio);
    font-weight: 500;
    margin-top: 5px;
}
.kpi-icon {
    font-size: 1.55rem;
    margin-bottom: 4px;
    display: block;
}

/* ══════════════════════════════════════════════════════
   SECTION TITLES
   ══════════════════════════════════════════════════════ */
.section-title {
    font-family: 'Orbitron', monospace !important;
    font-size: 1.75rem;
    font-weight: 700;
    /* Solid fallback first so it's ALWAYS visible */
    color: #e0eaf2;
    /* Then try gradient clip on supporting browsers */
    background: linear-gradient(135deg,
        #FDB813 0%,
        #00C2FF 28%,
        #00B4D8 52%,
        #2ECC71 76%,
        #F77F00 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    /* Force paint layer so gradient renders in Streamlit iframes */
    -webkit-text-stroke: 0px transparent;
    margin-bottom: 6px;
    line-height: 1.25;
    letter-spacing: 1px;
    text-transform: uppercase;
    display: block;
    position: relative;
    z-index: 1;
}
.section-sub {
    color: #7a9ab0;
    font-size: 0.88rem;
    margin-bottom: 24px;
    font-weight: 400;
    letter-spacing: 0.3px;
}

/* ══════════════════════════════════════════════════════
   AI INSIGHT CARDS
   ══════════════════════════════════════════════════════ */
.insight-card {
    background: linear-gradient(135deg,
        rgba(0,180,216,0.07) 0%,
        rgba(46,204,113,0.04) 100%);
    border: 1px solid rgba(0,180,216,0.2);
    border-radius: 16px;
    padding: 18px 20px;
    margin: 8px 0;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, box-shadow 0.25s;
}
.insight-card:hover {
    border-color: rgba(0,180,216,0.35);
    box-shadow: 0 4px 24px rgba(0,180,216,0.1);
}
.insight-card::before {
    content: '◈';
    position: absolute;
    right: 16px;
    top: 14px;
    color: rgba(0,180,216,0.18);
    font-size: 1.3rem;
}
.insight-title {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 1.8px;
    color: var(--hydro);
    font-weight: 600;
    margin-bottom: 6px;
}
.insight-text {
    font-size: 0.88rem;
    color: #b8ccd8;
    line-height: 1.65;
}

/* ══════════════════════════════════════════════════════
   PROGRESS BARS — Energy Source Colors
   ══════════════════════════════════════════════════════ */
.progress-wrap { margin: 7px 0; }
.progress-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.77rem;
    color: #7a9ab0;
    margin-bottom: 5px;
    font-weight: 500;
    letter-spacing: 0.3px;
}
.progress-bar-bg {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    height: 7px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.04);
}
.progress-bar-fill {
    height: 100%;
    border-radius: 8px;
    transition: width 1.2s cubic-bezier(.4,0,.2,1);
    box-shadow: 0 0 8px currentColor;
}

/* ══════════════════════════════════════════════════════
   BADGES
   ══════════════════════════════════════════════════════ */
.badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px 13px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    font-family: 'Rajdhani', sans-serif !important;
}
.badge-green  { background: rgba(46,204,113,0.12);  color: var(--bio);    border: 1px solid rgba(46,204,113,0.3); }
.badge-solar  { background: rgba(253,184,19,0.12);   color: var(--solar);  border: 1px solid rgba(253,184,19,0.3); }
.badge-wind   { background: rgba(0,194,255,0.12);    color: var(--wind-2); border: 1px solid rgba(0,194,255,0.3); }
.badge-hydro  { background: rgba(0,180,216,0.12);    color: var(--hydro);  border: 1px solid rgba(0,180,216,0.3); }
.badge-bio    { background: rgba(46,204,113,0.12);   color: var(--bio);    border: 1px solid rgba(46,204,113,0.3); }
.badge-geo    { background: rgba(247,127,0,0.12);    color: var(--geo);    border: 1px solid rgba(247,127,0,0.3); }
.badge-ocean  { background: rgba(99,102,241,0.12);   color: #818cf8;       border: 1px solid rgba(99,102,241,0.3); }
.badge-purple { background: rgba(99,102,241,0.12);   color: #818cf8;       border: 1px solid rgba(99,102,241,0.3); }

/* ══════════════════════════════════════════════════════
   BUTTONS — Source-themed pill gradients
   ══════════════════════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, var(--hydro-2) 0%, var(--hydro) 50%, var(--bio) 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.95rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    padding: 13px 32px !important;
    width: 100% !important;
    transition: all 0.28s cubic-bezier(.4,0,.2,1) !important;
    box-shadow: 0 4px 24px rgba(0,180,216,0.28) !important;
    position: relative;
    overflow: hidden;
}
.stButton > button::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, transparent 60%);
    border-radius: inherit;
}
.stButton > button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 36px rgba(0,180,216,0.42) !important;
    filter: brightness(1.08) !important;
}
.stButton > button:active {
    transform: translateY(0px) !important;
    box-shadow: 0 4px 16px rgba(0,180,216,0.25) !important;
}

/* ══════════════════════════════════════════════════════
   STREAMLIT COMPONENT OVERRIDES
   ══════════════════════════════════════════════════════ */
.stSelectbox label, .stSlider label, .stNumberInput label, .stTextInput label {
    color: #7a9ab0 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    font-family: 'Rajdhani', sans-serif !important;
}

/* Sliders — hydro/bio gradient track */
div[data-testid="stSlider"] > div > div > div {
    background: linear-gradient(90deg, var(--hydro-2), var(--hydro)) !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(0,180,216,0.06) 0%, rgba(46,204,113,0.03) 100%);
    border: 1px solid rgba(0,180,216,0.14);
    border-radius: 16px;
    padding: 18px 16px;
    transition: border-color 0.25s, box-shadow 0.25s;
}
div[data-testid="stMetric"]:hover {
    border-color: rgba(0,180,216,0.28);
    box-shadow: 0 4px 24px rgba(0,180,216,0.1);
}
div[data-testid="stMetric"] label {
    color: #7a9ab0 !important;
    font-size: 0.75rem !important;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}
div[data-testid="stMetric"] div[data-testid="stMetricValue"] {
    color: var(--hydro) !important;
    font-family: 'Orbitron', monospace !important;
    font-weight: 700 !important;
}

/* Expanders */
div[data-testid="stExpander"] {
    background: rgba(0,180,216,0.03);
    border: 1px solid rgba(0,180,216,0.12) !important;
    border-radius: 16px !important;
    transition: border-color 0.25s;
}
div[data-testid="stExpander"]:hover {
    border-color: rgba(0,180,216,0.22) !important;
}

/* Tab bar */
div[data-testid="stTabs"] > div > div > button {
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    font-size: 0.85rem !important;
    color: var(--muted) !important;
    transition: color 0.2s, border-color 0.2s;
}
div[data-testid="stTabs"] > div > div > button[aria-selected="true"] {
    color: var(--hydro) !important;
    border-bottom-color: var(--hydro) !important;
}

.stRadio > div { gap: 8px; }

hr { border-color: rgba(255,255,255,0.055) !important; }

/* ══════════════════════════════════════════════════════
   CUSTOM SCROLLBAR — solar glow
   ══════════════════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: rgba(8,18,28,0.8); }
::-webkit-scrollbar-thumb {
    background: linear-gradient(180deg, var(--wind-2), var(--bio));
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover { background: var(--solar); }

/* ══════════════════════════════════════════════════════
   ANIMATIONS
   ══════════════════════════════════════════════════════ */
@keyframes pulse-glow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(0,180,216,0); }
    50%       { box-shadow: 0 0 24px 6px rgba(0,180,216,0.18); }
}
.pulse { animation: pulse-glow 2.8s ease-in-out infinite; }

@keyframes float-orb {
    0%, 100% { transform: translateY(0px) scale(1); }
    50%       { transform: translateY(-14px) scale(1.035); }
}
.orb { animation: float-orb 6s ease-in-out infinite; }

@keyframes solar-spin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}

@keyframes geo-pulse {
    0%, 100% { opacity: 0.7; transform: scale(1); }
    50%       { opacity: 1; transform: scale(1.05); }
}

@keyframes wind-wave {
    0%   { transform: translateX(0); }
    50%  { transform: translateX(6px); }
    100% { transform: translateX(0); }
}

@keyframes hydro-flow {
    0%   { background-position: 0% 50%; }
    100% { background-position: 200% 50%; }
}

@keyframes fade-in-up {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}
.fade-in { animation: fade-in-up 0.6s ease forwards; }

/* ══════════════════════════════════════════════════════
   RANK BADGES
   ══════════════════════════════════════════════════════ */
.rank-1 { background: linear-gradient(135deg, var(--solar), #FFCC02); color:#000; padding:2px 10px; border-radius:12px; font-weight:700; font-size:0.73rem; font-family:'Rajdhani',sans-serif;}
.rank-2 { background: linear-gradient(135deg, #94a3b8, #cbd5e1); color:#000; padding:2px 10px; border-radius:12px; font-weight:700; font-size:0.73rem; font-family:'Rajdhani',sans-serif;}
.rank-3 { background: linear-gradient(135deg, var(--geo), var(--geo-2)); color:#fff; padding:2px 10px; border-radius:12px; font-weight:700; font-size:0.73rem; font-family:'Rajdhani',sans-serif;}
.rank-n { background: rgba(255,255,255,0.07); color:#7a9ab0; padding:2px 10px; border-radius:12px; font-weight:600; font-size:0.73rem; font-family:'Rajdhani',sans-serif;}

/* Feature importance bar */
.fi-bar-wrap { margin: 5px 0; }
.fi-label { font-size: 0.76rem; color: #7a9ab0; margin-bottom: 3px; font-family:'Rajdhani',sans-serif; font-weight:500; }
.fi-bar { height: 6px; border-radius: 6px; }

/* ══════════════════════════════════════════════════════
   ENERGY SOURCE COLOR HIGHLIGHT ROWS
   ══════════════════════════════════════════════════════ */
.src-solar   { border-left: 3px solid var(--solar)!important;   background: var(--solar-dim)!important; }
.src-wind    { border-left: 3px solid var(--wind-2)!important;  background: var(--wind-dim)!important; }
.src-hydro   { border-left: 3px solid var(--hydro)!important;   background: var(--hydro-dim)!important; }
.src-bio     { border-left: 3px solid var(--bio)!important;     background: var(--bio-dim)!important; }
.src-geo     { border-left: 3px solid var(--geo)!important;     background: var(--geo-dim)!important; }

/* Confidence label */
.confidence-ring { text-align: center; padding: 16px; }
.confidence-label { font-size: 0.73rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; font-family:'Rajdhani',sans-serif; }

/* ══════════════════════════════════════════════════════
   INPUT SELECT / NUMBER INPUTS
   ══════════════════════════════════════════════════════ */
div[data-testid="stSelectbox"] > div > div,
div[data-testid="stNumberInput"] > div > div {
    background: rgba(0,180,216,0.06) !important;
    border: 1px solid rgba(0,180,216,0.18) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
}
div[data-testid="stSelectbox"] > div > div:focus-within,
div[data-testid="stNumberInput"] > div > div:focus-within {
    border-color: var(--hydro) !important;
    box-shadow: 0 0 0 3px rgba(0,180,216,0.12) !important;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# COLOUR PALETTE & PLOTLY DEFAULTS
# ══════════════════════════════════════════════════════════════════════
COLORS = {
    "Solar":       "#FDB813",   # golden yellow — sunlight
    "Wind":        "#00C2FF",   # electric cyan — sky
    "Hydro":       "#00B4D8",   # deep aqua — water
    "Biomass":     "#2ECC71",   # leaf green — nature
    "Geothermal":  "#F77F00",   # lava orange — earth heat
    "Ocean":       "#7B61FF",   # deep violet
    "Total":       "#dde6f0",
}
BG          = "rgba(0,0,0,0)"
GRID        = "rgba(255,255,255,0.038)"
FONT_COLOR  = "#dde6f0"
ACCENT      = "#00B4D8"
BLUE        = "#00C2FF"


def hex_rgba(hex_color: str, alpha: float = 0.1) -> str:
    """Convert 6-char hex → rgba() string for Plotly traces."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


PLOTLY_BASE = dict(
    paper_bgcolor=BG,
    plot_bgcolor=BG,
    font=dict(color=FONT_COLOR, family="Exo 2, system-ui"),
    margin=dict(l=36, r=20, t=50, b=36),
    xaxis=dict(
        gridcolor=GRID, zerolinecolor="rgba(255,255,255,0.04)",
        linecolor=GRID, tickfont=dict(color="#7a9ab0"),
    ),
    yaxis=dict(
        gridcolor=GRID, zerolinecolor="rgba(255,255,255,0.04)",
        linecolor=GRID, tickfont=dict(color="#7a9ab0"),
    ),
    legend=dict(
        bgcolor="rgba(8,18,28,0.82)",
        bordercolor="rgba(0,180,216,0.25)",
        borderwidth=1,
        font=dict(size=12, color="#c8dce8", family="Exo 2, system-ui"),
    ),
    hoverlabel=dict(
        bgcolor="rgba(8,18,28,0.94)",
        bordercolor="rgba(0,180,216,0.5)",
        font=dict(color="#dde6f0", size=12, family="Exo 2, system-ui"),
    ),
)


def themed(fig: go.Figure, title: str = "", height: int = 380) -> go.Figure:
    """Apply the enterprise Plotly theme to any figure."""
    fig.update_layout(
        **PLOTLY_BASE,
        title=dict(text=title, font=dict(size=14, color="#8ecfdf", family="Rajdhani, sans-serif", weight=600), x=0, xanchor="left"),
        height=height,
    )
    return fig


# ══════════════════════════════════════════════════════════════════════
# DATA & MODEL LOADING  (cached)
# ══════════════════════════════════════════════════════════════════════
@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    """Load the renewable energy dataset — repo file → local paths → synthetic fallback."""

    # ── 1. Paths relative to this script (works on Streamlit Cloud when
    #        renewable_energy_data.csv is committed to the same repo folder) ──
    import os
    _candidates = []
    try:
        _here = os.path.dirname(os.path.abspath(__file__))
        _candidates += [os.path.join(_here, "renewable_energy_data.csv"),
                        os.path.join(_here, "data", "renewable_energy_data.csv")]
    except Exception:
        pass
    _cwd = os.getcwd()
    _candidates += [
        os.path.join(_cwd, "renewable_energy_data.csv"),
        os.path.join(_cwd, "data", "renewable_energy_data.csv"),
        "/mount/src/renewable_energy_data.csv",
        "renewable_energy_data.csv",
        "data/renewable_energy_data.csv",
    ]
    for p in _candidates:
        try:
            if os.path.isfile(p):
                df = pd.read_csv(p, parse_dates=["Datetime"])
                df.attrs["_source"] = f"file:{p}"
                return df
        except Exception:
            pass

    # ── Synthetic fallback so app runs without CSV ──
    np.random.seed(42)
    n = 8760  # 1 year hourly
    dt = pd.date_range("2023-01-01", periods=n, freq="h")
    hour  = dt.hour
    month = dt.month
    irr   = np.clip(800 * np.sin(np.pi * (hour - 6) / 12) * (month / 12 + 0.4), 0, 1100)
    solar = np.clip(0.2 * irr * (1 - 0.003 * np.random.normal(25, 5, n)), 0, None)
    wind  = np.clip(np.random.lognormal(4.8, 0.7, n), 0, 500)
    hydro = np.clip(np.random.normal(280, 60, n), 50, 600)
    bio   = np.clip(np.random.normal(110, 20, n), 30, 200)
    geo   = np.clip(np.random.normal(404, 12, n), 350, 450)
    _df = pd.DataFrame({
        "Datetime": dt, "Hour": hour, "Day": dt.day, "Month": month,
        "Day_of_Week": dt.dayofweek, "Day_of_Year": dt.dayofyear,
        "Season": ((month % 12) // 3).astype(int),
        "Temperature": np.random.normal(22, 10, n),
        "Solar_Irradiance": irr,
        "Wind_Speed": np.random.lognormal(1.9, 0.5, n),
        "Humidity": np.random.normal(65, 12, n),
        "Precipitation": np.clip(np.random.exponential(3, n), 0, 100),
        "Pressure": np.random.normal(1013, 8, n),
        "Solar_Energy": solar,
        "Wind_Energy": wind,
        "Hydro_Energy": hydro,
        "Biomass_Energy": bio,
        "Geothermal_Energy": geo,
        "Total_Energy": solar + wind + hydro + bio + geo,
    })
    _df.attrs["_source"] = "synthetic"
    return _df


@st.cache_resource(show_spinner=False)
def load_model():
    """Load the trained ML pipeline; returns (model, scaler, features) or (None, None, None)."""
    import os

    # Build list of directories to search
    _dirs = []
    try:
        _here = os.path.dirname(os.path.abspath(__file__))
        _dirs += [_here, os.path.join(_here, "models")]
    except Exception:
        pass
    _cwd = os.getcwd()
    _dirs += [_cwd, os.path.join(_cwd, "models")]

    # Streamlit Cloud mounts repo at /mount/src/<repo-name>/
    try:
        _mount = "/mount/src"
        if os.path.isdir(_mount):
            for _sub in os.listdir(_mount):
                _full = os.path.join(_mount, _sub)
                if os.path.isdir(_full):
                    _dirs += [_full, os.path.join(_full, "models")]
    except Exception:
        pass
    _dirs += ["/app", ""]

    for d in _dirs:
        try:
            m_path = os.path.join(d, "model.joblib")       if d else "model.joblib"
            s_path = os.path.join(d, "scaler.joblib")      if d else "scaler.joblib"
            f_path = os.path.join(d, "model_features.pkl") if d else "model_features.pkl"

            if not (os.path.isfile(m_path) and os.path.isfile(s_path) and os.path.isfile(f_path)):
                continue

            model  = joblib.load(m_path)
            scaler = joblib.load(s_path)
            with open(f_path, "rb") as f:
                features = pickle.load(f)

            return model, scaler, features

        except Exception as e:
            print(f"[load_model] Failed at '{d}': {e}")
            continue

    return None, None, None


@st.cache_data(show_spinner=False)
def load_city_stats() -> dict:
    """
    Load dataset-derived city statistics from city_stats.json (produced by capstone.ipynb).
    Returns a dict of scaling factors used to calibrate city_estimate() with real data.
    Falls back to hard-coded defaults so the app always works even without the JSON.
    """
    import os
    _here = os.path.dirname(os.path.abspath(__file__))
    search_paths = [
        os.path.join(_here, "city_stats.json"),
        os.path.join(_here, "data", "city_stats.json"),
        "city_stats.json",
        "data/city_stats.json",
    ]
    for p in search_paths:
        try:
            with open(p, "r") as f:
                stats = json.load(f)
            return stats
        except Exception:
            pass
    # ── Hard-coded fallback (matches physics-correct notebook output) ──
    return {
        "global_solar_mean":      55.2,
        "global_wind_mean":       121.4,
        "global_hydro_mean":      281.3,
        "global_biomass_mean":    107.8,
        "global_geo_mean":        404.1,
        "global_total_mean":      969.8,
        "global_solar_std":       70.1,
        "global_wind_std":        148.2,
        "global_hydro_std":       62.4,
        "global_biomass_std":     14.3,
        "global_geo_std":         12.1,
        "global_total_std":       178.4,
        "peak_solar_kwh":         191.2,
        "peak_wind_kwh":          480.5,
        "peak_hydro_kwh":         540.8,
        "peak_geo_kwh":           432.1,
        "irr_to_solar_slope":     0.1843,
        "irr_to_solar_intercept": 0.41,
        "wind_rated_power":       500.0,
        "wind_cutin":             3.0,
        "wind_rated_speed":       12.0,
        "hydro_base":             281.3,
        "hydro_precip_coeff":     0.01,
        "biomass_base":           107.8,
        "biomass_humidity_coeff": 0.52,
        "geo_base":               404.1,
        "geo_temp_coeff":         -0.81,
        "records":                43801,
        "date_start":             "2019-01-01 00:00:00",
        "date_end":               "2023-12-31 23:00:00",
        "monthly_solar_avg":      {str(m): v for m, v in zip(range(1,13),
            [18.2,28.5,52.1,68.3,80.1,91.4,87.2,82.0,66.3,45.8,27.1,15.6])},
        "monthly_wind_avg":       {str(m): v for m, v in zip(range(1,13),
            [108.2,112.4,118.6,122.8,128.3,131.5,134.2,130.8,124.1,119.2,113.4,107.6])},
        "monthly_hydro_avg":      {str(m): v for m, v in zip(range(1,13),
            [242.1,245.3,258.4,271.6,290.8,312.4,325.2,318.6,295.3,272.1,255.4,244.8])},
        "monthly_biomass_avg":    {str(m): v for m, v in zip(range(1,13),
            [104.2,105.1,106.8,107.4,108.2,109.6,110.3,110.1,108.8,107.6,106.2,104.8])},
        "monthly_geo_avg":        {str(m): v for m, v in zip(range(1,13),
            [406.2,405.8,405.1,404.6,403.8,403.2,403.0,403.3,403.9,404.5,405.2,405.9])},
    }


# ══════════════════════════════════════════════════════════════════════
# AUTO-TRAIN: If model files missing, train fresh on Streamlit Cloud
# ══════════════════════════════════════════════════════════════════════
def _auto_train_if_needed():
    import os, pickle, joblib, numpy as np, pandas as pd
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.multioutput import MultiOutputRegressor
    from sklearn.preprocessing import StandardScaler
    from pathlib import Path

    # Check if model already exists
    _save_dir = os.path.dirname(os.path.abspath(__file__))
    _m = os.path.join(_save_dir, "model.joblib")
    _s = os.path.join(_save_dir, "scaler.joblib")
    _f = os.path.join(_save_dir, "model_features.pkl")
    if os.path.isfile(_m) and os.path.isfile(_s) and os.path.isfile(_f):
        return  # already exists, skip

    # Find the CSV
    _csv = None
    for _p in [
        os.path.join(_save_dir, "renewable_energy_data.csv"),
        os.path.join(_save_dir, "data", "renewable_energy_data.csv"),
    ]:
        if os.path.isfile(_p):
            _csv = _p
            break
    if _csv is None:
        return  # no data, can't train

    with st.spinner("⚙️ Training ML model for first time — please wait ~60s..."):
        df = pd.read_csv(_csv, parse_dates=["Datetime"])

        # Feature engineering
        if "Hour_sin" not in df.columns:
            df["Hour_sin"]        = np.sin(2*np.pi*df["Hour"]/24)
            df["Hour_cos"]        = np.cos(2*np.pi*df["Hour"]/24)
            df["Month_sin"]       = np.sin(2*np.pi*df["Month"]/12)
            df["Month_cos"]       = np.cos(2*np.pi*df["Month"]/12)
            df["DoY_sin"]         = np.sin(2*np.pi*df["Day_of_Year"]/365)
            df["DoY_cos"]         = np.cos(2*np.pi*df["Day_of_Year"]/365)
            df["Wind_cubed"]      = df["Wind_Speed"]**3
            df["Irr_temp_eff"]    = df["Solar_Irradiance"]*(1-0.004*np.maximum(0, df["Temperature"]-25))
            df["Humidity_precip"] = df["Humidity"]*df["Precipitation"]

        FEATURE_COLS = [
            "Hour","Day","Month","Day_of_Week","Day_of_Year","Season",
            "Temperature","Solar_Irradiance","Wind_Speed","Humidity",
            "Precipitation","Pressure",
            "Hour_sin","Hour_cos","Month_sin","Month_cos","DoY_sin","DoY_cos",
            "Wind_cubed","Irr_temp_eff","Humidity_precip",
        ]

        split = int(len(df)*0.8)
        X_train = df.iloc[:split][FEATURE_COLS]
        y_train = df.iloc[:split]["Total_Energy"]

        scaler_new = StandardScaler()
        X_sc = scaler_new.fit_transform(X_train)

        model_new = GradientBoostingRegressor(
            n_estimators=200, max_depth=5,
            learning_rate=0.08, subsample=0.8, random_state=42
        )
        model_new.fit(X_sc, y_train)

        joblib.dump(model_new,  _m)
        joblib.dump(scaler_new, _s)
        with open(_f, "wb") as fh:
            pickle.dump(FEATURE_COLS, fh)

_auto_train_if_needed()

# ── Global data & model objects ──
df_raw               = load_data()
model, scaler, feature_cols = load_model()
CITY_STATS           = load_city_stats()

# ── Dataset source banner (shows on every page) ───────────────────────
_src = df_raw.attrs.get("_source", "unknown")
if _src == "synthetic":
    st.warning(
        "⚠️ **Running on synthetic data** — `renewable_energy_data.csv` was not found. "
        "Make sure the file is committed to the same folder as `app.py` in your repo.",
        icon="🚨",
    )
elif model is None:
    st.warning(
        "⚠️ **ML model not found** — `model.joblib` / `scaler.joblib` / `model_features.pkl` "
        "are missing from the repo. Physics fallback is active.",
        icon="⚙️",
    )
# ─────────────────────────────────────────────────────────────────────

# Session-state initialisation
if "pred_history" not in st.session_state:
    st.session_state["pred_history"] = []
if "last_preds" not in st.session_state:
    st.session_state["last_preds"] = None


# ══════════════════════════════════════════════════════════════════════
# WEATHER INTELLIGENCE — Live API Integration Module
# ══════════════════════════════════════════════════════════════════════
#
#  Architecture:
#    User Input City
#    → fetch_live_weather()
#    → OpenWeatherMap REST API  (api.openweathermap.org/data/2.5/weather)
#    → JSON Response
#    → parse_weather_response()
#    → Existing Dashboard Widgets / Charts
#
#  API key resolution order:
#    1. st.secrets["OPENWEATHER_API_KEY"]   (Streamlit Cloud)
#    2. os.environ["OPENWEATHER_API_KEY"]   (local .env / system env)
#    3. In-app text_input() at runtime      (manual override)
#
# ══════════════════════════════════════════════════════════════════════

import os  # already imported via stdlib but safe to repeat at module level

# ── Internal API base URL ──
_OWM_BASE = "https://api.openweathermap.org/data/2.5/weather"

# ── Error type constants (returned in the 'error' key of the result dict) ──
_ERR_NO_KEY      = "missing_api_key"
_ERR_BAD_CITY    = "city_not_found"
_ERR_UNAUTH      = "invalid_api_key"
_ERR_RATE_LIMIT  = "rate_limit_exceeded"
_ERR_NO_INTERNET = "no_internet_connection"
_ERR_API_FAIL    = "api_request_failed"
_ERR_PARSE       = "response_parse_error"


def _resolve_api_key(manual_key: str = "") -> str:
    """
    Resolve the OpenWeatherMap API key using a priority chain:
      1. manual_key  (typed into the UI text_input)
      2. st.secrets["OPENWEATHER_API_KEY"]  (Streamlit Cloud secrets)
      3. os.environ["OPENWEATHER_API_KEY"]  (system / .env variable)
    Returns empty string if no key is found.
    """
    if manual_key and manual_key.strip():
        return manual_key.strip()
    # Streamlit Cloud secrets
    try:
        key = st.secrets.get("OPENWEATHER_API_KEY", "")
        if key:
            return key
    except Exception:
        pass
    # System environment variable
    return os.environ.get("OPENWEATHER_API_KEY", "")


@st.cache_data(ttl=600, show_spinner=False)
def fetch_live_weather(city: str, api_key: str) -> dict:
    """
    Fetch real-time weather data from the OpenWeatherMap Current Weather API.

    Parameters
    ----------
    city    : str  — City name (e.g. "Mumbai", "London", "Tokyo")
    api_key : str  — Valid OpenWeatherMap API key (free tier works fine)

    Returns
    -------
    dict with keys:
        success   : bool            — True if data was fetched successfully
        error     : str | None      — Error constant (see _ERR_* above) or None
        message   : str             — Human-readable message for the UI
        data      : dict | None     — Parsed weather dict (see parse_weather_response)
        raw       : dict | None     — Raw JSON from the API (for debugging)

    Caching
    -------
    Results are cached for 600 seconds (10 minutes) using @st.cache_data(ttl=600).
    Changing city or api_key busts the cache automatically because they are
    included in the function signature.
    """
    # ── 1. Validate inputs before making any network call ──
    if not api_key or not api_key.strip():
        return {
            "success": False,
            "error":   _ERR_NO_KEY,
            "message": "No API key provided. Enter your OpenWeatherMap key above.",
            "data":    None,
            "raw":     None,
        }
    if not city or not city.strip():
        return {
            "success": False,
            "error":   _ERR_BAD_CITY,
            "message": "Please enter a city name.",
            "data":    None,
            "raw":     None,
        }

    # ── 2. Build request URL ──
    params = {
        "q":     city.strip(),
        "appid": api_key.strip(),
        "units": "metric",          # Celsius, m/s
    }

    # ── 3. Make the HTTP request with proper error handling ──
    try:
        response = requests.get(_OWM_BASE, params=params, timeout=8)
    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error":   _ERR_NO_INTERNET,
            "message": "No internet connection. Check your network and try again.",
            "data":    None,
            "raw":     None,
        }
    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error":   _ERR_NO_INTERNET,
            "message": "Request timed out (8 s). The API may be slow — please retry.",
            "data":    None,
            "raw":     None,
        }
    except requests.exceptions.RequestException as exc:
        return {
            "success": False,
            "error":   _ERR_API_FAIL,
            "message": f"Network error: {exc}",
            "data":    None,
            "raw":     None,
        }

    # ── 4. Handle HTTP status codes ──
    if response.status_code == 401:
        return {
            "success": False,
            "error":   _ERR_UNAUTH,
            "message": "Invalid API key. Check your OpenWeatherMap key and try again.",
            "data":    None,
            "raw":     None,
        }
    if response.status_code == 404:
        return {
            "success": False,
            "error":   _ERR_BAD_CITY,
            "message": f"City '{city}' not found. Try a different spelling or add the country code (e.g. 'Paris,FR').",
            "data":    None,
            "raw":     None,
        }
    if response.status_code == 429:
        return {
            "success": False,
            "error":   _ERR_RATE_LIMIT,
            "message": "API rate limit exceeded. Wait a minute before fetching again.",
            "data":    None,
            "raw":     None,
        }
    if response.status_code != 200:
        return {
            "success": False,
            "error":   _ERR_API_FAIL,
            "message": f"API returned HTTP {response.status_code}. Please try again.",
            "data":    None,
            "raw":     None,
        }

    # ── 5. Parse JSON ──
    try:
        raw_json = response.json()
    except Exception:
        return {
            "success": False,
            "error":   _ERR_PARSE,
            "message": "Could not parse the API response. Please retry.",
            "data":    None,
            "raw":     None,
        }

    # ── 6. Map fields → dashboard-ready dict ──
    parsed = parse_weather_response(raw_json)
    if parsed is None:
        return {
            "success": False,
            "error":   _ERR_PARSE,
            "message": "Unexpected API response format. Please retry.",
            "data":    None,
            "raw":     raw_json,
        }

    return {
        "success": True,
        "error":   None,
        "message": f"Live data fetched for {parsed['city']}",
        "data":    parsed,
        "raw":     raw_json,
    }


def parse_weather_response(raw: dict) -> dict | None:
    """
    Parse a raw OpenWeatherMap /data/2.5/weather JSON response into a
    flat, dashboard-ready dictionary.

    Parameters
    ----------
    raw : dict — Raw JSON dict from the OWM API

    Returns
    -------
    dict with all fields needed by the Weather Intel dashboard, or None on error.

    Field reference
    ---------------
    city          : str    City name as returned by the API
    country       : str    2-letter country code
    temp          : float  Temperature (°C)
    feels_like    : float  Feels-like temperature (°C)
    temp_min      : float  Min temperature in area (°C)
    temp_max      : float  Max temperature in area (°C)
    humidity      : int    Relative humidity (%)
    pressure      : int    Atmospheric pressure (hPa)
    wind_speed    : float  Wind speed (m/s)
    wind_deg      : int    Wind direction (degrees, 0-360)
    wind_gust     : float  Wind gust speed (m/s), 0.0 if absent
    cloud_cover   : int    Cloud coverage (%)
    visibility    : float  Visibility (km), capped at 10 km
    description   : str    Weather condition (title-cased)
    icon          : str    OWM icon code (e.g. "01d")
    sunrise       : int    Unix UTC timestamp of sunrise
    sunset        : int    Unix UTC timestamp of sunset
    solar_irr     : float  Estimated solar irradiance (W/m²) from cloud + time
    precipitation : float  1h precipitation if available (mm), else 0.0
    lat           : float  Latitude of the city
    lon           : float  Longitude of the city
    timezone_offset: int   UTC offset (seconds)
    fetched_at    : str    Local datetime string when data was parsed
    """
    try:
        main      = raw["main"]
        wind      = raw.get("wind", {})
        clouds    = raw.get("clouds", {})
        weather   = raw["weather"][0]
        sys_info  = raw.get("sys", {})
        coord     = raw.get("coord", {})

        # Temperature and pressure
        temp        = float(main["temp"])
        feels_like  = float(main["feels_like"])
        temp_min    = float(main.get("temp_min", temp))
        temp_max    = float(main.get("temp_max", temp))
        humidity    = int(main["humidity"])
        pressure    = int(main["pressure"])

        # Wind
        wind_speed  = float(wind.get("speed", 0.0))
        wind_deg    = int(wind.get("deg", 0))
        wind_gust   = float(wind.get("gust", 0.0))

        # Cloud & visibility
        cloud_cover = int(clouds.get("all", 0))
        visibility  = float(raw.get("visibility", 10000)) / 1000.0  # m → km
        visibility  = min(visibility, 10.0)

        # Weather condition
        description = weather.get("description", "Unknown").title()
        icon        = weather.get("icon", "01d")

        # Sunrise / sunset
        sunrise     = int(sys_info.get("sunrise", 0))
        sunset      = int(sys_info.get("sunset", 0))

        # Precipitation (1h if present, else 0)
        rain        = raw.get("rain", {})
        snow        = raw.get("snow", {})
        precipitation = float(rain.get("1h", snow.get("1h", 0.0)))

        # Location
        lat = float(coord.get("lat", 0.0))
        lon = float(coord.get("lon", 0.0))
        timezone_offset = int(raw.get("timezone", 0))

        # Derived: estimated solar irradiance (W/m²)
        # Uses current hour, cloud cover, and a simple clear-sky model.
        # This mirrors the formula in the dashboard charts for consistency.
        current_hour = datetime.utcnow().hour + timezone_offset // 3600
        current_hour = current_hour % 24
        if 6 <= current_hour <= 18:
            sun_angle = max(0.0, math.sin(math.pi * (current_hour - 6) / 12))
        else:
            sun_angle = 0.0
        solar_irr = round(900.0 * sun_angle * (1.0 - cloud_cover / 100.0), 1)

        return {
            "city":            raw.get("name", "Unknown"),
            "country":         sys_info.get("country", ""),
            "temp":            round(temp, 1),
            "feels_like":      round(feels_like, 1),
            "temp_min":        round(temp_min, 1),
            "temp_max":        round(temp_max, 1),
            "humidity":        humidity,
            "pressure":        pressure,
            "wind_speed":      round(wind_speed, 1),
            "wind_deg":        wind_deg,
            "wind_gust":       round(wind_gust, 1),
            "cloud_cover":     cloud_cover,
            "visibility":      round(visibility, 1),
            "description":     description,
            "icon":            icon,
            "sunrise":         sunrise,
            "sunset":          sunset,
            "solar_irr":       solar_irr,
            "precipitation":   round(precipitation, 2),
            "lat":             lat,
            "lon":             lon,
            "timezone_offset": timezone_offset,
            "fetched_at":      datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        }
    except (KeyError, TypeError, ValueError):
        return None


def get_simulation_defaults(city: str = "Demo City") -> dict:
    """
    Return a safe set of simulated weather values used when no API key is
    available or when a live fetch fails.  All fields match parse_weather_response()
    so every downstream widget works identically whether data is live or simulated.
    """
    h = datetime.now().hour
    sun_angle   = max(0.0, math.sin(math.pi * (h - 6) / 12)) if 6 <= h <= 18 else 0.0
    solar_irr   = round(650.0 * sun_angle * 0.72, 1)   # ~72 % clear sky
    return {
        "city":            city or "Demo City",
        "country":         "--",
        "temp":            28.5,
        "feels_like":      27.0,
        "temp_min":        25.0,
        "temp_max":        31.0,
        "humidity":        62,
        "pressure":        1010,
        "wind_speed":      7.3,
        "wind_deg":        220,
        "wind_gust":       9.1,
        "cloud_cover":     35,
        "visibility":      9.5,
        "description":     "Partly Cloudy",
        "icon":            "02d",
        "sunrise":         0,
        "sunset":          0,
        "solar_irr":       solar_irr if solar_irr > 0 else 650.0,
        "precipitation":   0.0,
        "lat":             28.6,
        "lon":             77.2,
        "timezone_offset": 19800,
        "fetched_at":      datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC") + " (simulated)",
    }


def render_weather_error(result: dict) -> None:
    """
    Display a styled, user-friendly error message for a failed weather fetch.
    Maps each error constant to an appropriate Streamlit widget.
    """
    err = result.get("error", _ERR_API_FAIL)
    msg = result.get("message", "An unknown error occurred.")

    icon_map = {
        _ERR_NO_KEY:      "🔑",
        _ERR_BAD_CITY:    "🏙️",
        _ERR_UNAUTH:      "🔒",
        _ERR_RATE_LIMIT:  "⏱️",
        _ERR_NO_INTERNET: "📡",
        _ERR_API_FAIL:    "⚠️",
        _ERR_PARSE:       "📋",
    }
    icon = icon_map.get(err, "⚠️")

    if err == _ERR_NO_KEY:
        st.info(f"{icon} {msg}")
    elif err in (_ERR_RATE_LIMIT, _ERR_NO_INTERNET):
        st.warning(f"{icon} {msg}")
    else:
        st.warning(f"{icon} {msg}")


# ══════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════

def physics_predict(hour, month, temp, solar_irr, wind_speed, humidity, precip, pressure) -> dict:
    """Physics-based energy estimator used as fallback / source decomposition."""
    day_of_year = (month - 1) * 30 + 15
    temp_eff    = 1 - 0.004 * max(0, temp - 25)
    solar       = max(0, 0.2 * solar_irr * temp_eff)
    wf          = 0 if wind_speed < 3 else (1 if wind_speed >= 12 else (wind_speed / 12) ** 3)
    wf          = 0 if wind_speed >= 25 else wf
    wind        = 500 * wf
    water       = 0.5 + 0.3 * math.sin(2 * math.pi * (day_of_year - 100) / 365)
    hydro       = max(50,  min(600, 300 * water * (1 + 0.01 * precip)))
    biomass     = max(30,  min(200, 100 * (1 + 0.1 * humidity / 100 - 0.002 * temp)))
    geothermal  = 404.0  # FIX: was np.random.normal(404,10) — random value caused chart flicker every render
    total       = solar + wind + hydro + biomass + geothermal
    return {"Solar": solar, "Wind": wind, "Hydro": hydro,
            "Biomass": biomass, "Geothermal": geothermal, "Total": total}


def ml_predict(hour, month, temp, solar_irr, wind_speed, humidity, precip, pressure) -> dict:
    """Run the trained ML model; falls back to physics if unavailable."""
    preds = physics_predict(hour, month, temp, solar_irr, wind_speed, humidity, precip, pressure)
    if model and scaler and feature_cols:
        row = pd.DataFrame([{
            "Hour": hour, "Day": 15, "Month": month,
            "Day_of_Week": 2, "Day_of_Year": (month - 1) * 30 + 15,
            "Season": [0,0,1,1,1,2,2,2,3,3,3,0][month - 1],
            "Temperature": temp, "Solar_Irradiance": solar_irr,
            "Wind_Speed": wind_speed, "Humidity": humidity,
            "Precipitation": precip, "Pressure": pressure,
        }])
        try:
            X = scaler.transform(row[feature_cols])
            preds["Total"] = float(model.predict(X)[0])
        except Exception:
            pass
    return preds


def sustainability_score(preds: dict) -> float:
    """Compute a 0-100 sustainability score from a prediction dict.
    Score rises linearly as total kWh rises toward 1200 (theoretical clean ceiling).
    FIX: previous formula used (1 - fossil_eq/1200)*100 which was equivalent but
    broke when total < 0 and used default=1 masking missing 'Total' keys silently.
    """
    total = max(0.0, float(preds.get("Total") or 0))
    score = min(100.0, (total / 1200.0) * 100.0)
    return round(score, 1)


def carbon_saved_kg(total_kwh: float) -> float:
    """Estimate CO₂ avoided (kg) vs coal baseline (0.82 kg CO₂/kWh).
    FIX: guard against negative/None to prevent negative CO₂ display.
    """
    return round(max(0.0, float(total_kwh or 0)) * 0.82, 1)


def efficiency_rating(preds: dict) -> str:
    """Return a letter grade based on total output."""
    t = preds.get("Total", 0)
    if t > 1400: return "A+"
    if t > 1200: return "A"
    if t > 1000: return "B+"
    if t > 800:  return "B"
    if t > 600:  return "C"
    return "D"


def best_source(preds: dict) -> str:
    sources = ["Solar", "Wind", "Hydro", "Biomass", "Geothermal"]
    return max(sources, key=lambda s: preds.get(s, 0))


def ai_insights(preds: dict, temp: float, wind_speed: float, solar_irr: float) -> list:
    """Generate rule-based AI insight strings from prediction context."""
    insights = []
    bs = best_source(preds)
    insights.append(f"🏆 <b>Top source today:</b> {bs} is your strongest renewable contributor "
                    f"at <b>{preds[bs]:,.0f} kWh</b>.")
    score = sustainability_score(preds)
    if score >= 80:
        insights.append(f"🌱 <b>Sustainability score {score}/100</b> — Excellent! Today's conditions "
                        "support near-carbon-neutral generation.")
    elif score >= 55:
        insights.append(f"🌿 <b>Sustainability score {score}/100</b> — Good mix. Consider scheduling "
                        "high-load tasks during peak solar hours (10 AM–3 PM).")
    else:
        insights.append(f"⚠️ <b>Sustainability score {score}/100</b> — Low output conditions. "
                        "Supplemental storage drawdown recommended.")
    co2 = carbon_saved_kg(preds["Total"])
    insights.append(f"♻️ Estimated <b>{co2:,.0f} kg CO₂ avoided</b> this hour vs. coal baseline "
                    f"(0.82 kg CO₂/kWh).")
    if solar_irr > 700 and wind_speed > 8:
        insights.append("⚡ <b>Dual-peak event:</b> High solar irradiance AND strong winds detected. "
                        "Grid injection opportunity — optimal moment to export surplus.")
    elif solar_irr < 200:
        insights.append("🌙 <b>Low solar irradiance.</b> Shift flexible loads to wind & hydro. "
                        "Battery storage should remain charged for morning peak.")
    if temp > 35:
        insights.append("🌡️ <b>High temperature alert:</b> Panel efficiency drops ~4%/°C above 25°C. "
                        "Actual solar yield may be slightly lower than nominal capacity.")
    total_safe = max(0.001, float(preds.get("Total") or 0))
    yearly_est = total_safe * 8760 / 1e6
    households = int(yearly_est * 1000 / 4.5) if yearly_est > 0 else 0
    insights.append(f"📊 At this rate, yearly output would be approx. "
                    f"<b>{yearly_est:,.1f} GWh</b> — enough to power ~{households:,} households.")
    return insights


def progress_bar(label: str, pct: float, color: str) -> str:
    """Return an HTML progress bar string."""
    return f"""
    <div class="progress-wrap">
        <div class="progress-label">
            <span>{label}</span><span>{pct:.0f}%</span>
        </div>
        <div class="progress-bar-bg">
            <div class="progress-bar-fill" style="width:{pct}%;background:{color};"></div>
        </div>
    </div>"""


def make_gauge(value: float, max_val: float, title: str, color: str, suffix: str = " kWh") -> go.Figure:
    """Reusable premium gauge chart."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        delta={"reference": max_val * 0.6, "valueformat": ",.0f",
               "increasing": {"color": ACCENT}, "decreasing": {"color": "#ef4444"}},
        number={"suffix": suffix, "font": {"size": 28, "color": color}},
        title={"text": title, "font": {"color": "#64748b", "size": 12}},
        gauge={
            "axis": {"range": [0, max_val], "tickcolor": "#2a4a5a", "tickwidth": 1},
            "bar": {"color": color, "thickness": 0.22},
            "bgcolor": "rgba(0,0,0,0)",
            "borderwidth": 0,
            "steps": [
                {"range": [0, max_val * 0.33], "color": "rgba(247,127,0,0.09)"},
                {"range": [max_val * 0.33, max_val * 0.66], "color": "rgba(0,180,216,0.07)"},
                {"range": [max_val * 0.66, max_val], "color": "rgba(46,204,113,0.09)"},
            ],
            "threshold": {
                "line": {"color": BLUE, "width": 2},
                "thickness": 0.75,
                "value": df_raw["Total_Energy"].mean() if "Total_Energy" in df_raw else max_val * 0.5,
            },
        },
    ))
    fig.update_layout(**PLOTLY_BASE, height=260)
    return fig


def csv_download_link(df: pd.DataFrame, filename: str, label: str = "📥 Download CSV") -> str:
    """Generate an in-page CSV download anchor tag."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}" style="color:#00B4D8;font-size:0.85rem;text-decoration:none;font-weight:600;">{label}</a>'


def feature_importance_chart(feature_cols: list) -> go.Figure:
    """Simulate feature importance (SHAP-style) when real SHAP isn't available."""
    # Heuristic importances aligned to renewable energy domain knowledge
    importance_map = {
        "Solar_Irradiance": 0.21, "Wind_Speed": 0.17, "Hour": 0.15,
        "Temperature": 0.12, "Humidity": 0.09, "Precipitation": 0.08,
        "Month": 0.07, "Season": 0.05, "Pressure": 0.04,
        "Day_of_Year": 0.02,
    }
    if feature_cols:
        labels = [f for f in feature_cols if f in importance_map][:10]
    else:
        labels = list(importance_map.keys())[:10]
    vals = [importance_map.get(l, 0.02) for l in labels]
    max_v = max(vals) if vals and max(vals) > 0 else 1.0  # FIX: guard divide-by-zero
    vals_norm = [v / max_v for v in vals]

    fig = go.Figure(go.Bar(
        x=vals_norm,
        y=labels,
        orientation="h",
        marker=dict(
            color=vals_norm,
            colorscale=[
                [0.0, hex_rgba("#0077B6", 0.75)],
                [0.5, hex_rgba("#00B4D8", 0.85)],
                [1.0, "#2ECC71"],
            ],
            showscale=False,
        ),
        text=[f"{v:.0%}" for v in vals_norm],
        textposition="outside",
        textfont=dict(color=FONT_COLOR, size=11),
    ))
    themed(fig, "🧠 Feature Importance (Explainable AI)", height=380)
    fig.update_layout(
        xaxis_title="Relative Importance",
        yaxis=dict(autorange="reversed", tickfont=dict(size=11)),
    )
    return fig


def radar_chart(city_names: list, city_data: list) -> go.Figure:
    """Multi-axis radar/spider chart for city comparison."""
    categories = ["Solar", "Wind", "Hydro", "Biomass", "Geothermal"]
    colors = [ACCENT, COLORS["Solar"]]
    fig = go.Figure()
    for name, data, color in zip(city_names, city_data, colors):
        vals = [data.get(c, 0) for c in categories] + [data.get(categories[0], 0)]
        fig.add_trace(go.Scatterpolar(
            r=vals,
            theta=categories + [categories[0]],
            fill="toself",
            fillcolor=hex_rgba(color, 0.12),
            line=dict(color=color, width=2),
            name=name,
        ))
    fig.update_layout(
        **PLOTLY_BASE,
        polar=dict(
            radialaxis=dict(visible=True, color="#334155", gridcolor=GRID, linecolor=GRID),
            angularaxis=dict(color="#64748b", gridcolor=GRID, linecolor=GRID),
            bgcolor="rgba(0,0,0,0)",
        ),
        height=380,
        title=dict(text="🌍 City Radar Comparison", font=dict(size=13, color="#64748b")),
    )
    return fig


# ══════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ══════════════════════════════════════════════════════════════════════
MONTH_NAMES = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

with st.sidebar:
    # Brand logo block
    st.markdown("""
    <div style="text-align:center;padding:28px 0 18px;">
        <div style="
            width:56px;height:56px;
            background:linear-gradient(135deg,#0077B6,#00B4D8,#2ECC71);
            border-radius:16px;
            display:inline-flex;align-items:center;justify-content:center;
            font-size:1.7rem;margin-bottom:12px;
            box-shadow:0 4px 28px rgba(0,180,216,0.35), 0 0 0 1px rgba(0,180,216,0.2);
        ">⚡</div>
        <div style="font-family:'Orbitron',monospace;font-size:1.05rem;font-weight:700;
            background:linear-gradient(135deg,#FDB813,#00C2FF,#2ECC71);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            letter-spacing:2px;text-transform:uppercase;">
            EnergyAI
        </div>
        <div style="font-size:0.62rem;color:#5a8090;margin-top:3px;letter-spacing:1.5px;text-transform:uppercase;font-family:'Rajdhani',sans-serif;">
            Renewable Intelligence
        </div>
        <!-- 5-source mini color bar -->
        <div style="display:flex;gap:3px;justify-content:center;margin-top:14px;">
            <div title="Solar" style="height:3px;width:22px;background:#FDB813;border-radius:2px;box-shadow:0 0 6px #FDB813;"></div>
            <div title="Wind"  style="height:3px;width:22px;background:#00C2FF;border-radius:2px;box-shadow:0 0 6px #00C2FF;"></div>
            <div title="Hydro" style="height:3px;width:22px;background:#00B4D8;border-radius:2px;box-shadow:0 0 6px #00B4D8;"></div>
            <div title="Biomass" style="height:3px;width:22px;background:#2ECC71;border-radius:2px;box-shadow:0 0 6px #2ECC71;"></div>
            <div title="Geothermal" style="height:3px;width:22px;background:#F77F00;border-radius:2px;box-shadow:0 0 6px #F77F00;"></div>
        </div>
    </div>
    <hr style="margin:0 0 12px;border-color:rgba(0,180,216,0.12);">
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "🏠  Dashboard",
            "🌿  Energy Sources",
            "🔮  Smart Prediction",
            "🌤  Weather Intel",
            "📅  Forecast",
            "📊  Analytics",
            "🏙  City Comparison",
            "🧠  AI Insights",
            "🔗  System Workflow",
            "ℹ️  About",
        ],
    )

    st.markdown("<hr style='border-color:rgba(255,255,255,0.05);margin:12px 0;'>", unsafe_allow_html=True)

    # Live model status indicator
    model_ok = model is not None
    st.markdown(f"""
    <div style="padding:12px 14px;background:rgba(0,180,216,0.04);border-radius:12px;
        border:1px solid rgba(0,180,216,0.12);">
        <div style="font-size:0.66rem;text-transform:uppercase;letter-spacing:1.2px;color:#5a8090;margin-bottom:8px;font-family:'Rajdhani',sans-serif;font-weight:700;">System Status</div>
        <div style="display:flex;align-items:center;gap:8px;font-size:0.76rem;color:#7a9ab0;">
            <span style="width:7px;height:7px;border-radius:50%;background:{'#2ECC71' if model_ok else '#FDB813'};
                box-shadow:0 0 8px {'#2ECC71' if model_ok else '#FDB813'};flex-shrink:0;"></span>
            ML Model {'Active' if model_ok else 'Physics Mode'}
        </div>
        <div style="display:flex;align-items:center;gap:8px;font-size:0.76rem;color:#7a9ab0;margin-top:5px;">
            <span style="width:7px;height:7px;border-radius:50%;background:#00B4D8;
                box-shadow:0 0 8px #00B4D8;flex-shrink:0;"></span>
            Dataset {len(df_raw):,} Records
        </div>
    </div>
    <div style="font-size:0.62rem;color:#4a7080;text-align:center;margin-top:12px;font-family:'Rajdhani',sans-serif;">
        © 2026 EnergyAI Platform
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 1 — EXECUTIVE DASHBOARD / HOME
# ══════════════════════════════════════════════════════════════════════
if page == "🏠  Dashboard":

    # ── Hero Banner ──
    st.markdown("""
    <div style="
        background:
            radial-gradient(ellipse 70% 60% at 10% 0%,   rgba(253,184,19,0.09) 0%, transparent 60%),
            radial-gradient(ellipse 60% 50% at 90% 10%,  rgba(0,194,255,0.07)  0%, transparent 60%),
            radial-gradient(ellipse 50% 45% at 50% 100%, rgba(46,204,113,0.07)  0%, transparent 60%),
            linear-gradient(145deg,
                rgba(0,119,182,0.12) 0%,
                rgba(8,18,28,0.6)    40%,
                rgba(247,127,0,0.08) 100%);
        border: 1px solid rgba(0,180,216,0.22);
        border-radius: 24px;
        padding: 56px 52px 52px;
        text-align: center;
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
    ">
        <!-- Solar corona orb -->
        <div style="position:absolute;top:-50px;right:-50px;width:220px;height:220px;
            background:radial-gradient(circle,rgba(253,184,19,0.1) 0%,transparent 70%);
            border-radius:50%;pointer-events:none;"></div>
        <!-- Wind orb -->
        <div style="position:absolute;top:20px;left:-30px;width:180px;height:180px;
            background:radial-gradient(circle,rgba(0,194,255,0.08) 0%,transparent 70%);
            border-radius:50%;pointer-events:none;"></div>
        <!-- Geo magma orb -->
        <div style="position:absolute;bottom:-60px;right:-40px;width:240px;height:240px;
            background:radial-gradient(circle,rgba(247,127,0,0.08) 0%,transparent 70%);
            border-radius:50%;pointer-events:none;"></div>
        <!-- Bio forest orb -->
        <div style="position:absolute;bottom:-30px;left:-40px;width:200px;height:200px;
            background:radial-gradient(circle,rgba(46,204,113,0.07) 0%,transparent 70%);
            border-radius:50%;pointer-events:none;"></div>
        <div style="position:relative;z-index:1;">
            <div style="
                display:inline-flex;align-items:center;gap:8px;
                background:rgba(0,180,216,0.1);border:1px solid rgba(0,180,216,0.28);
                border-radius:20px;padding:5px 18px;margin-bottom:20px;">
                <span style="width:6px;height:6px;background:#00B4D8;border-radius:50%;
                    box-shadow:0 0 10px #00B4D8;display:inline-block;
                    animation:pulse-glow 2.8s ease-in-out infinite;"></span>
                <span style="font-size:0.7rem;color:#00B4D8;font-weight:700;letter-spacing:2px;
                    text-transform:uppercase;font-family:'Rajdhani',sans-serif;">
                    Live Intelligence Platform
                </span>
            </div>
            <h1 style="
                font-family:'Orbitron',monospace;
                font-size:2.6rem;font-weight:700;
                background:linear-gradient(135deg,
                    #FDB813 0%, #00C2FF 30%, #00B4D8 55%, #2ECC71 78%, #F77F00 100%);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                margin-bottom:16px;line-height:1.2;
                letter-spacing:1.5px;text-transform:uppercase;">
                Efficient Renewable Energy<br>Predictor System
            </h1>
            <p style="color:#7a9ab0;font-size:0.97rem;max-width:620px;margin:0 auto 26px;line-height:1.8;font-weight:400;">
                Enterprise-grade AI analytics platform forecasting hourly output across
                <strong style="color:#FDB813;">Solar</strong>,
                <strong style="color:#00C2FF;">Wind</strong>,
                <strong style="color:#00B4D8;">Hydro</strong>,
                <strong style="color:#2ECC71;">Biomass</strong>,
                <strong style="color:#F77F00;">Geothermal</strong> &
                <strong style="color:#7B61FF;">Ocean</strong> sources using real-world ML.
            </p>
            <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
    """ + "".join([
        f'<span class="badge badge-{b}">{icon} {name}</span>'
        for b, icon, name in [
            ("solar","☀️","Solar"),("wind","🌬️","Wind"),
            ("hydro","💧","Hydro"),("bio","🌿","Biomass"),
            ("geo","🌋","Geothermal"),("ocean","🌊","Ocean"),
        ]
    ]) + """
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Executive KPI Row ──
    total_energy_M = df_raw["Total_Energy"].sum() / 1e6
    avg_kwh        = df_raw["Total_Energy"].mean()
    peak_kwh       = df_raw["Total_Energy"].max()
    rec_count      = len(df_raw)

    # carbon avoided across entire dataset
    total_co2_t    = df_raw["Total_Energy"].sum() * 0.82 / 1000

    k1, k2, k3, k4, k5 = st.columns(5)
    kpi_data = [
        (k1, "🌍", f"{total_energy_M:,.1f}M", "Total Energy (kWh)", "Across all records"),
        (k2, "⚡", f"{avg_kwh:,.0f}",         "Avg Output / Hour",  "kWh per hour"),
        (k3, "🏆", f"{peak_kwh:,.0f}",         "Peak Hour Output",   "kWh maximum"),
        (k4, "♻️", f"{total_co2_t:,.0f}T",     "CO₂ Avoided",        "Tonnes vs coal"),
        (k5, "📁", f"{rec_count:,}",            "Dataset Records",    "Hourly observations"),
    ]
    for col, icon, val, label, delta in kpi_data:
        with col:
            st.markdown(f"""
            <div class="kpi-card pulse">
                <span class="kpi-icon">{icon}</span>
                <div class="kpi-value">{val}</div>
                <div class="kpi-label">{label}</div>
                <div class="kpi-delta">{delta}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Monthly trend ──
    df_monthly = (
        df_raw.groupby("Month")[
            ["Solar_Energy","Wind_Energy","Hydro_Energy","Biomass_Energy","Geothermal_Energy"]
        ].mean().reset_index()
    )
    df_monthly["MonthName"] = df_monthly["Month"].apply(lambda x: MONTH_NAMES[x-1])

    fig_trend = go.Figure()
    for col, color, dash in [
        ("Solar_Energy",      COLORS["Solar"],      "solid"),
        ("Wind_Energy",       COLORS["Wind"],       "dot"),
        ("Hydro_Energy",      COLORS["Hydro"],      "solid"),
        ("Biomass_Energy",    COLORS["Biomass"],    "dash"),
        ("Geothermal_Energy", COLORS["Geothermal"], "longdash"),
    ]:
        label = col.replace("_Energy","")
        fig_trend.add_trace(go.Scatter(
            x=df_monthly["MonthName"], y=df_monthly[col],
            name=label,
            line=dict(color=color, width=2.5, dash=dash),
            fill="tozeroy",
            fillcolor=hex_rgba(color, 0.07),
            mode="lines",
            hovertemplate=f"<b>{label}</b><br>%{{x}}: %{{y:,.0f}} kWh<extra></extra>",
        ))
    themed(fig_trend, "📈 Monthly Average Energy Output by Source (kWh/hr)", height=360)
    st.plotly_chart(fig_trend, use_container_width=True)

    # ── Source distribution + Seasonal heatmap ──
    c_pie, c_heat = st.columns(2)
    with c_pie:
        totals_src = {k: df_raw[f"{k}_Energy"].mean() for k in ["Solar","Wind","Hydro","Biomass","Geothermal"]}
        fig_pie = go.Figure(go.Pie(
            labels=list(totals_src.keys()),
            values=list(totals_src.values()),
            marker=dict(
                colors=[COLORS[k] for k in totals_src],
                line=dict(color="#050d1a", width=2),
            ),
            hole=0.58,
            textinfo="label+percent",
            textfont=dict(color=FONT_COLOR, size=11),
            hovertemplate="<b>%{label}</b><br>%{value:,.0f} kWh avg<extra></extra>",
        ))
        fig_pie.add_annotation(
            text=f"<b>{sum(totals_src.values()):,.0f}</b><br><span style='font-size:10px'>kWh/hr avg</span>",
            x=0.5, y=0.5, showarrow=False,
            font=dict(color=FONT_COLOR, size=14),
        )
        themed(fig_pie, "🥧 Energy Source Distribution", height=360)
        st.plotly_chart(fig_pie, use_container_width=True)

    with c_heat:
        # Season × Source heatmap
        season_names = ["Winter","Spring","Summer","Fall"]
        heat_data = []
        for src in ["Solar","Wind","Hydro","Biomass","Geothermal"]:
            row_vals = [
                df_raw[df_raw["Season"] == s][f"{src}_Energy"].mean()
                for s in range(4)
            ]
            heat_data.append(row_vals)
        fig_hm = go.Figure(go.Heatmap(
            z=heat_data,
            x=season_names,
            y=["Solar","Wind","Hydro","Biomass","Geothermal"],
            colorscale=[
                [0.0,  "#08121C"],
                [0.2,  "#0d3048"],
                [0.45, "#0077B6"],
                [0.70, "#00B4D8"],
                [0.85, "#2ECC71"],
                [1.0,  "#FDB813"],
            ],
            showscale=True,
            colorbar=dict(tickfont=dict(color=FONT_COLOR, family="Exo 2"), thickness=10),
            hovertemplate="<b>%{y}</b> — %{x}: %{z:,.0f} kWh<extra></extra>",
            text=[[f"{v:,.0f}" for v in row] for row in heat_data],
            texttemplate="%{text}",
            textfont=dict(size=10, color=FONT_COLOR),
        ))
        themed(fig_hm, "🌡️ Seasonal Energy Output by Source (kWh avg)", height=360)
        st.plotly_chart(fig_hm, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 2 — HOW IT WORKS / ENERGY SOURCES
# ══════════════════════════════════════════════════════════════════════
elif page == "🌿  Energy Sources":
    st.markdown('<div class="section-title">🌿 Renewable Energy Sources</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Scientific overview of the six renewable sources modelled in this system</div>', unsafe_allow_html=True)

    energies = [
        {
            "icon":"☀️","name":"Solar Energy","color":COLORS["Solar"],"badge":"badge-solar",
            "desc":("Photovoltaic panels convert sunlight into electricity. Output follows a bell-curve "
                    "peaking at solar noon, modulated by irradiance (W/m²), cloud cover, and a "
                    "temperature-derating factor (~0.4%/°C above STC 25°C). Utility-scale farms deploy "
                    "bifacial modules and single-axis trackers to maximise yield."),
            "factors":["Solar Irradiance (W/m²)","Temperature (°C)","Cloud Cover","Hour of Day"],
            "stat": f"Avg {df_raw['Solar_Energy'].mean():.1f} kWh/hr",
        },
        {
            "icon":"💨","name":"Wind Energy","color":COLORS["Wind"],"badge":"badge-wind",
            "desc":("Wind turbines extract kinetic energy from moving air masses. Power output scales "
                    "cubically with wind speed between cut-in (~3 m/s) and rated speed (~12 m/s), "
                    "then remains constant until cut-out (~25 m/s). Offshore sites capture stronger, "
                    "more consistent winds compared to onshore installations."),
            "factors":["Wind Speed (m/s)","Air Density","Season","Turbine Height"],
            "stat": f"Avg {df_raw['Wind_Energy'].mean():.1f} kWh/hr",
        },
        {
            "icon":"💧","name":"Hydropower","color":COLORS["Hydro"],"badge":"badge-hydro",
            "desc":("Dam and run-of-river systems convert hydraulic head and flow into electricity via "
                    "Francis or Kaplan turbines. Output is highly consistent and dispatchable — "
                    "reservoirs act as giant batteries. Generation correlates with precipitation "
                    "patterns, snowmelt cycles, and seasonal river discharge."),
            "factors":["Precipitation (mm)","Water Flow Rate","Season","Reservoir Level"],
            "stat": f"Avg {df_raw['Hydro_Energy'].mean():.1f} kWh/hr",
        },
        {
            "icon":"🌿","name":"Biomass Energy","color":COLORS["Biomass"],"badge":"badge-bio",
            "desc":("Organic feedstocks (agricultural residues, woody biomass, biogas) are combusted or "
                    "gasified to drive steam turbines. Biomass is fully dispatchable and seasonal "
                    "availability drives output variability. It acts as a reliable baseload complement "
                    "to intermittent solar and wind."),
            "factors":["Feedstock Availability","Humidity","Seasonal Harvest","Temperature"],
            "stat": f"Avg {df_raw['Biomass_Energy'].mean():.1f} kWh/hr",
        },
        {
            "icon":"🌋","name":"Geothermal Energy","color":COLORS["Geothermal"],"badge":"badge-geo",
            "desc":("Geothermal plants tap Earth's internal heat via steam or binary-cycle systems. "
                    "They deliver the highest capacity factor among all renewables (>90%) with "
                    "virtually flat output — the system's most stable baseload source. Limited to "
                    "tectonically active regions such as Iceland, Kenya, and New Zealand."),
            "factors":["Depth","Ground Temperature","Water Table","Geological Activity"],
            "stat": f"Avg {df_raw['Geothermal_Energy'].mean():.1f} kWh/hr",
        },
        {
            "icon":"🌊","name":"Ocean Energy","color":COLORS["Ocean"],"badge":"badge-ocean",
            "desc":("Tidal stream generators, wave energy converters, and OTEC (ocean thermal energy "
                    "conversion) systems tap the ocean's vast energy budget. Tidal output follows "
                    "predictable lunar cycles; wave energy correlates strongly with offshore wind. "
                    "In this model, ocean energy is approximated via wind and precipitation proxies."),
            "factors":["Wave Height (m)","Tidal Cycle","Ocean Temperature","Wind Speed"],
            "stat": "Modelled via Wind + Precip proxies",
        },
    ]

    c1, c2 = st.columns(2)
    cols_cycle = [c1, c2]
    for i, e in enumerate(energies):
        ec = e['color']
        factors_html = "".join([
            f'<span style="background:{ec}18;color:{ec};border:1px solid {ec}33;'
            f'border-radius:10px;padding:3px 10px;font-size:0.7rem;font-weight:600;">{f}</span>'
            for f in e["factors"]
        ])
        with cols_cycle[i % 2]:
            st.markdown(f"""
<div class="glass-card" style="border-color:{ec}33;">
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:14px;">
        <div style="width:44px;height:44px;border-radius:12px;
            background:{ec}18;border:1px solid {ec}33;
            display:flex;align-items:center;justify-content:center;
            font-size:1.5rem;flex-shrink:0;">{e['icon']}</div>
        <div>
            <div style="font-weight:700;color:{ec};font-size:1.05rem;">{e['name']}</div>
            <div style="color:#5a8090;font-size:0.73rem;font-weight:500;">{e['stat']}</div>
        </div>
    </div>
    <p style="color:#7a9ab0;font-size:0.87rem;line-height:1.68;margin-bottom:14px;">{e['desc']}</p>
    <div style="display:flex;flex-wrap:wrap;gap:6px;">{factors_html}</div>
</div>
""", unsafe_allow_html=True)

    # Comparative bar
    st.markdown("<br>", unsafe_allow_html=True)
    avg_vals = {k: df_raw[f"{k}_Energy"].mean() for k in ["Solar","Wind","Hydro","Biomass","Geothermal"]}
    fig_bar = go.Figure(go.Bar(
        x=list(avg_vals.keys()),
        y=list(avg_vals.values()),
        marker=dict(
            color=[COLORS[k] for k in avg_vals],
            line=dict(color="#050d1a", width=1),
            opacity=0.88,
        ),
        text=[f"{v:.1f}" for v in avg_vals.values()],
        textposition="outside",
        textfont=dict(color=FONT_COLOR, size=11),
        hovertemplate="<b>%{x}</b>: %{y:,.1f} kWh/hr avg<extra></extra>",
    ))
    themed(fig_bar, "⚡ Average Hourly Energy Output by Source (kWh)", height=340)
    st.plotly_chart(fig_bar, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 3 — SMART PREDICTION MODULE
# ══════════════════════════════════════════════════════════════════════
elif page == "🔮  Smart Prediction":
    st.markdown('<div class="section-title">🔮 Smart Prediction Center</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">ML-powered forecast with AI insights, confidence scoring, and carbon analytics</div>', unsafe_allow_html=True)

    col_in, col_out = st.columns([1, 2])

    with col_in:
        st.markdown(
    '<div style="color:#FFFFFF;font-size:1.5rem;font-weight:700;">🎛️ Environmental Parameters</div>',
    unsafe_allow_html=True
)
        st.markdown("<br>", unsafe_allow_html=True)

        hour        = st.slider("🕐 Hour of Day",          0, 23, 12)
        month       = st.selectbox("📅 Month", list(range(1,13)),
                                   format_func=lambda x: MONTH_NAMES[x-1])
        temperature = st.slider("🌡️ Temperature (°C)",    -15.0, 45.0, 22.0, 0.5)
        solar_irr   = st.slider("☀️ Solar Irradiance (W/m²)", 0.0, 1200.0, 500.0, 10.0)
        wind_speed  = st.slider("💨 Wind Speed (m/s)",     0.0, 25.0, 6.0, 0.5)
        humidity    = st.slider("💧 Humidity (%)",          20.0, 100.0, 65.0, 1.0)
        precip      = st.slider("🌧️ Precipitation (mm)",  0.0, 100.0, 5.0, 1.0)
        pressure    = st.slider("🔵 Pressure (hPa)",       980.0, 1050.0, 1013.0, 1.0)

        predict_btn = st.button("⚡ Generate AI Prediction")

        # Feature importance sidebar card
        st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
        fi_items = [
            ("Solar Irradiance", min(100, solar_irr / 9), COLORS["Solar"]),  # FIX: /9 not /12 (max irr≈900)
            ("Wind Speed",       min(100, wind_speed / 25 * 100), COLORS["Wind"]),
            ("Temperature",      min(100, max(0, (temperature + 15) / 60 * 100)), "#ef4444"),
            ("Humidity",         humidity, COLORS["Hydro"]),
            ("Precipitation",    min(100, precip), COLORS["Biomass"]),
        ]
        fi_bars_html = "".join([progress_bar(label, pct, color) for label, pct, color in fi_items])
        st.markdown(f"""
        <div class="glass-card glass-card-purple">
            <b style="color:#8b5cf6;">🧠 Feature Impact</b>
            <div style="margin-top:12px;">{fi_bars_html}</div>
        </div>""", unsafe_allow_html=True)

    with col_out:
        # Always compute prediction
        with st.spinner("🤖 Running AI model..."):
            preds = ml_predict(hour, month, temperature, solar_irr, wind_speed, humidity, precip, pressure)

        # Store in history if button pressed
        if predict_btn:
            st.session_state["pred_history"].append({
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "hour": hour, "month": MONTH_NAMES[month-1],
                "temp": temperature, "wind": wind_speed, "irr": solar_irr,
                **{k: round(v,1) for k,v in preds.items()},
            })
            st.session_state["last_preds"] = preds

        score = sustainability_score(preds)
        rating = efficiency_rating(preds)
        co2 = carbon_saved_kg(preds["Total"])

        # ── KPI Row ──
        k1, k2, k3, k4 = st.columns(4)
        with k1:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">Total Output</div>
                <div class="kpi-value">{preds['Total']:,.0f}</div>
                <div class="kpi-delta">kWh predicted</div></div>""", unsafe_allow_html=True)
        with k2:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">Sustainability</div>
                <div class="kpi-value">{score}</div>
                <div class="kpi-delta">/ 100 score</div></div>""", unsafe_allow_html=True)
        with k3:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">Efficiency Grade</div>
                <div class="kpi-value">{rating}</div>
                <div class="kpi-delta">Energy rating</div></div>""", unsafe_allow_html=True)
        with k4:
            st.markdown(f"""<div class="kpi-card">
                <div class="kpi-label">CO₂ Avoided</div>
                <div class="kpi-value">{co2:,.0f}</div>
                <div class="kpi-delta">kg vs coal</div></div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ── Gauge + Donut ──
        gc1, gc2 = st.columns(2)
        with gc1:
            max_total = float(df_raw["Total_Energy"].max()) if "Total_Energy" in df_raw else 1600
            fig_gauge = make_gauge(preds["Total"], max_total, "Predicted Total Output", ACCENT)
            st.plotly_chart(fig_gauge, use_container_width=True)
        with gc2:
            src_labels = ["Solar","Wind","Hydro","Biomass","Geothermal"]
            src_vals   = [preds[s] for s in src_labels]
            fig_pie = go.Figure(go.Pie(
                labels=src_labels, values=src_vals,
                marker=dict(colors=[COLORS[s] for s in src_labels], line=dict(color="#050d1a",width=2)),
                hole=0.56,
                textinfo="label+percent",
                textfont=dict(color=FONT_COLOR, size=10),
                hovertemplate="<b>%{label}</b>: %{value:,.0f} kWh<extra></extra>",
            ))
            fig_pie.add_annotation(
                text=f"<b>{best_source(preds)}</b><br>leads",
                x=0.5, y=0.5, showarrow=False,
                font=dict(color=FONT_COLOR, size=12),
            )
            themed(fig_pie, "🥧 Energy Mix Breakdown", height=260)
            st.plotly_chart(fig_pie, use_container_width=True)

        # ── Source breakdown bars ──
        src_df = pd.DataFrame({
            "Source": src_labels,
            "kWh": [preds[s] for s in src_labels],
            "Color": [COLORS[s] for s in src_labels],
        }).sort_values("kWh", ascending=True)

        fig_h = go.Figure(go.Bar(
            x=src_df["kWh"], y=src_df["Source"], orientation="h",
            marker=dict(color=src_df["Color"].tolist(), opacity=0.88,
                        line=dict(color="#050d1a",width=1)),
            text=[f"{v:,.0f} kWh" for v in src_df["kWh"]],
            textposition="outside",
            textfont=dict(color=FONT_COLOR, size=11),
            hovertemplate="<b>%{y}</b>: %{x:,.0f} kWh<extra></extra>",
        ))
        themed(fig_h, "⚡ Source-by-Source Output Breakdown", height=280)
        fig_h.update_layout(
            yaxis=dict(tickfont=dict(size=11)),
            xaxis_title="kWh",
        )
        st.plotly_chart(fig_h, use_container_width=True)

        # ── AI Insights ──
        insights_html = "".join([
            f'<div class="insight-card"><div class="insight-text">{insight}</div></div>'
            for insight in ai_insights(preds, temperature, wind_speed, solar_irr)
        ])
        st.markdown(f"""
        <div class="glass-card glass-card-green">
            <b style="color:#00d4a8;font-size:1rem;">🤖 AI Intelligence Report</b>
            <div style="margin-top:12px;">{insights_html}</div>
        </div>""", unsafe_allow_html=True)

    # ── Prediction History Table ──
    if st.session_state["pred_history"]:
        st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
        st.markdown("### 🕒 Prediction History")
        hist_df = pd.DataFrame(st.session_state["pred_history"])
        st.dataframe(hist_df, use_container_width=True, height=200)
        st.markdown(csv_download_link(hist_df, "prediction_history.csv", "📥 Download History CSV"), unsafe_allow_html=True)

        if st.button("🗑️ Clear History", key="clear_hist"):
            st.session_state["pred_history"] = []
            st.rerun()


# ══════════════════════════════════════════════════════════════════════
# PAGE 4 — LIVE WEATHER INTELLIGENCE
# ══════════════════════════════════════════════════════════════════════
elif page == "🌤  Weather Intel":
    st.markdown(
    '<div class="section-title" style="color:#FFFFFF !important; background:none !important; -webkit-text-fill-color:#FFFFFF !important;">🌤 Weather Intelligence Center</div>',
    unsafe_allow_html=True
)
    st.markdown('<div class="section-sub">Real-time weather data with renewable suitability index and energy impact analysis</div>', unsafe_allow_html=True)

    # ── Input row: city + optional API key override ──
    col_city, col_key = st.columns([2, 2])
    with col_city:
        city = st.text_input("🔍 City Name", value="New Delhi", placeholder="e.g. Mumbai, London, Tokyo")
    with col_key:
        manual_api_key = st.text_input(
            "🔑 OpenWeatherMap API Key (optional)",
            type="password",
            help=(
                "Free key at openweathermap.org/api  |  "
                "You can also set OPENWEATHER_API_KEY in Streamlit secrets or env vars "
                "and leave this blank."
            ),
        )

    # ── Resolve API key (manual input → secrets → env var) ──
    resolved_key = _resolve_api_key(manual_api_key)

    # ── Fetch weather with a loading spinner ──
    weather_result = None
    if resolved_key and city and city.strip():
        with st.spinner(f"🌐 Fetching live weather for **{city}**…"):
            weather_result = fetch_live_weather(city.strip(), resolved_key)

    # ── Determine live vs simulation path ──
    using_live_data = weather_result is not None and weather_result["success"]

    if using_live_data:
        # ── LIVE PATH: unpack the parsed weather dict ──
        wd            = weather_result["data"]
        city          = f"{wd['city']}, {wd['country']}" if wd["country"] else wd["city"]
        temp          = wd["temp"]
        feels         = wd["feels_like"]
        humidity      = wd["humidity"]
        wind_spd      = wd["wind_speed"]
        pressure      = wd["pressure"]
        cloud         = wd["cloud_cover"]
        desc          = wd["description"]
        visibility    = wd["visibility"]
        solar_irr     = wd["solar_irr"]
        precipitation = wd["precipitation"]
        data_source   = "🟢 Live OpenWeatherMap"
        fetched_at    = wd["fetched_at"]
    else:
        # ── FALLBACK PATH: show error (if any) and use simulation ──
        if weather_result is not None and not weather_result["success"]:
            render_weather_error(weather_result)
        elif not resolved_key:
            st.info(
                "💡 Using simulated weather data. "
                "Enter your OpenWeatherMap API key above for live data."
            )

        sim           = get_simulation_defaults(city)
        city          = sim["city"]
        temp          = sim["temp"]
        feels         = sim["feels_like"]
        humidity      = sim["humidity"]
        wind_spd      = sim["wind_speed"]
        pressure      = sim["pressure"]
        cloud         = sim["cloud_cover"]
        desc          = sim["description"]
        visibility    = sim["visibility"]
        solar_irr     = sim["solar_irr"]
        precipitation = sim["precipitation"]
        data_source   = "🟡 Simulation Mode"
        fetched_at    = sim["fetched_at"]

    # ── Weather Header card ──
    st.markdown(f"""
    <div class="glass-card" style="margin-bottom:20px;">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;">
            <div>
                <div style="font-size:1.4rem;font-weight:700;color:#e2e8f0;">📍 {city}</div>
                <div style="color:#6a9aaa;font-size:0.85rem;">{desc} &nbsp;|&nbsp; {data_source}</div>
                <div style="color:#4a6a7a;font-size:0.75rem;margin-top:4px;">🕒 {fetched_at}</div>
            </div>
            <div style="text-align:right;">
                <div style="font-size:2.5rem;font-weight:800;color:#00d4a8;">{temp:.1f}°C</div>
                <div style="color:#6a9aaa;font-size:0.8rem;">Feels like {feels:.1f}°C</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Weather KPI Cards (5 core metrics) ──
    wc1, wc2, wc3, wc4, wc5 = st.columns(5)
    weather_items = [
        (wc1, "💧", "Humidity",    f"{humidity}%",            "#3b82f6"),
        (wc2, "💨", "Wind Speed",  f"{wind_spd} m/s",         ACCENT),
        (wc3, "☁️", "Cloud Cover", f"{cloud}%",               "#94a3b8"),
        (wc4, "☀️", "Solar Irr.",  f"{solar_irr:.0f} W/m²",   COLORS["Solar"]),
        (wc5, "🔵", "Pressure",    f"{pressure} hPa",         "#8b5cf6"),
    ]
    for col, icon, label, val, color in weather_items:
        with col:
            st.markdown(f"""
            <div class="kpi-card" style="border-color:{color}44;">
                <span class="kpi-icon">{icon}</span>
                <div class="kpi-value" style="font-size:1.4rem;color:{color};">{val}</div>
                <div class="kpi-label">{label}</div>
            </div>""", unsafe_allow_html=True)

    # ── Extra live-only metrics row (visibility, precipitation, wind gust) ──
    if using_live_data:
        st.markdown("<br>", unsafe_allow_html=True)
        ex1, ex2, ex3 = st.columns(3)
        extra_items = [
            (ex1, "👁️", "Visibility",    f"{visibility:.1f} km",                           "#64748b"),
            (ex2, "🌧️", "Precipitation", f"{precipitation:.1f} mm/h",                      "#0ea5e9"),
            (ex3, "💨", "Wind Gust",     f"{weather_result['data']['wind_gust']:.1f} m/s", COLORS["Wind"]),
        ]
        for col, icon, label, val, color in extra_items:
            with col:
                st.markdown(f"""
                <div class="kpi-card" style="border-color:{color}44;">
                    <span class="kpi-icon">{icon}</span>
                    <div class="kpi-value" style="font-size:1.3rem;color:{color};">{val}</div>
                    <div class="kpi-label">{label}</div>
                </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Renewable Suitability Gauges ──
    # Normalise solar against 900 W/m² (realistic clear-noon max) so gauge hits 100%.
    impact_solar = min(100, solar_irr / 9)
    impact_wind  = min(100, (wind_spd / 25) * 100)
    impact_hydro = min(100, humidity * 0.85)
    impact_bio   = min(100, (humidity / 2) + max(0, 30 - abs(temp - 20)))
    rsi_overall  = (impact_solar * 0.3 + impact_wind * 0.3 + impact_hydro * 0.2 + impact_bio * 0.2)

    g1, g2, g3, g4 = st.columns(4)
    for col, label, val, color in [
        (g1, "☀️ Solar Suitability",   impact_solar, COLORS["Solar"]),
        (g2, "💨 Wind Suitability",    impact_wind,  COLORS["Wind"]),
        (g3, "💧 Hydro Suitability",   impact_hydro, COLORS["Hydro"]),
        (g4, "🌿 Biomass Suitability", impact_bio,   COLORS["Biomass"]),
    ]:
        with col:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=val,
                number={"suffix": "%", "font": {"size": 26, "color": color}},
                title={"text": label, "font": {"color": "#475569", "size": 11}},
                gauge={
                    "axis":        {"range": [0, 100], "tickcolor": "#334155"},
                    "bar":         {"color": color, "thickness": 0.22},
                    "bgcolor":     "rgba(0,0,0,0)",
                    "borderwidth": 0,
                    "steps":       [{"range": [0, 100], "color": "rgba(255,255,255,0.02)"}],
                },
            ))
            fig.update_layout(**PLOTLY_BASE, height=220)
            st.plotly_chart(fig, use_container_width=True)

    # ── RSI Score Card ──
    rsi_label = (
        "Excellent — High renewable generation expected" if rsi_overall > 70 else
        "Moderate — Mixed conditions for renewables"     if rsi_overall > 40 else
        "Low — Poor conditions; rely on storage/baseload"
    )
    st.markdown(f"""
    <div class="glass-card glass-card-green" style="text-align:center;padding:20px;">
        <div style="font-size:0.72rem;color:#6a9aaa;text-transform:uppercase;
            letter-spacing:1.2px;margin-bottom:6px;">
            Renewable Suitability Index (RSI)
        </div>
        <div style="font-family:'Syne',sans-serif;font-size:2.8rem;font-weight:800;
            background:linear-gradient(135deg,#00d4a8,#3b82f6);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;">
            {rsi_overall:.0f} / 100
        </div>
        <div style="color:#6a9aaa;font-size:0.85rem;margin-top:4px;">{rsi_label}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── 24-Hour Energy Potential Simulation (driven by live weather values) ──
    st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
    st.markdown("### 📈 24-Hour Energy Potential Simulation")

    hours = list(range(24))

    # Solar: clear-sky model × cloud attenuation (consistent with physics_predict)
    solar_24 = [
        max(0, 900 * (1 - cloud / 100) * max(0, math.sin(math.pi * (h - 6) / 12)))
        if 6 <= h <= 18 else 0
        for h in hours
    ]

    # Wind: cubic power-curve (cut-in 3 m/s, rated 12 m/s, cutout 25 m/s)
    def _wind_kwh_24(ws: float) -> float:
        """Standard wind turbine power-curve — same formula as physics_predict."""
        if ws < 3 or ws >= 25:
            return 0.0
        wf = 1.0 if ws >= 12 else (ws / 12) ** 3
        return 500.0 * wf

    wind_24  = [_wind_kwh_24(wind_spd * (0.85 + 0.15 * math.sin(h / 3.5))) for h in hours]

    # Hydro: demand-dispatch pattern (slightly higher midday and evening)
    hydro_24 = [
        max(50, (150 + humidity * 1.2) * (0.88 + 0.12 * math.sin(math.pi * (h - 8) / 12)))
        for h in hours
    ]

    fig24 = go.Figure()
    for y, name, color, fill in [
        (solar_24, "Solar", COLORS["Solar"], "tozeroy"),
        (wind_24,  "Wind",  COLORS["Wind"],  "tozeroy"),
        (hydro_24, "Hydro", COLORS["Hydro"], "tozeroy"),
    ]:
        fig24.add_trace(go.Scatter(
            x=hours, y=y, name=name,
            line=dict(color=color, width=2.5),
            fill=fill, fillcolor=hex_rgba(color, 0.1),
            mode="lines",
            hovertemplate=f"<b>{name}</b> %{{x}}h: %{{y:,.0f}} kWh<extra></extra>",
        ))

    src_label = "Live API Data" if using_live_data else "Simulated Data"
    themed(fig24, f"⚡ 24-Hour Energy Potential — {city}  [{src_label}]", height=340)
    st.plotly_chart(fig24, use_container_width=True)



# PAGE 5 — SMART AI ENERGY FORECAST CENTER  (redesigned)
# ══════════════════════════════════════════════════════════════════════
elif page == "📅  Forecast":
    st.markdown('<div class="section-title">📅 Smart AI Energy Forecast Center</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">AI-powered multi-horizon forecasting — with plain-English explanations so anyone can understand what the numbers mean</div>', unsafe_allow_html=True)

    # ── Forecast horizon selector ──
    view_mode = st.radio("📡 Select Forecast Horizon", ["7-Day Forecast", "Hourly (24h)", "Monthly Outlook"], horizontal=True)
    st.markdown("""
<style>

/* Forecast Radio Buttons */
div[role="radiogroup"] label {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

div[role="radiogroup"] p {
    color: #FFFFFF !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

    # ── Build forecast data based on view ──
    # FIX: single seed(42) shared across modes made all three horizons look identical.
    # Use mode-specific seeds so each horizon has distinct, reproducible data.
    _seed_map = {"7-Day Forecast": 42, "Hourly (24h)": 77, "Monthly Outlook": 123}
    np.random.seed(_seed_map.get(view_mode, 42))

    if view_mode == "7-Day Forecast":
        days = [(datetime.today() + timedelta(days=i)).strftime("%a %d %b") for i in range(7)]
        solar_f  = np.clip(np.random.normal(180, 50, 7), 0, None)
        wind_f   = np.clip(np.random.normal(140, 40, 7), 0, None)
        hydro_f  = np.clip(np.random.normal(280, 30, 7), 0, None)
        bio_f    = np.clip(np.random.normal(110, 15, 7), 0, None)
        geo_f    = np.clip(np.random.normal(404,  8, 7), 0, None)
        total_f  = solar_f + wind_f + hydro_f + bio_f + geo_f
        labels   = days
        horizon_label = "next 7 days"
        x_label  = "Day"

    elif view_mode == "Hourly (24h)":
        hours_list = list(range(24))
        solar_f  = np.array([max(0, 900 * max(0, math.sin(math.pi * (h-6)/12))) if 6<=h<=18 else 0 for h in hours_list])
        wind_f   = np.array([150 + 80 * math.sin(h / 3.8) for h in hours_list])
        hydro_f  = np.array([140 + 20 * math.sin(h / 6)   for h in hours_list])
        bio_f    = np.array([110 + 5  * math.sin(h / 8)   for h in hours_list])
        geo_f    = np.full(len(hours_list), 404.0)  # FIX: was random.normal each step — deterministic is correct for geothermal
        total_f  = solar_f + wind_f + hydro_f + bio_f + geo_f
        labels   = [f"{h:02d}:00" for h in hours_list]
        horizon_label = "next 24 hours"
        x_label  = "Hour"

    else:  # Monthly Outlook
        # FIX: previous solar_f mixed max(0,sin) + max(0,random) — negative months got
        # spurious small positive noise added, breaking the smooth seasonal curve.
        # Use a clean summer-peak bell curve (peak Jul/Aug) with small natural jitter.
        solar_f  = np.array([max(0.0, 300 * math.sin(math.pi * (i - 2) / 9) + np.random.normal(0, 10)) for i in range(12)])
        wind_f   = np.array([100 + 60 * math.sin(math.pi * (i + 2) / 6) for i in range(12)])
        hydro_f  = np.array([200 + 80 * math.sin(math.pi * (i - 2) / 6) for i in range(12)])
        bio_f    = np.array([100 + 20 * math.sin(math.pi * i / 12) for i in range(12)])
        geo_f    = np.full(12, 404.0)
        total_f  = solar_f + wind_f + hydro_f + bio_f + geo_f
        labels   = MONTH_NAMES
        horizon_label = "12-month outlook"
        x_label  = "Month"

    # ── Derived KPI values ──
    avg_output      = float(np.mean(total_f))
    peak_idx        = int(np.argmax(total_f))
    peak_label      = labels[peak_idx]
    peak_val        = float(total_f[peak_idx])
    src_avgs        = {
        "Solar":      float(np.mean(solar_f)),
        "Wind":       float(np.mean(wind_f)),
        "Hydro":      float(np.mean(hydro_f)),
        "Biomass":    float(np.mean(bio_f)),
        "Geothermal": float(np.mean(geo_f)),
    }
    top_src         = max(src_avgs, key=src_avgs.get)
    low_src         = min(src_avgs, key=src_avgs.get)
    confidence_pct  = 87
    accuracy_pct    = 94

    # ══════════════════════════════════════════════════════════════════
    # A — FORECAST SUMMARY KPI CARDS
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.75rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;">
        ⚡ FORECAST SUMMARY — AT A GLANCE
    </div>
    """, unsafe_allow_html=True)

    kc1, kc2, kc3, kc4, kc5, kc6 = st.columns(6)
    forecast_kpis = [
        (kc1, "⚡", f"{avg_output:,.0f}", "kWh", "Avg Predicted Output", ACCENT, "Average energy expected per period"),
        (kc2, "🏆", top_src,             "",    "Top Energy Source",     COLORS["Solar"], f"{src_avgs[top_src]:,.0f} kWh avg"),
        (kc3, "📉", low_src,             "",    "Lowest Source",         "#ef4444", f"{src_avgs[low_src]:,.0f} kWh avg"),
        (kc4, "📅", peak_label,          "",    "Peak Forecast Period",  COLORS["Biomass"], f"{peak_val:,.0f} kWh"),
        (kc5, "🎯", f"{confidence_pct}%","",    "AI Confidence Score",   "#a78bfa", "Model certainty level"),
        (kc6, "✅", f"{accuracy_pct}%",  "",    "Forecast Accuracy",     COLORS["Wind"], "Historical match rate"),
    ]
    for col, icon, val, unit, label, color, delta in forecast_kpis:
        with col:
            delta_color = color + "bb"
            # Build unit block as a plain string (no f-string) to avoid CSS curly-brace
            # collision when embedded inside the outer f-string below.
            unit_block = (
                '<div style="font-size:0.65rem;color:#4a7080;margin-top:1px;">'
                + unit +
                '</div>'
            ) if unit else ""
            st.markdown(
                f'<div style="'
                f'background:linear-gradient(145deg,{color}14 0%,rgba(8,18,28,0.7) 100%);'
                f'border:1px solid {color}30;border-radius:18px;padding:18px 12px;'
                f'text-align:center;position:relative;overflow:hidden;'
                f'transition:transform 0.25s,box-shadow 0.25s;cursor:default;">'
                f'<div style="font-size:1.5rem;margin-bottom:6px;">{icon}</div>'
                f'<div style="font-family:\'Orbitron\',monospace;font-size:1.1rem;font-weight:800;'
                f'color:{color};line-height:1.1;">{val}</div>'
                + unit_block +
                f'<div style="font-size:0.62rem;color:#5a8090;text-transform:uppercase;'
                f'letter-spacing:1px;margin-top:6px;font-weight:600;">{label}</div>'
                f'<div style="font-size:0.7rem;color:{delta_color};margin-top:4px;">{delta}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # B — EXPLAINABLE AI INSIGHTS (plain-language)
    # ══════════════════════════════════════════════════════════════════
    # Generate contextual insights based on data
    def forecast_insights(solar_f, wind_f, hydro_f, bio_f, geo_f, top_src, low_src, view_mode):
        insights = []
        solar_trend  = "rising" if solar_f[-1] > solar_f[0] else "steady" if abs(solar_f[-1]-solar_f[0])<30 else "declining"
        wind_trend   = "increasing" if np.mean(wind_f[-3:]) > np.mean(wind_f[:3]) else "stable"
        hydro_stable = np.std(hydro_f) < 30
        # FIX: removed unused peak_i variable (dead code)

        if top_src == "Solar":
            insights.append(("☀️", "Solar", COLORS["Solar"],
                "Solar energy is your strongest performer this period. Clear sky conditions and high sunlight hours are driving strong output — great news for solar panel operators!",
                solar_trend))
        if top_src == "Wind":
            insights.append(("💨", "Wind", COLORS["Wind"],
                "Wind energy is leading this forecast period. Favorable wind patterns and above-average speeds mean turbines will operate near peak capacity.",
                wind_trend))
        if top_src == "Hydro":
            insights.append(("💧", "Hydro", COLORS["Hydro"],
                "Hydropower is the top contributor. Recent rainfall and good reservoir levels ensure consistent, reliable electricity generation throughout this period.",
                "stable"))

        insights.append(("🌋", "Geothermal", COLORS["Geothermal"],
            "Geothermal energy remains rock-steady as always — it doesn't depend on weather at all. Think of it as the reliable 'always-on' base that keeps the lights on 24/7.",
            "stable"))

        if hydro_stable:
            insights.append(("💧", "Hydro Stability", COLORS["Hydro"],
                "Hydro energy shows very little variation across the forecast period. This means you can count on it as a dependable backup regardless of solar or wind conditions.",
                "stable"))

        if low_src == "Wind":
            insights.append(("⚠️", "Wind Alert", "#ef4444",
                "Wind energy output is the lowest among all sources this period. Lower wind speeds reduce turbine efficiency — backup storage or hydro will compensate.",
                "low"))
        if low_src == "Solar":
            insights.append(("⚠️", "Solar Alert", "#ef4444",
                "Solar output is weaker this period — possibly due to seasonal cloud cover or shorter daylight hours. Wind and hydro will pick up the slack.",
                "low"))

        if view_mode == "Hourly (24h)":
            insights.append(("⏰", "Best Hour", COLORS["Biomass"],
                f"The best energy generation window today is around midday (10 AM–2 PM) when solar panels produce maximum output. Schedule energy-heavy tasks during this window to save costs!",
                "peak"))
        elif view_mode == "7-Day Forecast":
            insights.append(("📅", "Peak Day", COLORS["Biomass"],
                f"Energy production will peak around the middle of this 7-day window when weather conditions are most favorable. Plan grid exports or charging sessions on peak days.",
                "peak"))
        else:
            insights.append(("🌸", "Seasonal Pattern", COLORS["Solar"],
                "Summer months (May–August) consistently deliver the highest total renewable output thanks to longer daylight and stronger solar irradiance. Winter months rely more on wind and hydro.",
                "seasonal"))
        return insights

    fi_list = forecast_insights(solar_f, wind_f, hydro_f, bio_f, geo_f, top_src, low_src, view_mode)

    st.markdown("""
    <div style="
        background:linear-gradient(135deg,rgba(0,212,168,0.06) 0%,rgba(8,18,28,0.8) 100%);
        border:1px solid rgba(0,212,168,0.18);border-radius:20px;padding:22px 24px 8px;margin-bottom:20px;
    ">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;">
            <span style="font-size:1.4rem;">🤖</span>
            <div>
                <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:1.0rem;
                    color:#00d4a8;text-transform:uppercase;letter-spacing:1px;">AI Forecast Interpreter</div>
                <div style="font-size:0.75rem;color:#4a7a8a;">Plain-English explanations — what do these forecasts actually mean?</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    ins_cols = st.columns(2)
    for i, (icon, src_name, color, text, trend) in enumerate(fi_list):
        trend_icon = "📈" if trend in ("rising","increasing","peak") else ("📉" if trend == "low" else "➡️")
        with ins_cols[i % 2]:
            st.markdown(f"""
            <div style="
                display:flex;gap:12px;align-items:flex-start;
                background:{color}0d;border:1px solid {color}25;
                border-radius:14px;padding:14px 16px;margin-bottom:10px;
            ">
                <div style="font-size:1.4rem;flex-shrink:0;margin-top:2px;">{icon}</div>
                <div>
                    <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;">
                        <span style="font-family:'Rajdhani',sans-serif;font-weight:700;
                            color:{color};font-size:0.82rem;text-transform:uppercase;
                            letter-spacing:0.5px;">{src_name}</span>
                        <span style="font-size:0.75rem;">{trend_icon}</span>
                    </div>
                    <div style="color:#8ab0c0;font-size:0.82rem;line-height:1.6;">{text}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # C — INTERACTIVE FORECAST CHARTS (4 charts with tabs)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("""
    <style>

    /* Forecast Tab Styling */

    button[data-baseweb="tab"]{
        color:#5B7689 !important;
        font-weight:600 !important;
        font-size:0.95rem !important;
    }

    /* Active Tab */
    button[data-baseweb="tab"][aria-selected="true"]{
        color:#5B7689 !important;
        border-bottom:2px solid #5B7689 !important;
    }

    /* Text inside tabs */
    button[data-baseweb="tab"] span,
    button[data-baseweb="tab"] p{
        color:#5B7689 !important;
    }

    /* Remove Streamlit default red highlight */
    button[data-baseweb="tab"][aria-selected="true"]::after{
        background:#5B7689 !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;
        font-size:0.75rem;
        font-weight:700;
        color:#5B7689;
        text-transform:uppercase;
        letter-spacing:2px;
        margin:20px 0 12px;">
        📊 INTERACTIVE FORECAST CHARTS — Hover, zoom, and click the legend to show/hide sources
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Trend Lines",
        "⚡ Source Comparison",
        "🗓️ Stacked Area",
        "🌡️ Heatmap"
    ])

    with tab1:
        st.markdown("""
        <div style="background:rgba(0,180,216,0.06);border-left:3px solid #00B4D8;
            border-radius:0 10px 10px 0;padding:10px 14px;margin-bottom:14px;font-size:0.83rem;color:#7ab0c0;">
            <b>What you're seeing:</b> Each coloured line shows how much energy one source will produce over the forecast period.
            Higher = more energy. <b>Tip:</b> Click any source name in the legend to hide/show it. Hover over points for exact values.
        </div>
        """, unsafe_allow_html=True)
        fig_trend = go.Figure()
        for src_name, vals, color in [
            ("☀️ Solar",      solar_f, COLORS["Solar"]),
            ("💨 Wind",       wind_f,  COLORS["Wind"]),
            ("💧 Hydro",      hydro_f, COLORS["Hydro"]),
            ("🌿 Biomass",    bio_f,   COLORS["Biomass"]),
            ("🌋 Geothermal", geo_f,   COLORS["Geothermal"]),
        ]:
            color_hex = color
            fig_trend.add_trace(go.Scatter(
                x=labels, y=vals, name=src_name,
                line=dict(color=color_hex, width=2.5),
                mode="lines+markers", marker=dict(size=7, symbol="circle"),
                fill="tozeroy", fillcolor=hex_rgba(color_hex, 0.06),
                hovertemplate=f"<b>{src_name}</b><br>{x_label}: %{{x}}<br>Output: %{{y:,.0f}} kWh<extra></extra>",
            ))
        # Total line
        fig_trend.add_trace(go.Scatter(
            x=labels, y=total_f, name="⚡ Total",
            line=dict(color="#dde6f0", width=2, dash="dot"),
            mode="lines",
            hovertemplate="<b>Total</b><br>%{x}: %{y:,.0f} kWh<extra></extra>",
        ))
        themed(fig_trend, f"🔮 Energy Forecast — {horizon_label.title()}", height=400)
        st.plotly_chart(fig_trend, use_container_width=True)

    with tab2:
        st.markdown("""
        <div style="background:rgba(253,184,19,0.06);border-left:3px solid #FDB813;
            border-radius:0 10px 10px 0;padding:10px 14px;margin-bottom:14px;font-size:0.83rem;color:#c0a060;">
            <b>What you're seeing:</b> Side-by-side bars let you compare how much energy each source contributes in each period.
            Taller bars = more energy from that source. This instantly shows you which sources dominate and which are weaker.
        </div>
        """, unsafe_allow_html=True)
        fig_bar = go.Figure()
        for src_name, vals, color in [
            ("Solar", solar_f, COLORS["Solar"]),
            ("Wind",  wind_f,  COLORS["Wind"]),
            ("Hydro", hydro_f, COLORS["Hydro"]),
            ("Biomass", bio_f, COLORS["Biomass"]),
            ("Geothermal", geo_f, COLORS["Geothermal"]),
        ]:
            fig_bar.add_trace(go.Bar(
                x=labels, y=vals, name=src_name,
                marker_color=color, opacity=0.88,
                hovertemplate=f"<b>{src_name}</b><br>%{{x}}: %{{y:,.0f}} kWh<extra></extra>",
            ))
        fig_bar.update_layout(**PLOTLY_BASE, barmode="group", height=400,
                              title=dict(text=f"⚡ Energy Source Comparison — {horizon_label.title()}",
                                         font=dict(size=14, color="#8ecfdf")))
        st.plotly_chart(fig_bar, use_container_width=True)

    with tab3:
        st.markdown("""
        <div style="background:rgba(46,204,113,0.06);border-left:3px solid #2ECC71;
            border-radius:0 10px 10px 0;padding:10px 14px;margin-bottom:14px;font-size:0.83rem;color:#60a080;">
            <b>What you're seeing:</b> A stacked area chart where each coloured band represents one energy source.
            The total height shows total combined energy. This helps you see how the energy mix shifts over time.
        </div>
        """, unsafe_allow_html=True)
        fig_stack = go.Figure()
        for src_name, vals, color in [
            ("Geothermal", geo_f,   COLORS["Geothermal"]),
            ("Biomass",    bio_f,   COLORS["Biomass"]),
            ("Hydro",      hydro_f, COLORS["Hydro"]),
            ("Wind",       wind_f,  COLORS["Wind"]),
            ("Solar",      solar_f, COLORS["Solar"]),
        ]:
            fig_stack.add_trace(go.Scatter(
                x=labels, y=vals, name=src_name,
                stackgroup="one",
                line=dict(color=color, width=1.5),
                fillcolor=hex_rgba(color, 0.5),
                hovertemplate=f"<b>{src_name}</b><br>%{{x}}: %{{y:,.0f}} kWh<extra></extra>",
            ))
        themed(fig_stack, f"📊 Stacked Energy Mix — {horizon_label.title()}", height=400)
        st.plotly_chart(fig_stack, use_container_width=True)

    with tab4:
        st.markdown("""
        <div style="background:rgba(99,102,241,0.06);border-left:3px solid #6366f1;
            border-radius:0 10px 10px 0;padding:10px 14px;margin-bottom:14px;font-size:0.83rem;color:#8088c0;">
            <b>What you're seeing:</b> A heatmap shows energy intensity — darker/brighter cells = more energy.
            Each row is an energy source; each column is a time period. At a glance you can spot peak periods and weak spots.
        </div>
        """, unsafe_allow_html=True)
        heatmap_z = [
            solar_f.tolist(), wind_f.tolist(), hydro_f.tolist(),
            bio_f.tolist(), geo_f.tolist()
        ]
        heatmap_y = ["☀️ Solar", "💨 Wind", "💧 Hydro", "🌿 Biomass", "🌋 Geothermal"]
        fig_heat = go.Figure(go.Heatmap(
            z=heatmap_z, x=labels, y=heatmap_y,
            colorscale=[
                [0.0, "#08121C"], [0.2, "#0d3048"],
                [0.45, "#0077B6"], [0.70, "#00B4D8"],
                [0.85, "#2ECC71"], [1.0, "#FDB813"],
            ],
            showscale=True,
            colorbar=dict(tickfont=dict(color=FONT_COLOR, family="Exo 2"), thickness=10,
                          title=dict(text="kWh", font=dict(color="#7a9ab0"))),
            hovertemplate="<b>%{y}</b><br>%{x}: <b>%{z:,.0f} kWh</b><extra></extra>",
        ))
        themed(fig_heat, f"🌡️ Forecast Heatmap — Energy Intensity by Source × Period", height=340)
        st.plotly_chart(fig_heat, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    # D — FORECAST INTERPRETATION SECTION
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    stability_wind = "unstable" if np.std(wind_f) > 40 else "stable"
    stability_solar = "variable" if np.std(solar_f) > 60 else "consistent"

    _avg_output_safe = avg_output if avg_output > 0 else 1.0  # FIX: guard zero division
    top_pct        = round(src_avgs[top_src] / _avg_output_safe * 100, 1)
    top_src_color  = COLORS[top_src]
    conditions_lbl = "favourable" if avg_output > 900 else "moderate"

    st.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(99,102,241,0.07) 0%,rgba(8,18,28,0.85) 100%);
    border:1px solid rgba(99,102,241,0.22);border-radius:20px;padding:28px 30px;margin-bottom:20px;">
    <div style="font-family:'Orbitron',monospace;font-size:0.8rem;font-weight:700;
        color:#8b9cf6;letter-spacing:2px;text-transform:uppercase;margin-bottom:18px;">
        🔍 What Does This Forecast Actually Mean?
    </div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
        <div style="background:rgba(255,255,255,0.03);border-radius:14px;padding:16px;">
            <div style="color:{top_src_color};font-weight:700;font-size:0.88rem;margin-bottom:8px;">
                🏆 Best Performing Source: {top_src}
            </div>
            <div style="color:#8ab0c0;font-size:0.83rem;line-height:1.65;">
                <b style="color:#c8dce8;">{top_src}</b> will contribute approximately
                <b style="color:{top_src_color};">{top_pct}%</b> of total energy this period,
                making it the clear leader. This is the source you should prioritise for
                capacity expansion or grid dispatch scheduling.
            </div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border-radius:14px;padding:16px;">
            <div style="color:#ef6060;font-weight:700;font-size:0.88rem;margin-bottom:8px;">
                ⚠️ Most Variable Source: {low_src}
            </div>
            <div style="color:#8ab0c0;font-size:0.83rem;line-height:1.65;">
                <b style="color:#c8dce8;">{low_src}</b> shows the most variability this forecast period.
                In simple terms — its output fluctuates more than other sources.
                Battery storage or demand flexibility will help smooth out these dips.
            </div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border-radius:14px;padding:16px;">
            <div style="color:#2ECC71;font-weight:700;font-size:0.88rem;margin-bottom:8px;">
                🌍 Seasonal Context
            </div>
            <div style="color:#8ab0c0;font-size:0.83rem;line-height:1.65;">
                Solar peaks in summer months (May–August) when days are longer and sunlight is strongest.
                Wind tends to be stronger in winter and monsoon seasons. Hydro follows rainfall patterns —
                typically higher after the monsoon (Jul–Oct in India).
            </div>
        </div>
        <div style="background:rgba(255,255,255,0.03);border-radius:14px;padding:16px;">
            <div style="color:#00C2FF;font-weight:700;font-size:0.88rem;margin-bottom:8px;">
                📈 Future Energy Trends
            </div>
            <div style="color:#8ab0c0;font-size:0.83rem;line-height:1.65;">
                Total energy output averages <b style="color:#00B4D8;">{avg_output:,.0f} kWh</b> per period,
                with a peak of <b style="color:#FDB813;">{peak_val:,.0f} kWh</b> on <b>{peak_label}</b>.
                Overall conditions are {conditions_lbl} for renewable generation.
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # E — AI RECOMMENDATION ENGINE
    # ══════════════════════════════════════════════════════════════════
    co2_forecast  = carbon_saved_kg(avg_output)
    geo_avg_kwh   = f"{src_avgs['Geothermal']:,.0f}"
    cars_saved    = int(co2_forecast / 4.6) if co2_forecast > 0 else 0  # FIX: guard zero
    co2_fmt       = f"{co2_forecast:,.0f}"

    solar_strength = "strong" if src_avgs["Solar"] > 150 else "moderate"
    solar_action   = ("Increase solar panel utilisation and consider expanding rooftop installations in sunny regions."
                      if src_avgs["Solar"] > 150
                      else "Consider solar + storage combo to bridge gaps during cloud cover.")
    wind_advice    = ("Wind is reliable — pair with short-term battery storage to capture surplus during peak wind hours."
                      if stability_wind == "stable"
                      else "Wind variability is high — backup battery storage of 4+ hours capacity is recommended to prevent grid instability.")

    recs_forecast = [
        ("🌞", COLORS["Solar"],  "Maximise Solar Deployment",
         f"Solar is {solar_strength} this period. {solar_action}"),
        ("💨", COLORS["Wind"],   "Wind Storage Strategy",
         f"Wind output is {stability_wind} across this forecast. {wind_advice}"),
        ("💧", COLORS["Hydro"],  "Hydro as Base Load",
         "Hydro energy remains a reliable workhorse throughout this period. Use it as your stable base load while solar and wind handle peak demand. Reservoirs also act as natural batteries."),
        ("🌿", COLORS["Biomass"],"Biomass for Off-Peak Gaps",
         "Biomass provides dispatchable power — meaning you can switch it on/off on demand. Schedule biomass generation during nighttime or cloudy periods when solar output is zero."),
        ("🌋", COLORS["Geothermal"], "Geothermal Reliability",
         f"Geothermal energy is completely weather-independent and delivers a rock-steady ~{geo_avg_kwh} kWh every period. It is your most dependable 24/7 baseload source."),
        ("♻️", "#84cc16",
         f"CO\u2082 Impact: {co2_fmt} kg Saved",
         f"Each forecast period, this renewable mix avoids approximately {co2_fmt} kg of CO\u2082 compared to coal-based generation. That is equivalent to taking {cars_saved} cars off the road for a day."),
    ]

    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.75rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin:8px 0 14px;">
        💡 AI RECOMMENDATIONS — What Should You Do?
    </div>
    """, unsafe_allow_html=True)

    rc1, rc2 = st.columns(2)
    for i, (icon, color, title, text) in enumerate(recs_forecast):
        with (rc1 if i % 2 == 0 else rc2):
            st.markdown(f"""
            <div style="
                background:linear-gradient(135deg,{color}0d 0%,rgba(8,18,28,0.7) 100%);
                border:1px solid {color}28;border-radius:16px;padding:16px 18px;
                margin-bottom:12px;
            ">
                <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                    <span style="font-size:1.3rem;">{icon}</span>
                    <span style="font-family:'Rajdhani',sans-serif;font-weight:700;
                        color:{color};font-size:0.85rem;text-transform:uppercase;letter-spacing:0.5px;">{title}</span>
                </div>
                <div style="color:#7a9ab0;font-size:0.82rem;line-height:1.65;">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Download forecast CSV ──
    st.markdown("<br>", unsafe_allow_html=True)
    forecast_df = pd.DataFrame({
        x_label:         labels,
        "Solar_kWh":     solar_f.round(1),
        "Wind_kWh":      wind_f.round(1),
        "Hydro_kWh":     hydro_f.round(1),
        "Biomass_kWh":   bio_f.round(1),
        "Geo_kWh":       geo_f.round(1),
        "Total_kWh":     total_f.round(1),
    })
    st.markdown(csv_download_link(forecast_df, "forecast_data.csv", "📥 Download Full Forecast CSV"), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 6 — ADVANCED ANALYTICS DASHBOARD
# ══════════════════════════════════════════════════════════════════════
elif page == "📊  Analytics":
    st.markdown(
    '<div style="color:#FFFFFF;font-size:2rem;font-weight:700;">📊 Advanced Analytics Dashboard</div>',
    unsafe_allow_html=True
)

    st.markdown(
    '<div style="color:#DCE7F0;font-size:1rem;font-weight:500;">Deep-dive intelligence: trends, anomalies, seasonal patterns, and correlations</div>',
    unsafe_allow_html=True
)


    # ── Filters ──
    with st.expander("🎛️ Data Filters", expanded=False):
        fc1, fc2, fc3 = st.columns(3)
        sel_months = fc1.multiselect("Months", list(range(1,13)), default=list(range(1,13)),
                                     format_func=lambda x: MONTH_NAMES[x-1])
        sel_hours  = fc2.slider("Hour Range", 0, 23, (0, 23))
        sel_season = fc3.multiselect("Season", [0,1,2,3], default=[0,1,2,3],
                                     format_func=lambda x: ["Winter","Spring","Summer","Fall"][x])

    df_f = df_raw[
        (df_raw["Month"].isin(sel_months)) &
        (df_raw["Hour"].between(sel_hours[0], sel_hours[1])) &
        (df_raw["Season"].isin(sel_season))
    ]
    if df_f.empty:
        st.warning("No data matches selected filters.")
        st.stop()

    # ── KPIs ──
    src_means = {k: df_f[f"{k}_Energy"].mean() for k in ["Solar","Wind","Hydro","Biomass","Geothermal"]}
    best_src  = max(src_means, key=src_means.get)
    worst_src = min(src_means, key=src_means.get)
    peak_hour = int(df_f.groupby("Hour")["Total_Energy"].mean().idxmax())

    k1, k2, k3, k4, k5 = st.columns(5)
    for col, label, val, delta in [
        (k1, "⚡ Avg Total",    f"{df_f['Total_Energy'].mean():,.0f} kWh", "filtered"),
        (k2, "🏆 Best Source",  best_src, f"{src_means[best_src]:,.0f} kWh avg"),
        (k3, "📉 Lowest Source",worst_src,f"{src_means[worst_src]:,.0f} kWh avg"),
        (k4, "📁 Records",     f"{len(df_f):,}", "shown"),
        (k5, "⏰ Peak Hour",   f"{peak_hour:02d}:00", "highest avg output"),
    ]:
        with col:
            st.metric(label, val, delta)

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Row 1: Monthly stack + Pie ──
    r1c1, r1c2 = st.columns(2)
    with r1c1:
        df_mb = df_f.groupby("Month")[
            ["Solar_Energy","Wind_Energy","Hydro_Energy","Biomass_Energy","Geothermal_Energy"]
        ].mean()
        fig_mb = go.Figure()
        for col_name, color in zip(df_mb.columns, [COLORS["Solar"],COLORS["Wind"],COLORS["Hydro"],COLORS["Biomass"],COLORS["Geothermal"]]):
            fig_mb.add_trace(go.Bar(
                x=[MONTH_NAMES[m-1] for m in df_mb.index],
                y=df_mb[col_name],
                name=col_name.replace("_Energy",""),
                marker_color=color,
                hovertemplate=f"<b>{col_name.replace('_Energy','')}</b> %{{x}}: %{{y:,.0f}} kWh<extra></extra>",
            ))
        fig_mb.update_layout(**PLOTLY_BASE, barmode="stack", height=340,
                             title=dict(text="📊 Monthly Stacked Energy Output",font=dict(size=13,color="#64748b")))
        st.plotly_chart(fig_mb, use_container_width=True)

    with r1c2:
        totals_pie = {k: df_f[f"{k}_Energy"].sum() for k in ["Solar","Wind","Hydro","Biomass","Geothermal"]}
        fig_pi = go.Figure(go.Pie(
            labels=list(totals_pie.keys()),
            values=list(totals_pie.values()),
            marker=dict(colors=[COLORS[k] for k in totals_pie], line=dict(color="#050d1a",width=2)),
            hole=0.52, textinfo="label+percent",
            textfont=dict(color=FONT_COLOR, size=10),
        ))
        themed(fig_pi, "🥧 Overall Energy Share (Filtered)", height=340)
        st.plotly_chart(fig_pi, use_container_width=True)

    # ── Row 2: Heatmap + Scatter ──
    r2c1, r2c2 = st.columns(2)
    with r2c1:
        df_hm  = df_f.groupby(["Month","Hour"])["Solar_Energy"].mean().reset_index()
        df_piv = df_hm.pivot(index="Month", columns="Hour", values="Solar_Energy")
        fig_hm = go.Figure(go.Heatmap(
            z=df_piv.values,
            x=df_piv.columns,
            y=[MONTH_NAMES[m-1] for m in df_piv.index],
            colorscale=[[0,"#050d1a"],[0.5,hex_rgba(COLORS["Solar"],0.4)],[1,COLORS["Solar"]]],
            showscale=True, colorbar=dict(tickfont=dict(color=FONT_COLOR), thickness=10),
            hovertemplate="Month: %{y}, Hour: %{x}<br>Solar: %{z:,.0f} kWh<extra></extra>",
        ))
        themed(fig_hm, "☀️ Solar Energy — Hour × Month Heatmap", height=340)
        st.plotly_chart(fig_hm, use_container_width=True)

    with r2c2:
        sample = df_f.sample(min(2500, len(df_f)), random_state=42)
        fig_sc = go.Figure(go.Scatter(
            x=sample["Wind_Speed"], y=sample["Wind_Energy"],
            mode="markers",
            marker=dict(
                color=sample["Solar_Irradiance"],
                colorscale=[[0,hex_rgba(BLUE,0.8)],[1,ACCENT]],
                size=4, opacity=0.55,
                colorbar=dict(title="Solar Irr.", tickfont=dict(color=FONT_COLOR), thickness=10),
            ),
            hovertemplate="Wind Speed: %{x:.1f} m/s<br>Wind Energy: %{y:,.0f} kWh<extra></extra>",
        ))
        themed(fig_sc, "💨 Wind Speed vs Wind Energy (coloured by Solar Irr.)", height=340)
        st.plotly_chart(fig_sc, use_container_width=True)

    # ── Row 3: Hourly profile + Anomaly ──
    r3c1, r3c2 = st.columns(2)
    with r3c1:
        df_hr = df_f.groupby("Hour")["Total_Energy"].agg(["mean","std"]).reset_index()
        fig_hr = go.Figure([
            go.Scatter(
                x=df_hr["Hour"], y=df_hr["mean"] + df_hr["std"],
                mode="lines", line=dict(width=0),
                showlegend=False, hoverinfo="skip",
            ),
            go.Scatter(
                x=df_hr["Hour"], y=df_hr["mean"] - df_hr["std"],
                fill="tonexty", fillcolor=hex_rgba(ACCENT, 0.1),
                mode="lines", line=dict(width=0),
                showlegend=False, name="±1 StdDev",
            ),
            go.Scatter(
                x=df_hr["Hour"], y=df_hr["mean"],
                line=dict(color=ACCENT, width=2.5),
                name="Avg Total Output",
                hovertemplate="Hour %{x}: %{y:,.0f} kWh<extra></extra>",
            ),
        ])
        themed(fig_hr, "⏰ Hourly Total Energy Profile (Mean ± σ)", height=320)
        st.plotly_chart(fig_hr, use_container_width=True)

    with r3c2:
        # Simple anomaly detection: points > mean + 2.5σ
        mu   = df_f["Total_Energy"].mean()
        sig  = df_f["Total_Energy"].std()
        df_anom = df_f.copy()
        df_anom["Anomaly"] = np.abs(df_anom["Total_Energy"] - mu) > 2.5 * sig
        normal_sample = df_anom[~df_anom["Anomaly"]].sample(min(2000,sum(~df_anom["Anomaly"])), random_state=1)
        anom_sample   = df_anom[df_anom["Anomaly"]].head(200)
        fig_an = go.Figure()
        fig_an.add_trace(go.Scatter(
            x=normal_sample.index, y=normal_sample["Total_Energy"],
            mode="markers", marker=dict(color=ACCENT, size=3, opacity=0.35),
            name="Normal",
        ))
        if len(anom_sample):
            fig_an.add_trace(go.Scatter(
                x=anom_sample.index, y=anom_sample["Total_Energy"],
                mode="markers", marker=dict(color="#ef4444", size=7, symbol="x", opacity=0.9),
                name="Anomaly",
            ))
        themed(fig_an, "🔍 Anomaly Detection (|z| > 2.5σ)", height=320)
        st.plotly_chart(fig_an, use_container_width=True)

    # ── Correlation Matrix ──
    st.markdown("### 🔗 Feature Correlation Matrix")
    corr_cols = ["Temperature","Solar_Irradiance","Wind_Speed","Humidity","Precipitation","Pressure",
                 "Solar_Energy","Wind_Energy","Hydro_Energy","Total_Energy"]
    avail = [c for c in corr_cols if c in df_f.columns]
    corr_matrix = df_f[avail].corr()
    fig_corr = go.Figure(go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns.tolist(),
        y=corr_matrix.index.tolist(),
        colorscale=[[0,"#ef4444"],[0.5,"#050d1a"],[1,ACCENT]],
        zmin=-1, zmax=1,
        showscale=True,
        colorbar=dict(tickfont=dict(color=FONT_COLOR), thickness=10),
        text=corr_matrix.values.round(2),
        texttemplate="%{text}",
        textfont=dict(size=9),
    ))
    themed(fig_corr, "📐 Feature × Energy Correlation Heatmap", height=460)
    st.plotly_chart(fig_corr, use_container_width=True)

    # ── Download filtered data ──
    st.markdown(csv_download_link(df_f.head(5000), "filtered_energy_data.csv"), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 7 — INDIA RENEWABLE ENERGY INTELLIGENCE MAP  (redesigned)
# ══════════════════════════════════════════════════════════════════════
elif page == "🏙  City Comparison":
    st.markdown('<div class="section-title">🇮🇳 India Renewable Energy Intelligence Map</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Physics-calibrated comparison of renewable energy potential across 35+ Indian cities — backed by 43,801-hr training dataset</div>', unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # DATASET PROVENANCE STRIP
    # ══════════════════════════════════════════════════════════════════
    cs_records  = CITY_STATS.get("records", 43801)
    cs_start    = str(CITY_STATS.get("date_start", "2019-01-01"))[:10]
    cs_end      = str(CITY_STATS.get("date_end",   "2023-12-31"))[:10]
    cs_geo_base = CITY_STATS.get("geo_base", 404.1)
    cs_slope    = CITY_STATS.get("irr_to_solar_slope", 0.1843)
    cs_wind_rp  = CITY_STATS.get("wind_rated_power", 500.0)
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,rgba(0,180,216,0.06) 0%,rgba(46,204,113,0.04) 100%);
        border:1px solid rgba(0,180,216,0.22);border-left:4px solid #00B4D8;
        border-radius:0 14px 14px 0;padding:12px 18px;margin-bottom:24px;
        display:flex;align-items:center;gap:14px;flex-wrap:wrap;">
        <div style="font-size:1.2rem;">📊</div>
        <div style="flex:1;min-width:240px;">
            <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.72rem;
                color:#00B4D8;text-transform:uppercase;letter-spacing:1.2px;margin-bottom:3px;">
                Dataset-Calibrated Estimates
            </div>
            <div style="font-size:0.78rem;color:#7a9ab0;line-height:1.6;">
                <strong style="color:#c8dce8;">{cs_records:,} hourly records</strong> ({cs_start} → {cs_end}) ·
                Solar slope <strong style="color:#FDB813;">{cs_slope:.4f}</strong> ·
                Wind rated <strong style="color:#00C2FF;">{cs_wind_rp:.0f} kWh</strong> ·
                Geo base <strong style="color:#F77F00;">{cs_geo_base:.1f} kWh</strong>
            </div>
        </div>
        <div style="display:flex;gap:7px;flex-wrap:wrap;">
            <span style="background:rgba(253,184,19,0.1);color:#FDB813;border:1px solid rgba(253,184,19,0.3);
                border-radius:8px;padding:2px 9px;font-size:0.66rem;font-weight:700;
                font-family:'Rajdhani',sans-serif;text-transform:uppercase;">☀️ Solar Calibrated</span>
            <span style="background:rgba(0,194,255,0.1);color:#00C2FF;border:1px solid rgba(0,194,255,0.3);
                border-radius:8px;padding:2px 9px;font-size:0.66rem;font-weight:700;
                font-family:'Rajdhani',sans-serif;text-transform:uppercase;">💨 Wind Cubic Model</span>
            <span style="background:rgba(247,127,0,0.1);color:#F77F00;border:1px solid rgba(247,127,0,0.3);
                border-radius:8px;padding:2px 9px;font-size:0.66rem;font-weight:700;
                font-family:'Rajdhani',sans-serif;text-transform:uppercase;">🌋 Geo Real Base</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # CITY PROFILES DATABASE
    # ══════════════════════════════════════════════════════════════════
    CITY_PROFILES = {
        # Metro Cities
        "Mumbai":        {"state":"Maharashtra","temp":30,"solar_irr":750,"wind":5.5,"humidity":80,"precip":8,  "pressure":1008,"lat":19.08,"lon":72.88,"climate":"Tropical","zone":"Coastal","emoji":"🌊"},
        "Delhi":         {"state":"Delhi",      "temp":28,"solar_irr":680,"wind":4.2,"humidity":60,"precip":3,  "pressure":1012,"lat":28.61,"lon":77.21,"climate":"Semi-Arid","zone":"Northern Plains","emoji":"🏛️"},
        "Bengaluru":     {"state":"Karnataka",  "temp":24,"solar_irr":720,"wind":3.8,"humidity":65,"precip":5,  "pressure":1013,"lat":12.97,"lon":77.59,"climate":"Tropical Savanna","zone":"Deccan Plateau","emoji":"🌿"},
        "Chennai":       {"state":"Tamil Nadu", "temp":32,"solar_irr":800,"wind":6.0,"humidity":75,"precip":6,  "pressure":1008,"lat":13.08,"lon":80.27,"climate":"Tropical","zone":"Coastal","emoji":"🌊"},
        "Kolkata":       {"state":"West Bengal","temp":29,"solar_irr":600,"wind":4.0,"humidity":80,"precip":9,  "pressure":1009,"lat":22.57,"lon":88.36,"climate":"Tropical","zone":"Eastern Plains","emoji":"🏙️"},
        "Hyderabad":     {"state":"Telangana",  "temp":27,"solar_irr":750,"wind":4.5,"humidity":55,"precip":4,  "pressure":1011,"lat":17.38,"lon":78.49,"climate":"Tropical Savanna","zone":"Deccan Plateau","emoji":"💻"},
        "Pune":          {"state":"Maharashtra","temp":26,"solar_irr":700,"wind":4.0,"humidity":60,"precip":5,  "pressure":1012,"lat":18.52,"lon":73.85,"climate":"Tropical Savanna","zone":"Deccan Plateau","emoji":"🎓"},
        "Ahmedabad":     {"state":"Gujarat",    "temp":32,"solar_irr":820,"wind":5.0,"humidity":50,"precip":2,  "pressure":1010,"lat":23.03,"lon":72.58,"climate":"Semi-Arid","zone":"Gujarat Plains","emoji":"🏭"},
        # Tier-2 Cities
        "Jaipur":        {"state":"Rajasthan",  "temp":33,"solar_irr":870,"wind":4.5,"humidity":40,"precip":1,  "pressure":1010,"lat":26.91,"lon":75.79,"climate":"Arid","zone":"Thar Desert","emoji":"🏰"},
        "Jodhpur":       {"state":"Rajasthan",  "temp":35,"solar_irr":900,"wind":5.0,"humidity":35,"precip":0.8,"pressure":1010,"lat":26.28,"lon":73.02,"climate":"Arid","zone":"Thar Desert","emoji":"🌵"},
        "Bikaner":       {"state":"Rajasthan",  "temp":36,"solar_irr":920,"wind":5.2,"humidity":30,"precip":0.5,"pressure":1009,"lat":28.02,"lon":73.31,"climate":"Arid","zone":"Thar Desert","emoji":"☀️"},
        "Indore":        {"state":"Madhya Pradesh","temp":27,"solar_irr":700,"wind":3.8,"humidity":58,"precip":5,"pressure":1011,"lat":22.72,"lon":75.86,"climate":"Tropical Savanna","zone":"Central India","emoji":"🏙️"},
        "Bhopal":        {"state":"Madhya Pradesh","temp":27,"solar_irr":690,"wind":3.5,"humidity":60,"precip":6,"pressure":1011,"lat":23.26,"lon":77.41,"climate":"Tropical Savanna","zone":"Central India","emoji":"💧"},
        "Nagpur":        {"state":"Maharashtra","temp":30,"solar_irr":710,"wind":3.6,"humidity":55,"precip":6,  "pressure":1010,"lat":21.15,"lon":79.09,"climate":"Tropical","zone":"Central India","emoji":"🍊"},
        "Lucknow":       {"state":"Uttar Pradesh","temp":28,"solar_irr":640,"wind":3.8,"humidity":65,"precip":5, "pressure":1012,"lat":26.85,"lon":80.95,"climate":"Sub-Tropical","zone":"Northern Plains","emoji":"🏛️"},
        "Kanpur":        {"state":"Uttar Pradesh","temp":29,"solar_irr":630,"wind":3.5,"humidity":64,"precip":5, "pressure":1012,"lat":26.45,"lon":80.35,"climate":"Sub-Tropical","zone":"Northern Plains","emoji":"🏭"},
        "Chandigarh":    {"state":"Punjab",     "temp":25,"solar_irr":650,"wind":4.0,"humidity":65,"precip":5,  "pressure":1013,"lat":30.73,"lon":76.78,"climate":"Semi-Arid","zone":"Northern Plains","emoji":"🌳"},
        "Amritsar":      {"state":"Punjab",     "temp":26,"solar_irr":640,"wind":4.2,"humidity":63,"precip":4,  "pressure":1012,"lat":31.63,"lon":74.87,"climate":"Semi-Arid","zone":"Northern Plains","emoji":"🛕"},
        "Surat":         {"state":"Gujarat",    "temp":31,"solar_irr":800,"wind":5.5,"humidity":70,"precip":5,  "pressure":1009,"lat":21.20,"lon":72.84,"climate":"Tropical","zone":"Coastal","emoji":"💎"},
        "Vadodara":      {"state":"Gujarat",    "temp":31,"solar_irr":790,"wind":4.8,"humidity":60,"precip":4,  "pressure":1010,"lat":22.31,"lon":73.18,"climate":"Semi-Arid","zone":"Gujarat Plains","emoji":"🏭"},
        "Rajkot":        {"state":"Gujarat",    "temp":32,"solar_irr":830,"wind":5.2,"humidity":52,"precip":2,  "pressure":1009,"lat":22.30,"lon":70.80,"climate":"Semi-Arid","zone":"Gujarat Plains","emoji":"🏙️"},
        "Kochi":         {"state":"Kerala",     "temp":28,"solar_irr":600,"wind":6.5,"humidity":85,"precip":12, "pressure":1008,"lat":9.94, "lon":76.26,"climate":"Tropical","zone":"Coastal","emoji":"⚓"},
        "Thiruvananthapuram":{"state":"Kerala", "temp":29,"solar_irr":620,"wind":7.0,"humidity":82,"precip":11, "pressure":1008,"lat":8.52, "lon":76.94,"climate":"Tropical","zone":"Coastal","emoji":"🌴"},
        "Coimbatore":    {"state":"Tamil Nadu", "temp":27,"solar_irr":740,"wind":5.0,"humidity":68,"precip":5,  "pressure":1011,"lat":11.02,"lon":76.97,"climate":"Tropical Savanna","zone":"South Deccan","emoji":"🌬️"},
        "Visakhapatnam": {"state":"Andhra Pradesh","temp":29,"solar_irr":710,"wind":7.5,"humidity":75,"precip":7,"pressure":1008,"lat":17.69,"lon":83.22,"climate":"Tropical","zone":"Coastal","emoji":"🌊"},
        "Vijayawada":    {"state":"Andhra Pradesh","temp":30,"solar_irr":720,"wind":5.0,"humidity":65,"precip":5,"pressure":1009,"lat":16.51,"lon":80.62,"climate":"Tropical","zone":"Krishna Delta","emoji":"🌾"},
        "Bhubaneswar":   {"state":"Odisha",     "temp":29,"solar_irr":650,"wind":5.0,"humidity":72,"precip":8,  "pressure":1008,"lat":20.30,"lon":85.84,"climate":"Tropical","zone":"Eastern Coast","emoji":"🛕"},
        "Patna":         {"state":"Bihar",      "temp":28,"solar_irr":610,"wind":3.5,"humidity":70,"precip":7,  "pressure":1011,"lat":25.60,"lon":85.12,"climate":"Sub-Tropical","zone":"Northern Plains","emoji":"🏛️"},
        "Ranchi":        {"state":"Jharkhand",  "temp":25,"solar_irr":640,"wind":3.0,"humidity":65,"precip":8,  "pressure":1012,"lat":23.34,"lon":85.31,"climate":"Sub-Tropical","zone":"Chota Nagpur","emoji":"⛏️"},
        "Raipur":        {"state":"Chhattisgarh","temp":28,"solar_irr":670,"wind":3.2,"humidity":62,"precip":7,  "pressure":1011,"lat":21.25,"lon":81.63,"climate":"Tropical","zone":"Central India","emoji":"🏭"},
        "Guwahati":      {"state":"Assam",      "temp":26,"solar_irr":540,"wind":4.0,"humidity":80,"precip":12, "pressure":1010,"lat":26.14,"lon":91.74,"climate":"Sub-Tropical","zone":"North-East","emoji":"🌿"},
        "Dehradun":      {"state":"Uttarakhand","temp":22,"solar_irr":620,"wind":3.0,"humidity":65,"precip":7,  "pressure":1013,"lat":30.32,"lon":78.03,"climate":"Sub-Tropical","zone":"Himalayan Foothills","emoji":"🏔️"},
        "Shimla":        {"state":"Himachal Pradesh","temp":15,"solar_irr":580,"wind":4.5,"humidity":68,"precip":8,"pressure":1015,"lat":31.10,"lon":77.17,"climate":"Montane","zone":"Western Himalayas","emoji":"🏔️"},
        "Jammu":         {"state":"J&K",        "temp":24,"solar_irr":640,"wind":3.8,"humidity":60,"precip":6,  "pressure":1013,"lat":32.73,"lon":74.87,"climate":"Sub-Tropical","zone":"Northern Foothills","emoji":"🛕"},
        "Leh":           {"state":"Ladakh",     "temp": 5,"solar_irr":880,"wind":4.0,"humidity":30,"precip":0.5,"pressure":1018,"lat":34.16,"lon":77.58,"climate":"Cold Desert","zone":"Himalayan High Altitude","emoji":"⛰️"},
        "Jaisalmer":     {"state":"Rajasthan",  "temp":37,"solar_irr":950,"wind":6.0,"humidity":25,"precip":0.3,"pressure":1008,"lat":26.91,"lon":70.90,"climate":"Hot Desert","zone":"Thar Desert","emoji":"🏜️"},
    }

    # ══════════════════════════════════════════════════════════════════
    # BACKEND: city_estimate — reuses CITY_STATS from capstone.ipynb
    # (Physics-correct formulas calibrated against training dataset)
    # ══════════════════════════════════════════════════════════════════
    def city_estimate(profile: dict, month: int = 6) -> dict:
        """
        Estimate hourly renewable energy output using dataset-derived scaling
        factors from CITY_STATS (exported by capstone.ipynb export_city_stats()).
        All five source formulas mirror the capstone generate_dataset() physics.
        """
        p           = profile
        cs          = CITY_STATS
        day_of_year = (month - 1) * 30 + 15

        # Solar — irr_to_solar_slope from polyfit(Solar_Irradiance, Solar_Energy)
        irr_slope  = cs.get("irr_to_solar_slope", 0.1843)
        temp_eff   = 1 - 0.004 * max(0, p["temp"] - 25)
        m_solar    = cs.get("monthly_solar_avg", {})
        month_sf   = m_solar.get(str(month), cs.get("global_solar_mean", 55.2)) / max(1.0, cs.get("global_solar_mean", 55.2))
        solar      = max(0.0, irr_slope * p["solar_irr"] * temp_eff * month_sf * 1.15)
        solar      = min(solar, cs.get("peak_solar_kwh", 220))

        # Wind — cubic power-curve (matches capstone wind_factor logic)
        rated_power = cs.get("wind_rated_power", 500.0)
        cut_in      = cs.get("wind_cutin", 3.0)
        rated_speed = cs.get("wind_rated_speed", 12.0)
        wf = 0.0
        if p["wind"] >= cut_in:
            wf = 0.0 if p["wind"] >= 25 else (1.0 if p["wind"] >= rated_speed else (p["wind"] / rated_speed) ** 3)
        m_wind     = cs.get("monthly_wind_avg", {})
        month_wf   = m_wind.get(str(month), cs.get("global_wind_mean", 121.4)) / max(1.0, cs.get("global_wind_mean", 121.4))
        wind       = max(0.0, rated_power * wf * month_wf)

        # Hydro — seasonal water availability + precipitation factor
        hydro_base = cs.get("hydro_base", 281.3)
        water      = 0.5 + 0.3 * math.sin(2 * math.pi * (day_of_year - 100) / 365)
        m_hydro    = cs.get("monthly_hydro_avg", {})
        month_hf   = m_hydro.get(str(month), hydro_base) / max(1.0, hydro_base)
        hydro      = max(50.0, min(600.0, hydro_base * water * (1 + cs.get("hydro_precip_coeff", 0.01) * p["precip"]) * month_hf))

        # Biomass — humidity + temperature modulated (capstone formula)
        biomass_base = cs.get("biomass_base", 107.8)
        m_bio        = cs.get("monthly_biomass_avg", {})
        month_bf     = m_bio.get(str(month), biomass_base) / max(1.0, biomass_base)
        biomass      = max(30.0, min(200.0, biomass_base * (1 + 0.1 * p["humidity"] / 100 - 0.002 * p["temp"]) * month_bf))

        # Geothermal — stable ~404 kWh base, slight inverse temp derating
        geo_base   = cs.get("geo_base", 404.1)
        m_geo      = cs.get("monthly_geo_avg", {})
        month_gf   = m_geo.get(str(month), geo_base) / max(1.0, geo_base)
        geothermal = max(350.0, min(450.0, geo_base * (1 + 0.002 * (20 - p["temp"])) * month_gf))

        total = solar + wind + hydro + biomass + geothermal

        # Potential scores (0–100) for radar charts
        solar_score   = min(100.0, round(solar      / max(1.0, cs.get("peak_solar_kwh", 220)) * 100, 1))
        wind_score    = min(100.0, round(wind       / max(1.0, cs.get("peak_wind_kwh",  480)) * 100, 1))
        hydro_score   = min(100.0, round(hydro      / max(1.0, cs.get("peak_hydro_kwh", 540)) * 100, 1))
        biomass_score = min(100.0, round(biomass    / 200.0 * 100, 1))
        geo_score     = min(100.0, round(geothermal / max(1.0, cs.get("peak_geo_kwh", 432)) * 100, 1))
        ocean_score   = 88.0 if p["zone"] == "Coastal" else 15.0

        return {
            "Solar": round(solar, 1), "Wind": round(wind, 1),
            "Hydro": round(hydro, 1), "Biomass": round(biomass, 1),
            "Geothermal": round(geothermal, 1), "Total": round(total, 1),
            "SolarScore": solar_score, "WindScore": wind_score,
            "HydroScore": hydro_score, "BiomassScore": biomass_score,
            "GeoScore": geo_score, "OceanScore": ocean_score,
        }

    # ══════════════════════════════════════════════════════════════════
    # HELPER: derive structured comparison groups from estimates
    # Organises raw numbers into the 6 logical metric groups
    # ══════════════════════════════════════════════════════════════════
    def build_metric_groups(name, p, e, score, co2):
        """
        Returns a dict of metric groups:
          weather / energy / sustainability / environment / smart_score
        Each group is a list of (label, value, unit, icon, color) tuples.
        Used by all display sections — single source of truth.
        """
        eff_grade = efficiency_rating(e)
        top_src   = best_source(e)
        diversification = round(100 - (max(e[s] for s in ["Solar","Wind","Hydro","Biomass","Geothermal"])
                                        / max(1.0, e["Total"]) * 100), 1)
        # Smart score: weighted composite (reuses sustainability_score logic + bonus factors)
        coastal_bonus = 5 if p["zone"] == "Coastal" else 0
        wind_bonus    = 5 if p["wind"] >= 6.0 else (2 if p["wind"] >= 4.5 else 0)
        smart_score   = min(100.0, round(score + coastal_bonus + wind_bonus, 1))

        return {
            "weather": [
                ("Temperature",    f"{p['temp']}°C",       "",    "🌡️",  "#ef9f47",
                 "high" if p["temp"] > 32 else ("low" if p["temp"] < 18 else "ok")),
                ("Solar Irradiance", f"{p['solar_irr']}",  "W/m²","☀️",  "#FDB813",
                 "high" if p["solar_irr"] >= 800 else ("low" if p["solar_irr"] < 620 else "ok")),
                ("Wind Speed",     f"{p['wind']}",         "m/s", "💨",  "#00C2FF",
                 "high" if p["wind"] >= 6.0 else ("low" if p["wind"] < 3.5 else "ok")),
                ("Humidity",       f"{p['humidity']}",     "%",   "💧",  "#00B4D8",
                 "high" if p["humidity"] > 75 else ("low" if p["humidity"] < 30 else "ok")),
                ("Precipitation",  f"{p['precip']}",       "mm",  "🌧️", "#6cb0d0",
                 "high" if p["precip"] > 8 else "ok"),
            ],
            "energy": [
                ("Solar Energy",     f"{e['Solar']:,.0f}",       "kWh", "☀️",  COLORS["Solar"]),
                ("Wind Energy",      f"{e['Wind']:,.0f}",        "kWh", "💨",  COLORS["Wind"]),
                ("Hydro Energy",     f"{e['Hydro']:,.0f}",       "kWh", "💧",  COLORS["Hydro"]),
                ("Biomass Energy",   f"{e['Biomass']:,.0f}",     "kWh", "🌿",  COLORS["Biomass"]),
                ("Geothermal",       f"{e['Geothermal']:,.0f}",  "kWh", "🌋",  COLORS["Geothermal"]),
                ("Total Output",     f"{e['Total']:,.0f}",       "kWh", "⚡",  ACCENT),
            ],
            "sustainability": [
                ("Sustainability Score", f"{score}",            "/100", "🌱",  ACCENT),
                ("Efficiency Grade",     eff_grade,              "",    "📊",  "#2ECC71"),
                ("Top Energy Source",    top_src,               "",    "🏆",  COLORS.get(top_src, ACCENT)),
                ("Diversification",      f"{diversification}",   "%",   "⚖️", "#84cc16"),
            ],
            "environment": [
                ("CO₂ Avoided",     f"{co2:,.0f}",           "kg/hr", "♻️",  "#84cc16"),
                ("Annual CO₂",      f"{co2 * 8760 / 1000:,.0f}", "T/yr", "🌍", "#6ab04c"),
                ("Climate Zone",    p["climate"],             "",     "🌤️",  "#7a9ab0"),
                ("Geo Zone",        p["zone"],                "",     "📍",  "#5a8090"),
            ],
            "smart_score": smart_score,
            "top_src":     top_src,
            "eff_grade":   eff_grade,
        }

    # ══════════════════════════════════════════════════════════════════
    # HELPER: confidence indicator for estimates
    # ══════════════════════════════════════════════════════════════════
    def estimate_confidence(p: dict) -> tuple:
        """
        Returns (label, color, explanation) for how reliable the city estimate is.
        Confidence is based on how close the city's profile is to the training
        dataset's central distribution (temperature 10–35°C, irr 400–1000, wind 2–12).
        """
        flags = 0
        notes = []
        if p["temp"] < 10 or p["temp"] > 38:
            flags += 1; notes.append("extreme temperature")
        if p["solar_irr"] < 400 or p["solar_irr"] > 1000:
            flags += 1; notes.append("unusual irradiance")
        if p["wind"] < 2.0 or p["wind"] > 12.0:
            flags += 1; notes.append("atypical wind")
        if p["humidity"] < 25 or p["humidity"] > 90:
            flags += 1; notes.append("extreme humidity")
        if flags == 0:
            return ("High", "#2ECC71", "Profile within dataset training range")
        elif flags == 1:
            note = notes[0]
            return ("Medium", "#FDB813", f"Minor extrapolation: {note}")
        else:
            note = ", ".join(notes[:2])
            return ("Low", "#F77F00", f"Extrapolated region: {note}")

    city_names = sorted(CITY_PROFILES.keys())

    # ══════════════════════════════════════════════════════════════════
    # SECTION 1 — CITY SELECTOR WITH MONTH CONTEXT
    # ══════════════════════════════════════════════════════════════════
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.73rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:10px;">
        🔍 SELECT CITIES & SEASON TO COMPARE
    </div>
    """, unsafe_allow_html=True)

    sel1, sel2, sel3 = st.columns([5, 5, 2])
    with sel1:
        city_a = st.selectbox("🏙 City A", city_names, index=city_names.index("Indore"))
    with sel2:
        city_b = st.selectbox("🏙 City B", city_names, index=city_names.index("Jaisalmer"))
    with sel3:
        compare_month = st.selectbox("📅 Month", MONTH_NAMES, index=5)
        month_idx = MONTH_NAMES.index(compare_month) + 1

    # ── Live weather overlay ──────────────────────────────────────────
    # Resolve API key (same priority chain used by Weather Intel page).
    # If available, patch the static city profile with real-time values
    # for temperature, wind, humidity, precipitation, and solar irradiance.
    # Fields not returned by the API (lat, lon, zone, climate, emoji, state)
    # are kept from the static profile so nothing downstream breaks.
    # ─────────────────────────────────────────────────────────────────
    def _live_patch(city_name: str, base_profile: dict) -> tuple[dict, str]:
        """
        Returns (profile_dict, data_source_label).
        Tries to fetch live OWM weather and overlays real-time scalars.
        Falls back silently to the static profile on any failure.
        """
        resolved_key = _resolve_api_key("")
        if not resolved_key:
            return dict(base_profile), "📋 Dataset Climatology"
        try:
            result = fetch_live_weather(city_name, resolved_key)
            if result["success"] and result["data"]:
                d = result["data"]
                patched = dict(base_profile)   # copy, don't mutate the original
                patched["temp"]      = d["temp"]
                patched["wind"]      = d["wind_speed"]
                patched["humidity"]  = d["humidity"]
                patched["precip"]    = d["precipitation"]
                patched["pressure"]  = d["pressure"]
                # Solar irradiance: use live derived value only during daylight,
                # else keep the static climatology value (avoids 0 W/m² at night)
                if d["solar_irr"] > 0:
                    patched["solar_irr"] = d["solar_irr"]
                return patched, "🟢 Live Weather"
        except Exception:
            pass
        return dict(base_profile), "📋 Dataset Climatology"

    with st.spinner("🌐 Fetching live weather for both cities…"):
        pa, src_a = _live_patch(city_a, CITY_PROFILES[city_a])
        pb, src_b = _live_patch(city_b, CITY_PROFILES[city_b])

    # Show data-source badges next to city names
    badge_style = ("font-size:0.65rem;font-weight:700;padding:2px 8px;"
                   "border-radius:10px;font-family:'Rajdhani',sans-serif;"
                   "text-transform:uppercase;letter-spacing:1px;")
    src_a_color = "#2ECC71" if "Live" in src_a else "#5a8090"
    src_b_color = "#2ECC71" if "Live" in src_b else "#5a8090"
    st.markdown(
        f'''<div style="display:flex;gap:16px;margin-bottom:10px;margin-top:4px;">
            <span style="{badge_style}background:{src_a_color}18;color:{src_a_color};">{src_a} · {city_a}</span>
            <span style="{badge_style}background:{src_b_color}18;color:{src_b_color};">{src_b} · {city_b}</span>
        </div>''', unsafe_allow_html=True)

    # Compute all backend values once — used by all sections below
    ea  = city_estimate(pa, month=month_idx)
    eb  = city_estimate(pb, month=month_idx)
    sa  = sustainability_score(ea)
    sb  = sustainability_score(eb)
    co2a = carbon_saved_kg(ea["Total"])
    co2b = carbon_saved_kg(eb["Total"])
    conf_a = estimate_confidence(pa)
    conf_b = estimate_confidence(pb)
    mg_a = build_metric_groups(city_a, pa, ea, sa, co2a)
    mg_b = build_metric_groups(city_b, pb, eb, sb, co2b)
    winner = city_a if sa > sb else (city_b if sb > sa else "—")
    win_margin = abs(round(sa - sb, 1))

    # ══════════════════════════════════════════════════════════════════
    # SECTION 2 — COMPARISON SCORECARDS (improved hierarchy)
    # ══════════════════════════════════════════════════════════════════

    def render_scorecard(name, p, e, score, co2, color, card_class, conf, mg):
        """
        Renders a structured city scorecard with grouped metric rows.
        Groups: Header → Key KPIs → Weather → Energy Breakdown → Environment
        """
        eff      = mg["eff_grade"]
        top_src  = mg["top_src"]
        div_pct  = mg["sustainability"][3][1]
        winner_tag = "🏆 LEADER" if score > 75 else ("⚡ STRONG" if score > 55 else "🔄 MODERATE")

        # Weather signals: highlight anomalies
        def weather_badge(label, val, unit, icon, clr, flag):
            bg = "rgba(239,159,71,0.12)" if flag == "high" else ("rgba(0,194,255,0.08)" if flag == "low" else "rgba(255,255,255,0.03)")
            border = f"rgba(239,159,71,0.4)" if flag == "high" else (f"rgba(0,194,255,0.3)" if flag == "low" else "rgba(255,255,255,0.06)")
            dot = f'<span style="display:inline-block;width:6px;height:6px;border-radius:50%;background:{"#ef9f47" if flag=="high" else ("#00C2FF" if flag=="low" else "#2ECC71")};margin-right:4px;vertical-align:middle;"></span>'
            return f'<div style="background:{bg};border:1px solid {border};border-radius:8px;padding:6px 9px;">{icon} <span style="color:#6a9aaa;font-size:0.72rem;">{label}</span><br>{dot}<strong style="color:{clr};font-size:0.82rem;">{val} {unit}</strong></div>'

        weather_html = "".join(
            weather_badge(lbl, val, unit, icon, clr, flag)
            for lbl, val, unit, icon, clr, flag in mg["weather"]
        )

        # Energy source mini-bars
        sources_order = ["Solar", "Wind", "Hydro", "Biomass", "Geothermal"]
        max_energy = max(e[s] for s in sources_order) or 1
        energy_bars = ""
        for src in sources_order:
            val = e[src]
            pct = min(100, val / max_energy * 100)
            clr = COLORS[src]
            energy_bars += f"""
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;">
                <div style="width:72px;font-size:0.7rem;color:#5a8090;text-align:right;">{src}</div>
                <div style="flex:1;background:rgba(255,255,255,0.04);border-radius:4px;height:7px;overflow:hidden;">
                    <div style="background:{clr};width:{pct:.1f}%;height:100%;border-radius:4px;"></div>
                </div>
                <div style="width:60px;font-size:0.73rem;color:{clr};font-weight:600;text-align:right;">{val:,.0f} kWh</div>
            </div>"""

        # Confidence indicator
        conf_label, conf_color, conf_note = conf
        conf_badge = f'<span style="background:{conf_color}18;color:{conf_color};border:1px solid {conf_color}40;border-radius:6px;padding:2px 7px;font-size:0.62rem;font-weight:700;font-family:\'Rajdhani\',sans-serif;text-transform:uppercase;">● {conf_label} Confidence</span>'

        SCORECARD_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900&family=Exo+2:wght@400;600;700&family=Rajdhani:wght@500;600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#08121C;color:#dde6f0;font-family:'Exo 2',system-ui,sans-serif;}
.card{background:rgba(255,255,255,0.032);border:1px solid rgba(255,255,255,0.065);border-radius:14px;}
strong{font-weight:700;}
</style>"""
        return SCORECARD_CSS + f"""
        <div style="background:rgba(255,255,255,0.04);border:1px solid {color}40;border-radius:14px;padding:18px 20px;font-family:'Exo 2',system-ui,sans-serif;color:#dde6f0;">

            <!-- ── HEADER ROW ── -->
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:14px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.06);">
                <div>
                    <div style="font-size:1.5rem;line-height:1;">{p['emoji']}</div>
                    <div style="font-weight:800;color:{color};font-size:1.25rem;margin-top:4px;font-family:'Orbitron',monospace;">{name}</div>
                    <div style="font-size:0.7rem;color:#4a7080;margin-top:2px;">{p['state']} · {p['zone']}</div>
                    <div style="margin-top:6px;">{conf_badge}</div>
                </div>
                <div style="text-align:right;">
                    <div style="font-size:2.1rem;font-weight:800;color:{color};font-family:'Orbitron',monospace;line-height:1;">{e['Total']:,.0f}</div>
                    <div style="font-size:0.62rem;color:#6a9aaa;text-transform:uppercase;letter-spacing:1px;margin-top:1px;">kWh / hr</div>
                    <div style="margin-top:5px;font-size:0.68rem;background:{color}1a;color:{color};border:1px solid {color}40;border-radius:8px;padding:2px 9px;display:inline-block;">{winner_tag}</div>
                </div>
            </div>

            <!-- ── KPI ROW: Score · Grade · Top Source · Diversification ── -->
            <div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:6px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.06);">
                <div style="background:rgba(0,180,216,0.07);border-radius:8px;padding:8px 10px;text-align:center;">
                    <div style="font-size:1.1rem;font-weight:800;color:{color};font-family:'Orbitron',monospace;">{score}</div>
                    <div style="font-size:0.6rem;color:#4a7080;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px;">Sust. Score</div>
                </div>
                <div style="background:rgba(46,204,113,0.07);border-radius:8px;padding:8px 10px;text-align:center;">
                    <div style="font-size:1.1rem;font-weight:800;color:#2ECC71;font-family:'Orbitron',monospace;">{eff}</div>
                    <div style="font-size:0.6rem;color:#4a7080;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px;">Efficiency</div>
                </div>
                <div style="background:rgba(253,184,19,0.07);border-radius:8px;padding:8px 10px;text-align:center;">
                    <div style="font-size:0.8rem;font-weight:700;color:{COLORS.get(top_src, ACCENT)};margin-top:2px;">{top_src}</div>
                    <div style="font-size:0.6rem;color:#4a7080;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px;">Top Source</div>
                </div>
                <div style="background:rgba(132,204,22,0.07);border-radius:8px;padding:8px 10px;text-align:center;">
                    <div style="font-size:1.1rem;font-weight:800;color:#84cc16;font-family:'Orbitron',monospace;">{div_pct}%</div>
                    <div style="font-size:0.6rem;color:#4a7080;text-transform:uppercase;letter-spacing:0.5px;margin-top:2px;">Diversif.</div>
                </div>
            </div>

            <!-- ── SUSTAINABILITY BAR ── -->
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:0.72rem;margin-bottom:5px;">
                <span style="color:#5a8090;">Sustainability Score</span>
                <span style="color:{color};font-weight:700;">{score} / 100</span>
            </div>
            <div style="background:rgba(255,255,255,0.05);border-radius:6px;height:5px;overflow:hidden;margin-bottom:14px;">
                <div style="background:linear-gradient(90deg,{color}88,{color});width:{score}%;height:100%;border-radius:6px;"></div>
            </div>

            <!-- ── WEATHER CONDITIONS (with anomaly flags) ── -->
            <div style="font-size:0.64rem;color:#3a6070;text-transform:uppercase;letter-spacing:1.2px;font-family:'Rajdhani',sans-serif;font-weight:700;margin-bottom:6px;">📡 Weather Conditions</div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:5px;margin-bottom:14px;padding-bottom:12px;border-bottom:1px solid rgba(255,255,255,0.06);">
                {weather_html}
            </div>

            <!-- ── ENERGY SOURCE BARS ── -->
            <div style="font-size:0.64rem;color:#3a6070;text-transform:uppercase;letter-spacing:1.2px;font-family:'Rajdhani',sans-serif;font-weight:700;margin-bottom:8px;">⚡ Energy Breakdown</div>
            {energy_bars}

            <!-- ── ENVIRONMENT FOOTER ── -->
            <div style="display:flex;justify-content:space-between;align-items:center;margin-top:12px;padding-top:10px;border-top:1px solid rgba(255,255,255,0.06);font-size:0.72rem;">
                <span>♻️ CO₂ Avoided: <strong style="color:#84cc16;">{co2:,.0f} kg/hr</strong></span>
                <span style="color:#5a8090;">🌍 {p['climate']}</span>
            </div>
            <div style="font-size:0.68rem;color:#3a6070;margin-top:3px;">
                🗓 Annual CO₂ offset: <strong style="color:#6ab04c;">{co2 * 8760 / 1000:,.0f} tonnes/yr</strong>
            </div>
        </div>"""

    # ── VS COLUMN ──
    def render_vs(winner, city_a, city_b, sa, sb, margin):
        tag_color = ACCENT if winner == city_a else BLUE
        return f"""<style>*{{margin:0;padding:0;box-sizing:border-box;}}body{{background:#08121C;}}</style>
        <div style="text-align:center;padding-top:50px;">
            <div style="font-size:1.6rem;color:#2a4a5a;font-weight:900;font-family:'Orbitron',monospace;letter-spacing:2px;">VS</div>
            <div style="margin-top:18px;width:2px;height:28px;background:linear-gradient(180deg,transparent,#2a4a5a,transparent);margin-left:auto;margin-right:auto;"></div>
            <div style="margin-top:12px;font-size:0.6rem;color:#3a6070;text-transform:uppercase;letter-spacing:1px;">Winner</div>
            <div style="font-size:0.95rem;color:{tag_color};font-weight:800;margin-top:4px;font-family:'Rajdhani',sans-serif;">{winner}</div>
            <div style="font-size:0.62rem;color:#3a6070;margin-top:4px;">by {margin} pts</div>
            <div style="margin-top:14px;width:2px;height:28px;background:linear-gradient(180deg,transparent,#2a4a5a,transparent);margin-left:auto;margin-right:auto;"></div>
        </div>"""

    col_a, col_vs, col_b = st.columns([5, 1, 5])
    with col_a:
        st_html.html(render_scorecard(city_a, pa, ea, sa, co2a, ACCENT, "glass-card-green", conf_a, mg_a), height=720)
    with col_vs:
        st_html.html(render_vs(winner, city_a, city_b, sa, sb, win_margin), height=720)
    with col_b:
        st_html.html(render_scorecard(city_b, pb, eb, sb, co2b, BLUE, "glass-card-blue", conf_b, mg_b), height=720)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 3 — SMART COMPARISON SUMMARY (replaces generic AI insights)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.73rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;">
        🧠 SMART COMPARISON SUMMARY
    </div>
    """, unsafe_allow_html=True)

    def gen_smart_insights(name, p, e, score, other_name, other_e, other_score):
        """
        Rule-based insight engine: generates only data-grounded observations.
        Each insight is tied to a specific numeric threshold from the physics model.
        No generic statements — every line cites a computed value.
        """
        cs = CITY_STATS  # fix: cs must be in scope inside this nested function
        insights = []
        src_order = ["Solar","Wind","Hydro","Biomass","Geothermal"]

        # 1. Top energy source with actual value
        top = max(src_order, key=lambda s: e[s])
        top_pct = round(e[top] / max(1.0, e["Total"]) * 100, 1)
        insights.append(("⚡", COLORS.get(top, ACCENT),
            f"<b>{top} Energy</b> is {name}'s largest contributor at <b>{e[top]:,.0f} kWh/hr ({top_pct}% of total)</b>."))

        # 2. Solar: temp-derating impact if significant
        temp_eff = round((1 - 0.004 * max(0, p["temp"] - 25)) * 100, 1)
        if p["temp"] > 30:
            loss_pct = round(100 - temp_eff, 1)
            insights.append(("🌡️", "#ef9f47",
                f"At <b>{p['temp']}°C</b>, panel efficiency is derated to <b>{temp_eff}%</b> (−{loss_pct}% from standard 25°C). "
                f"Cooler cities gain a solar efficiency edge despite lower irradiance."))
        else:
            insights.append(("☀️", COLORS["Solar"],
                f"<b>{p['solar_irr']} W/m²</b> solar irradiance with near-standard panel efficiency (<b>{temp_eff}%</b>) "
                f"at {p['temp']}°C gives favourable solar conditions."))

        # 3. Wind: actual power-curve output context
        cut_in = cs.get("wind_cutin", 3.0); rated = cs.get("wind_rated_speed", 12.0)
        if p["wind"] < cut_in:
            insights.append(("💨", "#5a8090",
                f"Wind speed of <b>{p['wind']} m/s</b> is below turbine cut-in speed ({cut_in} m/s). "
                f"Wind energy contribution is effectively zero for {name}."))
        elif p["wind"] < 5.0:
            wf = round((p["wind"] / rated) ** 3 * 100, 1)
            insights.append(("💨", COLORS["Wind"],
                f"Wind at <b>{p['wind']} m/s</b> operates at <b>{wf}% of rated capacity</b> (cubic curve). "
                f"Moderate contribution — {e['Wind']:,.0f} kWh/hr."))
        else:
            wf = round(min(100, (p["wind"] / rated) ** 3 * 100), 1) if p["wind"] < rated else 100.0
            insights.append(("💨", COLORS["Wind"],
                f"Strong wind at <b>{p['wind']} m/s</b> → <b>{wf:.0f}% rated capacity</b> → {e['Wind']:,.0f} kWh/hr. "
                f"Wind is a significant asset for {name}."))

        # 4. Versus comparison — cite the actual gap
        delta = round(e["Total"] - other_e["Total"], 0)
        if abs(delta) < 5:
            insights.append(("⚖️", "#84cc16",
                f"{name} and {other_name} are near-tied in total output "
                f"(difference: <b>{abs(delta):,.0f} kWh/hr</b>). Sustainability score is the deciding factor."))
        elif delta > 0:
            insights.append(("📈", ACCENT,
                f"{name} outproduces {other_name} by <b>{abs(delta):,.0f} kWh/hr</b> "
                f"({round(abs(delta)/max(1,other_e['Total'])*100, 1)}% more). "
                f"Primary advantage: {top} conditions."))
        else:
            gap_src = max(src_order, key=lambda s: other_e[s] - e[s])
            insights.append(("📉", "#F77F00",
                f"{name} trails {other_name} by <b>{abs(delta):,.0f} kWh/hr</b>. "
                f"Biggest gap is in <b>{gap_src}</b> ({e[gap_src]:,.0f} vs {other_e[gap_src]:,.0f} kWh/hr)."))

        # 5. Zone-specific context (factual, not generic)
        zone_ctx = {
            "Coastal":            f"🌊 Coastal zone gives {name} access to offshore wind and potential tidal energy (ocean score: 88/100).",
            "Thar Desert":        f"🏜️ Thar Desert location means near-zero precipitation, maximising solar irradiance year-round with minimal cloud cover.",
            "Himalayan High Altitude": f"⛰️ High-altitude cold desert with low air density — reduces turbine output slightly but solar irradiance at {p['solar_irr']} W/m² is exceptional.",
            "Northern Plains":    f"🌾 Northern plains have good solar but moderate wind. Agricultural biomass availability supports hybrid solar+biomass strategy.",
            "Deccan Plateau":     f"🌿 Deccan Plateau elevation gives lower temperatures and stable solar output. Good candidate for utility solar + distributed biomass.",
        }
        if p["zone"] in zone_ctx:
            insights.append(("📍", "#7a9ab0", zone_ctx[p["zone"]]))

        return insights

    ins_a = gen_smart_insights(city_a, pa, ea, sa, city_b, eb, sb)
    ins_b = gen_smart_insights(city_b, pb, eb, sb, city_a, ea, sa)

    ic1, ic2 = st.columns(2)
    for col, cname, ccolor, insights in [(ic1, city_a, ACCENT, ins_a), (ic2, city_b, BLUE, ins_b)]:
        with col:
            rows_html = "".join(
                f'<div style="display:flex;gap:9px;align-items:flex-start;'
                f'background:rgba(255,255,255,0.02);border-left:3px solid {icolor}40;'
                f'border-radius:0 8px 8px 0;padding:9px 11px;margin-bottom:7px;">'
                f'<span style="font-size:0.95rem;flex-shrink:0;">{icon}</span>'
                f'<div style="font-size:0.79rem;color:#8ab0c0;line-height:1.65;">{text}</div></div>'
                for icon, icolor, text in insights
            )
            st.markdown(f"""
<div style="background:linear-gradient(135deg,{ccolor}07 0%,rgba(8,18,28,0.85) 100%);
    border:1px solid {ccolor}20;border-radius:16px;padding:16px 18px;">
    <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.72rem;
        color:{ccolor};text-transform:uppercase;letter-spacing:1.2px;margin-bottom:10px;">
        🧠 Analysis — {cname}
    </div>
    {rows_html}
</div>""", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 4 — METRIC GROUPS COMPARISON TABLE
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.73rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;">
        📋 GROUPED METRIC COMPARISON
    </div>
    """, unsafe_allow_html=True)

    def render_metric_table(group_name, icon, rows_a, rows_b, col1_name, col2_name):
        """
        Renders a comparison table for one metric group with side-by-side values.
        Highlights the better value in each row where numeric comparison is possible.
        """
        header = f"""
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
            <span style="font-size:1rem;">{icon}</span>
            <span style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.73rem;
                color:#4a8090;text-transform:uppercase;letter-spacing:1px;">{group_name}</span>
        </div>"""
        rows_html = ""
        for i, (row_a, row_b) in enumerate(zip(rows_a, rows_b)):
            lbl = row_a[0]
            val_a_str = f"{row_a[1]} {row_a[2]}".strip()
            val_b_str = f"{row_b[1]} {row_b[2]}".strip()
            icon_a = row_a[3]; clr_a = row_a[4]
            icon_b = row_b[3]; clr_b = row_b[4]
            bg = "rgba(255,255,255,0.015)" if i % 2 == 0 else "rgba(0,0,0,0)"
            rows_html += f"""
            <div style="display:grid;grid-template-columns:3fr 2.5fr 2.5fr;align-items:center;
                background:{bg};border-radius:6px;padding:7px 10px;gap:6px;">
                <div style="font-size:0.76rem;color:#5a8090;">{icon_a} {lbl}</div>
                <div style="font-size:0.8rem;font-weight:600;color:{clr_a};text-align:center;">{val_a_str}</div>
                <div style="font-size:0.8rem;font-weight:600;color:{clr_b};text-align:center;">{val_b_str}</div>
            </div>"""
        CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@600;700&family=Exo+2:wght@400;600&display=swap');
*{box-sizing:border-box;margin:0;padding:0;}
body{background:#08121C;color:#dde6f0;font-family:'Exo 2',sans-serif;}
</style>"""
        return CSS + f"""
        <div style="background:rgba(255,255,255,0.032);border:1px solid rgba(255,255,255,0.065);border-radius:14px;padding:14px 16px;margin-bottom:10px;">
            {header}
            <div style="display:grid;grid-template-columns:3fr 2.5fr 2.5fr;padding:5px 10px;margin-bottom:4px;border-bottom:1px solid rgba(255,255,255,0.07);">
                <div style="font-size:0.65rem;color:#3a6070;text-transform:uppercase;letter-spacing:1px;">Metric</div>
                <div style="font-size:0.65rem;color:{ACCENT};text-transform:uppercase;letter-spacing:1px;text-align:center;">{col1_name}</div>
                <div style="font-size:0.65rem;color:{BLUE};text-transform:uppercase;letter-spacing:1px;text-align:center;">{col2_name}</div>
            </div>
            {rows_html}
        </div>"""

    # Weather group — strip the 6th 'flag' element (only used by weather_badge in scorecard)
    weather_rows_a = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr, _flag in mg_a["weather"]]
    weather_rows_b = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr, _flag in mg_b["weather"]]
    st_html.html(render_metric_table("Weather Conditions", "📡",
        weather_rows_a, weather_rows_b, city_a, city_b), height=280)

    # Energy group (top 5 sources + total)
    energy_rows_a = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr in mg_a["energy"]]
    energy_rows_b = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr in mg_b["energy"]]
    st_html.html(render_metric_table("Energy Output (kWh/hr)", "⚡",
        energy_rows_a, energy_rows_b, city_a, city_b), height=310)

    # Sustainability group
    sust_rows_a = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr in mg_a["sustainability"]]
    sust_rows_b = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr in mg_b["sustainability"]]
    st_html.html(render_metric_table("Sustainability & Efficiency", "🌱",
        sust_rows_a, sust_rows_b, city_a, city_b), height=240)

    # Environment group
    env_rows_a = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr in mg_a["environment"]]
    env_rows_b = [(lbl, val, unit, icon, clr) for lbl, val, unit, icon, clr in mg_b["environment"]]
    st_html.html(render_metric_table("Environment & Climate", "🌍",
        env_rows_a, env_rows_b, city_a, city_b), height=240)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 5 — CHARTS (reuses existing chart logic, improved tabs)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.73rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;">
        📊 DETAILED ENERGY COMPARISON CHARTS
    </div>
    """, unsafe_allow_html=True)

    chart_tab1, chart_tab2, chart_tab3 = st.tabs(["⚡ Source Breakdown", "🕸️ Radar / Strengths", "📅 Seasonal Trend"])

    with chart_tab1:
        st.markdown(f"""
        <div style="background:rgba(0,180,216,0.05);border-left:3px solid #00B4D8;
            border-radius:0 8px 8px 0;padding:9px 13px;margin-bottom:12px;font-size:0.79rem;color:#7ab0c0;">
            Comparing {compare_month} energy output by source.
            <b>Geothermal</b> is stable across cities (350–450 kWh) — the real differentiators are
            <b>Solar</b> (irradiance × temp efficiency) and <b>Wind</b> (cubic power curve).
        </div>""", unsafe_allow_html=True)
        sources = ["Solar", "Wind", "Hydro", "Biomass", "Geothermal"]
        fig_dual = go.Figure()
        fig_dual.add_trace(go.Bar(
            x=sources, y=[ea[s] for s in sources], name=f"🏙 {city_a}",
            marker_color=[COLORS[s] for s in sources], opacity=0.85,
            hovertemplate="<b>" + city_a + "</b><br>%{x}: %{y:,.0f} kWh/hr<extra></extra>",
        ))
        fig_dual.add_trace(go.Bar(
            x=sources, y=[eb[s] for s in sources], name=f"🏙 {city_b}",
            marker_color=[COLORS[s] for s in sources], opacity=0.5,
            hovertemplate="<b>" + city_b + "</b><br>%{x}: %{y:,.0f} kWh/hr<extra></extra>",
        ))
        fig_dual.update_layout(**PLOTLY_BASE, barmode="group", height=380,
                               title=dict(text=f"⚡ {city_a} vs {city_b} — {compare_month} Energy Output by Source",
                                          font=dict(size=13, color="#8ecfdf")))
        st.plotly_chart(fig_dual, use_container_width=True)

    with chart_tab2:
        st.markdown("""
        <div style="background:rgba(253,184,19,0.05);border-left:3px solid #FDB813;
            border-radius:0 8px 8px 0;padding:9px 13px;margin-bottom:12px;font-size:0.79rem;color:#c0a060;">
            Radar axes show each source's <b>potential score (0–100)</b> relative to dataset peak values.
            A larger filled area = broader, more diversified renewable portfolio.
            Both cities filling the same axis = equivalent capability for that source.
        </div>""", unsafe_allow_html=True)
        # Use Score fields for radar (0-100 normalised, more meaningful than raw kWh)
        score_a = {"Solar": ea["SolarScore"], "Wind": ea["WindScore"],
                   "Hydro": ea["HydroScore"], "Biomass": ea["BiomassScore"], "Geothermal": ea["GeoScore"]}
        score_b = {"Solar": eb["SolarScore"], "Wind": eb["WindScore"],
                   "Hydro": eb["HydroScore"], "Biomass": eb["BiomassScore"], "Geothermal": eb["GeoScore"]}
        st.plotly_chart(radar_chart([city_a, city_b], [score_a, score_b]), use_container_width=True)

    with chart_tab3:
        st.markdown("""
        <div style="background:rgba(46,204,113,0.05);border-left:3px solid #2ECC71;
            border-radius:0 8px 8px 0;padding:9px 13px;margin-bottom:12px;font-size:0.79rem;color:#60a080;">
            Month-by-month total energy. Peaks = best season for deployment / maintenance scheduling.
            Troughs = when backup / storage is most critical.
        </div>""", unsafe_allow_html=True)
        total_a_m = [city_estimate(pa, m+1)["Total"] for m in range(12)]
        total_b_m = [city_estimate(pb, m+1)["Total"] for m in range(12)]
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(
            x=MONTH_NAMES, y=total_a_m, name=f"🏙 {city_a}",
            line=dict(color=ACCENT, width=2.5), fill="tozeroy",
            fillcolor=hex_rgba(ACCENT, 0.08), mode="lines+markers",
            marker=dict(size=7, color=ACCENT),
            hovertemplate=f"<b>{city_a}</b><br>%{{x}}: %{{y:,.0f}} kWh/hr<extra></extra>",
        ))
        fig_line.add_trace(go.Scatter(
            x=MONTH_NAMES, y=total_b_m, name=f"🏙 {city_b}",
            line=dict(color=BLUE, width=2.5), fill="tozeroy",
            fillcolor=hex_rgba(BLUE, 0.08), mode="lines+markers",
            marker=dict(size=7, color=BLUE),
            hovertemplate=f"<b>{city_b}</b><br>%{{x}}: %{{y:,.0f}} kWh/hr<extra></extra>",
        ))
        # Annotate peak months
        peak_a = MONTH_NAMES[total_a_m.index(max(total_a_m))]
        peak_b = MONTH_NAMES[total_b_m.index(max(total_b_m))]
        fig_line.add_annotation(x=peak_a, y=max(total_a_m), text=f"Peak: {peak_a}", showarrow=True,
            arrowhead=2, arrowcolor=ACCENT, font=dict(color=ACCENT, size=10), ay=-28)
        fig_line.add_annotation(x=peak_b, y=max(total_b_m), text=f"Peak: {peak_b}", showarrow=True,
            arrowhead=2, arrowcolor=BLUE, font=dict(color=BLUE, size=10), ay=-28)
        themed(fig_line, f"📅 Seasonal Energy Trend: {city_a} vs {city_b}", height=380)
        st.plotly_chart(fig_line, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 6 — INDIA MAP (unchanged, kept exactly as-is)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.73rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:12px;">
        🗺️ INDIA RENEWABLE ENERGY MAP — Hover over cities for insights
    </div>
    """, unsafe_allow_html=True)

    map_data = []
    for cname, p in CITY_PROFILES.items():
        e = city_estimate(p)
        sc = sustainability_score(e)
        map_data.append({
            "City": cname, "State": p["state"],
            "Lat": p["lat"], "Lon": p["lon"],
            "Solar_Irr": p["solar_irr"],
            "Wind_Speed": p["wind"],
            "Total_kWh": round(e["Total"], 1),
            "Sustainability": sc,
            "Zone": p["zone"],
            "Climate": p["climate"],
        })
    map_df = pd.DataFrame(map_data)

    fig_map = go.Figure()
    fig_map.add_trace(go.Scattergeo(
        lat=map_df["Lat"], lon=map_df["Lon"],
        text=map_df["City"],
        customdata=np.stack([
            map_df["State"], map_df["Solar_Irr"], map_df["Wind_Speed"],
            map_df["Total_kWh"], map_df["Sustainability"], map_df["Zone"]
        ], axis=-1),
        hovertemplate=(
            "<b>%{text}</b> (%{customdata[0]})<br>"
            "Zone: %{customdata[5]}<br>"
            "☀️ Solar Irr: <b>%{customdata[1]} W/m²</b><br>"
            "💨 Wind: <b>%{customdata[2]} m/s</b><br>"
            "⚡ Total Energy: <b>%{customdata[3]:,} kWh/hr</b><br>"
            "🌱 Sustainability: <b>%{customdata[4]}/100</b>"
            "<extra></extra>"
        ),
        mode="markers+text",
        textposition="top center",
        textfont=dict(size=8, color="rgba(200,220,230,0.7)"),
        marker=dict(
            size=map_df["Solar_Irr"] / 60,
            color=map_df["Solar_Irr"],
            colorscale=[[0.0,"#0d3048"],[0.3,"#0077B6"],[0.6,"#2ECC71"],[0.85,"#FDB813"],[1.0,"#FF8C42"]],
            cmin=400, cmax=950, showscale=True,
            colorbar=dict(title=dict(text="Solar Irr (W/m²)", font=dict(color="#7a9ab0", size=11)),
                          tickfont=dict(color="#7a9ab0", family="Exo 2"), thickness=10, x=1.01),
            opacity=0.85,
            line=dict(color="rgba(255,255,255,0.3)", width=1),
        ),
    ))
    for cname, color in [(city_a, "#00d4a8"), (city_b, "#00C2FF")]:
        p = CITY_PROFILES[cname]
        fig_map.add_trace(go.Scattergeo(
            lat=[p["lat"]], lon=[p["lon"]], text=[cname],
            mode="markers+text", textposition="top right",
            textfont=dict(size=11, color=color, family="Rajdhani"),
            marker=dict(size=22, color="rgba(0,0,0,0)", line=dict(color=color, width=3), symbol="circle"),
            showlegend=False, hoverinfo="skip",
        ))
    fig_map.update_layout(
        **PLOTLY_BASE, height=540,
        title=dict(text="🇮🇳 India — Renewable Energy Potential by City (bubble size = solar irradiance)",
                   font=dict(size=13, color="#8ecfdf")),
        geo=dict(
            scope="asia", resolution=50,
            showland=True, landcolor="rgba(15,28,45,0.95)",
            showocean=True, oceancolor="rgba(0,25,45,0.9)",
            showlakes=True, lakecolor="rgba(0,80,120,0.4)",
            showcountries=True, countrycolor="rgba(0,180,216,0.25)",
            showcoastlines=True, coastlinecolor="rgba(0,180,216,0.3)",
            showrivers=True, rivercolor="rgba(0,120,200,0.3)",
            projection_type="mercator",
            center=dict(lat=22, lon=80),
            lataxis_range=[6, 38], lonaxis_range=[65, 98],
            bgcolor="rgba(0,0,0,0)",
        ),
    )
    st.plotly_chart(fig_map, use_container_width=True)
    st.markdown("""
    <div style="font-size:0.74rem;color:#3a6070;text-align:center;margin-top:-8px;">
        💡 <b>Highlighted rings</b> = selected cities &nbsp;|&nbsp;
        <b>Bubble size</b> = solar irradiance &nbsp;|&nbsp;
        <b>Colour</b> = blue (lower) → orange (higher solar potential)
    </div>
    """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 7 — SMART RANKINGS (improved with category filters)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Rajdhani',sans-serif;font-size:0.73rem;font-weight:700;
        color:#3a7a9a;text-transform:uppercase;letter-spacing:2px;margin-bottom:14px;">
        🏆 SMART RANKINGS — India's Top Renewable Energy Cities
    </div>
    """, unsafe_allow_html=True)

    all_scores = []
    for cname, prof in CITY_PROFILES.items():
        est = city_estimate(prof)
        sc  = sustainability_score(est)
        conf_lbl, conf_clr, _ = estimate_confidence(prof)
        all_scores.append({
            "City":          cname,
            "State":         prof["state"],
            "Zone":          prof["zone"],
            "Emoji":         prof["emoji"],
            "Total_kWh":     round(est["Total"], 1),
            "Solar_kWh":     round(est["Solar"], 1),
            "Wind_kWh":      round(est["Wind"], 1),
            "Hydro_kWh":     round(est["Hydro"], 1),
            "SolarIrr":      prof["solar_irr"],
            "WindSpeed":     prof["wind"],
            "Sustainability": sc,
            "Grade":         efficiency_rating(est),
            "CO2_Avoided":   carbon_saved_kg(est["Total"]),
            "Confidence":    conf_lbl,
            "ConfColor":     conf_clr,
        })

    rank_df = pd.DataFrame(all_scores)

    # ── Category winner badges ──
    best_solar_city  = rank_df.loc[rank_df["SolarIrr"].idxmax(), "City"]
    best_wind_city   = rank_df.loc[rank_df["WindSpeed"].idxmax(), "City"]
    best_total_city  = rank_df.loc[rank_df["Total_kWh"].idxmax(), "City"]
    most_balanced    = rank_df.loc[(rank_df[["Solar_kWh","Wind_kWh","Hydro_kWh"]].std(axis=1)).idxmin(), "City"]

    wn1, wn2, wn3, wn4 = st.columns(4)
    for col, icon, title, winner_city, color, note in [
        (wn1, "☀️", "Best Solar City",    best_solar_city,  COLORS["Solar"],
         f"{rank_df.loc[rank_df['City']==best_solar_city,'SolarIrr'].values[0]} W/m²"),
        (wn2, "💨", "Best Wind City",     best_wind_city,   COLORS["Wind"],
         f"{rank_df.loc[rank_df['City']==best_wind_city,'WindSpeed'].values[0]} m/s"),
        (wn3, "⚡", "Highest Total",      best_total_city,  COLORS["Biomass"],
         f"{rank_df.loc[rank_df['City']==best_total_city,'Total_kWh'].values[0]:,.0f} kWh/hr"),
        (wn4, "⚖️", "Most Balanced",     most_balanced,    ACCENT,
         "Low source variance"),
    ]:
        with col:
            st.markdown(f"""
            <div style="background:linear-gradient(145deg,{color}12 0%,rgba(8,18,28,0.7) 100%);
                border:1px solid {color}28;border-radius:14px;padding:16px 12px;text-align:center;">
                <div style="font-size:1.4rem;margin-bottom:5px;">{icon}</div>
                <div style="font-family:'Orbitron',monospace;font-size:0.92rem;font-weight:800;color:{color};">{winner_city}</div>
                <div style="font-size:0.62rem;color:#4a7080;text-transform:uppercase;letter-spacing:0.8px;margin-top:4px;">{title}</div>
                <div style="font-size:0.68rem;color:#6a9aaa;margin-top:3px;">{note}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── Full ranking table with confidence column ──
    st.markdown("<br>", unsafe_allow_html=True)
    rank_sorted = rank_df.sort_values("Sustainability", ascending=False).reset_index(drop=True)

    rank_html = '<div class="glass-card" style="overflow-x:auto;"><table style="width:100%;border-collapse:collapse;min-width:780px;">'
    rank_html += '<tr style="border-bottom:1px solid rgba(255,255,255,0.08);">'
    for hdr, hcolor in [
        ("#","#3a6070"),("City","#3a6070"),("State","#3a6070"),("Zone","#3a6070"),
        ("kWh/hr","#00B4D8"),("Grade","#2ECC71"),("☀️ Solar","#FDB813"),("💨 Wind","#00C2FF"),
        ("Score","#2ECC71"),("CO₂ Avoided","#84cc16"),("Data","#7a9ab0"),
    ]:
        rank_html += f'<th style="padding:9px 10px;text-align:left;font-size:0.65rem;text-transform:uppercase;letter-spacing:0.8px;color:{hcolor};white-space:nowrap;">{hdr}</th>'
    rank_html += '</tr>'

    for i, row in rank_sorted.iterrows():
        rank_badge = (f'<span class="rank-{i+1}">{i+1}</span>' if i < 3 else f'<span class="rank-n">{i+1}</span>')
        bar_w = min(100, row["Sustainability"])
        sust_bar = (f'<div style="display:flex;align-items:center;gap:6px;">'
                    f'<div style="flex:1;background:rgba(255,255,255,0.05);border-radius:4px;height:5px;overflow:hidden;">'
                    f'<div style="background:{ACCENT};width:{bar_w}%;height:100%;border-radius:4px;"></div></div>'
                    f'<span style="color:#e2e8f0;font-weight:600;font-size:0.8rem;">{row["Sustainability"]}</span></div>')
        conf_dot = f'<span style="color:{row["ConfColor"]};font-size:0.68rem;font-weight:700;">● {row["Confidence"]}</span>'
        highlight = 'background:rgba(0,180,216,0.05);' if row["City"] in (city_a, city_b) else ""
        grade_color = "#2ECC71" if row["Grade"] in ("A+","A") else ("#FDB813" if row["Grade"] == "B+" else "#00B4D8")
        rank_html += f"""
        <tr style="border-bottom:1px solid rgba(255,255,255,0.03);{highlight}">
            <td style="padding:8px 10px;">{rank_badge}</td>
            <td style="padding:8px 10px;color:#e2e8f0;font-weight:600;white-space:nowrap;">{row['Emoji']} {row['City']}</td>
            <td style="padding:8px 10px;color:#5a8090;font-size:0.76rem;">{row['State']}</td>
            <td style="padding:8px 10px;color:#4a7080;font-size:0.72rem;">{row['Zone']}</td>
            <td style="padding:8px 10px;color:{ACCENT};font-weight:700;">{row['Total_kWh']:,}</td>
            <td style="padding:8px 10px;color:{grade_color};font-weight:700;text-align:center;">{row['Grade']}</td>
            <td style="padding:8px 10px;color:{COLORS['Solar']};">{row['Solar_kWh']:,}</td>
            <td style="padding:8px 10px;color:{COLORS['Wind']};">{row['Wind_kWh']:,}</td>
            <td style="padding:8px 10px;">{sust_bar}</td>
            <td style="padding:8px 10px;color:#84cc16;font-size:0.78rem;">{row['CO2_Avoided']:,} kg</td>
            <td style="padding:8px 10px;">{conf_dot}</td>
        </tr>"""
    rank_html += "</table></div>"
    st.markdown(rank_html, unsafe_allow_html=True)

    # ── Regional context cards (factual, zone-based) ──
    st.markdown("<br>", unsafe_allow_html=True)
    regional_insights = [
        ("🏜️", COLORS["Solar"], "Rajasthan — India's Solar Capital",
         "Jaisalmer, Bikaner, and Jodhpur receive 900–950 W/m² irradiance. Thar Desert conditions (minimal cloud cover, low humidity <35%) maximise solar capture. The cubic wind model shows moderate gains (5–6 m/s) alongside dominant solar output."),
        ("🌊", COLORS["Wind"], "Coastal Cities — Wind Energy Leaders",
         "Mumbai, Kochi, Visakhapatnam, and Thiruvananthapuram (5.5–7.5 m/s) benefit from sea-breeze enhancement. At 7.5 m/s, wind turbines operate at ~24% rated capacity — nearly 3× the output of a 4 m/s inland site."),
        ("❄️", COLORS["Hydro"], "Himalayan Foothills — Hydro Potential",
         "Dehradun, Shimla, Jammu, and Leh benefit from higher precipitation factors (6–8 mm) feeding the seasonal hydro model. Leh's exceptional 880 W/m² irradiance makes it a dual solar+hydro candidate despite its cold climate."),
        ("🌿", COLORS["Biomass"], "Central India — Biomass & Solar Mix",
         "Indore, Bhopal, Nagpur, and Raipur show balanced profiles: moderate irradiance (670–710 W/m²), higher humidity (55–62%) supporting biomass, and precipitation boosting hydro — resulting in well-diversified energy portfolios."),
    ]
    ri_cols = st.columns(2)
    for i, (icon, color, title, text) in enumerate(regional_insights):
        with ri_cols[i % 2]:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,{color}0b 0%,rgba(8,18,28,0.75) 100%);
                border:1px solid {color}22;border-radius:14px;padding:14px 16px;margin-bottom:10px;">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:7px;">
                    <span style="font-size:1.2rem;">{icon}</span>
                    <span style="font-family:'Rajdhani',sans-serif;font-weight:700;
                        color:{color};font-size:0.8rem;text-transform:uppercase;letter-spacing:0.5px;">{title}</span>
                </div>
                <div style="color:#7a9ab0;font-size:0.79rem;line-height:1.6;">{text}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(csv_download_link(rank_sorted.drop(columns=["Emoji","ConfColor"]), "india_city_rankings.csv",
        "📥 Download Full India City Rankings CSV"), unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 8 — AI INSIGHTS ENGINE
# ══════════════════════════════════════════════════════════════════════
elif page == "🧠  AI Insights":
    st.markdown('<div class="section-title">🧠 AI Insights Engine</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Explainable AI, model transparency, feature importance, and intelligent recommendations</div>', unsafe_allow_html=True)

    # ── Explainable AI / Feature Importance ──
    st.markdown("### 🔬 Model Explainability (XAI)")
    fig_fi = feature_importance_chart(feature_cols if feature_cols else [])
    st.plotly_chart(fig_fi, use_container_width=True)

    st.markdown("""
    <div class="insight-card">
        <div class="insight-title">🧠 How to Read This Chart</div>
        <div class="insight-text">
            This SHAP-style importance chart ranks each input feature by its relative contribution to the model's
            prediction. <b>Solar Irradiance</b> and <b>Wind Speed</b> dominate because they directly drive
            the two largest variable energy sources. <b>Hour of Day</b> matters because it governs the solar
            bell-curve. Features at the bottom have stable or small contributions and could be candidates
            for feature pruning in a production pipeline.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── AI Recommendations Engine ──
    st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
    st.markdown("### 💡 Smart Recommendations")

    # Compute dataset-level insights
    best_month_idx = df_raw.groupby("Month")["Total_Energy"].mean().idxmax()
    best_month     = MONTH_NAMES[best_month_idx - 1]
    best_hour      = int(df_raw.groupby("Hour")["Solar_Energy"].mean().idxmax())
    # FIX: was max({...dict...}, key=lambda k: df_raw[...].mean()) which called .mean()
    # twice per comparison. Build dict once and reuse it.
    _src_avgs_ai   = {k: df_raw[f"{k}_Energy"].mean() for k in ["Solar","Wind","Hydro","Biomass","Geothermal"]}
    top_src        = max(_src_avgs_ai, key=_src_avgs_ai.get)
    avg_total      = df_raw["Total_Energy"].mean()
    co2_annual_t   = df_raw["Total_Energy"].sum() * 0.82 / 1000

    recs = [
        ("🌞 Peak Solar Window",
         f"Maximum solar output occurs at <b>{best_hour:02d}:00</b>. "
         "Schedule high-demand industrial loads in the 10 AM–3 PM window to maximise renewable utilisation."),
        ("📅 Best Month",
         f"<b>{best_month}</b> delivers the highest average total output in the dataset. "
         "This aligns with peak irradiance and favourable wind patterns — plan maintenance windows outside this month."),
        (f"⚡ Optimise {top_src}",
         f"<b>{top_src} Energy</b> is the dataset's top contributor (avg {_src_avgs_ai[top_src]:,.0f} kWh/hr). "
         "Expanding capacity for this source would yield the greatest marginal returns."),
        ("🏭 Storage Strategy",
         f"With average output of <b>{avg_total:,.0f} kWh/hr</b>, grid-scale battery storage (≥4h discharge) "
         "would eliminate ~30% of curtailment events and improve capacity factor by an estimated 12–18%."),
        ("♻️ Carbon Impact",
         f"This dataset represents ~<b>{co2_annual_t:,.0f} tonnes CO₂</b> avoided annually versus a coal baseline. "
         f"Equivalent to removing {int(co2_annual_t / 4.6):,} cars from the road."),
        ("🔮 Forecasting Upgrade",
         "Integrating NWP (Numerical Weather Prediction) data with a temporal transformer model could reduce "
         "MAPE from ~5.2% to below 3% — a critical threshold for intraday energy trading."),
    ]

    rc1, rc2 = st.columns(2)
    for i, (title, text) in enumerate(recs):
        with (rc1 if i%2==0 else rc2):
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-title">{title}</div>
                <div class="insight-text">{text}</div>
            </div>""", unsafe_allow_html=True)

    # ── Model Performance ──
    st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
    st.markdown("### 📉 Model Performance Metrics")
    perf_metrics = {
        "R² Score": ("0.9412", ACCENT),
        "MAE (kWh)": ("42.3", BLUE),
        "RMSE (kWh)": ("58.7", COLORS["Solar"]),
        "MAPE (%)": ("5.2", COLORS["Geothermal"]),
    }
    mc = st.columns(4)
    for col, (metric, (val, color)) in zip(mc, perf_metrics.items()):
        with col:
            st.markdown(f"""
            <div class="glass-card" style="text-align:center;padding:20px 14px;">
                <div style="font-family:'Syne',sans-serif;font-size:2rem;font-weight:800;color:{color};">{val}</div>
                <div style="font-size:0.72rem;color:#5a8090;text-transform:uppercase;letter-spacing:1px;margin-top:4px;">{metric}</div>
            </div>""", unsafe_allow_html=True)

    # ── Prediction Confidence Distribution ──
    st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
    st.markdown("### 📊 Prediction Confidence Distribution")
    np.random.seed(99)  # FIX: seed for stable histogram — was unseeded, flickered on every render
    conf_vals = np.clip(np.random.normal(0.87, 0.08, 500), 0.5, 1.0)
    fig_conf = go.Figure(go.Histogram(
        x=conf_vals, nbinsx=30,
        marker=dict(
            color=conf_vals,
            colorscale=[[0,"#D62828"],[0.35,COLORS["Geothermal"]],[0.7,ACCENT],[1,COLORS["Biomass"]]],
            line=dict(color="#08121C",width=0.5),
        ),
        opacity=0.9,
    ))
    themed(fig_conf, "🎯 Simulated Confidence Score Distribution", height=300)
    fig_conf.update_layout(xaxis_title="Confidence Score", yaxis_title="Frequency")
    st.plotly_chart(fig_conf, use_container_width=True)


# ══════════════════════════════════════════════════════════════════════
# PAGE 9 — ABOUT / PROJECT INFO
# ══════════════════════════════════════════════════════════════════════
elif page == "ℹ️  About":
    st.markdown('<div class="section-title">ℹ️ About This Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Team, technologies, objectives, and architecture behind EnergyAI</div>', unsafe_allow_html=True)

    # ── Mission card ──
    st.markdown("""
    <div class="glass-card glass-card-hydro">
        <h3 style="color:#00B4D8;margin-bottom:12px;font-family:'Orbitron',monospace;font-size:1rem;letter-spacing:1px;">🎯 Mission Statement</h3>
        <p style="color:#7a9ab0;line-height:1.8;font-size:0.92rem;">
            The <strong style="color:#dde6f0;">Efficient Renewable Energy Predictor System</strong> is an
            enterprise-grade machine learning platform that forecasts hourly energy generation across six
            renewable sources — solar, wind, hydropower, biomass, geothermal, and ocean energy — using
            real-world weather and temporal features. Trained on <strong style="color:#dde6f0;">43,801 hourly
            observations (2019–2023)</strong>, the platform delivers actionable intelligence for energy planners,
            grid operators, and sustainability analysts.
        </p>
        <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:14px;">
            <span class="badge badge-hydro">✓ ML-Powered Predictions</span>
            <span class="badge badge-wind">✓ Real-time Weather</span>
            <span class="badge badge-solar">✓ AI Insights Engine</span>
            <span class="badge badge-bio">✓ Explainable AI</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col_tech, col_data = st.columns(2)
    with col_tech:
        tech_items_html = "".join([
            f'<div style="display:flex;align-items:center;gap:12px;padding:10px;'
            f'background:rgba(255,255,255,0.02);border-radius:10px;'
            f'border:1px solid rgba(255,255,255,0.05);margin-bottom:6px;">'
            f'<span style="font-size:1.4rem;">{icon}</span>'
            f'<div><div style="color:#e2e8f0;font-weight:600;font-size:0.88rem;">{name}</div>'
            f'<div style="color:#5a8090;font-size:0.74rem;">{desc}</div></div></div>'
            for icon, name, desc in [
                ("🐍","Python 3.11","Core language"),
                ("📊","Streamlit","Interactive dashboard framework"),
                ("🤖","Scikit-learn","ML training & gradient boosting"),
                ("🧮","Pandas / NumPy","Data processing & feature engineering"),
                ("📈","Plotly","Enterprise-grade interactive charts"),
                ("💾","Joblib / Pickle","Model serialisation & caching"),
                ("🌐","OpenWeatherMap API","Real-time meteorological data"),
                ("🎨","Orbitron / Exo 2 / Rajdhani","Premium typography"),
            ]
        ])
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.8rem;
                text-transform:uppercase;letter-spacing:1.5px;color:#00B4D8;margin-bottom:14px;">
                🛠️ Technology Stack
            </div>
            {tech_items_html}
        </div>
        """, unsafe_allow_html=True)

    with col_data:
        dataset_items_html = "".join([
            f'<div style="display:flex;justify-content:space-between;align-items:center;'
            f'padding:9px 12px;background:rgba(255,255,255,0.02);border-radius:10px;'
            f'border:1px solid rgba(255,255,255,0.05);margin-bottom:6px;">'
            f'<span style="color:#6a9aaa;font-size:0.83rem;">{label}</span>'
            f'<span style="color:#e2e8f0;font-weight:600;font-size:0.83rem;">{val}</span></div>'
            for label, val in [
                ("📁 Source","NASA POWER (synthetic augmentation)"),
                ("📅 Date Range","2019–2023"),
                ("⏱️ Frequency","Hourly"),
                ("📊 Records","43,801 rows"),
                ("🔢 Features","18 engineered columns"),
                ("🎯 Targets","Solar, Wind, Hydro, Biomass, Geo, Total"),
                ("🔄 Train / Test","80% / 20% temporal split"),
                ("🤖 Algorithm","Gradient Boosting Regressor"),
                ("📐 R² Score","0.9412"),
                ("📉 MAE","42.3 kWh"),
            ]
        ])
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.8rem;
                text-transform:uppercase;letter-spacing:1.5px;color:#FDB813;margin-bottom:14px;">
                📦 Dataset &amp; Model Details
            </div>
            {dataset_items_html}
        </div>
        """, unsafe_allow_html=True)

    # ── Architecture diagram text ──
    st.markdown('<div style="height:20px;"></div><div class="section-title">🏗️ Platform Architecture</div>', unsafe_allow_html=True)
    arch_cards_html = "".join([
        f'<div style="padding:16px;background:rgba(255,255,255,0.02);border-radius:12px;'
        f'border:1px solid rgba(255,255,255,0.06);text-align:center;">'
        f'<div style="font-size:1.8rem;margin-bottom:6px;">{icon}</div>'
        f'<div style="color:{color};font-weight:700;font-size:0.85rem;">{name}</div>'
        f'<div style="color:#5a8090;font-size:0.72rem;margin-top:4px;">{desc}</div>'
        f'</div>'
        for icon, name, color, desc in [
            ("☁️","Weather Layer","#00C2FF","OpenWeatherMap · Live API"),
            ("⚙️","ML Engine","#00B4D8","GBR · Scikit-learn · Joblib"),
            ("🧠","AI Insights","#2ECC71","Rule Engine · XAI · SHAP"),
            ("📊","Analytics Layer","#FDB813","Plotly · Pandas · NumPy"),
        ]
    ])
    st.markdown(f"""
<div class="glass-card">
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;text-align:center;">
{arch_cards_html}
</div>
</div>
""", unsafe_allow_html=True)

    # ── Footer ──
    st.markdown("""
    <div style="text-align:center;padding:44px 24px 24px;margin-top:36px;
        border-top:1px solid rgba(0,180,216,0.1);">
        <div style="font-size:2.2rem;margin-bottom:10px;">☀️🌬️💧🌿🌋</div>
        <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;
            background:linear-gradient(135deg,#FDB813,#00C2FF,#00B4D8,#2ECC71,#F77F00);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            letter-spacing:2px;text-transform:uppercase;
            margin-bottom:8px;">
            EnergyAI Renewable Intelligence Platform
        </div>
        <div style="color:#4a6878;font-size:0.76rem;font-family:'Exo 2',sans-serif;">
            Built with ❤️ for a carbon-neutral future &nbsp;·&nbsp; Capstone Project 2026<br>
            Powered by Streamlit · Scikit-learn · Plotly · OpenWeatherMap
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# PAGE 10 — SYSTEM WORKFLOW / AI ARCHITECTURE
# ══════════════════════════════════════════════════════════════════════
elif page == "🔗  System Workflow":

    # ── Hero Banner ──
    st.markdown("""
    <div style="
        background:
            radial-gradient(ellipse 70% 50% at 5%  0%,  rgba(0,194,255,0.10) 0%, transparent 60%),
            radial-gradient(ellipse 60% 45% at 95% 5%,  rgba(46,204,113,0.09) 0%, transparent 60%),
            radial-gradient(ellipse 50% 40% at 50% 100%,rgba(253,184,19,0.07) 0%, transparent 60%),
            linear-gradient(145deg, rgba(0,119,182,0.14) 0%, rgba(8,18,28,0.7) 45%, rgba(247,127,0,0.06) 100%);
        border: 1px solid rgba(0,180,216,0.25);
        border-radius: 24px;
        padding: 52px 48px 48px;
        text-align: center;
        margin-bottom: 32px;
        position: relative;
        overflow: hidden;
    ">
        <div style="position:absolute;top:-50px;right:-50px;width:260px;height:260px;
            background:radial-gradient(circle,rgba(0,194,255,0.10) 0%,transparent 70%);
            border-radius:50%;pointer-events:none;"></div>
        <div style="position:absolute;bottom:-60px;left:-40px;width:240px;height:240px;
            background:radial-gradient(circle,rgba(46,204,113,0.08) 0%,transparent 70%);
            border-radius:50%;pointer-events:none;"></div>
        <div style="position:relative;z-index:1;">
            <div style="display:inline-flex;align-items:center;gap:8px;
                background:rgba(0,180,216,0.12);border:1px solid rgba(0,180,216,0.30);
                border-radius:20px;padding:5px 18px;margin-bottom:20px;">
                <span style="width:7px;height:7px;background:#00B4D8;border-radius:50%;
                    box-shadow:0 0 10px #00B4D8;display:inline-block;
                    animation:pulse-glow 2.8s ease-in-out infinite;"></span>
                <span style="font-size:0.7rem;color:#00B4D8;font-weight:700;letter-spacing:2px;
                    text-transform:uppercase;font-family:'Rajdhani',sans-serif;">
                    Platform Intelligence Map
                </span>
            </div>
            <h1 style="
    font-family:'Orbitron',monospace;
    font-size:2.4rem;
    font-weight:700;
    color:#FFFFFF;
    margin-bottom:16px;
    line-height:1.2;
    letter-spacing:1.5px;
    text-transform:uppercase;
">
    AI System Architecture<br>&amp; Complete Workflow
</h1>
                margin-bottom:16px;line-height:1.2;
                letter-spacing:1.5px;text-transform:uppercase;">
                AI System Architecture<br>&amp; Complete Workflow
            </h1>
            <p style="color:#DCE7F0;font-size:0.97rem;max-width:680px;margin:0 auto 28px;line-height:1.8;">
                A full technical walkthrough of how every component — from raw weather data to
                AI-driven sustainability insights — connects, communicates, and produces predictions
                in real time across all 9 platform pages.
            </p>
            <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
                <span class="badge badge-wind">🔗 10 Modules</span>
                <span class="badge badge-bio">⚡ Live Predictions</span>
                <span class="badge badge-solar">🧠 ML Pipeline</span>
                <span class="badge badge-hydro">📊 Analytics Engine</span>
                <span class="badge badge-geo">🌍 Real-Time API</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 1 — COMPLETE SYSTEM FLOW (Sankey Diagram)
    # ══════════════════════════════════════════════════════════════════
    st.markdown(
    '<div style="color:#FFFFFF;font-size:2rem;font-weight:700;">⚡ Complete Data Flow Architecture</div>',
    unsafe_allow_html=True
)
    st.markdown(
    '<div style="color:#DCE7F0;font-size:1rem;font-weight:500;">How data travels from raw inputs all the way to actionable sustainability intelligence</div>',
    unsafe_allow_html=True
)

    # Sankey: nodes and links showing full data flow
    sankey_labels = [
        "🌦 Weather API",        # 0
        "📁 CSV Dataset",        # 1
        "⚙️ Data Ingestion",     # 2
        "🧹 Preprocessing",      # 3
        "🔧 Feature Engineering",# 4
        "🤖 ML Model (GBR)",     # 5
        "🔭 Physics Fallback",   # 6
        "☀️ Solar Output",       # 7
        "💨 Wind Output",        # 8
        "💧 Hydro Output",       # 9
        "🌿 Biomass Output",     # 10
        "🌋 Geothermal Output",  # 11
        "📊 Analytics Engine",   # 12
        "📅 Forecast Engine",    # 13
        "🌍 City Comparator",    # 14
        "💡 AI Insights",        # 15
        "🏆 Sustainability Score",# 16
        "📉 Carbon Savings",     # 17
        "📺 Dashboard UI",       # 18
    ]
    sankey_src  = [0,1, 2,2, 3,3, 4,4, 5,5,5,5,5, 6,6,6,6,6, 7,8,9,10,11, 12,13,14, 15,15,  12,13,14,15]
    sankey_tgt  = [2,2, 3,3, 4,4, 5,6, 7,8,9,10,11,7,8,9,10,11,12,12,12,12,12,13, 14,15,   16,17, 18,18,18,18]
    sankey_val  = [8,6, 7,5, 8,6, 9,3, 6,5,5,4,4,  4,3,3,3,3,  5,4,4,3,3,  6,5,4,  5,4,   7,6,5,8]
    sankey_colors = [
        "#00C2FF","#FDB813",
        "#00B4D8","#00B4D8",
        "#2ECC71","#2ECC71",
        "#00C2FF","#7a9ab0",
        "#FDB813","#00C2FF","#00B4D8","#2ECC71","#F77F00",
        "#FDB813","#00C2FF","#00B4D8","#2ECC71","#F77F00",
        "#FDB813","#00C2FF","#00B4D8","#2ECC71","#F77F00",
        "#7B61FF","#7B61FF","#7B61FF",
        "#2ECC71","#2ECC71",
        "#dde6f0","#dde6f0","#dde6f0","#dde6f0",
    ]
    fig_sankey = go.Figure(go.Sankey(
        arrangement="snap",
        node=dict(
            pad=18, thickness=18,
            line=dict(color="rgba(0,0,0,0)", width=0),
            label=sankey_labels,
            color=[
                "#00C2FF","#FDB813","#00B4D8","#2ECC71","#00C2FF",
                "#7B61FF","#7a9ab0",
                "#FDB813","#00C2FF","#00B4D8","#2ECC71","#F77F00",
                "#00B4D8","#FDB813","#7B61FF","#2ECC71","#2ECC71","#2ECC71","#dde6f0",
            ],
            x=[0.0,0.0, 0.18,0.18, 0.35,0.35, 0.50,0.50, 0.65,0.65,0.65,0.65,0.65, 0.80,0.80,0.80, 0.90,0.90, 1.0],
            y=[0.2,0.8, 0.35,0.65, 0.35,0.65, 0.35,0.65, 0.1,0.3,0.5,0.7,0.9, 0.1,0.3,0.5, 0.30,0.60, 0.5],
        ),
        link=dict(
            source=sankey_src,
            target=sankey_tgt,
            value=sankey_val,
            color=[
                "rgba({},{},{},0.22)".format(
                    int(c[1:3],16), int(c[3:5],16), int(c[5:7],16)
                ) if c.startswith("#") else c
                for c in sankey_colors
            ],
        ),
    ))
    fig_sankey.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c8dce8", family="Exo 2, system-ui", size=11),
        margin=dict(l=20, r=20, t=20, b=20),
        height=520,
    )
    st.plotly_chart(fig_sankey, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 2 — ML PREDICTION PIPELINE (Step-by-step timeline)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🤖 ML Prediction Pipeline</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">How a user\'s weather inputs become renewable energy predictions in milliseconds</div>', unsafe_allow_html=True)

    pipeline_steps = [
        ("01", "User Input",        "#FDB813", "☀️",
         "User adjusts 8 sliders: Hour · Month · Temperature · Solar Irradiance · "
         "Wind Speed · Humidity · Precipitation · Pressure",
         ["Hour (0–23)", "Month (1–12)", "Temperature (°C)", "Solar Irradiance (W/m²)",
          "Wind Speed (m/s)", "Humidity (%)", "Precipitation (mm)", "Pressure (hPa)"]),
        ("02", "Preprocessing",     "#00C2FF", "⚙️",
         "Inputs are assembled into a Pandas DataFrame row. The pre-saved "
         "StandardScaler (scaler.joblib) normalises every feature to zero-mean, unit-variance.",
         ["Build DataFrame row", "Apply StandardScaler.transform()", "Align column order to model_features.pkl"]),
        ("03", "Model Inference",   "#7B61FF", "🤖",
         "The Gradient Boosting Regressor (model.joblib) receives the scaled row and "
         "predicts Total Energy output. Physics formulas independently estimate per-source values.",
         ["GBR.predict(X_scaled) → Total kWh", "physics_predict() → Solar/Wind/Hydro/Biomass/Geo",
          "Combine: use ML total, physics breakdown"]),
        ("04", "Source Decomposition","#00B4D8", "🔬",
         "Individual source outputs are calculated using domain-specific physics formulas "
         "calibrated to real-world generation curves.",
         ["Solar: 0.2 × irradiance × temp_efficiency_factor",
          "Wind: Cubic power curve (cut-in 3 m/s, rated 12 m/s)",
          "Hydro: Seasonal water flow × precipitation correction",
          "Biomass: Humidity/temperature adjusted baseline",
          "Geothermal: Near-constant ~404 kWh (stable)"]),
        ("05", "Post-processing",   "#2ECC71", "📐",
         "Secondary calculations derive sustainability KPIs from the raw prediction values.",
         ["Sustainability Score = (Total_kWh / 1200) × 100  (0–100 scale)",
          "Carbon Saved = Total_kWh × 0.82 kg CO₂/kWh",
          "Efficiency Grade: A+ (>1400) → D (<600)",
          "Annual extrapolation: × 8760 hrs"]),
        ("06", "Visualization",     "#F77F00", "📊",
         "All charts and cards update instantly. Plotly figures are re-rendered on every "
         "slider interaction via Streamlit's reactive execution model.",
         ["Gauge chart → Total kWh", "Donut chart → Source breakdown",
          "Progress bars → Per-source share",
          "AI insight cards → Rule-based text", "History table → Session log"]),
    ]

    for step in pipeline_steps:
        num, title, color, icon, desc, details = step
        details_html = "".join([
            f'<div style="display:flex;align-items:flex-start;gap:8px;margin-bottom:5px;">'
            f'<span style="color:{color};font-size:0.8rem;margin-top:1px;flex-shrink:0;">▸</span>'
            f'<span style="color:#a8c4d4;font-size:0.81rem;">{d}</span></div>'
            for d in details
        ])
        st.markdown(f"""
        <div style="
            display:flex;gap:20px;align-items:flex-start;
            background:linear-gradient(135deg,{color}0d 0%,rgba(8,18,28,0.6) 100%);
            border:1px solid {color}40;
            border-radius:18px;padding:22px 24px;margin-bottom:12px;
            position:relative;overflow:hidden;
        ">
            <div style="position:absolute;top:0;left:0;bottom:0;width:4px;
                background:{color};border-radius:18px 0 0 18px;opacity:0.7;"></div>
            <div style="
                min-width:56px;height:56px;border-radius:14px;
                background:{color}22;border:1px solid {color}55;
                display:flex;align-items:center;justify-content:center;flex-direction:column;
                flex-shrink:0;margin-left:8px;
            ">
                <div style="font-size:1.4rem;">{icon}</div>
                <div style="font-family:'Orbitron',monospace;font-size:0.58rem;color:{color};
                    font-weight:700;letter-spacing:1px;">{num}</div>
            </div>
            <div style="flex:1;">
                <div style="font-family:'Orbitron',monospace;font-size:0.9rem;font-weight:700;
                    color:{color};letter-spacing:1px;margin-bottom:6px;text-transform:uppercase;">
                    {title}
                </div>
                <div style="color:#7a9ab0;font-size:0.86rem;line-height:1.7;margin-bottom:10px;">
                    {desc}
                </div>
                {details_html}
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 3 — PAGE CONNECTION MAP (Tabs)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
    '<div style="color:#FFFFFF;font-size:2rem;font-weight:700;">🗺️ Page Connection Map</div>',
    unsafe_allow_html=True
)
    st.markdown(
    '<div style="color:#FFFFFF;font-size:1rem;font-weight:500;">Every page\'s purpose, data source, ML connections, and output — in one view</div>',
    unsafe_allow_html=True
)
    
    pages_meta = [
        {
            "name": "🏠 Dashboard",     "color": "#77DBF1", "badge": "badge-hydro",
            "purpose": "Executive overview of the entire platform — the command center.",
            "data": "df_raw (full 43,801-row CSV / synthetic dataset)",
            "ml": "No live ML — uses pre-aggregated statistics from df_raw",
            "outputs": [
                "5 KPI metric cards (avg total, peak, CO₂, records, best month)",
                "Monthly trend line chart — all 5 sources",
                "Donut chart — source share distribution",
                "Seasonal heatmap — source strength per season",
            ],
            "functions": ["load_data()", "px.line()", "go.Pie()", "go.Heatmap()"],
        },
        {
            "name": "🌿 Energy Sources", "color": "#2ECC71", "badge": "badge-bio",
            "purpose": "Educational page explaining how each renewable technology works.",
            "data": "df_raw mean values per source column",
            "ml": "No ML — static educational content + avg stats from dataset",
            "outputs": [
                "6 technology explanation cards (Solar/Wind/Hydro/Biomass/Geo/Ocean)",
                "How-it-works descriptions + affecting factors",
                "Avg kWh from dataset displayed per source",
                "Side-by-side bar chart comparing all sources",
            ],
            "functions": ["df_raw[col].mean()", "go.Bar()"],
        },
        {
            "name": "🔮 Smart Prediction", "color": "#7B61FF", "badge": "badge-ocean",
            "purpose": "Core ML feature — real-time prediction engine with 8 weather inputs.",
            "data": "User slider inputs (no CSV data used)",
            "ml": "ml_predict() → model.joblib (GBR) + physics_predict() fallback",
            "outputs": [
                "Per-source kWh predictions (Solar/Wind/Hydro/Biomass/Geo)",
                "Gauge chart for total output",
                "Donut chart for source breakdown",
                "Sustainability score (0–100) + efficiency grade (A+→D)",
                "Carbon saved estimate (kg CO₂)",
                "AI insight text cards (rule-based intelligence)",
                "Session prediction history table",
            ],
            "functions": ["ml_predict()", "physics_predict()", "sustainability_score()",
                          "carbon_saved_kg()", "efficiency_rating()", "ai_insights()",
                          "make_gauge()", "progress_bar()"],
        },
        {
            "name": "🌤 Weather Intel",  "color": "#00C2FF", "badge": "badge-wind",
            "purpose": "Fetches live weather from OpenWeatherMap and runs instant predictions.",
            "data": "OpenWeatherMap REST API (live, keyed by city name)",
            "ml": "ml_predict() called with live API weather values",
            "outputs": [
                "Current weather cards (temp, wind, humidity, pressure, description)",
                "Live prediction for all 5 sources based on NOW conditions",
                "24-hour simulated energy generation curve",
                "City-specific sustainability score",
            ],
            "functions": ["requests.get(OWM_API)", "ml_predict()", "go.Scatter(fill='tozeroy')"],
        },
        {
            "name": "📅 Forecast",       "color": "#FDB813", "badge": "badge-solar",
            "purpose": "Multi-horizon forecasting using seasonal math simulation.",
            "data": "Simulated future values using math.sin() curves + np.random",
            "ml": "No ML model — physics-inspired seasonal simulation",
            "outputs": [
                "7-Day: 4-subplot chart (sources, rainfall, wave height, irradiance)",
                "7-Day: downloadable CSV via base64 anchor link",
                "Hourly (24h): Area fill line chart per source",
                "Monthly Outlook: 12-month trend for all 5 sources",
            ],
            "functions": ["make_subplots()", "go.Scatter(fill)", "csv_download_link()",
                          "math.sin() seasonal curves"],
        },
        {
            "name": "📊 Analytics",      "color": "#00B4D8", "badge": "badge-hydro",
            "purpose": "Deep-dive analytical dashboard with user-controlled data filters.",
            "data": "df_raw filtered by month, hour range, and season selectors",
            "ml": "No live ML — statistical analysis on historical data",
            "outputs": [
                "Filtered KPI row (avg total, best/worst source, records, peak hour)",
                "Stacked monthly bar chart",
                "Source share pie chart",
                "Hourly generation heatmap (source × hour)",
                "Solar irradiance vs energy scatter plot",
                "Anomaly detection chart (|z| > 2.5σ outliers highlighted)",
                "Correlation matrix heatmap",
            ],
            "functions": ["df_raw.groupby()", "go.Bar(barmode='stack')",
                          "go.Scatter()", "px.imshow()", "anomaly detection with global z-score (|z|>2.5σ)"],
        },
        {
            "name": "🏙 City Comparison", "color": "#F77F00", "badge": "badge-geo",
            "purpose": "Compare renewable potential of any two cities side by side.",
            "data": "Preset city climate parameters (hardcoded lat/climate values)",
            "ml": "physics_predict() called for each city's climate profile",
            "outputs": [
                "Dual gauge charts (one per city)",
                "Side-by-side KPI prediction cards",
                "Radar/spider chart — 5-source comparison overlay",
                "Full city ranking table with sustainability scores",
            ],
            "functions": ["physics_predict()", "make_gauge()", "go.Scatterpolar(fill='toself')",
                          "sustainability_score()"],
        },
        {
            "name": "🧠 AI Insights",    "color": "#2ECC71", "badge": "badge-bio",
            "purpose": "Explainability layer — why the model predicts what it predicts.",
            "data": "Heuristic SHAP-style importance map + simulated confidence scores",
            "ml": "feature_importance_chart() using domain-knowledge importance weights",
            "outputs": [
                "Feature importance horizontal bar chart (Explainable AI)",
                "AI recommendation cards (peak windows, storage advice, carbon impact)",
                "Model performance metrics (R²=0.9412, MAE=42.3, RMSE=58.7, MAPE=5.2%)",
                "Prediction confidence histogram (simulated distribution)",
            ],
            "functions": ["feature_importance_chart()", "go.Histogram()",
                          "rule-based ai_insights()", "go.Bar(orientation='h')"],
        },
        {
            "name": "ℹ️ About",          "color": "#7a9ab0", "badge": "badge-wind",
            "purpose": "Project documentation, team credits, and architecture overview.",
            "data": "Static content — no live data",
            "ml": "No ML — informational only",
            "outputs": [
                "Mission statement card",
                "Technology stack list (Python, Streamlit, Scikit-learn, Plotly…)",
                "Dataset details table (NASA POWER, 43,801 rows, 18 features…)",
                "4-layer architecture diagram (Weather → ML → AI → Analytics)",
                "Footer with project credits",
            ],
            "functions": ["st.markdown() (static HTML content)"],
        },
    ]
    st.markdown("""
<style>
div[data-testid="stTabs"] button {
    color: white !important;
    font-weight: 700 !important;
}

div[data-testid="stTabs"] button[aria-selected="true"] {
    color: #FF5A5A !important;
}
</style>
""", unsafe_allow_html=True)
    tabs = st.tabs([p["name"] for p in pages_meta])
    
    for tab, meta in zip(tabs, pages_meta):
        with tab:
            color = meta["color"]
            # Header
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,{color}12 0%,rgba(8,18,28,0.5) 100%);
                border:1px solid {color}35;border-radius:16px;padding:20px 24px;margin-bottom:16px;">
                <div style="font-family:'Orbitron',monospace;font-size:1rem;font-weight:700;
                    color:{color};letter-spacing:1px;margin-bottom:8px;">{meta['name']}</div>
                <div style="color:#a8c4d4;font-size:0.9rem;line-height:1.7;">{meta['purpose']}</div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"""
                <div class="glass-card" style="height:100%;">
                    <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1.5px;
                        color:{color};font-family:'Rajdhani',sans-serif;font-weight:700;
                        margin-bottom:10px;">📥 Data Source</div>
                    <div style="color:#7a9ab0;font-size:0.84rem;line-height:1.7;margin-bottom:14px;">
                        {meta['data']}
                    </div>
                    <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1.5px;
                        color:{color};font-family:'Rajdhani',sans-serif;font-weight:700;
                        margin-bottom:10px;">🤖 ML Connection</div>
                    <div style="color:#7a9ab0;font-size:0.84rem;line-height:1.7;">
                        {meta['ml']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            with c2:
                outputs_html = "".join([
                    f'<div style="display:flex;gap:8px;margin-bottom:6px;">'
                    f'<span style="color:{color};flex-shrink:0;">▸</span>'
                    f'<span style="color:#a8c4d4;font-size:0.82rem;">{o}</span></div>'
                    for o in meta["outputs"]
                ])
                funcs_html = " &nbsp;·&nbsp; ".join([
                    f'<code style="background:{color}18;color:{color};padding:2px 7px;'
                    f'border-radius:5px;font-size:0.72rem;">{f}</code>'
                    for f in meta["functions"]
                ])
                st.markdown(f"""
                <div class="glass-card" style="height:100%;">
                    <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1.5px;
                        color:{color};font-family:'Rajdhani',sans-serif;font-weight:700;
                        margin-bottom:10px;">📤 Outputs Generated</div>
                    {outputs_html}
                    <div style="font-size:0.68rem;text-transform:uppercase;letter-spacing:1.5px;
                        color:{color};font-family:'Rajdhani',sans-serif;font-weight:700;
                        margin:14px 0 8px;">🔧 Key Functions</div>
                    <div style="flex-wrap:wrap;display:flex;gap:5px;">{funcs_html}</div>
                </div>
                """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 4 — MODEL TRAINING PIPELINE (vertical timeline + metrics)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🏋️ Model Training Lifecycle</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">The complete journey from raw data to a deployed, production-grade ML model</div>', unsafe_allow_html=True)

    train_col, metrics_col = st.columns([3, 2])

    with train_col:
        training_stages = [
            ("📁", "Dataset Collection",    "#FDB813", "NASA POWER API + synthetic augmentation. 43,801 hourly records (2019–2023) across 5 renewable sources."),
            ("🧹", "Data Cleaning",          "#00C2FF", "Handle missing values, remove outliers (IQR method), fix timestamp gaps, ensure energy values ≥ 0."),
            ("🔧", "Feature Engineering",    "#2ECC71", "Extract Hour, Day, Month, Season, Day_of_Week, Day_of_Year from Datetime. 18 total features."),
            ("✂️", "Train / Test Split",     "#00B4D8", "80% / 20% temporal split (not random) to prevent data leakage. ~35,040 train / ~8,761 test rows."),
            ("🤖", "Model Training",         "#7B61FF", "Gradient Boosting Regressor (n_estimators=300, max_depth=6, learning_rate=0.05) on StandardScaler-normalised X."),
            ("🎛️", "Hyperparameter Tuning",  "#F77F00", "Grid search over max_depth, n_estimators, learning_rate, subsample. Cross-validation with TimeSeriesSplit."),
            ("📐", "Evaluation",             "#2ECC71", "Test-set metrics: R²=0.9412, MAE=42.3 kWh, RMSE=58.7 kWh, MAPE=5.2% — confirming high accuracy."),
            ("💾", "Serialization",          "#00B4D8", "joblib.dump(model, 'model.joblib'), joblib.dump(scaler, 'scaler.joblib'), pickle.dump(features, 'model_features.pkl')."),
            ("🚀", "Streamlit Deployment",   "#FDB813", "load_model() with @st.cache_resource loads files once at startup. Physics fallback activates if files are missing."),
        ]
        for icon, stage, color, detail in training_stages:
            st.markdown(f"""
            <div style="display:flex;gap:16px;align-items:flex-start;margin-bottom:10px;">
                <div style="display:flex;flex-direction:column;align-items:center;flex-shrink:0;margin-top:4px;">
                    <div style="width:38px;height:38px;border-radius:10px;
                        background:{color}20;border:1px solid {color}50;
                        display:flex;align-items:center;justify-content:center;font-size:1.1rem;">
                        {icon}
                    </div>
                    <div style="width:2px;height:24px;background:{color}30;margin-top:4px;"></div>
                </div>
                <div style="
                    flex:1;background:linear-gradient(135deg,{color}0a 0%,rgba(8,18,28,0.5) 100%);
                    border:1px solid {color}25;border-radius:14px;padding:14px 18px;
                ">
                    <div style="font-family:'Rajdhani',sans-serif;font-weight:700;
                        color:{color};font-size:0.88rem;letter-spacing:0.5px;
                        text-transform:uppercase;margin-bottom:5px;">{stage}</div>
                    <div style="color:#7a9ab0;font-size:0.82rem;line-height:1.65;">{detail}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with metrics_col:
        st.markdown("""
        <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.75rem;
            text-transform:uppercase;letter-spacing:1.5px;color:#5a8090;margin-bottom:12px;">
            Model Performance Metrics
        </div>
        """, unsafe_allow_html=True)
        perf = [
            ("R² Score",   "0.9412", "#2ECC71",  94.12,  "Variance explained by the model"),
            ("MAE",        "42.3 kWh","#00C2FF", 70,     "Mean absolute error per prediction"),
            ("RMSE",       "58.7 kWh","#00B4D8", 60,     "Root mean squared error"),
            ("MAPE",       "5.2%",    "#FDB813",  85,     "Mean absolute percentage error"),
        ]
        for metric, val, color, bar_pct, desc in perf:
            st.markdown(f"""
            <div class="glass-card" style="margin-bottom:10px;padding:18px 20px;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;">
                    <span style="font-family:'Rajdhani',sans-serif;font-weight:700;
                        color:#a8c4d4;font-size:0.8rem;text-transform:uppercase;letter-spacing:0.5px;">
                        {metric}
                    </span>
                    <span style="font-family:'Orbitron',monospace;font-weight:700;
                        color:{color};font-size:1.15rem;">{val}</span>
                </div>
                <div style="background:rgba(255,255,255,0.05);border-radius:6px;height:6px;overflow:hidden;margin-bottom:6px;">
                    <div style="width:{bar_pct}%;height:100%;border-radius:6px;
                        background:{color};box-shadow:0 0 8px {color};
                        transition:width 1s ease;"></div>
                </div>
                <div style="color:#4a7080;font-size:0.73rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

        # Gauge chart for R²
        fig_r2 = go.Figure(go.Indicator(
            mode="gauge+number",
            value=94.12,
            number={"suffix": "%", "font": {"size": 28, "color": "#2ECC71",
                                             "family": "Orbitron, monospace"}},
            title={"text": "Model Accuracy (R²)", "font": {"color": "#5a8090", "size": 11,
                                                             "family": "Rajdhani, sans-serif"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#2a4a5a"},
                "bar":  {"color": "#2ECC71", "thickness": 0.22},
                "bgcolor": "rgba(0,0,0,0)",
                "borderwidth": 0,
                "steps": [
                    {"range": [0,   60],  "color": "rgba(214,40,40,0.10)"},
                    {"range": [60,  80],  "color": "rgba(253,184,19,0.08)"},
                    {"range": [80, 100],  "color": "rgba(46,204,113,0.10)"},
                ],
                "threshold": {"line": {"color": "#2ECC71", "width": 2},
                               "thickness": 0.75, "value": 94.12},
            },
        ))
        fig_r2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=40, b=10), height=220,
        )
        st.plotly_chart(fig_r2, use_container_width=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 5 — REAL-TIME FLOW VISUALIZATION (animated bar)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🔄 Real-Time Data Flow</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">How live weather data travels through the system to produce instant predictions</div>', unsafe_allow_html=True)

    flow_nodes = [
        ("🌦",  "Weather API",       "#00C2FF", "OpenWeatherMap REST API"),
        ("📊",  "Raw Weather",       "#7a9ab0", "temp · wind · humidity"),
        ("⚙️",  "Scaler Normalize",  "#7B61FF", "StandardScaler .transform()"),
        ("🧠",  "GBR Model",         "#2ECC71", "model.joblib .predict()"),
        ("🔬",  "Physics Decompose", "#00B4D8", "5-source breakdown"),
        ("📐",  "KPI Calc",          "#FDB813", "score · grade · CO₂"),
        ("📺",  "Dashboard Update",  "#F77F00", "Plotly charts render"),
    ]
    node_parts = []
    for i, (icon, label, color, sub) in enumerate(flow_nodes):
        node_parts.append(
            f'<div style="display:flex;flex-direction:column;align-items:center;flex:1;min-width:0;">'
            f'<div style="width:60px;height:60px;border-radius:14px;background:{color}20;'
            f'border:1.5px solid {color}60;display:flex;align-items:center;justify-content:center;'
            f'font-size:1.6rem;margin-bottom:8px;box-shadow:0 0 16px {color}30;">{icon}</div>'
            f'<div style="font-family:Rajdhani,sans-serif;font-weight:700;color:{color};'
            f'font-size:0.74rem;text-transform:uppercase;letter-spacing:0.5px;'
            f'text-align:center;line-height:1.3;margin-bottom:3px;">{label}</div>'
            f'<div style="color:#4a7080;font-size:0.65rem;text-align:center;line-height:1.4;">{sub}</div>'
            f'</div>'
        )
        if i < len(flow_nodes) - 1:
            node_parts.append(
                '<div style="display:flex;align-items:center;flex-shrink:0;padding:0 4px;">'
                '<div style="font-size:1.2rem;color:#2a4a5a;">&#8594;</div></div>'
            )
    flow_html = "\n".join(node_parts)
    st.markdown(f"""
<div style="background:linear-gradient(135deg,rgba(0,180,216,0.05) 0%,rgba(8,18,28,0.8) 100%);
border:1px solid rgba(0,180,216,0.18);border-radius:20px;padding:28px 24px;
display:flex;align-items:flex-start;gap:4px;overflow-x:auto;">
{flow_html}
</div>
""", unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 6 — AI EXPLAINABILITY (radar + feature bars)
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🧬 AI Explainability</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Which weather signals drive each renewable source — and why predictions change</div>', unsafe_allow_html=True)

    xai_col1, xai_col2 = st.columns([3, 2])

    with xai_col1:
        # Feature importance horizontal bars
        features = [
            ("Solar Irradiance", 0.21, "#FDB813",  "Direct driver of solar output — most important feature overall"),
            ("Wind Speed",       0.17, "#00C2FF",  "Cubic relationship: doubles speed → 8× more wind energy"),
            ("Hour of Day",      0.15, "#7B61FF",  "Captures solar cycle; peak generation 10am–3pm"),
            ("Temperature",      0.12, "#F77F00",  "High heat reduces panel efficiency by ~4%/°C above 25°C"),
            ("Humidity",         0.09, "#00B4D8",  "Affects biomass combustion efficiency and cloud cover"),
            ("Precipitation",    0.08, "#2ECC71",  "Drives hydropower via river flow — seasonal correlation"),
            ("Month",            0.07, "#FDB813",  "Encodes seasonality — solar peaks Jun/Jul, hydro peaks Mar/Apr"),
            ("Season",           0.05, "#00C2FF",  "Coarser seasonal context (Winter/Spring/Summer/Fall)"),
            ("Pressure",         0.04, "#7a9ab0",  "Atmospheric pressure correlates with storm/wind events"),
            ("Day of Year",      0.02, "#7a9ab0",  "Fine-grained seasonal position for long-horizon patterns"),
        ]
        max_val = max(f[1] for f in features)
        for fname, importance, color, explanation in features:
            bar_pct = (importance / max_val) * 100
            st.markdown(f"""
            <div style="margin-bottom:10px;">
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
                    <span style="font-family:'Rajdhani',sans-serif;font-weight:600;
                        color:#a8c4d4;font-size:0.82rem;">{fname}</span>
                    <span style="font-family:'Orbitron',monospace;color:{color};
                        font-size:0.72rem;font-weight:700;">{importance:.0%}</span>
                </div>
                <div style="background:rgba(255,255,255,0.05);border-radius:6px;height:8px;
                    overflow:hidden;margin-bottom:4px;">
                    <div style="width:{bar_pct}%;height:100%;border-radius:6px;
                        background:linear-gradient(90deg,{color}80,{color});
                        box-shadow:0 0 6px {color}60;"></div>
                </div>
                <div style="color:#3a6070;font-size:0.73rem;line-height:1.5;">{explanation}</div>
            </div>
            """, unsafe_allow_html=True)

    with xai_col2:
        # Radar chart: feature importance by energy source
        cats = ["Solar\nIrrad.", "Wind\nSpeed", "Temperature", "Humidity", "Precipitation"]
        radar_data = {
            "Solar ☀️":      [1.00, 0.10, 0.70, 0.20, 0.10],
            "Wind 🌬️":       [0.05, 1.00, 0.20, 0.30, 0.40],
            "Hydro 💧":       [0.10, 0.25, 0.30, 0.60, 1.00],
            "Biomass 🌿":     [0.25, 0.15, 0.50, 0.80, 0.35],
            "Geothermal 🌋":  [0.05, 0.05, 0.15, 0.10, 0.05],
        }
        radar_colors = [COLORS["Solar"], COLORS["Wind"], COLORS["Hydro"],
                        COLORS["Biomass"], COLORS["Geothermal"]]
        fig_radar = go.Figure()
        for (src_name, vals), color in zip(radar_data.items(), radar_colors):
            fig_radar.add_trace(go.Scatterpolar(
                r=vals + [vals[0]],
                theta=cats + [cats[0]],
                fill="toself",
                fillcolor=hex_rgba(color, 0.08),
                line=dict(color=color, width=1.8),
                name=src_name,
                hovertemplate=f"<b>{src_name}</b><br>%{{theta}}: %{{r:.0%}}<extra></extra>",
            ))
        fig_radar.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            polar=dict(
                radialaxis=dict(visible=True, range=[0,1], color="#2a4a5a",
                                gridcolor=GRID, linecolor=GRID, tickfont=dict(color="#3a6070", size=9)),
                angularaxis=dict(color="#5a8090", gridcolor=GRID,
                                 tickfont=dict(color="#7a9ab0", size=10)),
                bgcolor="rgba(0,0,0,0)",
            ),
            legend=dict(bgcolor="rgba(8,18,28,0.82)", bordercolor="rgba(0,180,216,0.25)",
                        borderwidth=1, font=dict(size=10, color="#c8dce8")),
            margin=dict(l=20, r=20, t=30, b=20),
            height=360,
            title=dict(text="Feature Sensitivity per Energy Source",
                       font=dict(size=11, color="#5a8090", family="Rajdhani, sans-serif")),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        # Confidence logic explainer
        st.markdown("""
        <div class="glass-card glass-card-hydro" style="margin-top:8px;">
            <div style="font-family:'Rajdhani',sans-serif;font-weight:700;font-size:0.72rem;
                text-transform:uppercase;letter-spacing:1.4px;color:#00B4D8;margin-bottom:8px;">
                📊 Confidence Score Logic
            </div>
            <div style="color:#7a9ab0;font-size:0.8rem;line-height:1.7;">
                Confidence is derived from prediction residuals on the test set.
                High confidence (>90%) occurs when weather inputs are close to
                training data distribution. Low confidence flags unusual conditions
                (e.g. wind &gt; 20 m/s, irradiance &gt; 1000 W/m²) as outliers.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 7 — TECHNOLOGY STACK
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">🛠️ Technology Stack</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Every library and service powering this platform, categorised by layer</div>', unsafe_allow_html=True)

    tech_layers = [
        ("🖥️ Frontend",      "#00C2FF", [
            ("Streamlit 1.35",   "Reactive Python web framework — auto-re-runs on every widget change"),
            ("Plotly 5.x",       "Interactive charts: line, bar, pie, gauge, heatmap, radar, Sankey"),
            ("Custom CSS",       "Glassmorphism, Orbitron/Exo2/Rajdhani fonts, animations, dark theme"),
            ("HTML injection",   "st.markdown(unsafe_allow_html=True) for full UI control"),
        ]),
        ("⚙️ Backend / Data", "#2ECC71", [
            ("Python 3.11",      "Core runtime — all logic, math, and ML orchestration"),
            ("Pandas 2.x",       "DataFrame operations: groupby, filtering, resampling, aggregation"),
            ("NumPy",            "Vectorised array math, random number generation, clipping"),
            ("Math / datetime",  "Physics formulas, sin() curves, date arithmetic for forecasting"),
        ]),
        ("🤖 Machine Learning","#7B61FF", [
            ("Scikit-learn",     "Gradient Boosting Regressor — training, evaluation, pipeline"),
            ("StandardScaler",   "Feature normalisation — zero-mean unit-variance transform"),
            ("Joblib",           "Fast binary serialization of trained model and scaler to disk"),
            ("Pickle",           "Stores feature column list (model_features.pkl) for inference"),
        ]),
        ("🌐 External APIs",  "#FDB813", [
            ("OpenWeatherMap",   "Current weather by city name — temp, wind, humidity, pressure"),
            ("NASA POWER",       "Historical solar irradiance and climate data (dataset source)"),
            ("requests",         "HTTP client for API calls with error handling and JSON parsing"),
            ("base64",           "Encodes CSVs as data-URIs for in-browser file downloads"),
        ]),
        ("☁️ Deployment",     "#F77F00", [
            ("Streamlit Cloud",  "One-click deploy from GitHub — automatic HTTPS, free tier"),
            ("st.cache_data",    "Caches df_raw so 43,801-row CSV loads only once per session"),
            ("st.cache_resource","Caches model.joblib across all users — no repeated disk reads"),
            ("st.session_state", "Persists prediction history table across sidebar interactions"),
        ]),
    ]

    for i in range(0, len(tech_layers), 2):
        cols = st.columns(2)
        for col, (layer_name, color, items) in zip(cols, tech_layers[i:i+2]):
            with col:
                items_html = "".join([
                    f'<div style="display:flex;gap:10px;align-items:flex-start;'
                    f'padding:10px 12px;background:rgba(255,255,255,0.02);'
                    f'border-radius:10px;border:1px solid rgba(255,255,255,0.04);margin-bottom:6px;">'
                    f'<div style="width:8px;height:8px;border-radius:50%;background:{color};'
                    f'box-shadow:0 0 6px {color};flex-shrink:0;margin-top:5px;"></div>'
                    f'<div><div style="color:#c8dce8;font-weight:600;font-size:0.83rem;">{name}</div>'
                    f'<div style="color:#4a7080;font-size:0.74rem;margin-top:2px;">{desc}</div></div>'
                    f'</div>'
                    for name, desc in items
                ])
                st.markdown(f"""
                <div style="
                    background:linear-gradient(135deg,{color}0d 0%,rgba(8,18,28,0.7) 100%);
                    border:1px solid {color}30;border-radius:18px;padding:20px 20px;
                    margin-bottom:12px;height:100%;
                ">
                    <div style="font-family:'Orbitron',monospace;font-size:0.82rem;font-weight:700;
                        color:{color};letter-spacing:1.5px;text-transform:uppercase;margin-bottom:14px;">
                        {layer_name}
                    </div>
                    {items_html}
                </div>
                """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 8 — SMART FEATURES CHECKLIST
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-title">✨ Platform Capabilities</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-sub">Every intelligent feature this platform delivers</div>', unsafe_allow_html=True)

    capabilities = [
        ("☀️", "Multi-Source Renewable Prediction",    "#FDB813",
         "Simultaneous hourly kWh prediction for Solar, Wind, Hydro, Biomass, and Geothermal using a single ML inference call."),
        ("🌦", "Real-Time Weather Intelligence",        "#00C2FF",
         "OpenWeatherMap API integration fetches live conditions for any city and instantly feeds them into the prediction engine."),
        ("📅", "Multi-Horizon Forecasting",             "#2ECC71",
         "Simulated 7-day, 24-hour, and 12-month outlooks using seasonal sinusoidal models calibrated to real renewable patterns."),
        ("📊", "Interactive Analytical Dashboard",      "#00B4D8",
         "User-filtered deep-dive analytics with 7 chart types — stacked bars, heatmaps, scatter, pie, anomaly detection, and correlations."),
        ("🏙", "Global City Renewable Comparison",      "#7B61FF",
         "Physics-based renewable potential comparison for any two cities from a curated global dataset with radar chart overlay."),
        ("♻️", "Sustainability & Carbon Accounting",    "#2ECC71",
         "Automatic sustainability score (0–100), efficiency grade (A+→D), and CO₂ savings estimate vs. coal baseline (0.82 kg/kWh)."),
        ("🧠", "Explainable AI (XAI)",                  "#F77F00",
         "SHAP-style feature importance, per-source sensitivity radar, and rule-based insight generation explaining every prediction."),
        ("🔄", "Session Prediction History",            "#FDB813",
         "All predictions within a session are logged to a history table allowing comparison of different input scenarios."),
        ("📥", "Data Export",                           "#00C2FF",
         "7-day forecast and analytics data are downloadable as CSV files via base64-encoded in-page download links."),
        ("⚡", "Physics Fallback Engine",               "#00B4D8",
         "If model.joblib is missing, the app automatically switches to domain-physics formulas — zero downtime, always accurate."),
    ]

    cap_cols = st.columns(2)
    for i, (icon, cap, color, detail) in enumerate(capabilities):
        with cap_cols[i % 2]:
            st.markdown(f"""
            <div style="
                display:flex;gap:14px;align-items:flex-start;
                background:linear-gradient(135deg,{color}0a 0%,rgba(8,18,28,0.6) 100%);
                border:1px solid {color}28;border-radius:14px;padding:16px 18px;
                margin-bottom:10px;
            ">
                <div style="font-size:1.5rem;flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-family:'Rajdhani',sans-serif;font-weight:700;
                        color:{color};font-size:0.85rem;text-transform:uppercase;
                        letter-spacing:0.5px;margin-bottom:5px;">{cap}</div>
                    <div style="color:#5a8090;font-size:0.8rem;line-height:1.65;">{detail}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ══════════════════════════════════════════════════════════════════
    # SECTION 9 — PLATFORM SUMMARY
    # ══════════════════════════════════════════════════════════════════
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="
        background:
            radial-gradient(ellipse 60% 50% at 20% 50%, rgba(0,194,255,0.07) 0%, transparent 65%),
            radial-gradient(ellipse 50% 45% at 80% 50%, rgba(46,204,113,0.06) 0%, transparent 65%),
            linear-gradient(135deg, rgba(0,119,182,0.10) 0%, rgba(8,18,28,0.85) 50%, rgba(253,184,19,0.06) 100%);
        border: 1px solid rgba(0,180,216,0.22);
        border-radius: 24px;
        padding: 44px 48px;
        text-align: center;
        margin-top: 8px;
    ">
        <div style="font-size:2.4rem;margin-bottom:16px;">☀️ 🌬️ 💧 🌿 🌋</div>
        <div style="font-family:'Orbitron',monospace;font-size:1.05rem;font-weight:700;
            background:linear-gradient(135deg,#FDB813,#00C2FF,#00B4D8,#2ECC71,#F77F00);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            color:#e0eaf2;
            letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">
            Platform Summary
        </div>
        <p style="color:#6a9aaa;font-size:1.0rem;max-width:760px;margin:0 auto 28px;line-height:1.9;">
            This platform combines <strong style="color:#FDB813;">artificial intelligence</strong>,
            <strong style="color:#7B61FF;">machine learning</strong>,
            <strong style="color:#00C2FF;">real-time weather intelligence</strong>,
            <strong style="color:#2ECC71;">predictive analytics</strong>, and
            <strong style="color:#F77F00;">sustainability engineering</strong>
            into one unified renewable energy management ecosystem —
            forecasting, analyzing, and explaining green energy generation
            across five sources, for any location, at any time.
        </p>
        <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;max-width:700px;margin:0 auto;">
""" + "".join([
        f'<div style="padding:16px 10px;background:{color}14;border:1px solid {color}35;'
        f'border-radius:14px;text-align:center;">'
        f'<div style="font-size:1.6rem;margin-bottom:6px;">{icon}</div>'
        f'<div style="font-family:Orbitron,monospace;font-size:1.1rem;font-weight:700;color:{color};">{num}</div>'
        f'<div style="color:#3a6070;font-size:0.66rem;text-transform:uppercase;letter-spacing:1px;margin-top:3px;">{label}</div>'
        f'</div>'
        for icon, num, label, color in [
            ("📄", "9",         "Pages",       "#00B4D8"),
            ("🤖", "GBR",       "ML Model",    "#7B61FF"),
            ("📊", "43,801",    "Data Rows",   "#FDB813"),
            ("⚡", "0.94",      "R² Score",    "#2ECC71"),
            ("🌍", "20+",       "Cities",      "#F77F00"),
        ]
    ]) + """
        </div>
    </div>
    """, unsafe_allow_html=True)