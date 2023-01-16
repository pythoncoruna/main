from wordpress_xmlrpc import *
from wordpress_xmlrpc.methods.posts import *
from wordpress_xmlrpc.methods.users import *
from wordpress_xmlrpc.methods import *
from wordpress_xmlrpc.compat import *
from PIL import Image

wordpress = Client('http://dominio.url/xmlrpc.php', 'usuario', 'contraseña')

with open('test.jpg', 'rb') as img:
	data = {
	'name': 'test.jpg',
	'type': 'image/jpeg', #mimetype
	}
	data['bits'] = xmlrpc_client.Binary(img.read())
	datos_imagen = wordpress.call(media.UploadFile(data))

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
imagen = "<figure class=\"wp-block-image size-large\"><img src=\"" + datos_imagen['url'] + "\" \"alt=\"python coruña\" class=\"wp-image\"/></figure>"

post = WordPressPost()
post.title = "pyBirras Test 6"
post.content = texto + "<br>" + imagen
post.post_status = "publish"
wordpress.call(NewPost(post))
