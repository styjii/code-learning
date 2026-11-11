from django.db import migrations

JS, TS, PY = "codelab-js", "codelab-ts", "codelab-py"


def forwards(apps, schema_editor):
    """Web : le contenu passe dans ``data`` ; TypeScript et Python : une ligne ``Project`` par ancien projet."""
    Project = apps.get_model("editor", "Project")
    TypeScriptProject = apps.get_model("editor", "TypeScriptProject")
    PythonProject = apps.get_model("editor", "PythonProject")

    for project in Project.objects.filter(editor=JS).iterator():
        project.data = {"html": project.html, "css": project.css, "js": project.js}
        project.save(update_fields=["data"])

    Project.objects.bulk_create([
        Project(
            owner_id=old.owner_id, editor=TS, name=old.name,
            data={"html": old.html, "css": old.css, "ts": old.ts, "compiler_options": old.compiler_options},
        )
        for old in TypeScriptProject.objects.order_by("id").iterator()
    ])
    Project.objects.bulk_create([
        Project(owner_id=old.owner_id, editor=PY, name=old.name, data={"files": old.files})
        for old in PythonProject.objects.order_by("id").iterator()
    ])


def backwards(apps, schema_editor):
    """Inverse : redistribue les projets dans les anciennes tables."""
    Project = apps.get_model("editor", "Project")
    TypeScriptProject = apps.get_model("editor", "TypeScriptProject")
    PythonProject = apps.get_model("editor", "PythonProject")

    for project in Project.objects.filter(editor=JS).iterator():
        data = project.data or {}
        project.html, project.css, project.js = data.get("html", ""), data.get("css", ""), data.get("js", "")
        project.save(update_fields=["html", "css", "js"])

    TypeScriptProject.objects.bulk_create([
        TypeScriptProject(
            owner_id=p.owner_id, name=p.name, html=(p.data or {}).get("html", ""), css=(p.data or {}).get("css", ""),
            ts=(p.data or {}).get("ts", ""), compiler_options=(p.data or {}).get("compiler_options", {}),
        )
        for p in Project.objects.filter(editor=TS).order_by("id").iterator()
    ])
    PythonProject.objects.bulk_create([
        PythonProject(owner_id=p.owner_id, name=p.name, files=(p.data or {}).get("files", []))
        for p in Project.objects.filter(editor=PY).order_by("id").iterator()
    ])
    Project.objects.exclude(editor=JS).delete()


class Migration(migrations.Migration):
    """Étape 2/3 : copie des projets existants dans le modèle unique (aucune perte, aucun renommage)."""

    dependencies = [
        ("editor", "0003_project_editor_data"),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
