# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from about_form import models


def check_name(value):
    if 'lq' in value:
        raise ValidationError("用户名不能包含lq")


class RegForm(forms.Form):
    user = forms.CharField(
        label='用户名',
        required=True,
        min_length=6,
        initial='Laura_lq',
        disabled=False,
        validators=[check_name],
        error_messages={
            'min_length': 'too short name',
            'required': 'can not be empty',
        }

    )

    pwd = forms.CharField(
        label='密码',
        min_length=6,
        widget=widgets.PasswordInput(),
    )

    re_pwd = forms.CharField(
        label="确认密码",
        min_length=6,
        widget=widgets.PasswordInput()
    )
    phone = forms.CharField(
        label='手机号',
        # validators=[
        #     RegexValidator(r"^1[3-9]\d{9}$", "phone number is error")
        # ]
    )
    gender = forms.ChoiceField(
        label="性别",
        choices=((1, '男'), (2, '女')),
        # widget=widgets.CheckboxSelectMultiple(),
    )

    # MultipleChoiceField 多选字段不能用单选的字段去接，会报错
    hobby = forms.MultipleChoiceField(
        label="爱好",
        # choices=((1, 'football'), (2, "basketball"), (3, "doublecolorball")),
        choices=models.Hobby.objects.all().values_list("id", "name"),
        widget=widgets.SelectMultiple(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 在字段中写会导致，在数据库中添加数据的时候，刷新后页面不展示，写在init函数中，保证每次都可以刷新最新的数据
        self.fields['hobby'].choices = models.Hobby.objects.all().values_list("id", "name")
        for i in self.fields:
            self.fields[i].widget.attrs.update({"class": 'form-control'})

    def clean_phone(self):
        value = self.cleaned_data.get("phone")
        if re.match(r'^1[3-9]\d{9}$', value):
            return value
        raise ValidationError("phone number is wrong")

    def clean_re_pwd(self):
        pwd = self.cleaned_data.get("pwd")
        re_pwd = self.cleaned_data.get("re_pwd")

        if pwd == re_pwd:
            return re_pwd
        raise ValidationError("pwd not equal re_pwd")

    # def clean(self):
    #     pwd = self.cleaned_data.get("pwd")
    #     re_pwd = self.cleaned_data.get('re_pwd')
    #
    #     if pwd == re_pwd:
    #         return self.cleaned_data
    #     self.add_error('re_pwd', 're_pwd is not equal pwd')
    #     raise ValidationError('re_pwd is not equal pwd')