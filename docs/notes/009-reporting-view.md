# Reporting View

Domain: finance operations

This note records an implementation detail for Invoice Leak Detector. The current operating
threshold is `0.55` and review should happen within `24` hours
for records above that level.

## Checks

- confirm input fields are present
- verify score ordering is stable
- compare high exposure records against the review queue
