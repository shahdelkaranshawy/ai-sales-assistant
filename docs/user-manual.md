# Sales Assistant — User Guide

This guide walks you through the application from login to the main tabs. Follow the steps in order for a smooth first-time experience.

---

## 1. Log in

**What you see**

- Open the Sales Assistant in your browser. You land on the **login** page.
- The page shows:
  - **Welcome Back** — “Sign in to the Sales Assistant”
  - **Username or Email** — text field
  - **Password** — password field
  - **Sign in** button

**What to do**

1. Enter your **username or email** in the first field.
2. Enter your **password** in the second field.
3. Click **Sign in**.
4. If credentials are wrong, an error message appears; correct the details and try again.
5. After a successful login, you are taken to the **Morning Brief** (your home screen). The **sidebar** on the left shows links to all tabs (Morning Brief, Evening Brief, Actions, Accounts, and more). The top bar shows the app header.

**Tip:** Use the sidebar to move between sections. You can collapse it with the arrow button to get more space.

<!-- Screenshot: Login screen -->

---

## 2. Morning Brief (your home screen)

**What you see**

After login you land on the **Morning Brief** (route: `/`). This is your daily dashboard.

- **Stats grid (top row)** — Four KPI cards:
  - **Sales Target** — Your achievement vs target (e.g. AED 1.2M of AED 1.5M), with percentage and trend.
  - **Quarterly Revenue** — Total revenue for the quarter (e.g. AED 2.4M), with change vs previous quarter.
  - **Pipeline Value** — Total value of deals in the pipeline (e.g. AED 1.8M).
  - **Accounts at Risk** — Count of accounts flagged as high churn risk (click to open accounts filtered by at-risk).
- **Daily focus banner** — Just below the stats. Shows counts by action type (e.g. “3 Churn Rescue, 2 Upsell”). Click a type to filter the action list below; the active filter is highlighted.
- **AI-recommended actions** — A **Refresh** (or **Generate actions**) button, then filters (priority, type, sort, card/table view), then the list. Actions are grouped into:
  - **Recommended Actions** — Your top priorities.
  - **Completed Actions** — Collapsible section for actions you have already completed.
  - **Skipped/Rejected Actions** — Collapsible section for actions you skipped or rejected.

**What to do**

1. Scan the **stats** to see your target, revenue, pipeline, and accounts at risk.
2. Use the **focus banner** — click an action type to filter the list (e.g. “Churn Rescue”).
3. In the action list, each **card** shows: rank, customer name, action type, priority (High/Medium/Low), short description, rationale, confidence score, revenue impact, and due date.
4. On a card you can:
   - Use the **status** dropdown to set **Complete**, **In Progress**, **Reject**, or **Snooze** (e.g. Later Today, Tomorrow, Next Week).
   - Click **Explain** to open a modal with the AI’s reasoning, drivers, and next steps.
5. Use **Refresh** or **Generate actions** if you want to request a new set of recommendations (subject to once-per-day rules).

**Where to go next:** Use the sidebar to open **Actions** (full list) or **Accounts** (your portfolio).

<!-- Screenshot: Morning Brief stats grid and focus banner -->

<!-- Screenshot: Morning Brief action cards -->

---

## 3. Actions

**What you see**

Open **Actions** from the sidebar (route: `/actions`). This is the dedicated place for **all** your AI recommendations (not only the daily snapshot on the home page).

- **Filters** — Search, priority, type, status, and a toggle for **card view** vs **table view**.
- **Top 10** — A highlighted block with your top-priority actions (same card format as on the Morning Brief: rank, customer, type, priority, reason, confidence, revenue impact, due date, status dropdown, Snooze, Explain).
- **Backlog** — Remaining actions below the Top 10.
- **Table view** — Columns: Rank, Customer, Type, Priority, Revenue, Confidence, Due Date, Actions (status and buttons).

If you are a **manager**, you also see **Team View** and **Feedback Log** tabs to see team actions and submitted feedback.

**What to do**

1. Use **filters** to narrow by priority, type, or status.
2. Switch between **card** and **table** view with the view toggle.
3. On each action, use the **status** dropdown (Complete, In Progress, Reject, Snooze) and **Snooze** options (Later Today, Tomorrow, Next Week) as on the Morning Brief.
4. Click **Explain** on any action to see the full AI reasoning and next steps.
5. (Managers) Use **Team View** to see actions by team member and **Feedback Log** to review feedback on completed actions.

**Where to go next:** Open **Accounts** from the sidebar to work with your customer portfolio.

<!-- Screenshot: Actions tab — Top 10 and filters -->

---

## 4. Accounts

**What you see**

Open **Accounts** from the sidebar (route: `/accounts`). This is your **customer portfolio**.

- **Summary** — Total accounts, how many are at risk, total revenue, and health overview.
- **Filters** — Risk, segment, NPS, and other filters, plus **card** or **table** view.
- **Account list** — Cards or rows showing each account. Each entry can show key metrics and a count of completed AI actions.

**What to do**

1. Use **filters** to focus on at-risk, segment, or NPS.
2. **Click a row or card** to open the **Account detail** page (route: `/accounts/[id]`).

**On the Account detail page**

- **Overview** — Health, churn risk, NPS, and summary metrics.
- **Products** — Products and rate plans for the account.
- **Sub-accounts** — All sub-accounts/lines under the client with product details.
- **Compliance** — Trade licence (TL), LOA, establishment card (EC) expiry and status.
- **NPS history** — Historical NPS scores (if available).
- **Risk details** — Risk analysis and types.
- **AI recommendations** — Recommendations that relate to this account.

Use the **Back to Accounts** link or the sidebar to return to the accounts list.

<!-- Screenshot: Accounts list -->

<!-- Screenshot: Account detail page — overview tab -->

---

## 5. Evening Brief

**What you see**

Open **Evening Brief** from the sidebar (route: `/evening-brief`). This tab is for **end-of-day review**.

- **Task execution summary (top)** — Counts of:
  - **Completed** — Actions you marked as completed today.
  - **In progress** — Actions you started but did not complete.
  - **Missed / postponed** — Actions not completed or snoozed for later (snoozed items show when they will resurface).
- **Lists** — **Completed actions** (with option to add outcome/feedback) and **Missed & postponed** actions (you can still change status or mark complete from here).
- **Close day** — Section that summarizes the day.
- **Feedback** — For completed actions you can open a feedback modal to rate (1–5) and add an outcome so the AI can improve.

**What to do**

1. Review the **summary** to see how many actions you completed, left in progress, or missed.
2. In **Completed actions**, click **Add outcome** (or similar) on an action to open the **feedback modal**.
3. In the modal:
   - **Rate** the recommendation (e.g. 1–5 stars or Helpful / Not helpful).
   - **Add comments or outcome** (e.g. “Contract signed”, “Customer declined”) so the system can learn from real results.
4. Submit feedback. Your input is used to improve future recommendations.

**Where to go next:** When you need more detail on any tab, use **Documentation** from the sidebar.

<!-- Screenshot: Evening Brief summary and completed list -->

<!-- Screenshot: Feedback modal -->

---

## 6. Documentation (help)

**What you see**

Open **Documentation** from the sidebar (route: `/documentation`). It lives under the **Administration** section at the bottom of the sidebar. This is the in-app **reference** for all features.

- A **sidebar on the left** lists sections (Application Overview, Morning Brief, Evening Brief, Action Center, Accounts, and other modules).
- The **main area** shows the selected section with subsections (e.g. Stats Grid, Daily Focus Banner, AI-Recommended Actions for Morning Brief).

**What to do**

1. Click a **section** in the left sidebar (e.g. “Morning Brief (Dashboard)”, “Evening Brief”, “Action Center”, “Accounts”) to jump to that part of the guide.
2. Expand or click **subsections** to read about specific elements (e.g. Action Card Components, Feedback Modal).
3. Use this page whenever you want a detailed description of a screen or feature. It covers the tabs in this user guide and additional modules (e.g. Proposals, Simulator, Coaching) if they are available in your environment.

**Tip:** This user guide is a short **walkthrough** from login through the main tabs. The in-app **Documentation** tab is the full **reference** — use it for deeper detail on any screen or button.

<!-- Screenshot: Documentation tab — sidebar and content -->

---

## Quick reference — main routes

| Tab             | Route            | Purpose                          |
|-----------------|------------------|----------------------------------|
| Morning Brief   | `/`              | Daily KPIs and AI recommendations |
| Evening Brief   | `/evening-brief` | End-of-day review and feedback   |
| Actions         | `/actions`       | Full list of AI recommendations  |
| Accounts        | `/accounts`      | Customer portfolio list           |
| Account detail  | `/accounts/[id]` | Single account — overview, products, compliance, AI recommendations |
| Documentation   | `/documentation` | In-app help and reference        |

---

*For technical or API documentation, see the project README and backend documentation.*
