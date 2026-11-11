from django.db import migrations, models


class Migration(migrations.Migration):
    """
    Étape 1/3 : un seul modèle ``Project`` pour les trois éditeurs.

    Ajoute ``editor`` et ``data`` et remplace la contrainte « nom unique par propriétaire » par « nom unique par
    propriétaire ET par éditeur » (avant la copie des projets TypeScript et Python, qui peuvent porter le même nom
    qu'un projet Web).
    """

    dependencies = [
        ("editor", "0002_python_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="editor",
            field=models.CharField(
                choices=[("codelab-js", "Web"), ("codelab-py", "Python"), ("codelab-ts", "TypeScript")],
                default="codelab-js",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="data",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.RemoveConstraint(
            model_name="project",
            name="unique_project_name_per_owner",
        ),
        migrations.AddConstraint(
            model_name="project",
            constraint=models.UniqueConstraint(
                fields=("owner", "editor", "name"), name="unique_project_name_per_owner_and_editor"),
        ),
    ]
