# Generated by Django 5.0.6 on 2024-06-03 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0010_remove_emprestimos_tempo_duracao'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]