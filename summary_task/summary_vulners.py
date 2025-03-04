import vulners

# подставить ключ апи
programs = [
    {"Program": "LibreOffice", "Version": "6.0.7"},
    {"Program": "7-Zip", "Version": "18.03"},
    {"Program": "Adobe Reader", "Version": "18.009.20050"},
    {"Program": "nginx", "Version": "1.14.0"},
    {"Program": "Apache HTTP Server", "Version": "2.4.29"},
    {"Program": "DjVu Reader", "Version": "2.0.0.27"},
    {"Program": "Wireshark", "Version": "2.6.1"},
    {"Program": "Notepad++", "Version": "8.0"},
    {"Program": "Google Chrome", "Version": "124.0.6367.18"},
    {"Program": "Mozilla Firefox", "Version": "128.0.2"}
]

software = []
for i, program in enumerate(programs):
    software.append({"product": program["Program"], "version": program["Version"]})

print(software)
vulners_api = vulners.Vulners(api_key="fix")

result = vulners_api.audit_software(
    software=software,
    fields=["title", "short_description", "type", "href", "published", "modified", "ai_score", "metrics",
            "exploitation", "cvelist"],
    match="full"
)


def cve_with_exploit(vulner: dict):
    cve = vulner["id"]
    if vulner["exploitation"]["wildExploited"]:
        exploits: list = vulner["exploitation"]["wildExploitedSources"]
        exploit_ids = []
        for i, exploit in enumerate(exploits):
            exploit_ids += exploit["idList"]
        return f"cve: {cve}, exploits: {exploit_ids}"
    return f"cve: {cve}"


print("Уязвимое ПО:")
for i, checked_program in enumerate(result):
    vulners: list = checked_program["vulnerabilities"]
    if vulners:
        product = checked_program["input"]["product"]
        version = checked_program["input"]["version"]
        print(f"{product} {version}")
        for j, vulner in enumerate(vulners):
            print(f"{j + 1}. {cve_with_exploit(vulner)}")
