import sys
sys.path.insert(0, ".")
errors = []

SECTIONS = [
    ("sections.hero",             "render_hero"),
    ("sections.about",            "render_about"),
    ("sections.skills",           "render_skills"),
    ("sections.projects",         "render_projects"),
    ("sections.experience",       "render_experience"),
    ("sections.education",        "render_education"),
    ("sections.certifications",   "render_certifications"),
    ("sections.achievements",     "render_achievements"),
]

for module_path, fn_name in SECTIONS:
    try:
        import importlib
        mod = importlib.import_module(module_path)
        fn  = getattr(mod, fn_name)
        assert callable(fn), f"{fn_name} is not callable"
        print(f"[PASS] {module_path}.{fn_name} — importable and callable")
    except Exception as e:
        errors.append(f"[FAIL] {module_path}: {e}")
        import traceback; traceback.print_exc()

# ── Extra structural checks ────────────────────────────────────────────────

# hero.py — verify it imports 3D photo and PERSONAL_INFO
try:
    import inspect, sections.hero as hero_mod
    src = inspect.getsource(hero_mod)
    assert "render_3d_photo"   in src, "Missing render_3d_photo import"
    assert "gradient-text"     in src, "Missing gradient-text CSS class"
    assert "typewriter"        in src, "Missing typewriter animation"
    assert "download_button"   in src, "Missing download_button for resume"
    assert 'id="home"'         in src, "Missing anchor id=home"
    print("[PASS] hero.py — structural checks: 3D photo, gradient-text, typewriter, download_button, anchor")
except Exception as e:
    errors.append(f"[FAIL] hero.py structural: {e}")

# about.py — verify bio and traits
try:
    import inspect, sections.about as about_mod
    src = inspect.getsource(about_mod)
    assert "render_3d_photo" in src, "Missing 3D photo"
    assert "traits"          in src, "Missing traits"
    assert 'id="about"'      in src, "Missing anchor id=about"
    print("[PASS] about.py — structural checks: 3D photo, traits, anchor")
except Exception as e:
    errors.append(f"[FAIL] about.py structural: {e}")

# skills.py — verify badge grid + skill_chart call
try:
    import inspect, sections.skills as skills_mod
    src = inspect.getsource(skills_mod)
    assert "render_skill_chart" in src, "Missing render_skill_chart"
    assert "skill-category"     in src, "Missing skill-category CSS"
    assert 'id="skills"'        in src, "Missing anchor id=skills"
    print("[PASS] skills.py — structural checks: render_skill_chart, skill-category, anchor")
except Exception as e:
    errors.append(f"[FAIL] skills.py structural: {e}")

# projects.py — verify render_card and all 5 projects usable
try:
    import inspect, sections.projects as proj_mod
    from utils.data import PROJECTS
    src = inspect.getsource(proj_mod)
    assert "render_card"   in src, "Missing render_card"
    assert 'id="projects"' in src, "Missing anchor id=projects"
    assert len(PROJECTS) == 5, f"Expected 5 projects, got {len(PROJECTS)}"
    for p in PROJECTS:
        assert p.get("url"), f"Project missing url: {p['title']}"
    print(f"[PASS] projects.py — structural checks: render_card, anchor, {len(PROJECTS)} projects with URLs")
except Exception as e:
    errors.append(f"[FAIL] projects.py structural: {e}")

# experience / education — verify timeline calls
try:
    import inspect
    import sections.experience as exp_mod
    import sections.education  as edu_mod
    exp_src = inspect.getsource(exp_mod)
    edu_src = inspect.getsource(edu_mod)
    assert "render_timeline" in exp_src and 'id="experience"' in exp_src
    assert "render_timeline" in edu_src and 'id="education"'  in edu_src
    from utils.data import EXPERIENCE, EDUCATION
    assert len(EXPERIENCE) == 2, f"Expected 2, got {len(EXPERIENCE)}"
    assert len(EDUCATION)  == 3, f"Expected 3, got {len(EDUCATION)}"
    print(f"[PASS] experience.py + education.py — render_timeline called, anchors OK")
except Exception as e:
    errors.append(f"[FAIL] experience/education structural: {e}")

# certifications.py — verify status badge logic
try:
    import inspect, sections.certifications as cert_mod
    from utils.data import CERTIFICATIONS
    src = inspect.getsource(cert_mod)
    assert "In Progress" in src,  "Missing In Progress badge logic"
    assert "Completed"   in src,  "Missing Completed badge logic"
    assert 'id="certifications"' in src
    assert len(CERTIFICATIONS) == 5
    in_prog = [c for c in CERTIFICATIONS if c["status"] == "In Progress"]
    completed = [c for c in CERTIFICATIONS if c["status"] == "Completed"]
    assert len(in_prog)  == 1, f"Expected 1 In Progress, got {len(in_prog)}"
    assert len(completed) == 4, f"Expected 4 Completed, got {len(completed)}"
    print(f"[PASS] certifications.py — 5 certs, 4 Completed, 1 In Progress, badges OK")
except Exception as e:
    errors.append(f"[FAIL] certifications.py structural: {e}")

# achievements.py — verify 4 cards
try:
    import inspect, sections.achievements as ach_mod
    from utils.data import ACHIEVEMENTS
    src = inspect.getsource(ach_mod)
    assert "achievement-card"  in src
    assert 'id="achievements"' in src
    assert len(ACHIEVEMENTS) == 4
    for a in ACHIEVEMENTS:
        for key in ["icon", "value", "label", "detail"]:
            assert key in a, f"Achievement missing key: {key}"
    print(f"[PASS] achievements.py — 4 cards, all required keys present")
except Exception as e:
    errors.append(f"[FAIL] achievements.py structural: {e}")

# ── Summary ────────────────────────────────────────────────────────────────
print()
if errors:
    for err in errors:
        print(err)
    sys.exit(1)
else:
    print("ALL SECTION 4.1–4.8 IMPORT & STRUCTURAL TESTS PASSED")
