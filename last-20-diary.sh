for d in ~/Brave_New_Commune/data/diary/*; do
  echo "=== $(basename $d) ==="
  tail -n 20 "$d/kernels.jsonl"
  echo
done
