# Customer Loyalty & Engagement

A Streamlit demo dashboard for exploring customer engagement, explainable
segmentation, loyalty offers, email-draft review, and workflow audit history.
It uses fictional sample records to demonstrate a customer-intelligence
workflow; it is not connected to a live customer system.

## Demo features

- **Overview Dashboard** — customer and loyalty KPIs, segment and payment
  summaries, engagement trend, pending approvals, and recent activity.
- **Customer Analysis** — find a sample customer and review their activity,
  payment status, loyalty details, and communication preference.
- **Customer Segmentation** — filter customers and inspect the reason and
  confidence score for each rule-based segment.
- **AI Email Generation** — create a template-based draft from sample customer
  facts and an eligible offer. No external AI service is connected.
- **Human Review & Approval** — edit drafts, validate them, and record an
  approve, reject, or pending decision.
- **Audit Logs** — filter sample and current-session events by customer,
  status, and action.

## Run locally

You need Python and pip installed.

### Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run frontend/app.py
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run frontend/app.py
```

Streamlit prints a local URL in the terminal, typically
`http://localhost:8501`.

## Try the demo

1. Review the KPIs and charts on **Overview Dashboard**.
2. Open **Customer Analysis** and search for a customer ID such as
   `CUST-1001`.
3. Use **Customer Segmentation** to filter segments and review the rule
   explanations.
4. Open **AI Email Generation**, select an eligible customer, objective, and
   offer, then generate a draft.
5. Review the draft on **Human Review & Approval**. Validation rules include
   email opt-in, required subject and body, body length, offer eligibility,
   and payment-status restrictions.
6. See workflow activity on **Audit Logs**.

## Segmentation rules

Rules are evaluated in this order; the first matching rule assigns the
customer's segment:

1. **Payment Reminder** — payment is due or overdue.
2. **Dormant Customers** — no visits and at least 60 days since activity.
3. **Declining Activity** — previous-month visits were at least 4, and current
   visits are at most half of the previous month's visits.
4. **Loyalty Candidates** — at least 500 points and at least 4 visits this
   month.
5. **Consistent Customers** — none of the earlier rules matched.

## Deploy on Streamlit Community Cloud

1. Push this repository to GitHub and make sure Streamlit Community Cloud has
   access to it.
2. In Streamlit Community Cloud, create a new app and select this repository.
3. Set the branch to `main` and the main file path to `frontend/app.py`.
4. Deploy the app. Dependencies are listed in the root `requirements.txt`.

## Project structure

```text
.
├── .streamlit/
│   └── config.toml      # Theme configuration
├── frontend/
│   └── app.py           # Streamlit app, sample data, rules, and workflows
├── requirements.txt     # Python dependencies
└── README.md
```

## Demo limitations

- All customer records and preloaded activity are fictional.
- Drafts are generated from local templates and sample data; no email is sent.
- The review queue and audit activity are held in Streamlit session state.
  They are for demonstration only and are not durable storage.
- This project does not connect to a production CRM, payment system, email
  provider, database, or external AI service.
