from django.shortcuts import render,redirect,reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .form import PostCreateForm, CategorieForm, CommentCreateForm
from .models import Post, Categorie, Comment

from django.shortcuts import get_object_or_404

# Create your views here.


class CategorieListView(ListView):
    model = Categorie
    template_name = "categories_list.html"


def CategorieView(request, cats):

    return render(request, 'posts.html', {"cats":cats})


class CategorieCreateView(CreateView):
    model = Categorie
    template_name = "categorie_create.html"
    form_class = CategorieForm
    success_url = reverse_lazy("list-categories")

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the author to the logged-in user
        return super().form_valid(form)


class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "categorie_delete.html"

    success_url = reverse_lazy("list-categories")


class CategorieEditView(UpdateView):
    model = Categorie
    template_name = "categorie_edit.html"
    form_class = CategorieForm
    success_url = reverse_lazy("list-categories")


class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "categorie_detail.html"


class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorie_id'] = self.kwargs['categorie_id']
        return context

    def get_queryset(self):
        categorie_id = self.kwargs['categorie_id']
        return Post.objects.filter(categorie_id=categorie_id)


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "post_create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.categorie = get_object_or_404(Categorie, id=self.kwargs['categorie_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_list", kwargs={"categorie_id": self.kwargs['categorie_id']})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"

    def get_success_url(self):
        return reverse("post_list", kwargs={"categorie_id": self.object.categorie_id})


class PostEditView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = (
        "title",
        "content",
    )

    def get_success_url(self):
        return reverse("post_list", kwargs={"categorie_id": self.object.categorie_id})


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = post.total_likes()
        context['liked_by'] = post.likes.all()
        context['liked'] = liked
        return context


def LikeView(request, categorie_id, post_id, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[categorie_id, post_id]))


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "add_comment.html"

    def form_valid(self, form):

        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post_detail", kwargs={"categorie_id": self.kwargs['categorie_id'], "pk": self.kwargs['post_id']})


class CommentEditView(UpdateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "comment_edit.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"categorie_id": self.kwargs['categorie_id'], "pk": self.kwargs['post_id']})


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "comment_delete.html"

    def get_success_url(self):
        return reverse("post_detail", kwargs={"categorie_id": self.kwargs['categorie_id'], "pk": self.kwargs['post_id']})

def user_posts(request):
    user = request.user  # Assuming the user is authenticated
    posts = Post.objects.filter(author=user)
    context = {'posts': posts}
    return render(request, 'user_posts.html', context)