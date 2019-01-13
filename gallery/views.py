from django.shortcuts import render
from .models import Photo, Topic
from django.views import View
from django.views.generic import DetailView


class TopicListView(View):
    def get(self, request):
        topics = Topic.objects.all()
        ctx = {
            'topics': topics
        }
        return render(request, 'gallery/topic_list.html', ctx)


class GalleryListView(View):

    def get(self, request, id):
        images = Photo.objects.filter(topic_id=id)
        ctx = {
            'images': images,
        }
        return render(request, 'gallery/topic.html', ctx)


# def detail(request, topic_name, photo_id):
#     photo = get_object_or_404(Photo, topic__name=topic_name, id=photo_id)
#     return render(request, 'gallery/detail.html', {'photo': photo})


class GalleryDetailView(DetailView):
    queryset = Photo.objects.all()
    template_name = 'gallery/detail.html'
