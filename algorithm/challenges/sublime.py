
import urllib.request,os
pf='Package Control.sublime-package'
ipp=sublime.installed_packages_path()
urllib.request.install_opener(
    urllib.request.build_opener(
        urllib.request.ProxyHandler(
            {"http":"http://069.15084016:1056018XYZ@10.1.1.45:80"}
        )
    )
)
open(os.path.join(ipp,pf),'wb').write(
    urllib.request.urlopen(
        'http://sublime.wbond.net/'+pf.replace(' ','%20')
    ).read()
)