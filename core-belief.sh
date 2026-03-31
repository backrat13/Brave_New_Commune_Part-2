for d in ~/Brave_New_Commune/data/axioms/*; do
  echo "=== $(basename $d) ==="
  tail -n 20 "$d/axiom_history.jsonl" | jq -r '.axioms.core_belief'
  echo
done
