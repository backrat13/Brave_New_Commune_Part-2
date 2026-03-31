grep -RIn --include="*.py" \
  --exclude-dir=BNC \
  --exclude-dir=.venv \
  --exclude-dir=venv \
  --exclude-dir=site-packages \
  -E '@(app|bp|blueprint)\.route|add_url_rule' \
  ~/Brave_New_Commune
