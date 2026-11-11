from datetime import datetime

import streamlit as st


st.set_page_config(
    page_title="Customer Loyalty & Engagement",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
)

# All records are fictional and exist only for this local demonstration.
CUSTOMERS = {
    "CUST-1001": {
        "name": "Avery Morgan",
        "visits": 8,
        "previous_visits": 7,
        "product": "Horizon Plus",
        "last_active": "2026-11-10",
        "days_inactive": 2,
        "payment_status": "Current",
        "loyalty_tier": "Gold",
        "points": 720,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1002": {
        "name": "Jordan Lee",
        "visits": 2,
        "previous_visits": 8,
        "product": "Horizon Standard",
        "last_active": "2026-10-25",
        "days_inactive": 18,
        "payment_status": "Current",
        "loyalty_tier": "Silver",
        "points": 340,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1003": {
        "name": "Taylor Brooks",
        "visits": 1,
        "previous_visits": 4,
        "product": "Horizon Plus",
        "last_active": "2026-10-18",
        "days_inactive": 25,
        "payment_status": "Payment due",
        "loyalty_tier": "Silver",
        "points": 410,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1004": {
        "name": "Casey Patel",
        "visits": 5,
        "previous_visits": 4,
        "product": "Horizon Standard",
        "last_active": "2026-11-07",
        "days_inactive": 5,
        "payment_status": "Payment due",
        "loyalty_tier": "Silver",
        "points": 480,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1005": {
        "name": "Riley Chen",
        "visits": 10,
        "previous_visits": 9,
        "product": "Horizon Plus",
        "last_active": "2026-11-11",
        "days_inactive": 1,
        "payment_status": "Current",
        "loyalty_tier": "Silver",
        "points": 590,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1006": {
        "name": "Quinn Davis",
        "visits": 0,
        "previous_visits": 1,
        "product": "Horizon Standard",
        "last_active": "2026-08-30",
        "days_inactive": 74,
        "payment_status": "Current",
        "loyalty_tier": "Member",
        "points": 120,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1007": {
        "name": "Sam Rivera",
        "visits": 6,
        "previous_visits": 5,
        "product": "Horizon Essentials",
        "last_active": "2026-11-08",
        "days_inactive": 4,
        "payment_status": "Current",
        "loyalty_tier": "Member",
        "points": 210,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1008": {
        "name": "Morgan Ellis",
        "visits": 9,
        "previous_visits": 10,
        "product": "Horizon Plus",
        "last_active": "2026-11-09",
        "days_inactive": 3,
        "payment_status": "Current",
        "loyalty_tier": "Gold",
        "points": 920,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1009": {
        "name": "Lee Thompson",
        "visits": 3,
        "previous_visits": 8,
        "product": "Horizon Essentials",
        "last_active": "2026-11-02",
        "days_inactive": 10,
        "payment_status": "Current",
        "loyalty_tier": "Member",
        "points": 180,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1010": {
        "name": "Parker Kim",
        "visits": 4,
        "previous_visits": 3,
        "product": "Horizon Standard",
        "last_active": "2026-11-06",
        "days_inactive": 6,
        "payment_status": "Current",
        "loyalty_tier": "Member",
        "points": 260,
        "email_opt_in": False,
        "preferred_channel": "No email",
    },
    "CUST-1011": {
        "name": "Jamie Wilson",
        "visits": 2,
        "previous_visits": 4,
        "product": "Horizon Essentials",
        "last_active": "2026-11-04",
        "days_inactive": 8,
        "payment_status": "Overdue",
        "loyalty_tier": "Member",
        "points": 140,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
    "CUST-1012": {
        "name": "Alex Bennett",
        "visits": 7,
        "previous_visits": 6,
        "product": "Horizon Plus",
        "last_active": "2026-11-09",
        "days_inactive": 3,
        "payment_status": "Current",
        "loyalty_tier": "Gold",
        "points": 680,
        "email_opt_in": True,
        "preferred_channel": "Email",
    },
}

SEGMENT_ORDER = [
    "Consistent Customers",
    "Declining Activity",
    "Dormant Customers",
    "Payment Reminder",
    "Loyalty Candidates",
]

SEGMENT_RULES = {
    "Payment Reminder": "Payment is due or overdue; payment rules take priority.",
    "Dormant Customers": "No recent visits and last activity was at least 60 days ago.",
    "Declining Activity": "Current-month visits are at most half of the previous month.",
    "Loyalty Candidates": "At least 500 points and 4 or more visits this month.",
    "Consistent Customers": "No higher-priority rule matched; activity is ongoing.",
}

OFFERS = {
    "No offer": {
        "description": "No promotional offer included.",
        "segments": SEGMENT_ORDER,
        "requires_current_payment": False,
    },
    "Welcome-back 10% offer": {
        "description": "An approved 10% welcome-back offer on the next eligible renewal.",
        "segments": ["Declining Activity", "Dormant Customers"],
        "requires_current_payment": True,
    },
    "Loyalty points boost": {
        "description": "An approved 100-point loyalty bonus on the next eligible renewal.",
        "segments": ["Loyalty Candidates"],
        "requires_current_payment": True,
    },
    "Member appreciation offer": {
        "description": "An approved 5% member appreciation offer on the next eligible renewal.",
        "segments": ["Consistent Customers", "Loyalty Candidates"],
        "requires_current_payment": True,
    },
}

OBJECTIVES = [
    "Re-engagement",
    "Payment reminder",
    "Loyalty appreciation",
    "Product education",
]

ENGAGEMENT_TREND = {
    "Week": ["Oct 01", "Oct 08", "Oct 15", "Oct 22", "Oct 29", "Nov 05", "Nov 12"],
    "Engagement score": [48, 53, 51, 62, 66, 72, 78],
}

SAMPLE_AUDIT_LOGS = [
    {
        "Timestamp": "2026-11-12 08:52",
        "Customer ID": "CUST-1002",
        "Action": "Email reviewed",
        "Segment": "Declining Activity",
        "Validation result": "Passed",
        "Reviewer decision": "Approved",
        "Status": "Approved — not sent",
    },
    {
        "Timestamp": "2026-11-11 16:30",
        "Customer ID": "CUST-1005",
        "Action": "Segment evaluated",
        "Segment": "Loyalty Candidates",
        "Validation result": "Passed",
        "Reviewer decision": "Not required",
        "Status": "Classified",
    },
    {
        "Timestamp": "2026-11-11 14:06",
        "Customer ID": "CUST-1004",
        "Action": "Email reviewed",
        "Segment": "Payment Reminder",
        "Validation result": "Passed",
        "Reviewer decision": "Rejected",
        "Status": "Rejected",
    },
    {
        "Timestamp": "2026-11-10 10:18",
        "Customer ID": "CUST-1006",
        "Action": "Segment evaluated",
        "Segment": "Dormant Customers",
        "Validation result": "Passed",
        "Reviewer decision": "Not required",
        "Status": "Classified",
    },
]


def classify_customer(customer):
    """Apply ordered, explainable business rules to one synthetic customer."""
    payment_status = customer["payment_status"]
    if payment_status in ("Payment due", "Overdue"):
        return "Payment Reminder", SEGMENT_RULES["Payment Reminder"], 0.99

    visits = customer["visits"]
    previous_visits = customer["previous_visits"]
    if customer["days_inactive"] >= 60 and visits == 0:
        return "Dormant Customers", SEGMENT_RULES["Dormant Customers"], 0.97

    if previous_visits >= 4 and visits * 2 <= previous_visits:
        return "Declining Activity", SEGMENT_RULES["Declining Activity"], 0.93

    if customer["points"] >= 500 and visits >= 4:
        return "Loyalty Candidates", SEGMENT_RULES["Loyalty Candidates"], 0.91

    return "Consistent Customers", SEGMENT_RULES["Consistent Customers"], 0.86


def get_customer_segment(customer):
    """Return the segment label for a customer."""
    return classify_customer(customer)[0]


def eligible_offers(customer):
    """List only offers allowed for the customer's segment and payment status."""
    segment = get_customer_segment(customer)
    return [
        offer_name
        for offer_name, offer in OFFERS.items()
        if segment in offer["segments"]
        and (
            not offer["requires_current_payment"]
            or customer["payment_status"] == "Current"
        )
    ]


def recommended_strategy(customer, objective):
    """Provide a brief, rule-based rationale for the selected objective."""
    segment = get_customer_segment(customer)
    if objective == "Payment reminder":
        return "Use a neutral account reminder and direct the customer to their account; do not include a promotion."
    if objective == "Re-engagement":
        return f"Use a low-pressure check-in tailored to the {segment.lower()} segment."
    if objective == "Loyalty appreciation":
        return (
            f"Thank the customer for their {customer['loyalty_tier']} membership "
            f"and {customer['points']} points."
        )
    return f"Offer a helpful follow-up about the customer's {customer['product']} plan."


def create_email_draft(customer_id, objective, offer_name):
    """Create a local template from verified demo facts and an approved offer."""
    customer = CUSTOMERS[customer_id]
    first_name = customer["name"].split()[0]
    segment, reason, confidence = classify_customer(customer)

    if objective == "Payment reminder":
        subject = "A reminder about your account"
        message = (
            f"Our records show your payment status is {customer['payment_status'].lower()}. "
            "Please review your account for the current details."
        )
    elif objective == "Re-engagement":
        subject = f"A note for you, {first_name}"
        message = (
            f"We noticed your last recorded activity was {customer['last_active']}. "
            "We would be glad to welcome you back whenever it suits you."
        )
    elif objective == "Loyalty appreciation":
        subject = "Thank you for being a valued member"
        message = (
            f"Thank you for being a {customer['loyalty_tier']} member. "
            f"Our records show you have {customer['points']} loyalty points."
        )
    else:
        subject = f"Your {customer['product']} plan"
        message = (
            f"We hope your {customer['product']} plan is working well for you. "
            "Our customer care team can help if you have questions about your plan."
        )

    offer_description = OFFERS[offer_name]["description"]
    if offer_name != "No offer":
        message += f" {offer_description}"

    body = (
        f"Hi {first_name},\n\n{message}\n\n"
        "If you prefer not to receive these messages, you can update your "
        "communication preferences in your account.\n\n"
        "Kind regards,\nCustomer Care Team"
    )
    return {
        "customer_id": customer_id,
        "segment": segment,
        "reason": reason,
        "confidence": confidence,
        "objective": objective,
        "strategy": recommended_strategy(customer, objective),
        "offer": offer_name,
        "offer_description": offer_description,
        "subject": subject,
        "body": body,
        "validation_result": "Not yet validated",
        "reviewer_decision": "Pending",
        "status": "Pending approval",
        "reviewer_comments": "",
        "created_at": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M"),
    }


def validate_email(email):
    """Check approval prerequisites; this does not send or semantically score email."""
    customer = CUSTOMERS[email["customer_id"]]
    issues = []
    if not customer["email_opt_in"]:
        issues.append("Customer has not opted in to email.")
    if not email["subject"].strip():
        issues.append("Subject is required.")
    if not email["body"].strip():
        issues.append("Email body is required.")
    if len(email["body"]) > 1200:
        issues.append("Email body must be 1,200 characters or fewer.")
    if email["offer"] not in eligible_offers(customer):
        issues.append("Offer is not eligible for this customer.")
    if email["objective"] == "Payment reminder" and customer["payment_status"] == "Current":
        issues.append("A payment reminder requires a due or overdue account.")
    if email["objective"] != "Payment reminder" and customer["payment_status"] != "Current":
        issues.append("Promotional communication is blocked while payment is due or overdue.")
    return issues


def make_audit_record(customer_id, action, validation_result, decision, status):
    """Create a consistent local audit record for a workflow action."""
    return {
        "Timestamp": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M"),
        "Customer ID": customer_id,
        "Action": action,
        "Segment": get_customer_segment(CUSTOMERS[customer_id]),
        "Validation result": validation_result,
        "Reviewer decision": decision,
        "Status": status,
    }


def initialize_session():
    """Seed a small review queue and audit history for an out-of-box demo."""
    if "email_queue" not in st.session_state:
        first_draft = create_email_draft("CUST-1002", "Re-engagement", "No offer")
        second_draft = create_email_draft("CUST-1004", "Payment reminder", "No offer")
        first_draft["email_id"] = "EMAIL-2001"
        second_draft["email_id"] = "EMAIL-2002"
        st.session_state.email_queue = [first_draft, second_draft]
    if "audit_records" not in st.session_state:
        st.session_state.audit_records = list(SAMPLE_AUDIT_LOGS)


def page_heading(title, description):
    st.markdown('<div class="eyebrow">CUSTOMER INTELLIGENCE PLATFORM</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="page-title">{title}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="page-description">{description}</p>', unsafe_allow_html=True)


def add_audit_record(record):
    st.session_state.audit_records.insert(0, record)


st.markdown(
    """
    <style>
    :root {
        --navy: #142b4a;
        --blue: #2f67ad;
        --muted: #64748b;
        --border: #e2e8f0;
        --canvas: #f5f7fb;
    }
    [data-testid="stAppViewContainer"] { background: var(--canvas); }
    [data-testid="stSidebar"] {
        background: #fff;
        border-right: 1px solid var(--border);
    }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stMainBlockContainer"] { max-width: 1440px; padding-top: 2rem; }
    [data-testid="stMetric"] {
        background: #fff;
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 18px 20px;
        min-height: 112px;
    }
    [data-testid="stMetricLabel"] { color: var(--muted); }
    [data-testid="stMetricValue"] { color: var(--navy); }
    h1, h2, h3, h4 { color: var(--navy); }
    .eyebrow {
        color: var(--blue);
        font-size: .73rem;
        font-weight: 700;
        letter-spacing: .12em;
        margin-bottom: .35rem;
    }
    .page-title { color: var(--navy); margin: 0 0 .25rem; }
    .page-description { color: var(--muted); margin: 0 0 1.5rem; }
    .stButton > button {
        border-radius: 8px;
        border: 1px solid #cbd8e8;
        color: #173a68;
        font-weight: 600;
        min-height: 2.5rem;
    }
    .stButton > button[kind="primary"] {
        background: #1d5fae;
        border-color: #1d5fae;
        color: #fff;
    }
    [data-testid="stDataFrame"] { border: 1px solid var(--border); border-radius: 10px; }
    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #fff;
        border-color: var(--border);
        border-radius: 12px;
    }
    @media (max-width: 700px) {
        [data-testid="stMainBlockContainer"] { padding: 1rem; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

initialize_session()

with st.sidebar:
    st.markdown("## Customer Intelligence")
    st.caption("Loyalty & Engagement Assistant")
    st.divider()
    page = st.radio(
        "WORKSPACE",
        [
            "Overview Dashboard",
            "Customer Analysis",
            "Customer Segmentation",
            "AI Email Generation",
            "Human Review & Approval",
            "Audit Logs",
        ],
        key="navigation",
        label_visibility="visible",
    )
    st.divider()
    st.caption("DEMO ENVIRONMENT")
    st.caption("Synthetic records · No messages are sent")


if page == "Overview Dashboard":
    page_heading(
        "Overview Dashboard",
        "Monitor customer health and the engagement work that needs human attention.",
    )
    segment_by_id = {
        customer_id: classify_customer(customer)[0]
        for customer_id, customer in CUSTOMERS.items()
    }
    loyal_count = sum(customer["loyalty_tier"] in ("Gold", "Platinum") for customer in CUSTOMERS.values())
    at_risk_count = sum(
        segment_by_id[customer_id] in ("Declining Activity", "Dormant Customers", "Payment Reminder")
        for customer_id in CUSTOMERS
    )
    dormant_count = sum(segment == "Dormant Customers" for segment in segment_by_id.values())
    pending_count = sum(
        email["status"] == "Pending approval" for email in st.session_state.email_queue
    )

    kpis = st.columns(5)
    kpis[0].metric("Total customers", f"{len(CUSTOMERS):,}")
    kpis[1].metric("Loyal customers", f"{loyal_count:,}")
    kpis[2].metric("At-risk customers", f"{at_risk_count:,}")
    kpis[3].metric("Dormant customers", f"{dormant_count:,}")
    kpis[4].metric("Pending approvals", f"{pending_count:,}")

    left, right = st.columns([1.25, 1])
    with left:
        with st.container(border=True):
            st.markdown("### Customer segment distribution")
            segment_counts = {
                segment: sum(value == segment for value in segment_by_id.values())
                for segment in SEGMENT_ORDER
            }
            st.bar_chart(
                {"Segment": list(segment_counts), "Customers": list(segment_counts.values())},
                x="Segment",
                y="Customers",
                color="#3973c6",
            )
        with st.container(border=True):
            st.markdown("### Customer engagement trend")
            st.line_chart(
                ENGAGEMENT_TREND,
                x="Week",
                y="Engagement score",
                color="#3973c6",
            )
    with right:
        with st.container(border=True):
            st.markdown("### Payment status overview")
            payment_counts = {
                status: sum(customer["payment_status"] == status for customer in CUSTOMERS.values())
                for status in ("Current", "Payment due", "Overdue")
            }
            st.bar_chart(
                {"Payment status": list(payment_counts), "Customers": list(payment_counts.values())},
                x="Payment status",
                y="Customers",
                color="#6b8fbe",
            )
        with st.container(border=True):
            st.markdown("### Pending review summary")
            pending_emails = [
                email for email in st.session_state.email_queue
                if email["status"] == "Pending approval"
            ]
            if pending_emails:
                st.dataframe(
                    [
                        {
                            "Email": email["email_id"],
                            "Customer": CUSTOMERS[email["customer_id"]]["name"],
                            "Purpose": email["objective"],
                            "Validation": "Ready to review" if not validate_email(email) else "Needs attention",
                        }
                        for email in pending_emails
                    ],
                    hide_index=True,
                    width="stretch",
                )
            else:
                st.info("There are no messages awaiting review.")
        with st.container(border=True):
            st.markdown("### Recent customer activities")
            recent = []
            for customer_id, customer in list(CUSTOMERS.items())[:5]:
                recent.append(
                    {
                        "Customer": customer["name"],
                        "Last active": customer["last_active"],
                        "Segment": segment_by_id[customer_id],
                    }
                )
            st.dataframe(recent, hide_index=True, width="stretch")
    st.caption(
        "All figures are calculated from the 12 fictional customer profiles in this demo."
    )

elif page == "Customer Analysis":
    page_heading(
        "Customer Analysis",
        "Search a synthetic customer profile and review the facts behind their current segment.",
    )
    customer_ids = list(CUSTOMERS)
    search_col, select_col = st.columns([1, 1.5])
    with search_col:
        search_text = st.text_input("Search by customer ID or name", placeholder="e.g. CUST-1001 or Avery")
    with select_col:
        matching_ids = [
            customer_id for customer_id, customer in CUSTOMERS.items()
            if not search_text.strip()
            or search_text.strip().lower() in customer_id.lower()
            or search_text.strip().lower() in customer["name"].lower()
        ]
        if not matching_ids:
            st.warning("No sample customers match that search.")
            matching_ids = customer_ids
        selected_customer_id = st.selectbox(
            "Select a customer",
            matching_ids,
            format_func=lambda customer_id: (
                f"{customer_id}  ·  {CUSTOMERS[customer_id]['name']}"
            ),
        )

    if st.button("Analyze customer", type="primary"):
        st.session_state.analyzed_customer_id = selected_customer_id

    analyzed_id = st.session_state.get("analyzed_customer_id")
    if analyzed_id in CUSTOMERS:
        customer = CUSTOMERS[analyzed_id]
        segment, reason, confidence = classify_customer(customer)
        st.markdown("---")
        st.markdown(f"## {customer['name']}  ·  `{analyzed_id}`")
        st.caption("Synthetic customer profile")
        cards = st.columns(4)
        cards[0].metric("Customer segment", segment)
        cards[1].metric("Website visits this month", customer["visits"])
        cards[2].metric("Payment status", customer["payment_status"])
        cards[3].metric("Loyalty points", customer["points"])
        profile_left, profile_right = st.columns(2)
        with profile_left:
            with st.container(border=True):
                st.markdown("### Activity and product")
                st.write(f"**Product / plan:** {customer['product']}")
                st.write(f"**This month:** {customer['visits']} website visits")
                st.write(f"**Previous month:** {customer['previous_visits']} website visits")
                st.write(f"**Last active:** {customer['last_active']}")
                st.write(f"**Days since activity:** {customer['days_inactive']}")
        with profile_right:
            with st.container(border=True):
                st.markdown("### Loyalty and communication")
                st.write(f"**Loyalty tier:** {customer['loyalty_tier']}")
                st.write(f"**Points balance:** {customer['points']}")
                st.write(f"**Email preference:** {'Opted in' if customer['email_opt_in'] else 'Opted out'}")
                st.write(f"**Preferred channel:** {customer['preferred_channel']}")
        st.info(
            f"**Classification reason:** {reason}  \n"
            f"**Rule confidence:** {confidence:.0%}"
        )
    st.caption("Communication preferences are respected by the draft validation rules.")

elif page == "Customer Segmentation":
    page_heading(
        "Customer Segmentation",
        "Explore rule-based customer groups. Every assignment includes a reason and confidence score.",
    )
    with st.expander("How the sample business rules work", expanded=True):
        st.markdown(
            """
            Rules run in this order so each customer receives one segment:
            1. **Payment Reminder:** payment is due or overdue.
            2. **Dormant Customers:** zero visits and at least 60 days since activity.
            3. **Declining Activity:** visits are at most half of the previous month (when previous visits were 4 or more).
            4. **Loyalty Candidates:** at least 500 points and 4 or more visits this month.
            5. **Consistent Customers:** none of the rules above matched.

            These rules use only synthetic account activity and payment facts. They do not use protected or sensitive characteristics.
            """
        )
    segment_filter = st.selectbox("Filter by segment", ["All segments"] + SEGMENT_ORDER)
    query = st.text_input("Find a customer", placeholder="Search customer ID or name")
    segmentation_rows = []
    for customer_id, customer in CUSTOMERS.items():
        segment, reason, confidence = classify_customer(customer)
        if segment_filter != "All segments" and segment != segment_filter:
            continue
        if query.strip() and query.strip().lower() not in customer_id.lower() and query.strip().lower() not in customer["name"].lower():
            continue
        segmentation_rows.append(
            {
                "Customer ID": customer_id,
                "Customer name": customer["name"],
                "Assigned segment": segment,
                "Reason for classification": reason,
                "Confidence": f"{confidence:.0%}",
            }
        )
    if segmentation_rows:
        st.dataframe(segmentation_rows, hide_index=True, width="stretch")
    else:
        st.info("No customers match the selected segment and search.")
    with st.expander("Rule definitions"):
        for segment in SEGMENT_ORDER:
            st.markdown(f"- **{segment}:** {SEGMENT_RULES[segment]}")

elif page == "AI Email Generation":
    page_heading(
        "AI Email Generation",
        "Create a template-based draft from verified demo facts. No external AI service or email delivery is connected.",
    )
    with st.container(border=True):
        customer_id = st.selectbox(
            "Customer",
            list(CUSTOMERS),
            format_func=lambda key: f"{key}  ·  {CUSTOMERS[key]['name']}",
            key="generation_customer",
        )
        customer = CUSTOMERS[customer_id]
        segment, reason, confidence = classify_customer(customer)
        st.write(f"**Customer segment:** {segment}")
        st.caption(f"Rule: {reason} · Confidence: {confidence:.0%}")
        objective_options = (
            ["Payment reminder"]
            if customer["payment_status"] in ("Payment due", "Overdue")
            else [objective for objective in OBJECTIVES if objective != "Payment reminder"]
        )
        objective = st.selectbox(
            "Communication objective",
            objective_options,
            key="generation_objective",
        )
        st.info(f"**Recommended strategy:** {recommended_strategy(customer, objective)}")
        offers = eligible_offers(customer)
        offer_name = st.selectbox(
            "Approved offer information",
            offers,
            format_func=lambda name: f"{name} — {OFFERS[name]['description']}",
            key="generation_offer",
        )
        st.caption(
            "Offer eligibility is checked by Python business rules. "
            "Promotional offers require current payment status and customer eligibility."
        )
        if not customer["email_opt_in"]:
            st.warning("This customer has opted out of email. A draft cannot be generated.")
        if st.button(
            "Generate email",
            type="primary",
            disabled=not customer["email_opt_in"],
        ):
            draft = create_email_draft(customer_id, objective, offer_name)
            issues = validate_email(draft)
            if issues:
                st.error("Draft was not added: " + " ".join(issues))
            else:
                draft["email_id"] = (
                    f"EMAIL-{2001 + len(st.session_state.email_queue)}"
                )
                st.session_state.email_queue.append(draft)
                st.session_state.audit_records.insert(
                    0,
                    make_audit_record(
                        customer_id,
                        "Email draft generated",
                        "Passed",
                        "Pending",
                        "Pending approval",
                    ),
                )
                st.session_state.generated_email_id = draft["email_id"]
                st.rerun()

    generated_id = st.session_state.get("generated_email_id")
    if generated_id:
        generated = next(
            (email for email in st.session_state.email_queue if email["email_id"] == generated_id),
            None,
        )
        if generated:
            st.success(
                f"{generated_id} is in the human review queue. "
                "Approval is required; this application never sends emails."
            )
            st.markdown(f"**Subject:** {generated['subject']}")
            st.text_area("Generated email body", value=generated["body"], height=200, disabled=True)

elif page == "Human Review & Approval":
    page_heading(
        "Human Review & Approval",
        "Review and validate every draft. Approval records a decision only; no message is sent.",
    )
    queue = st.session_state.email_queue
    if not queue:
        st.info("The review queue is empty. Generate a draft on the AI Email Generation page.")
    else:
        email_ids = [email["email_id"] for email in queue]
        selected_email_id = st.selectbox("Select a draft", email_ids, key="review_email_id")
        email = next(item for item in queue if item["email_id"] == selected_email_id)
        customer = CUSTOMERS[email["customer_id"]]
        segment, reason, confidence = classify_customer(customer)

        customer_col, communication_col = st.columns(2)
        with customer_col:
            with st.container(border=True):
                st.markdown("### Customer")
                st.write(f"**Name:** {customer['name']}")
                st.write(f"**ID:** {email['customer_id']}")
                st.write(f"**Segment:** {segment}")
                st.write(f"**Reason:** {reason}")
                st.write(f"**Communication preference:** {customer['preferred_channel']}")
        with communication_col:
            with st.container(border=True):
                st.markdown("### Draft details")
                st.write(f"**Objective:** {email['objective']}")
                st.write(f"**Strategy:** {email['strategy']}")
                st.write(f"**Offer:** {email['offer_description']}")
                st.write(f"**Rule confidence:** {confidence:.0%}")
                st.write(f"**Current status:** {email['status']}")

        subject = st.text_input(
            "Email subject",
            value=email["subject"],
            key=f"subject_{selected_email_id}",
        )
        body = st.text_area(
            "Email body",
            value=email["body"],
            height=230,
            key=f"body_{selected_email_id}",
        )
        reviewer_comments = st.text_area(
            "Reviewer comments",
            value=email["reviewer_comments"],
            height=90,
            placeholder="Optional notes about this review",
            key=f"comments_{selected_email_id}",
        )
        edited_email = dict(email, subject=subject, body=body)
        validation_issues = validate_email(edited_email)
        if validation_issues:
            validation_result = "Needs attention: " + " ".join(validation_issues)
            st.warning("**Validation status:** " + validation_result)
        else:
            validation_result = "Passed"
            st.success("**Validation status:** Passed — ready for a human decision.")

        approve_col, reject_col, pending_col = st.columns(3)
        with approve_col:
            approve_clicked = st.button(
                "Approve draft",
                type="primary",
                disabled=bool(validation_issues),
                key=f"approve_{selected_email_id}",
            )
        with reject_col:
            reject_clicked = st.button("Reject draft", key=f"reject_{selected_email_id}")
        with pending_col:
            pending_clicked = st.button(
                "Save as pending",
                key=f"pending_{selected_email_id}",
            )

        if approve_clicked or reject_clicked or pending_clicked:
            email["subject"] = subject
            email["body"] = body
            email["reviewer_comments"] = reviewer_comments
            email["validation_result"] = validation_result
            if approve_clicked:
                email["reviewer_decision"] = "Approved"
                email["status"] = "Approved — not sent"
                action = "Human review completed"
                status_message = (
                    f"{selected_email_id} approved and recorded. It has not been sent."
                )
            elif reject_clicked:
                email["reviewer_decision"] = "Rejected"
                email["status"] = "Rejected"
                action = "Human review completed"
                status_message = f"{selected_email_id} rejected. No message was sent."
            else:
                email["reviewer_decision"] = "Pending"
                email["status"] = "Pending approval"
                action = "Draft saved as pending"
                status_message = f"{selected_email_id} saved and remains pending approval."
            add_audit_record(
                make_audit_record(
                    email["customer_id"],
                    action,
                    validation_result,
                    email["reviewer_decision"],
                    email["status"],
                )
            )
            st.session_state.review_notice = status_message
            st.rerun()

        if "review_notice" in st.session_state:
            st.success(st.session_state.pop("review_notice"))

        st.markdown("### Approval queue")
        st.dataframe(
            [
                {
                    "Email ID": item["email_id"],
                    "Customer": CUSTOMERS[item["customer_id"]]["name"],
                    "Segment": item["segment"],
                    "Validation": item["validation_result"],
                    "Reviewer decision": item["reviewer_decision"],
                    "Status": item["status"],
                }
                for item in queue
            ],
            hide_index=True,
            width="stretch",
        )

elif page == "Audit Logs":
    page_heading(
        "Audit Logs",
        "Review sample and in-session workflow events, including validation and human decisions.",
    )
    records = st.session_state.audit_records
    customer_options = ["All customers"] + sorted(
        {record["Customer ID"] for record in records}
    )
    status_options = ["All statuses"] + sorted({record["Status"] for record in records})
    filter_customer, filter_status, filter_action = st.columns(3)
    with filter_customer:
        customer_filter = st.selectbox("Customer", customer_options)
    with filter_status:
        status_filter = st.selectbox("Status", status_options)
    with filter_action:
        action_options = ["All actions"] + sorted({record["Action"] for record in records})
        action_filter = st.selectbox("Action", action_options)

    filtered_records = [
        record for record in records
        if (customer_filter == "All customers" or record["Customer ID"] == customer_filter)
        and (status_filter == "All statuses" or record["Status"] == status_filter)
        and (action_filter == "All actions" or record["Action"] == action_filter)
    ]
    st.caption(f"Showing {len(filtered_records)} of {len(records)} audit records.")
    st.dataframe(filtered_records, hide_index=True, width="stretch")
    st.info(
        "Audit history is stored in this Streamlit session for demonstration. "
        "A production version would persist records in an access-controlled audit store."
    )
