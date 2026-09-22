from profiling.profier import count_unique_jobs, find_duplicates, count_missing, show_distribution
def profile_jobs(jobs):
    print("=" * 40)
    print("RAW DATA PROFILING")
    print("=" * 40)

    total = len(jobs)

    print(f"Total records: {total}")
    print(f"Unique records: {count_unique_jobs(jobs)}")
    duplicates = find_duplicates(jobs)

    print(f"Duplicate URLs: {len(duplicates)}")

    print("\nMissing values:")

    fields = [
        "title",
        "company_name",
        "location_raw",
        "salary_raw",
        "description",
        "requirements"
    ]

    for field in fields:
        missing = count_missing(jobs, field)
        rate = missing / total * 100 if total > 0 else 0

        print(
            f"{field:<20}"
            f"{missing:>5} "
            f"{rate:.2f}%"
        )
    show_distribution(jobs, "salary_raw")
    show_distribution(jobs, "location_raw")