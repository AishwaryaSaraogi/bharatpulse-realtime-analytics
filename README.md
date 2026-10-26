# 🇮🇳 BharatPulse — Real-Time Analytics Engine 📊

> **A real-time data streaming and analytics engine tracking city-specific commodity spot prices, bullion, fuel rates (INR ₹), and live meteorological telemetry across major Indian metropolitan hubs.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.37%2B-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75.svg)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Pytest](https://img.shields.io/badge/Pytest-Passing-brightgreen.svg)](test_app.py)

---

## 🌟 Overview

**BharatPulse** is an interactive multi-city monitoring platform designed to visualize regional financial commodities and environmental telemetry across India. It integrates asynchronous REST API ingestion with dynamic regional valuation models, providing localized rate differences across cities such as **New Delhi, Mumbai, Bengaluru, Kolkata, Ahmedabad, Jabalpur, and Hyderabad**.

The system features native auto-refresh triggers, client-side caching to prevent API rate-limiting, and unit-segmented Plotly visualizations.

---

## 🚀 Key Features

* **Live Meteorological Telemetry**: Ingests real-time temperature, relative humidity, wind velocity, and perceived "feels-like" metrics via the **Open-Meteo REST API**.
* **WMO Weather Code Decoding**: Dynamically parses World Meteorological Organization (WMO) numerical codes into descriptive sky conditions (`Clear Sky ☀️`, `Partly Cloudy 🌤️`, `Rainy 🌧️`, `Thunderstorm ⛈️`).
* **Automated Environmental Comfort Advice**: Evaluates real-time temperature and humidity vectors to calculate contextual health and comfort recommendations.
* **Unit-Segmented Financial Visualizations**:
  * **Bullion Rates**: 24K Gold (₹/10g) and Silver (₹/kg) separated with precise value annotations.
  * **Fuel Rates**: Petrol and Diesel pricing per Litre (₹/L) adjusted for state-level VAT.
  * **Historical Trendline**: 7-day comparative historical price trajectory for bullion assets.
* **Low-Latency Auto-Refresh**: Powered by Streamlit's native `@st.fragment(run_every=...)` architecture, avoiding full browser reloads.
* **Resilient Ingestion Pipeline**: In-memory caching (`@st.cache_data(ttl=300)`) with automated fallback to keep charts responsive under network failures.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technologies |
| :--- | :--- |
| **Frontend / UI** | Streamlit 1.37+, HTML5 / Markdown |
| **Visualizations** | Plotly Graph Objects (Interactive Dark Mode) |
| **Data Processing** | Python 3.10+, Pandas, Datetime |
| **Networking & APIs** | Requests, Open-Meteo REST API, CoinGecko Public Spot API |
| **Testing** | Pytest |

### System Architecture Flow:
```text
┌────────────────────────────────────────────────────────┐
│               Streamlit User Interface                 │
│         (Sidebar Controls & Dynamic Layout)            │
└───────────────▲────────────────────────▲───────────────┘
                │                        │
       [Graph Rendering]        [Fragment Auto-Sync]
                │                        │
┌───────────────┴────────────────────────┴───────────────┐
│               Data Engine (Data.py)                    │
├────────────────────────────────────────────────────────┤
│ ├── Open-Meteo API (Cached TTL=300s) -> Weather Data   │
│ ├── Spot Rate Ingestion (CoinGecko / Fallback Bench)   │
│ └── City Adjustment Matrix (State VAT / IBJA Deltas)   │
└────────────────────────────────────────────────────────┘
```
## 🕹️ Step-by-Step: How to Use & Control the Dashboard

### 1. Selecting a City
* Locate the **Regional & Sync Controls** panel in the left sidebar.
* Open the **Select Target City** dropdown menu.
* Select any supported Indian city (e.g., *Mumbai, New Delhi, Bengaluru, Ahmedabad, Kolkata, Jabalpur, Hyderabad*).
* **What happens:** The dashboard immediately recalibrates all bullion prices, local fuel prices (reflecting state taxes), and fetches real-time local weather coordinates.
* 
### 2. Controlling Auto-Refresh
* **Enable / Disable Auto-Sync:** Toggle the **Enable Auto Refresh** checkbox in the sidebar.
* **Adjust Refresh Rate:** Use the **Refresh Interval (Seconds)** slider to set intervals between **5 and 60 seconds**.
* **What happens:** The background fragment re-fetches live spot data automatically without flashing or reloading the whole page.
* 
### 3. Reading the Weather Telemetry
* Check the **Meteorological Telemetry** card to review current temperature, humidity, wind velocity, and cloud cover.
* Read the **Comfort Telemetry banner** (e.g., *"Pleasant & Highly Comfortable Weather"*, *"Hot conditions"*), which is calculated directly from the live temperature and humidity metrics.
* 
### 4. Interacting with Charts
* **Hover:** Place your mouse over any bar or line marker to inspect exact rates in Indian Rupees ($₹$).
* **Zoom & Pan:** Click and drag on any chart to zoom into specific time ranges or price bands.
* **Reset View:** Double-click anywhere inside the chart canvas to return to the default zoom level.
* **Inspect Raw Data:** Click the **"View Price Breakdown Table"** expander at the bottom to inspect raw values, units, and 24-hour percentage deltas.
* 
### 5. Manual Force Refresh
* Click the **"Manual Force Refresh"** button at the bottom of the page to trigger an instant on-demand sync cycle.
  
---

## 💻 Local Installation & Setup
### Prerequisites
* Python 3.10 or higher installed on your system.
* Git installed.
### Step 1: Clone the Repository
```bash
git clone https://github.com/AishwaryaSaraogi/bharatpulse-realtime-analytics.git
cd bharatpulse-realtime-analytics
```
### Step 2: Create and Activate a Virtual Environment
* **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **On macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Run the Application
```bash
streamlit run Dashboard.py
```
The application will launch in your default web browser at `http://localhost:8501`.

---

## 🧪 Running Unit Tests
Unit tests verify the WMO weather decoder, comfort assessment logic, and market data generation.
Run all tests using `pytest`:
```bash
pytest test_app.py
```
Expected output:
```text
============================= test session starts =============================
collected 7 items
test_app.py .......                                                      [100%]
============================== 7 passed in 0.42s ===============================
```
---

## 📂 Project Structure
```text
bharatpulse-realtime-analytics/
├── Dashboard.py       # Main Streamlit UI, sidebar controls & fragment orchestration
├── Data.py            # REST API ingestion, telemetry decoding, and city rate calculators
├── Graph.py           # Plotly visualization components and telemetry card displays
├── test_app.py        # Automated Pytest suite for business logic & decoders
├── requirements.txt   # Production dependencies
└── README.md          # Project documentation and control guide
```
