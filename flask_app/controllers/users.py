from flask_app import app
from flask import redirect, render_template,request
from ..models.user import User

@app.route('/')
def home():
    return redirect('/friendships')

@app.route('/friendships')
def friendships_display():
    all_friends = User.get_all_friendships()
    all_users = User.get_all()
    return render_template('friendships.html', all_friends=all_friends, all_users=all_users)

@app.route('/friendships/create', methods=['POST'])
def create_friendship():
    data={
        'user_id':request.form['user_id'],
        'friend_id':request.form['friend_id']
    }
    User.create_friendship(data)
    return redirect('/friendships')

@app.route('/friendships/newuser', methods=['POST'])
def create_user():
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name']
    }
    User.create_user(data)
    return redirect('/friendships')

# @app.route('/books/create',methods=['POST'])
# def create_book():
#     Book.save(request.form)
#     return redirect('/books')

# @app.route('/books/<int:id>')
# def show_book(id):
#     data ={
#         "id":id
#     }
#     return render_template("show_book.html", book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

# @app.route('/join/author',methods=['POST'])
# def join_author():
#     data = {
#         'author_id': request.form['author_id'],
#         'book_id': request.form['book_id']
#     }
#     Author.add_favorite(data)
#     return redirect(f"/books/{request.form['book_id']}")

# @app.route('/users/new')
# def new():
#     return render_template("create.html")


# @app.route('/user/edit/<int:id>')
# def edit(id):
#     data ={
#         "id":id
#     }
#     return render_template("edit.html", user = User.get_one(data))


# @app.route('/user/update',methods=['POST'])
# def update():
#     User.update(request.form)
#     return redirect('/users')

# @app.route('/user/delete/<int:id>')
# def delete(id):
#     data = {
#         'id': id
#     }
#     User.delete(data)
#     return redirect('/users')