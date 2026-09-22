from transform.salary import normalize_salary

from tests.load_lastest_data import load_latest_raw
from storage.test_transform import save_raw
def transform_job(job):
    salary_min, salary_max, salary_currency = normalize_salary(job.get("salary_raw"))

    transformed_job = {
        "source": job.get("source"),
        "source_url": job.get("source_url"),
        "source_job_id": job.get("source_job_id"),
        "title": job.get("title"),
        "company_name": job.get("company_name"),
        "job_location": job.get("job_location_raw"),
        "salary_raw": job.get("salary_raw"),
        "salary_min": salary_min,
        "salary_max": salary_max,
        "salary_currency": salary_currency,
        "description": job.get("description"),
        "requirements": job.get("requirements"),
        "posted_date": job.get("posted_date"),
        "expired_date": job.get("expired_date"),
        "company_url": job.get("company_url"),
        "company_location": job.get("company_location")
    }

    return transformed_job

if __name__ == "__main__":
    raw_data = load_latest_raw()
    transformed_data = [transform_job(job) for job in raw_data]
    save_raw(transformed_data)
    print(f"\nTransformed {len(transformed_data)} jobs")