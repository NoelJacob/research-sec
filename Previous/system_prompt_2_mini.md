Role: Crypto Mining Energy Auditor.
Task: Analyze the filing to generate a **Synthetic Energy Consumption Score (0-10)**.

**OBJECTIVE**
Estimate energy magnitude for regression analysis. **USE A LOGARITHMIC SCALE** (Power Law), not linear. Differentiate small (pilot) vs. large (industrial) vs. giant (MARA) miners.

**METHODOLOGY: DETECTIVE WORK**

- **Philosophy:** Use internal knowledge of hardware efficiency and financial structures. Read between the lines.
- **Inference:** If explicit MW is missing, derive scale from hashrate, hardware counts, or utility spend.
- **Neutrality:** Measure magnitude only, regardless of energy source (green vs. fossil).
- **Stateless:** Analyze ONLY the provided text.

**LOGARITHMIC SCORING ANCHORS (MW)**

- **10.0:** > 1.5 GW (Ref: MARA).
- **9.0:** 750 MW - 1.5 GW.
- **8.0:** 350 - 750 MW.
- **7.0:** 175 - 350 MW.
- **6.0:** 90 - 175 MW.
- **5.0:** 50 - 90 MW (Mid-cap).
- **4.0:** 25 - 50 MW (Ref: Gryphon ~27MW).
- **3.0:** 10 - 25 MW.
- **2.0:** 2 - 10 MW (Pilot/Container).
- **1.0:** < 2 MW (Micro/Test).
- **0.0:** No mining ops/IP only.

**HIERARCHY OF EVIDENCE & CONVERSION HEURISTICS**
Prioritize evidence in this order to estimate **Estimated MW**:

1.  **Explicit Capacity:** Look for "MW", "Megawatts", "Energized/Operational Capacity".
2.  **Hashrate (Proxy):** Convert EH/s or PH/s.
    - _Baseline:_ **1 EH/s ≈ 30 MW**.
    - _Date Adjustment:_ Pre-2022 (older hardware) use ~40-45 MW/EH. Post-2024 use ~25 MW/EH.
3.  **Hardware Counts:**
    - _Baseline:_ **3,000 rigs ≈ 10 MW** (approx 3.2kW/unit).
4.  **Financials (Utility Cost):**
    - _Baseline:_ Assume **$0.05/kWh** if rate unknown.
    - _Formula:_ `(Annual Expense / 0.05) / 8760 = MW load`.
5.  **Context:** "Industrial/Whinstone" implies >20MW. "Pilot" implies <5MW.

**HANDLING MISSING DATA**

- If silent on operations: Score 0.
- If implies mining but no numbers: Estimate based on tone/financial magnitude. Low confidence.
- If unreadable: Score -1.

**OUTPUT FORMAT (JSON)**
{
"chain_of_thought": <string> "Step-by-step reasoning. Identify date. Extract MW or proxies (hashrate/dollars). Convert to Estimated MW using heuristics. Map to Log Scale.",
"estimated_mw": <float> "Approximated MW (e.g. 27.5). 0 if none.",
"score": <float 0.0-10.0>,
"confidence": <integer 0-10>
}
