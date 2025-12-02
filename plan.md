# Context: Crypto Mining Energy Regression Project

## 1. Research Overview

I am conducting an econometric research project on **33 publicly traded cryptocurrency mining firms**. The objective is to run a regression analysis to determine the correlation between **Energy Consumption** (independent variable) and financial metrics like **P/E Ratios** and **Bitcoin Price**.

## 2. The Data Problem

A major hurdle in this sector is data opacity. While some firms explicitly state their energy capacity (in MW/GW), many do not. They often bury this information in regulatory filings (10-K, 8-K) using proxies such as:

- Hashrate (EH/s)
- Hardware counts (e.g., "15,000 S19j Pros")
- Financial utility costs (Cost of Revenues)

## 3. The Methodology: Synthetic Scoring via LLM

To solve the missing data problem, I am using **Gemini 3** to process unstructured text from regulatory filings and generate a **Synthetic Energy Consumption Score (0-10)**.

### The Scoring Logic (Logarithmic Scale)

Because the crypto mining industry follows a **Power Law distribution** (a few hyperscale giants like MARA, and a long tail of smaller miners), a linear scale is unsuitable for regression.

- **The Scale:** Logarithmic Magnitude.
- **The Anchor:** **MARA Holdings** (~1.74 GW) is the ceiling, represented as **10.0**.
- **The Low End:** A score of **0.0** represents no mining operations.
- **The Mid Range:** Gryphon Digital (~27 MW) represents a score of roughly **4.0**.

The LLM acts as a "Forensic Analyst," using chain-of-thought reasoning to infer MW capacity from proxies (hashrate, OpEx) when explicit numbers are missing.

## 4. Technical Pipeline Requirements

I need Python code to automate this process. The pipeline works as follows:

1.  **Input Data:** A dataset/folder containing text extracts from filings for the 33 firms over time.
2.  **LLM Interaction:**
    - Iterate through each filing text.
    - Send the text to the Gemini 3 API using a highly specific "Forensic Analyst" system prompt (provided separately).
    - **Constraint:** The process is **stateless**. The model does not remember previous filings; it scores based _only_ on the current text chunk.
3.  **Parsing:**
    - The LLM returns a JSON object containing: `chain_of_thought` (string), `estimated_mw` (float), `score` (float), and `confidence` (int).
    - The code must robustly parse this JSON, handling potential formatting errors.
4.  **Error Handling:**
    - If the LLM returns a score of `-1` (data unreadable), handle it gracefully.
    - Implement retries for API failures.
5.  **Output:**
    - A structured DataFrame/CSV containing: `Company`, `Filing_Date`, `Synthetic_Score`, `Estimated_MW`, `Confidence`, and `Reasoning`.

## 5. Specific Constraints for the Code

- **Model:** Google Gemini 3 (using `google-generativeai` library or Vertex AI).
- **Rate Limiting:** Must respect API quotas.
- **Cost Management:** Minimize token usage where possible (the prompt is already optimized).
- **Reproducibility:** Save the `chain_of_thought` for manual validation of outliers later.
