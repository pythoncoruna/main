from wordpress_xmlrpc import *
from wordpress_xmlrpc.methods.posts import *
from wordpress_xmlrpc.methods.users import *
from wordpress_xmlrpc.compat import *
import time

wordpress = Client('http://dominio.url/xmlrpc.php', 'usuario', 'contraseña')

ahora = int(time.time())
print(ahora)

i = 2
while i < 6:
	post = WordPressPost()
	post.title = "pyBirras Test " + str(i)
	post.content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
	post.date =  ahora + 86400*(i-2) - 3600
	post.post_status = "future"
	wordpress.call(NewPost(post))
	i = i+1
