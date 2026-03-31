find ~/Brave_New_Commune/data/diary -name "kernels.jsonl" \
  -exec cat {} \; \
| jq -s 'sort_by(.timestamp) | .[-20:][] | "\(.agent): \(.content)"'
