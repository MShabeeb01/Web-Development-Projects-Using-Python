from flask import Flask, render_template
app = Flask(__name__)

#Sample Blog Posts
posts = [
    {"id": 1, "title": "Introduction to Flask", "content": "Learn Flask Basics.","author": "Alice"},
    {"id": 2, "title":"Advanced Flask Routing", "content":"Understanding dynamic routes.","author":"John"},]
#A list of dictionaries that acts like a small database for now.

@app.route('/')
def home():
    return render_template('index.html', posts=posts)  
    #When you go to http://127.0.0.1:5000/ this function runs.It loads index.html and passes the posts list so the template can display them.

@app.route('/post/<int:post_id>')
def post_details(post_id):
    post = next((post for post in posts if post["id"]== post_id),None)
    if post:
        return render_template('post.html',post=post)
    return "<h1>Post Not Found</h1>", 404
    #Dynamic route → /post/1, /post/2, etc.
    #<int:post_id> means Flask will only accept numbers.
    #It searches the posts list for a matching ID:
    #If found → shows post.html with that post’s details.
    #If not found → shows a 404 error message.

if __name__ == '__main__':
    app.run(debug=True)
    #Runs the Flask server locally.
    #debug=True → Auto-reloads on code changes + shows error details.
