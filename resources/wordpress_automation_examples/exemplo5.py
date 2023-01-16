from wordpress_xmlrpc import *
from wordpress_xmlrpc.methods.posts import *
from wordpress_xmlrpc.methods.users import *
from wordpress_xmlrpc.methods import *
from wordpress_xmlrpc.compat import *

wordpress = Client('http://dominio.url/xmlrpc.php', 'usuario', 'contraseña')

pagina = WordPressPage()
pagina.id = 125
pagina.title = "Página de pyBirras"
pagina.content = "Hasta aqui Wordpress, ahora Woocomerce"
pagina.post_status = 'publish'
wordpress.call(posts.EditPost(pagina.id, pagina))
