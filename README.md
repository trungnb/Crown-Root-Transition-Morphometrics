# Crown–root transition morphometrics · exploratory prototype

> **CEJ-oriented prototype:** this project explores an intensity-derived crown–root
> transition proxy. It does **not** establish anatomical CEJ localisation.

**Idea:** explore whether changes in intensity along a segmented tooth can identify a
crown–root transition. Segmented teeth are aligned, their outer-shell intensity profiles
are sampled, and a heuristic searches for two relatively stable regions separated by a
transition zone.

```mermaid
flowchart LR
    Q["IDEA<br/>Explore a crown–root transition<br/>from tooth intensity changes"]
    Q --> A["REPRESENT<br/>Align teeth and extract shells<br/>Reduce them to intensity profiles"]
    A --> B["PROTOTYPE HEURISTIC<br/>Search for two stable regions<br/>and a transition zone"]
    B --> C["SAVED OUTPUTS<br/>Profiles and exploratory ratios<br/>16 teeth per case; two cases"]
    classDef idea fill:#EDF7F6,stroke:#168B8A,color:#17324D
    classDef output fill:#17324D,stroke:#17324D,color:#FFFFFF
    class Q idea
    class C output
```

## Saved result snapshot

| Case | Teeth | Median saved ratio | Saved range |
|---|---:|---:|---:|
| Person1 | 16 | 0.6885 | 0.375–3.222 |
| Person2 | 16 | 0.8315 | 0.569–3.625 |

Ratios summarize the historical `dynamic_10_90` output column `crown_root_ratio_mm`.
The numerator includes the transition zone. The chart shows all 16 teeth per case,
including large and anatomically implausible ratios. These are retained as prototype
failure cases, not reference CEJ annotations, validated measurements, or diagnostic results.

![Saved intensity profiles for one example tooth and all saved crown-root ratios](results/figures/prototype-overview.svg)

## How the prototype works

1. Start with CT/NIfTI images and existing tooth masks. Crop teeth and align them using
   principal axes.
2. Erode the binary tooth mask to make outer shells one to five voxels thick. For each
   slice, save shell voxel counts and intensity summaries (`mean`, `standard deviation`,
   `minimum`, `maximum`, and the historical `z_mm` field).
3. Compare shell profiles. The ratio notebooks use the three-voxel shell and search the
   10–90% profile interval for two stable regions separated by a transition. Candidate
   splits are scored using regional intensity differences, within-region variability, and
   a position weight. The maximum transition fraction varies by tooth type: 0.25 for
   incisors, 0.20 for canines/premolars, and 0.15 for molars.
4. Use profile direction to assign the crown side. The saved numerator is crown plus
   transition; the denominator is the root extent. The notebooks export slice-based and
   historically millimetre-labelled ratios.
5. `Pulp.ipynb` separately explores mask hole filling, cropping, PCA alignment, and
   interactive Matplotlib/Plotly slice views for one tooth.

## Notebooks and saved tables

| File | What it contains | Saved output represented here |
|---|---|---|
| [CEJ1](notebooks/CEJ1.ipynb) / [CEJ2](notebooks/CEJ2.ipynb) | Historical shell-profile experiments for Person1 / Person2 | FDI 11 shell-3 intensity profiles |
| [ratio1](notebooks/ratio1.ipynb) / [ratio2](notebooks/ratio2.ipynb) | Profile comparisons, heuristic zone search, and ratio export | 16 dynamic 10–90% ratios per case |
| [Pulp](notebooks/Pulp.ipynb) | Single-tooth mask filling, cropping, PCA, and interactive views | No table in this release |

| Saved file | Contents | Source |
|---|---|---|
| [`results/crown_root_ratio_dynamic_10_90.csv`](results/crown_root_ratio_dynamic_10_90.csv) and [`results/P2/crown_root_ratio_dynamic_10_90.csv`](results/P2/crown_root_ratio_dynamic_10_90.csv) | 16 historical ratios per case | `ratio1.ipynb` / `ratio2.ipynb` |
| [`results/ratio_summary.csv`](results/ratio_summary.csv) | Count, median, minimum, and maximum of saved `crown_root_ratio_mm` values | Descriptive calculation from the two ratio tables |
| [`results/3/upper_right_central_incisor_fdi11.csv`](results/3/upper_right_central_incisor_fdi11.csv) and [`results/P2/3/upper_right_central_incisor_fdi11.csv`](results/P2/3/upper_right_central_incisor_fdi11.csv) | FDI 11 per-slice intensity profile; shell thickness three voxels | `CEJ1.ipynb` / `CEJ2.ipynb` |
| [`results/figures/prototype-overview.svg`](results/figures/prototype-overview.svg) | Example profiles and all saved ratios | [`scripts/render_figures.py`](scripts/render_figures.py) and the four source profile/ratio tables above |

Column names are preserved from the historical notebooks. `crown_trans_mm` includes the
transition zone, `root_mm` is the saved root extent, and `trans_ratio_used` records the
tooth-type transition fraction. Large ratios are shown without outlier filtering or
retrospective correction.

## Limitations and interpretation

This is an early exploratory implementation, retained to show the development process.
The transition is an **intensity-derived proxy**, not a validated anatomical CEJ.

- PCA uses voxel-index coordinates rather than explicit physical/world coordinates. This
  matters when voxel spacing is anisotropic.
- After rotation, the historical code uses the original image z-spacing for `z_mm`.
  Millimetre-labelled lengths and ratios are therefore exploratory, not validated physical
  morphometry.
- Shell thickness is set in erosion voxels, not millimetres. Rotation and interpolation
  can affect the intensity profiles.
- The 10–90% search interval, minimum stable-region length, position weighting, and
  tooth-specific transition limits are hand-crafted assumptions.
- The profile panel shifts each saved `z_mm` series to start at zero independently; it
  does not recalculate alignment.
- There are no manual CEJ reference annotations, inter-rater comparisons, external
  validation, or clinical validation. The two cases do not establish population-level
  performance or diagnostic utility.

The historical notebooks and saved outputs were not rerun or retrospectively corrected
for this portfolio release. No segmentation, model training, or reproduction audit was
performed. Exact historical software versions, hardware, and input image versions are
not fully documented.

## Inputs and viewing

The notebooks refer to CT/NIfTI images and tooth masks from two cases. Raw scans, masks,
and acquisition/consent records are not distributed. Notebook paths to Colab/Google Drive
are preserved for historical context. Running the research notebooks requires authorised
input data, suitable compute resources, and dependencies; the original runtime is not
reconstructed here. Notebooks can be read directly on GitHub.

The figure renderer reads only the published CSV tables; it does not run image processing.
To render the SVG with Python 3.11–3.13:

```bash
python -m pip install -r requirements.txt
python scripts/render_figures.py
```

`requirements.txt` covers chart rendering. Notebook imports include additional libraries,
but exact historical package versions and a complete analysis environment are unverified.
The figure was rendered from saved results for this release.

## Provenance and reuse

The original analysis cell sources, parameters, and order are preserved in all five
notebooks. Publication clears session metadata, widget state, and output previews; no
notebook output cells are retained. The four selected source CSVs are existing saved
tables, byte-for-byte unchanged. Hashes and source details are recorded in
[`docs/data-provenance.md`](docs/data-provenance.md). Raw scans, masks, unrelated notebooks,
and local backups are excluded from Git.

No project-wide open-source license has been selected. Public availability does not grant
reuse rights; see [`LICENSE`](LICENSE). Third-party libraries and source datasets retain
their own terms.

**Author:** [trungnb](https://github.com/trungnb) · [Academic website](https://trungnb.github.io/)
