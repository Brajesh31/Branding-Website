# ⚠️ Project Risk Register

This register captures risks visible from the current repository structure. Ratings are qualitative and should be reviewed when implementation changes.

| ID | Risk | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| R-01 | Tailwind browser CDN remains a runtime dependency | Medium | Medium | Decide whether compiled CSS alone is sufficient | Open |
| R-02 | Generated CSS may be absent if deployment skips build | Medium | High | Require build and artifact verification | Open |
| R-03 | Existing images need alternative text review | High | Medium | Audit each image and add suitable alt values | Open |
| R-04 | Visible buttons have no real actions | High | Medium | Implement destinations or remove button semantics | Open |
| R-05 | Asset provenance and license records are incomplete | Medium | High | Verify source and record terms | Open |
| R-06 | Existing scheduled workflow writes to the repository | Medium | Medium | Review trigger, permissions, and concurrency | Review |
| R-07 | No dedicated browser automation suite | High | Medium | Add smoke tests if maintenance value justifies it | Open |
| R-08 | No measured performance baseline | Medium | Medium | Capture repeatable browser measurements | Open |

## 🧭 Risk handling
For each risk, record an owner, evidence, next action, due date, and review date in the relevant issue or pull request. A risk marked mitigated must have evidence.

## 📊 Rating guide
- Likelihood: Low, Medium, High.
- Impact: Low, Medium, High.
- Priority should consider user harm, exploitability, frequency, and operational cost.

This register is not a security audit or formal risk certification.
