class ReportGenerator:
    def generate_report(self, updates):
        # Generate a report based on the updates
        report = "GitHub Repository Updates\n\n"
        for (repo_owner, repo_name), update in updates.items():
            report += f"Repository: {repo_owner}/{repo_name}\n"
            for event in update:
                report += f"Event: {event['type']} | Date: {event['created_at']}\n"
        return report
