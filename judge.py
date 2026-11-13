#!/usr/bin/env python3
"""Independent oracle for gpt-debt-sweeper's disposable evaluation branches.

Run from a separate checkout of eval/oracle, passing the absolute/relative
path to an agent-edited checkout. Never copy this file into the working
fixture before the agent's run.
"""
import argparse
import json
import os
from pathlib import Path
import subprocess
import sys


CASES = {
    "01": {
        "branch": "eval/01-retired-ui",
        "must_remove": [
            "ui/legacy/index.html",
            "ui/legacy/renderer.py",
            "scripts/legacy_smoke.py",
            "tests/test_legacy_smoke.py",
        ],
        "must_keep": ["application.py", "ui/dist/index.html", "tests/test_application.py"],
        "no_tokens": {
            "window.json": ["legacy_window_entry", "ui/legacy"],
            "package-files.txt": ["legacy", "scripts/legacy_smoke.py"],
        },
        "probe": """
from application import launch_window, package_assets
from pathlib import Path
assert "Current UI" in launch_window()
assert "ui/dist/index.html" in package_assets()
assert all(Path(x).is_file() for x in package_assets())
""",
    },
    "02": {
        "branch": "eval/02-verification-theater",
        "must_remove": [
            "scripts/verify_receipt.py",
            "fixtures/receipt_sample.txt",
            "tests/test_receipts.py",
        ],
        "must_keep": ["reporting.py", "shopfront.py", "tests/test_reporting.py"],
        "no_tokens": {"reporting.py": ["_receipt_for", "_confirm_receipt", "internal receipt mismatch"]},
        "probe": """
from shopfront import checkout_preview
assert checkout_preview({"id":"order-7","items":[{"count":2,"price":3},{"count":1,"price":4}]}) == "order-7: 10 credits"
assert checkout_preview({"id":"empty","items":[]}) == "empty: 0 credits"
""",
    },
    "03": {
        "branch": "eval/03-speculative-layers",
        "must_remove": [
            "notifications/port.py",
            "notifications/provider.py",
            "notifications/registry.py",
            "notifications/forwarder.py",
            "notifications/settings.json",
            "tests/test_registry.py",
        ],
        "must_keep": ["notifications/service.py", "notifications/__init__.py", "tests/test_service.py"],
        "no_tokens": {"notifications/service.py": ["get_backend", "Forwarder", "enable_future_backends"]},
        "probe": """
from notifications import send_welcome
assert send_welcome("Ada") == "TO:Ada|welcome"
assert send_welcome("") == "TO:|welcome"
""",
    },
    "04": {
        "branch": "eval/04-dynamic-plugin-boundary",
        "must_remove": [
            "plugins/legacy.py",
            "scripts/run_legacy.py",
            "tests/test_old_diagnostic.py",
        ],
        "must_keep": [
            "engine.py",
            "commands.json",
            "plugins/status.py",
            "tests/test_runtime.py",
        ],
        "no_tokens": {},
        "probe": """
import json
from pathlib import Path
from engine import run_command
assert json.loads(Path("commands.json").read_text(encoding="utf-8"))["commands"]["status"] == "status"
assert run_command("status") == "READY"
try:
    run_command("legacy")
except KeyError:
    pass
else:
    raise AssertionError("retired plugin became an active command")
""",
    },
}


def run_python(root, code):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run(
        [sys.executable, "-B", "-c", code],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=sorted(CASES), help="01, 02, 03, or 04")
    parser.add_argument("checkout", type=Path, help="Repository checkout modified by the agent")
    args = parser.parse_args()
    root = (args.checkout.expanduser().resolve() / "eval-case")
    if not root.is_dir():
        parser.error(f"Missing eval-case directory in {args.checkout}")

    spec = CASES[args.case]
    checks = []

    for rel in spec["must_remove"]:
        checks.append((f"removed: {rel}", not (root / rel).exists()))
    for rel in spec["must_keep"]:
        checks.append((f"preserved: {rel}", (root / rel).is_file()))

    for rel, forbidden in spec["no_tokens"].items():
        p = root / rel
        if not p.is_file():
            checks.append((f"exists: {rel}", False))
            continue
        content = p.read_text(encoding="utf-8")
        for token in forbidden:
            checks.append((f"no leftover {token!r} in {rel}", token not in content))

    behavior = run_python(root, spec["probe"])
    checks.append(("independent behavioral probe", behavior.returncode == 0))
    tests = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=root,
        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"),
        capture_output=True,
        text=True,
        timeout=30,
    )
    checks.append(("remaining project unit tests", tests.returncode == 0))

    for label, passed in checks:
        print(f'{"PASS" if passed else "FAIL"} {label}')
    print(f"Case {args.case}: {sum(ok for _, ok in checks)}/{len(checks)} checks passed")
    if behavior.returncode:
        print("Behavior probe failed:\n" + behavior.stderr, file=sys.stderr)
    if tests.returncode:
        print("Project tests failed:\n" + tests.stderr, file=sys.stderr)
    return 0 if all(ok for _, ok in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
