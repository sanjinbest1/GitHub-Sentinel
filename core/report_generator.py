import os

def generate_report(latest_release, repo):
    """
    Generate a report based on the latest release data.
    :param latest_release: JSON response of the latest release
    :param repo: Repository name
    :return: Path to the generated report
    """
    tag_name = latest_release.get("tag_name", "N/A")
    release_name = latest_release.get("name", "N/A")
    published_at = latest_release.get("published_at", "N/A")
    body = latest_release.get("body", "N/A")
    author = latest_release.get("author", {}).get("login", "N/A")

    report_content = f"""
    GitHub Repository: {repo}
    ============================================
    Latest Release: {tag_name}
    Release Name: {release_name}
    Published At: {published_at}
    Author: {author}

    Release Notes:
    --------------------------------------------
    {body}
    """

    # Save the report to a file
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"{repo.replace('/', '_')}_release_report.txt")
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(report_content.strip())

    return report_path
