# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django import forms
from django.forms import widgets
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        min_length=4,
    )
    password = forms.CharField(
        label='密码',
        min_length=8,
        widget=widgets.PasswordInput,

    )
    # re_pwd = forms.CharField(
    #     label='确认密码',
    #     min_length=8,
    #     widget=widgets.PasswordInput,
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({"class": "form-control"})

    # def clean_re_pwd(self):
    #     pwd = self.cleaned_data['password']
    #     re_pwd = self.cleaned_data['re_pwd']
    #     if pwd == re_pwd:
    #         return re_pwd
    #     else:
    #         raise ValidationError("两次密码不一致")


class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        min_length=4,
    )
    password = forms.CharField(
        label='密码',
        min_length=8,
        widget=widgets.PasswordInput,

    )
    re_pwd = forms.CharField(
        label='确认密码',
        min_length=8,
        widget=widgets.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs.update({"class": "form-control"})

    def clean_re_pwd(self):
        pwd = self.cleaned_data['password']
        re_pwd = self.cleaned_data['re_pwd']
        if pwd == re_pwd:
            return re_pwd
        else:
            raise ValidationError("两次密码不一致")
