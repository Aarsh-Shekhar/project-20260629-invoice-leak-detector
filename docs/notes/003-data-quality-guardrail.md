# Data Quality Guardrail

Domain: finance operations

This note records an implementation detail for Invoice Leak Detector. The current operating
threshold is `0.41` and review should happen within `4` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
