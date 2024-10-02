from django.shortcuts import render, get_object_or_404, redirect
from .models import Comment, Store
from .forms import CommentForm, StoreForm
from django.db.models import Count
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
    stores = Store.objects.filter(prefecture='和歌山').annotate(comment_count=Count('comments'))
    return render(request, 'wakayama.html', {'stores': stores })

def shimasyo(request):
    return render(request, 'shimasyo.html')

def home_320(request):
    return render(request, 'home-320.html')

def kinki_320(request):
    return render(request, 'kinki-320.html')



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
    

def store_detail(request, store_id):
    store = get_object_or_404(Store, id=store_id)
    
    if store_id == 1:
        return redirect('shimasyo', page=1)
    if store_id == 2:
        return redirect('seino', page=1)
    


def upload_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)  # 画像ファイルも含める
        if form.is_valid():
            form.save()  # データを保存
            return redirect('store_list')  # アップロード後にリダイレクト
    else:
        form = StoreForm()
    
    return render(request, 'image_form.html', {'form': form})



def shimasyo(request, page):
    store = get_object_or_404(Store, id=1)
    comments = store.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.store = store
            comment.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = CommentForm()

    context = {
        'store': store,
        'comments': comments,
        'form': form,
    }
    if page == 1:
        return render(request, 'shimasyo.html', context)
    
def seino(request, page):
    store = get_object_or_404(Store, id=2)
    comments = store.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.store = store
            comment.save()
            return redirect('store_detail', store_id=store.id)
    else:
        form = CommentForm()

    context = {
        'store': store,
        'comments': comments,
        'form': form,
    }
    if page == 1:
        return render(request, 'seino/1.html', context)
    if page == 2:
        return render(request, 'seino/2.html', context)