# ⚡ GridMind

**Hybrid-Intelligence Smart Grid Platform** — an autonomous multi-agent dashboard concept for disaster-resilient energy management, built for a hackathon.

GridMind simulates how a smart power grid could **predict risk, negotiate energy allocation, self-heal, and explain its decisions** during an emergency (e.g. a flood knocking out normal supply), then shows the grid recovering and stabilizing in real time.

---

## 🧠 Concept

The demo walks through a full emergency-response lifecycle:

1. **Normal Mode** – grid runs with standard demand/supply metrics.
2. **🚨 Emergency Triggered** – simulated flood spikes hospital demand and transformer load.
3. **Risk Prediction** – congestion, hospital, and blackout risk are classified (LOW / MEDIUM / HIGH).
4. **Energy Negotiation** – battery and solar reserves are allocated to the hospital first; EV charging is deferred to cover the shortfall.
5. **Self-Healing** – the system "executes" a set of automated stabilization actions.
6. **Explainable AI** – each decision is shown alongside the reasons behind it.
7. **Resilience Recovery** – grid resilience score is tracked before vs. after intervention.
8. **Event Timeline** – a full audit trail of everything that happened during the incident.

## 🏗️ Architecture

```
smart_earth/
├── backend/
│   └── main.py          # FastAPI service — grid state, risk, negotiation, healing, explanations
├── fontend/              # Streamlit multi-page dashboard
│   ├── Home.py            # Landing page
│   ├── app.py             # Single-page prototype (all sections combined)
│   └── pages/
│       ├── 1_Grid_Overview.py       # Live metrics + map view
│       ├── 2_Risk_Analysis.py       # Risk prediction + explainability
│       ├── 3_Energy_Negotiation.py  # Battery/solar/EV allocation
│       ├── 4_Self_Healing.py        # Automated healing actions
│       └── 5_Recovery_Report.py     # Recovery, event log, impact summary
├── requirements.txt
└── LICENSE
```

- **Backend**: FastAPI serving grid telemetry and decision logic via REST endpoints.
- **Frontend**: Streamlit multi-page app that polls the backend and renders live dashboards, metrics, and a Pydeck map of grid risk.

> **Note:** This is a hackathon prototype. Backend responses are currently rule-based / mocked (fixed values and simple thresholds) to demonstrate the end-to-end workflow and UX — they are not powered by a trained model or live grid data yet. See [Roadmap](#-roadmap) below.

## 🔌 API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Health check |
| `/grid_status` | GET | Current grid metrics (normal mode) |
| `/simulate_emergency` | GET | Simulated flood-emergency grid metrics |
| `/predict_risk` | GET | Congestion / hospital / blackout risk levels |
| `/negotiate_energy` | GET | Battery + solar allocation to hospital, EV deferral |
| `/self_heal` | GET | List of automated self-healing actions |
| `/explain_decision` | GET | Explanation for the current AI decision |
| `/resilience_recovery` | GET | Before/after resilience score comparison |
| `/event_log` | GET | Full incident event timeline |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+

### Installation
```bash
git clone https://github.com/<your-username>/smart_earth.git
cd smart_earth
pip install -r requirements.txt
```

### Run the backend
```bash
cd backend
uvicorn main:app --reload
```
Backend runs at `http://localhost:8000`.

### Run the frontend
In a separate terminal:
```bash
cd fontend
streamlit run Home.py
```
Dashboard opens at `http://localhost:8501`.

### Try it out
1. Open the Streamlit app.
2. Click **🚨 Simulate Flood Emergency**.
3. Watch risk prediction, energy negotiation, self-healing, explainability, and resilience recovery play out across the pages.

## 🛠️ Tech Stack
- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit, Pydeck (map visualization)
- **Data handling:** Pandas
- **HTTP client:** Requests

## 🗺️ Roadmap
- [ ] Replace mocked backend logic with real risk-prediction models
- [ ] Connect to live/simulated sensor or grid data instead of hardcoded values
- [ ] Persist event logs (currently regenerated per request)
- [ ] Merge `app.py` (single-page prototype) into the multi-page app to remove duplication
- [ ] Rename `fontend/` → `frontend/`
- [ ] Add authentication and deployment config (Docker, env-based backend URL)

## 📄 License
This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

## 🙌 Acknowledgments
Built as a hackathon submission to explore how explainable, multi-agent AI could help power grids stay resilient during disasters.
