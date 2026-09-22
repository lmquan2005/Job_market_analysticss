import re

def normalize_salary(salary_raw):
    if salary_raw is None:
        return None, None, None

    salary_raw = salary_raw.strip().lower()

    if salary_raw in ["thỏa thuận", "thoa thuan", "thỏa thuận/thoả thuận", "thỏa thuận / thỏa thuận"]:
        return None, None, None

    pattern = r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*triệu"

    match = re.search(pattern, salary_raw)

    if match:
        salary_min = float(match.group(1)) * 1_000_000
        salary_max = float(match.group(2)) * 1_000_000

        return (
            int(salary_min),
            int(salary_max),
            "VND"
        )

    return None, None, None
