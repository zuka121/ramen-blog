from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment
from .forms import CommentForm

from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView

def home(request):
    return render(request, 'home.html')

def hokkaido(request):
    return render(request, 'hokkaido.html')

def tohoku(request):
    return render(request, 'tohoku.html')

def kanto(request):
    return render(request, 'kanto.html')

def tyubu(request):
    return render(request, 'tyubu.html')

def kinki(request):
    return render(request, 'kinki.html')

def tyugoku(request):
    return render(request, 'tyugoku.html')

def shikoku(request):
    return render(request, 'shikoku.html')

def kyusyu(request):
    return render(request, 'kyusyu.html')

def profile(request):
    return render(request, 'profile.html')

def wakayama(request):
    return render(request, 'wakayama.html')

def shimasyo(request):
    return render(request, 'shimasyo.html')



def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    form = None

    # ログインしている場合のみフォームを表示
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.save()
                return redirect('comment_list')
        else:
            form = CommentForm()

    context = {
        'comments': comments,
        'form': form
    }
    return render(request, 'comments/comment_list.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 登録後すぐにログインさせる場合
            return redirect('home')  # 成功後のリダイレクト先
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    # フォームが無効な場合の処理
    def form_invalid(self, form):
        # 独自のエラーメッセージを追加
        form.errors.clear()
        form.add_error(None, "ユーザー名またはパスワードが正しくありません　　もう一度入力してください")
        return super().form_invalid(form)