from ..config.mysqlconnection import connectToMySQL

class User:

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('friendships_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_all_friendships(cls):
        query  = "SELECT * FROM users JOIN friendships ON users.id = friendships.user_id JOIN users AS friends ON friendships.friend_id=friends.id;"
        result = connectToMySQL('friendships_schema').query_db(query)
        return result

    @classmethod
    def create_user(cls, data):
        query="INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        user_id = connectToMySQL('friendships_schema').query_db(query, data)
        return user_id

    @classmethod
    def create_friendship(cls, data):
        query="INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES (%(user_id)s, %(friend_id)s, NOW(), NOW());"
        friendship_id = connectToMySQL('friendships_schema').query_db(query, data)
        return friendship_id

    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO books ( title , num_of_pages, created_at, updated_at ) VALUES ( %(title)s, %(num_of_pages)s, NOW() , NOW() );"
    #     return connectToMySQL('friendships_schema').query_db( query, data )

    # @classmethod
    # def get_one(cls,data):
    #     query  = "SELECT * FROM books WHERE id = %(id)s;"
    #     result = connectToMySQL('books_schema').query_db(query, data)
    #     return cls(result[0])

    # @classmethod
    # def get_by_id(cls,data):
    #     query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
    #     results = connectToMySQL('books_schema').query_db(query,data)

    #     book = cls(results[0])

    #     for row in results:
    #         if row['authors.id'] == None:
    #             break
    #         data = {
    #             "id": row['authors.id'],
    #             "first_name": row['first_name'],
    #             "last_name": row['last_name'],
    #             'created_at': row['created_at'],
    #             'updated_at': row['updated_at']
    #         }
    #         book.authors_who_favorited.append(author.Author(data))
    #     return book

    # @classmethod
    # def unfavorited_books(cls,data):
    #     query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
    #     results = connectToMySQL('books_schema').query_db(query,data)
    #     books = []
    #     for row in results:
    #         books.append(cls(row))
    #     print(books)
    #     return books
    # @classmethod
    # def dojo_with_members(cls, data ):
    #     query = "SELECT * FROM books LEFT JOIN authors on books.id = authors.book_id WHERE books.id = %(id)s;"
    #     results = connectToMySQL('books_schema').query_db(query,data)
    #     book = cls(results[0])
    #     for row in results:
    #         n = {
    #             'id': row['books.id'],
    #             'title': row['title'],
    #             'num_of_pages': row['num_of_pages'],
    #             'created_at': row['books.created_at'],
    #             'updated_at': row['books.updated_at']
    #         }
    #         book.authors.append(Author(n))
    #     return book


    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE users SET first_name=%(fname)s,last_name=%(lname)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('books_schema').query_db(query,data)

    # @classmethod
    # def delete(cls,data):
    #     query  = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('books_schema').query_db(query,data)