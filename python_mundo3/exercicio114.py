import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.google.com/search?num=12&client=ubuntu-sn&sca_esv=853236ac3d6bce34&channel=fs&udm=2&fbs=AIIjpHydJdUtNKrM02hj0s4nbm4yAFb4PvhjIUcDtaFHkK_tyspyDJg0-Y4Ji8bGEtEDNJGPYR40HYWsbK7HyDMH1XbgsIEBuX2ZRVnpzXw_5CbKO5Dq_fEpRROEcsO1QxKDA_4LmxsfhmWhOZa0gkFQ2ufqibzU-k7XBPB0u2ylnCDtiAFPqTxqq553UpOMZomQ5Qm62ushU54qX2vayiEFZtuMgYxEXw&q=smiling+friends&sa=X&ved=2ahUKEwit_9PXraeQAxXGGbkGHQ9EO78QtKgLegQIGxAB&biw=1795&bih=968&dpr=1#vhid=-jFTVuMO-CazTM&vssid=mosaic')
except urllib.error.URLError:
    print ('ERROR: site inacessivel')
else:
    print ('site acessivel')