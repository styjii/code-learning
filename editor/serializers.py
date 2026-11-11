from rest_framework import serializers

from .models import Project

DUPLICATE_NAME_MESSAGE = "Un projet porte déjà ce nom."


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer unique des projets des trois éditeurs (champs : id, name + les champs de contenu de l'éditeur).

    L'éditeur courant (``editors.Editor``) est passé dans le contexte (``context["editor"]``) : c'est lui qui décide
    des champs de contenu (html/css/js, html/css/ts/compiler_options ou files), de leur validation et de ce qui est
    renvoyé au navigateur. Le contenu est stocké dans ``Project.data``.

    Le propriétaire et l'éditeur ne sont jamais fournis par le client : le premier vient de la session, le second de
    l'URL.
    """

    class Meta:
        model = Project
        fields = ["id", "name"]

    @property
    def editor(self):
        return self.context["editor"]

    def get_fields(self):
        fields = super().get_fields()
        fields.update(self.editor.fields())
        return fields

    def validate_name(self, value):
        """
        Le nom doit être unique parmi les projets de l'utilisateur dans cet éditeur.

        Ce contrôle donne un message clair dans le cas courant ; la contrainte en base
        (``unique_project_name_per_owner_and_editor``) reste la garantie finale, et la vue transforme son
        ``IntegrityError`` en 400 (deux requêtes simultanées peuvent passer ce contrôle ensemble).
        """
        user = self.context["request"].user
        duplicates = Project.objects.filter(owner=user, editor=self.editor.id, name=value)
        if self.instance is not None:
            duplicates = duplicates.exclude(pk=self.instance.pk)
        if duplicates.exists():
            raise serializers.ValidationError(DUPLICATE_NAME_MESSAGE)
        return value

    def to_representation(self, instance):
        return {"id": instance.pk, "name": instance.name, **self.editor.public(instance.data)}

    def create(self, validated_data):
        name = validated_data.pop("name")
        owner = validated_data.pop("owner", None)
        return Project.objects.create(
            owner=owner, editor=self.editor.id, name=name, data=self.editor.merge({}, validated_data))

    def update(self, instance, validated_data):
        instance.name = validated_data.pop("name", instance.name)
        instance.data = self.editor.merge(instance.data, validated_data)
        instance.save()
        return instance
