from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm

# Classbased Views For Listview:
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# Function Based View for CategoryView:
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html', {'cats':cats.title().replace('-',' '),'category_posts':category_posts})

# Classbased Views For DetailView:
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
# Classbased Views For CreateView:
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

# Classbased Views For CategoryView:
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields= '__all__'

# Classbased Views For UpdateView:
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title','title_tag','body']

# Classbased Views For Deleteview:
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


