def normalized_findings(service: str, check_id: str, title: str, resource: str, status: str, notes: str = "") -> dict:
    return {
        "service": service,
        "check_id": check_id,
        "title": title,
        "resource": resource,
        "status": status, #PASS / FAIL / MANUAL
        "notes": notes
    }

#expand this for other services once a basic AWS scanner is ready, or create separate files for each service(???)
