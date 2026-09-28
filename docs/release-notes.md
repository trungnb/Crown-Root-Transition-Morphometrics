# Portfolio packaging checks

2026-09-28.

Local Markdown targets were checked against the files selected for Git. Notebook analysis cell
sources and order were compared with local originals; hashes are recorded in the provenance
manifest. Raw image formats, row-level input data, unrelated notebooks and local backups are
excluded from Git. Selected public text was checked for common credential patterns.

The initial identifier scan flagged decimal digit sequences in four intensity-statistic columns.
Their numeric measurement contents were reviewed; these columns were allowed in the final
pattern scan. No remaining listed identifier pattern was found. Pattern scans do not establish
de-identification or rule out indirect identifiers. Public notebooks were scanned as JSON as
well as structurally inspected.

Figures were rendered from saved tables and visually inspected. The chart scripts passed Ruff
checks. No research notebook, segmentation, training, scientific validation or reproducibility
audit was run. These checks concern the publication package only.

A subsequent documentation-only review clarified the scientific scope of the prototype.
The README and methods now distinguish the intensity-derived crown–root transition proxy from
an anatomical CEJ, document voxel-space/spacing and interpolation limitations, and retain
extreme ratios as visible prototype failure cases. Historical notebooks, parameters, saved
tables and analysis outputs were not changed or rerun.
