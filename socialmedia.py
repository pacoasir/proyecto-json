def opcion1(posts):
    likes_por_usuario = {}
    total_likes_todos = 0
    for post in posts:
        author_username = post['author']['username']
        author_fullname = post['author']['full_name']
        likes = post['likes']
        if author_username in likes_por_usuario:
            likes_por_usuario[author_username, author_fullname] += likes
        else:
            likes_por_usuario[author_username, author_fullname] = likes
        
        total_likes_todos += likes
  
    print("{:<15} {:<15} {:<10}".format("USUARIO", "NOMBRE", "TOTAL LIKES"))
    print("-" * 50)
    for (username, full_name), total_likes in likes_por_usuario.items():
        print("{:<15} {:<15} {:<10}".format(username, full_name, total_likes))
    print("-" * 50)
    print("{:<30} {:<10}".format("TOTAL DE LIKES:", total_likes_todos))    

def opcion2(posts):
    total_comentarios = 0
    for post in posts:
        total_comentarios += len(post['comments'])
    print(f"Total de comentarios en todos los posts: {total_comentarios}")

def opcion3(posts, username):
    comprobacion_usuario = False
    for post in posts:
        if post['author']['username'] == username:
            comprobacion_usuario = True
            print(f"Post ID: {post['post_id']}")
            print(f"Timestamp: {post['timestamp']}")
            print(f"Contenido: {post['content']}")
            print(f"Likes: {post['likes']}")
            print(f"Comentarios: {len(post['comments'])}")
            print(f"Shares: {post['shares']}")
            print("------")
    if not comprobacion_usuario:
        print("Ese usuario no existe")

def opcion4(posts, username):
    comentario_encontr = False
    for post in posts:
        if post['likes'] > 100:
            for comment in post['comments']:
                if comment['commenter']['username'] == username:
                    comentario_encontr = True
                    print(f"Post ID: {post['post_id']}")
                    print(f"Fecha y Hora: {post['timestamp']}")
                    print(f"Contenido del comentario: {comment['comment_text']}")
                    print("------")
    if not comentario_encontr:
        print("No hay comentarios en publicaciones con mas de 100 likes de este usuario")

def opcion5(posts, min_comparticiones):
    usuarios_compart = []
    for post in posts:
        if post['shares'] > min_comparticiones:
            autor = post['author']['full_name']
            usuarios_compart.append({
                'autor': autor,
                'comparticiones': post['shares'],
                'publicacion': post['content'],
                'comentarios': post['comments']
            })
    
    print(f"Usuarios que han compartido más de {min_comparticiones} veces:")
    for usuario in usuarios_compart:
        print(f"Usuario: {usuario['autor']}")
        print(f"Comparticiones: {usuario['comparticiones']}")
        print(f"Publicación compartida: {usuario['publicacion']}")
        if usuario['comentarios']:
            print("Comentarios:")
            for comentario in usuario['comentarios']:
                print(f"- {comentario['commenter']['full_name']}: {comentario['comment_text']}")
        else:
            print("No hay comentarios en esta publicación.")
        print()

