from django.http import StreamingHttpResponse
from django.views.generic import DetailView, TemplateView, FormView, ListView, UpdateView

from .forms import *
from .stream import VideoCamera, gen


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                        content_type='multipart/x-mixed-replace; boundary=frame')

# class IndexView(TemplateView):
#     template_name = 'kulichtv/index.html'


class CommunityAddView(FormView):
    template_name = 'kulichtv/add_community.html'
    form_class = CommunityPostForm
    success_url = '/communities/'

    def form_valid(self, form):
        form.save()
        return super(CommunityAddView, self).form_valid(form)


class CommunityView(ListView):
    model = Community
    template_name = 'kulichtv/communities.html'

    def get_context_data(self, **kwargs):
        context = super(CommunityView, self).get_context_data(**kwargs)
        context['communities'] = Community.objects.all()
        return context


class CommunityUpdateView(UpdateView):
    model = Community
    template_name = 'kulichtv/update_community.html'
    form_class = CommunityPostForm


class CommunityDetailView(DetailView):
    model = Community
    template_name = 'kulichtv/detail_community.html'
    context_object_name = 'community'


class IndexView(ListView):
    model = Game
    template_name = 'kulichtv/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['games'] = Game.objects.all()
        return context