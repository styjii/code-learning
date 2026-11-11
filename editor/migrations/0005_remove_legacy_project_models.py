from django.db import migrations


class Migration(migrations.Migration):
    """Étape 3/3 : suppression des anciennes colonnes (html, css, js) et des tables TypeScript et Python."""

    dependencies = [
        ("editor", "0004_copy_projects"),
    ]

    operations = [
        migrations.RemoveField(model_name="project", name="html"),
        migrations.RemoveField(model_name="project", name="css"),
        migrations.RemoveField(model_name="project", name="js"),
        migrations.DeleteModel(name="TypeScriptProject"),
        migrations.DeleteModel(name="PythonProject"),
    ]
