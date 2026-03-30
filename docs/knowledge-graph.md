# Oracle Autonomous DB Property Graph — Initial Schema (from `KG_nodes(Nodes).csv`)

This document captures the initial **property graph schema** as provided in `backend/KG_nodes(Nodes).csv`. It is intended as a shared reference for the **future Query Generator** service that will query the graph and return structured results to the FastAPI backend.

> Notes
> - The CSV mixes **node types**, **attributes**, and **relationship labels** (edge types) in a compact format.
> - Relationship labels appear in the “Attribute” column on certain rows (e.g., `OWNS`, `HAS_OPPORTUNITY`).
> - Many attributes include source system field hints in parentheses (kept as-is).

---

## Node types and key attributes

### Customer
- **Identifiers**
  - Customer Id
  - Party Id
  - Parent Customer Id
- **Segmentation**
  - Customer Segment
  - Segment
  - Sub Segment
  - Industry
- **NPS**
  - NPS Score
  - NPS Customer Comment
  - NPS Date and Time
- **Compliance / documents**
  - TL Expiry Date (Trade licence expiry date) `TL_EXP_DT`
  - EC Expiry Date (establishment card expiry date) `est_card_exp_date`, `est_card_exp_dt`
  - Active LOA flag `loa_status`
  - LOA Expiry Date `loa_exp_dt`
  - Tenure (Customer)

### Account
- **Identifiers**
  - Account Id
  - Party id (link to Customer/Party)
- **Commercial**
  - ARPU
  - MRC (RCR_FEE)
  - OTC (One time fee) `BILL_ONETIME_M1`
- **Product subscription / package**
  - Product category
  - Product level_1
  - Product level_2
  - Package (rate plan desc, product levels)
  - Rate plan code
  - Rate plan desc
- **Contract**
  - Contract_Start_Date
  - Contract_End_Date
- **Usage**
  - Usage
  - Usage_Cloud_Storage_GB `DATA_UPLD_DUR_M1`
  - Usage_Data_Allowance
  - Usage_Mobile_Data_GB
  - Internet_Speed (Rate plan Desc, pd_lv_4)
  - DATA_UNKNOWN_MB_M1 / _GS / _WS
- **Derived**
  - Revenue_By_Product (to be calculated) (RCR_Fee, OTC, timewindow)

### Opportunity
- **Identifiers**
  - Opportunity_ID / Lead Id
- **Linkage**
  - Customer Id
- **Pipeline**
  - Deal_Size_AED (estimated_value)
  - Expected_Close_Date
  - Opportunity Stage
  - Opportunity_Status
  - Type (Opportunity/Lead)

### Product
- Product category
- Product Level 1..4
- Rate plan
- Package
- MRC
- OTC
- Product Features
- Product Knowledge Base
- Product Knowledge Version

### Interaction
- **Interaction metadata**
  - Interaction Date
  - Interaction Status
  - Interaction channel / sub channel / group
  - Interaction offer id
- **Support ticket**
  - Type of Support Ticket
  - Support Ticket Description
  - Support Ticket Created / Closed
  - Support_Tickets_Open (`UNQ_ID_IN_SRC_STM`, `CMM_CTC_ST`)
- **Linkage**
  - Account Id
  - Account Number
  - Customer Id / Party id (also referenced in CSV)

### Contract
- Party Id
- Account Id
- Contract Dates (multiple source fields listed)
- Contract_Start_Date
- Contract_End_Date

### Invoice
- Party id
- Account Id
- Billing Date (BILL_DUE_DATE_M1..M6)
- Billing_Forecast_AED
- Monthly_Billing_AED
- Outstanding_Invoices_AED (Account)
- Outstanding_Invoices_AED (Party)
- Revenue_By_Product (derived)

### Campaign
- Campaign Id (PK)
- Party id
- Account Id
- Campaign Priority Score
- OTC
- MRC (RCR_FEE)
- ARPA (updated ARPU_1,3,6,12)

### CampaignActivity
- CampaignActivity Id
- Campaign Id (PK)
- Opportunity_ID / Lead Id (also referenced)
- Out of Bundle Revenue (%OB_REV%)
- Products Pitched / Accepted
- Rejection Reason
- Product_Category
- Product Level 1..2
- RatePlan / Package / Package code
- Offering / Offer group
- Usage / Allowance
- ARPA (updated ARPU_1,3,6,12)
- Customer Segment
- Interaction offer id

### Open Orders / Order node
- **Order node** (label `ORDER`): linked from Customer via `HAS_ORDER` (or `HAS_OPEN_ORDER`). Attributes:
  - ORDER_ID, ORDER_CREATED_DATE, SUBREQUEST_STAT, ORDER_STATUS, PARTY_ID, PRODUCT_CATEGORY
  - RatePlan / Package, MRC (RCR_FEE), OTC (One time fee), PRODUCT_NAME, Product Level 1..4 (when present)
- Order id, Party Id, Order Created Date, Order Status
- RatePlan / Package, MRC (RCR_FEE), OTC (One time fee), Product_Category, PRODUCT_NAME, Product Level 1..4

### Sales Manager
- Sales Manager Id
- Sales Manager Name
- Sales Manager Email
- Sales Manager Mobile
- Target_AED
- Achievement_AED
- Party id
- Account id
- TL NAME
- Senior Manager
- Director

### RiskScore
- Account_Id
- Party_Id
- Churn_Score_Account, Risk_Account
- Churn_Score_Party, Risk_Party
- CREDIT_SCORE, BUCKET
- SCORE, CUSTOMER_RISK
- RISK_SCORE, CUSTOMER_RISK
- Final_Segment_Prediction (segment), Final_Prediction (sub seg)
- Forecast_with_opps
- TARGET (recommended), Finalized_Target
- TARGET
- Tier
- FIRST/SECOND/CLAWBACK/NET/ACCELERATION payment forecasts
- RECOMMENDATION

### Feedback
- Recommendation Id
- Recommendation rating by SM (Helpful/Not Helpful)
- Recommendation rating remarks by SM
- Recommendation Date & Time
- Recommendation Description
- Recommendation Action Type (New Acquisition, Upsell etc)
- Recommendation Expected Outcome (Predicted Revenue Impact)
- Account Id
- Sales Manager Id
- Party Id
- Recommendation Actual Outcome (Actual Revenue Impact)

### AI Recommendation
- Queue Id
- Recommendation Id
- Campaign Id
- CampaignActivity Id
- Sales Manager Id
- Party Id
- Opportunity Id
- Order Id
- Type
- Creation Date & Time
- Due Date & Time
- Description
- Reason
- source
- expected_impact(AED)
- action_reference (partyid/accountid/opportunityid/etc)
- confidence_score
- priority (high/med/low)
- priority score
- status (open/in-progress/skipped/completed)
- Recommendation Expected Outcome (Predicted Revenue Impact)

### Work Queue
- Queue Id
- Sales Manager Id
- Queue name
- Priority level
- Status (active/inactive/completed)
- Date Created
- End Date
- max_capacity
- Recommendation Id

### Deal Simulation
- Opportunity_ID / Lead Id
- Simulation Id

### Proposal
- Simulation Id
- Party Id
- Account Id

### Coaching
- Recommendation Id

---

## Relationship (edge) labels observed

The CSV includes these relationship labels (as literals in the sheet):
- **OWNS**: (Party id) → Account
- **SUBSCRIBED_TO**: Account → Rate plan / Package (implicit)
- **HAS_OPPORTUNITY**: Customer / CampaignActivity → Opportunity
- **HAS_INTERACTION**: Account / Customer → Interaction
- **GENERATES**: Invoice relationship (Account/Party → Invoice)
- **TARGETS_CUSTOMER**: Campaign → Customer/Party
- **HAS_ACTIVITY**: Campaign → CampaignActivity
- **HAS_OPEN_ORDER**: Customer/Party → Open Orders (and also referenced from AI Recommendation)
- **MANAGES_CUSTOMER**: Sales Manager → Customer/Party
- **FOR_ACCOUNT**: RiskScore → Account
- **FOR_CUSTOMER**: RiskScore → Customer/Party
- **GAVE_FEEDBACK**: Sales Manager → Feedback
- **GENERATES_TASK**: AI Recommendation → Work Queue / Task concept
- **FOR_CAMPAIGN_ACTIVITY**: AI Recommendation → CampaignActivity
- **ASSIGNED_TO**: AI Recommendation → Sales Manager
- **USED_FOR**: AI Recommendation → Party/Customer
- **FOR_OPPORTUNITY**: AI Recommendation → Opportunity
- **HAS_SIMULATION**: Opportunity → Deal Simulation
- **CREATES_PROPOSAL**: Deal Simulation → Proposal
- **PROPOSED_FOR_CUSTOMER**: Proposal → Party/Customer
- **PROPOSED_FOR_ACCOUNT**: Proposal → Account
- **SUGGESTS_COACHING**: Coaching → Recommendation

---

## Mapping to MVP: “Top 10 Actions Recommender”

For the MVP recommender, the most relevant graph entities/relationships are:
- **Customer / Account**: base entity to recommend actions for
- **RiskScore (FOR_ACCOUNT / FOR_CUSTOMER)**: churn risk, credit risk, forecasting signals
- **Opportunity (HAS_OPPORTUNITY)**: pipeline opportunities and expected value
- **Contract / Invoice / Interaction**: renewal triggers, overdue invoices, open tickets, negative signals
- **Campaign / CampaignActivity**: active campaigns and outcomes
- **AI Recommendation / Feedback**: historical recommendations + outcomes (later used for learning/precision metrics)

Expected Query Generator outputs (future):
- **Action candidates**: structured objects similar to the frontend `Action` model:
  - `account_id`, `party_id`, related `opportunity_id` (if any)
  - `type`, `priority`, `expected_impact`, `confidence_score`
  - `reason` and structured explanation (evidence subgraph references)
- **Evidence references**: pointers to the underlying graph nodes/edges used in the recommendation rationale.

---

## Next step (when we integrate the graph DB)

When the Query Generator service is introduced, it should:
- Query Oracle Autonomous DB Property Graph using the above node/edge semantics.
- Return **typed**, **versioned** payloads to the backend (REST or gRPC).
- Keep the backend decoupled from graph query details (backend consumes only the structured outputs).


