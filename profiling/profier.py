from collections import Counter

def count_jobs(jobs):
    return len(jobs)

def count_unique_jobs(jobs):
    urls = []

    for job in jobs:
        urls.append(job.get("source_url"))

    return len(set(urls))

def find_duplicates(jobs):
    urls = [
        job.get("source_url")
        for job in jobs
        if job.get("source_url")
    ]

    counts = Counter(urls)

    return {
        url: count
        for url, count in counts.items()
        if count > 1
    }

def count_missing(jobs, field):
    count = 0

    for job in jobs:
        value = job.get(field)

        if value is None or value == "":
            count += 1

    return count

def show_distribution(jobs, field, top_n=20):
    values = [
        job.get(field)
        for job in jobs
        if job.get(field)
    ]

    counter = Counter(values)

    print(f"\nDistribution: {field}")
    print("-" * 50)

    for value, count in counter.most_common(top_n):
        print(f"{count:>4} | {value}")