# Week 4 Report: Rule-Based Coach Filtering

## 1. Introduction

Week 4 focuses on developing rule-based coach filtering for the Smart Railway Coach Allocation and Management System.

The objective is to identify coaches that may satisfy the requirements of a selected train by checking coach type, current station, maintenance status, and existing allocation records.

## 2. Objectives

- Understand train-wise coach requirements.
- Filter coaches according to the required coach type.
- Check coach availability and current station.
- Exclude coaches under maintenance.
- Exclude coaches that already have an active allocation, where allocation checking is implemented.
- Validate the filtering logic using suitable test cases.

## 3. Filtering Criteria

### 3.1 Coach Type

A coach should match the type requested for the selected train. For example, a request for Sleeper coaches should not return coaches of a different type.

### 3.2 Current Station

The recorded station of the coach should match the station required for the selection when station matching is part of the implemented rules.

### 3.3 Maintenance Status

Coaches marked as Under Maintenance should be excluded from eligible results.

### 3.4 Existing Allocation

Coaches with an active allocation should be excluded from new allocations when the application checks existing allocation records.

### 3.5 Availability

The coach must satisfy the availability conditions implemented in the application before it is considered suitable.

## 4. Filtering Procedure

The intended filtering procedure is:

1. Retrieve the requirements for the selected train.
2. Identify the required coach type and quantity.
3. Find coaches matching the requested type.
4. Apply station and availability conditions.
5. Exclude coaches under maintenance.
6. Exclude coaches that already have an active allocation, where supported.
7. Return the remaining eligible coaches.

## 5. Test Cases

| Test Case | Expected Result |
|---|---|
| Coach type matches and coach is available | Coach may qualify |
| Coach is under maintenance | Coach is excluded |
| Coach type does not match | Coach is excluded |
| Coach is at a different station | Coach is excluded when station matching is required |
| Coach has an active allocation | Coach is excluded when allocation checking is implemented |
| No coach satisfies the rules | No eligible coaches are returned |

## 6. Expected Deliverables

- Rule-based coach selection logic.
- Filtering based on coach type and availability.
- Maintenance-status checks.
- Allocation checks where implemented.
- Test cases for eligible and ineligible coaches.


## 7. Challenges and Observations

The filtering result depends on accurate coach status, station information, and allocation records. The application must apply the rules consistently to avoid returning coaches that should not be eligible.

## 8. Conclusion

Week 4 focuses on rule-based coach filtering and validation. Together with the database design and management functionality developed in the earlier stages, this work supports the initial four-week scope of the Smart Railway Coach Allocation and Management System.

