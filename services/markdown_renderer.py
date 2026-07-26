from pathlib import Path

from models.daily_report import DailyReport


DEFAULT_OUTPUT_DIRECTORY = Path("output")


def render_daily_report(report: DailyReport) -> str:
    """Convert a DailyReport into Markdown text."""

    lines = [
        f"# {report.topic} Daily Report",
        "",
        f"Generated: {report.generated_at.isoformat()}",
        "",
        f"Articles included: {len(report.items)}",
        "",
        "---",
        "",
    ]

    for position, item in enumerate(report.items, start=1):
        article = item.article
        summary = item.summary

        lines.extend(
            [
                f"## {position}. {article.title}",
                "",
                f"**Source:** {article.source}",
                "",
                f"**Published:** {article.published}",
                "",
                f"**URL:** {article.url}",
                "",
                "### Overview",
                "",
                summary.overview,
                "",
                "---",
                "",
            ]
        )

    return "\n".join(lines)


def write_daily_report(
    report: DailyReport,
    output_directory: Path = DEFAULT_OUTPUT_DIRECTORY,
) -> Path:
    """Render and save a DailyReport as a Markdown file."""

    output_directory.mkdir(parents=True, exist_ok=True)

    report_date = report.generated_at.date().isoformat()
    filename = f"{report_date}-ai-report.md"
    output_path = output_directory / filename

    markdown = render_daily_report(report)

    output_path.write_text(
        markdown,
        encoding="utf-8",
    )

    return output_path
