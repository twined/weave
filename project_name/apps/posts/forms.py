# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Submit,
    HTML, Field, Fieldset)
from tinymce.widgets import TinyMCE
from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'well test'
        self.helper.layout = Layout(
            Field(
                'post_type',
                css_class="span4 disabled",
                readonly=True),
            Field('status', css_class="span4"),

            HTML('<div class="row">'),
            Fieldset(
                '',
                Field('header', placeholder="Header",
                    css_class="hw"),
                Field('slug', placeholder="header",
                    css_class="hw disabled"),
                css_class="span8",
            ),
            HTML('</div>'),

            HTML('<div class="row">'),
            Fieldset(
                '',
                Field('lead', placeholder="Lead",
                    css_class="fw"),
                Field('body', placeholder="Main body",
                    css_class="fw"),
                css_class="span8",
            ),
            HTML('</div>'),
            Field('publish_at', css_class="span4"),
        )
        self.helper.add_input(
            Submit('submit', 'Save', css_class="btn btn-primary"))

        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        exclude = ('user',)
