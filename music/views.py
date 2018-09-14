from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from music.utils import AjaxableResponseMixin

from music.models import Album, Track
from music.forms import TrackFormSet
# Create your views here.

class AlbumListView(ListView):
    model = Album


class AlbumCreateView(AjaxableResponseMixin, CreateView):
    model = Album
    success_url = reverse_lazy('music:album_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AlbumCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Create new album'
        if self.request.POST and self.request.is_ajax():
            context['track_formset'] = TrackFormSet(self.request.POST)
        else:
            context['track_formset'] = TrackFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['track_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumUpdateView(AjaxableResponseMixin, UpdateView):
    model = Album
    success_url = reverse_lazy('music:album_list')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(AlbumUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Album update'
        if self.request.POST:
            context['track_formset'] = TrackFormSet(self.request.POST, instance=self.object)
            context['track_formset'].full_clean()
        else:
            context['track_formset'] = TrackFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['track_formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('music:album_list')