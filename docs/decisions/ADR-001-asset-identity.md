# ADR-001: Asset Identity and Identifier Generation

**Status:** Accepted

**Date:** 2026-08-27

## Context

Nexus requires every asset to have a unique identity within the system.

Asset identifiers must be unique and human-readable so that users can easily reference individual assets.

Allowing users to manually assign asset identifiers could result in duplicate identifiers or inconsistent identifier formats across the system.

Nexus must preserve asset records throughout their lifecycle, including when an asset is retired, so that historical records remain available.

Asset identifiers must remain permanently associated with their original assets and must not be reused for another asset after retirement.

## Decision

Nexus will generate Asset identifiers automatically when a new asset is created.

Asset identifiers will use a sequential, human-readable format beginning with the `NXS-` prefix.

Examples include `NXS-000001`, `NXS-000002`, and `NXS-000003`.

The Asset identifier will represent the asset's permanent identity within Nexus and will not encode mutable information such as category, type, location, assignment, or status.

Each Asset identifier will remain permanently associated with its original asset throughout that asset's lifecycle, including after retirement.

The system must guarantee that concurrent asset creation requests receive unique Asset identifiers.

The identifier allocation mechanism must use an atomic operation or equivalent database-level guarantee to prevent duplicate identifiers during concurrent asset creation.

Asset identifier values will increase sequentially and will not be reused, including when an earlier identifier belongs to a retired asset.

## Alternatives Considered

### User-Assigned Asset IDs

Rejected.

Allowing users to manually assign Asset identifiers could result in duplicate identifiers, inconsistent formats, and accidental reuse of identifiers that belong to retired assets. This would make data integrity dependent on user input rather than being enforced by the system.

### Randomly Generated Asset IDs

Rejected for the initial design.

Random identifiers could provide uniqueness without requiring a sequential counter, but they would be less human-readable and would make sequential asset references less convenient for users. Nexus currently has no requirement for globally distributed or cryptographically random identifiers.

### Type-Based Asset IDs

Rejected.

Embedding category or type information into an Asset identifier would make the identifier dependent on attributes that may change over the asset's lifecycle. This would create unnecessary coupling between the asset's permanent identity and its mutable classification.

## Consequences

### Positive

Nexus will have a consistent and system-controlled method of identifying assets throughout their entire lifecycle.

### Negative

Nexus will need persistent state to track identifier allocation so that identifiers remain unique and are never reused.

Nexus will need to enforce identifier allocation safely when multiple asset creation requests occur at the same time, requiring database-level concurrency controls or an equivalent mechanism.

## Implementation Notes

The specific persistence mechanism for Asset identifier allocation has not yet been selected. The eventual implementation must satisfy the uniqueness, sequential allocation, permanence, and concurrency requirements defined in this decision.