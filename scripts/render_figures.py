"""Render portfolio charts from saved CSV tables only. No notebook execution."""

import csv
import re
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
OUT = RESULTS / "figures"
OUT.mkdir(exist_ok=True)
NAVY, TEAL, ORANGE = "#17324D", "#168B8A", "#D17845"
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.labelcolor": NAVY,
        "text.color": NAVY,
        "axes.titleweight": "bold",
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "svg.fonttype": "none",
    }
)


def rows(name):
    with (RESULTS / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def save(fig, name, footer):
    fig.text(0.06, 0.018, footer, fontsize=8, color="#586777")
    fig.savefig(OUT / (name + ".svg"), bbox_inches="tight")
    svg = OUT / (name + ".svg")
    svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
    plt.close(fig)


cases = [
    ("Person1", "ratios_person1.csv", TEAL),
    ("Person2", "ratios_person2.csv", ORANGE),
]
fig, (a, b) = plt.subplots(
    1, 2, figsize=(12.8, 6.2), gridspec_kw={"width_ratios": [1.15, 1]}
)
fig.subplots_adjust(left=0.075, right=0.97, top=0.79, bottom=0.19, wspace=0.32)
fig.suptitle(
    "Exploring crown–root transition from tooth intensity profiles",
    x=0.06,
    ha="left",
    y=0.97,
    fontsize=18,
    fontweight="bold",
)
fig.text(
    0.06,
    0.90,
    "Exploratory prototype • shell-intensity profiles and saved crown–root ratios in two cases",
    fontsize=11,
    color="#586777",
)
for person, file, color in cases:
    profile = "profiles/person1_fdi11_shell3.csv" if person == "Person1" else "profiles/person2_fdi11_shell3.csv"
    data = rows(profile)
    x = [float(r["z_mm"]) for r in data]
    x = [v - x[0] for v in x]
    a.plot(x, [float(r["mean_HU"]) for r in data], color=color, lw=2, label=person)
a.set(
    xlabel="Saved z_mm offset (historical mm label; exploratory)",
    ylabel="Mean shell intensity",
)
a.set_title(
    "A  Example tooth: upper right central incisor", loc="left", pad=14, fontsize=10
)
a.text(
    0.98,
    0.98,
    "3-voxel shell • FDI 11 • each case starts at zero",
    transform=a.transAxes,
    va="top",
    ha="right",
    fontsize=9,
    color="#586777",
)
a.grid(axis="y", alpha=0.15)
a.legend(frameon=False, loc="lower right")
data1, data2 = rows(cases[0][1]), rows(cases[1][1])
labels = [re.search(r"fdi(\d+)", r["filename"])[1] for r in data1]
lookup = {r["filename"]: float(r["crown_root_ratio_mm"]) for r in data2}
for i, r in enumerate(data1):
    x1 = float(r["crown_root_ratio_mm"])
    x2 = lookup[r["filename"]]
    b.scatter(x1, i, color=TEAL, marker="o", s=38, label="Person1" if i == 0 else None, zorder=2)
    b.scatter(x2, i, color=ORANGE, marker="s", s=38, label="Person2" if i == 0 else None, zorder=2)
b.set(
    yticks=range(16),
    yticklabels=labels,
    xlabel="Saved crown + transition / root ratio",
    ylabel="FDI tooth number",
    xlim=(0, 4),
)
b.invert_yaxis()
b.set_title("B  Sixteen teeth per case", loc="left", pad=14, fontsize=10)
b.grid(axis="x", alpha=0.15)
b.legend(frameon=False, loc="upper right", bbox_to_anchor=(1, -0.18), ncol=2)
save(
    fig,
    "prototype-overview",
    "Sources: selected shell-3 intensity CSVs and published ratio tables. All 16 teeth shown; cases are not paired; no CEJ recalculation.",
)
